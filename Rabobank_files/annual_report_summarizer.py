"""Cross-platform PDF evidence extraction and annual-report summary generation."""

from __future__ import annotations

import asyncio
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

EVIDENCE_SYSTEM_PROMPT = """You are a senior bank credit analyst extracting sustainability evidence from an annual report. Use only the supplied REPORT EVIDENCE and PREVIOUS RESPONSE. Do not use external knowledge or assumptions. Extract only information explicitly stated in the supplied report pages. Preserve material inconsistencies rather than resolving them. Write in English. Every factual statement must be immediately followed by its exact source filename and printed page number in the form [filename, p. N]. Keep exact values, units, financial years, target dates, progress metrics, stated reasons, and named initiatives. Consider governance, climate, GHG emissions, energy, waste, sourcing, nature, water, land use, transport and logistics, labour conditions, and diversity and inclusion. Select the most material documented topics and link materiality to stated operations, geography, or revenue drivers. Cover Planet score and subthemes; sustainability goals with scope/deadline/progress/on-track status/reasons/actions; structural strategies versus isolated actions; MSCI, Sustainalytics, EcoVadis, WBA or other named benchmarks; Scope 1/2 latest and prior values and calculated trend; stated reasons for emissions changes; Scope 3 measured/estimated/absent status; intensity metrics and benchmarks; and EU Taxonomy eligibility/alignment for revenue, CAPEX and OPEX. Clearly distinguish absent information from a stated zero. Avoid duplication. Return concise evidence bullets, not a final assessment."""

FINAL_SYSTEM_PROMPT = """You are a senior credit analyst at a bank. Use only the facts in REPORT EVIDENCE and PREVIOUS RESPONSE. Do not use external knowledge or assumptions. If the context contains no relevant information for the requested task, respond exactly: No relevant data found in provided context. Mention materially inconsistent information when present. Write in English. Express all monetary values with ISO currency codes, using mln or bln (for example, EUR 1,000mln as EUR 1bln); write amounts below 1 mln in full. Refer to financial years as FYxx. Produce exactly five unnumbered paragraphs, no headings, with no more than 300 words total. Paragraph 1: sustainability governance, structural strategy, and roadmap. Paragraph 2: Planet performance score and its material subthemes. Paragraph 3: the 2-3 most material documented ESG topics, why each connects to operations/geography/revenue, stated goals, progress metrics, on-track status, and actions or stated underperformance drivers. Paragraph 4: other material target progress, Scope 1/2 trend and stated reasons, Scope 3 measurement status, intensity, EU Taxonomy, and external ESG ratings/benchmarks where available; avoid repeating paragraph 3. Paragraph 5: concise credit-risk assessment based only on previously stated facts, without introducing new facts. Do not include filenames, page references, citations, source commentary, disclaimers, follow-up questions, tables, titles, conclusions beyond paragraph 5, or trailing commentary. Do not repeat information. The output must contain only the five requested narrative paragraphs."""

BUSINESS_DESCRIPTION_EVIDENCE_PROMPT = """You are preparing an educational company and business overview from an annual report. Use only the supplied REPORT EVIDENCE and PREVIOUS RESPONSE. Do not use external knowledge or assumptions. Extract information explicitly supported by the report. Preserve materially inconsistent information rather than resolving it. Write in English. Immediately follow every factual statement with the source filename and printed page number in the form [filename, p. N]. Identify the company, ownership or group structure if described, principal products and services, business model, operating segments, geographic footprint, customer groups, project portfolio or capacity where relevant, named technology suppliers or material counterparties where stated, and key revenue or cost drivers. Summarize the company's stated strategy, investments, financial and operating developments, and principal risks together with the disclosed risk-management actions. Include quantitative context only where reported and retain its financial year and units. Do not infer ratings, risk grades, bankability, lender acceptability, or project-finance conclusions. Do not invent construction, offtake, technology, operations and maintenance, permitting, grid, or LTA assessments if the annual report does not discuss them. Distinguish reported facts from management outlook. Avoid duplication. Return concise, source-cited evidence notes, not the final overview."""

BUSINESS_DESCRIPTION_FINAL_PROMPT = """You are writing an educational company and business description based on an annual report, not a lender's credit memo. Use only facts in REPORT EVIDENCE and PREVIOUS RESPONSE. Do not use external knowledge or assumptions. If no relevant information is provided, respond exactly: No relevant data found in provided context. Mention material inconsistencies without attempting to resolve them. Write in English, define abbreviations on first use, and retain reported periods and units. Produce a concise, self-contained overview of no more than 1,500 words. Start with 3-5 bullets introducing the company and its business. Include project count/capacity or named technology suppliers only when explicitly supported and relevant. Continue with short, clearly titled sections describing the business model and operations, markets and strategy, and principal disclosed risks and responses. Include financial and operating metrics only where they help explain the business. Explain risks in neutral analytical language and connect them to the company's reported activities or outlook. Do not assign Low/Medium/High grades or make lending, bankability, LTA, or project-finance judgments. Omit unsupported project-specific construction, technology, offtake, O&M, permitting, grid, counterparty-rating, or per-MW metrics. Immediately follow each factual statement with the supporting filename and printed page number in the form [filename, p. N]. Do not add source commentary, disclaimers, or notes. Do not repeat information or add a closing recap. Output only the requested overview."""



def _clean_page_text(text: str) -> str:
    """Normalize PDF text artifacts while retaining meaningful line breaks.

    Args:
        text: Raw text extracted from one PDF page.

    Returns:
        Normalized page text with blank lines and common PDF artifacts removed.
    """
    text = text.replace("\u00a0", " ").replace("\u00ad", "")
    return "\n".join(" ".join(line.split()) for line in text.splitlines() if line.strip())


def _split_text(text: str, max_characters: int) -> list[str]:
    """Split long text into bounded pieces without dropping characters.

    Args:
        text: Text to split.
        max_characters: Maximum desired length for each returned piece.

    Returns:
        Ordered text pieces no longer than the limit, except where a single
        unsplittable boundary is reached by the existing line-splitting logic.
    """
    chunks: list[str] = []
    current = ""
    for line in text.splitlines():
        while len(line) > max_characters:
            if current:
                chunks.append(current)
                current = ""
            chunks.append(line[:max_characters])
            line = line[max_characters:]
        if current and len(current) + len(line) + 1 > max_characters:
            chunks.append(current)
            current = line
        else:
            current = f"{current}\n{line}" if current else line
    if current:
        chunks.append(current)
    return chunks


class AnnualReportSummarizer:
    """Extract report evidence and generate sustainability or business summaries.

    PDF text is extracted locally with PyMuPDF on macOS and Windows. The configured
    language-model callable processes page-cited chunks with prompts selected by
    summary type.
    """

    def __init__(
        self,
        llm_client: Any,
        *,
        max_chunk_characters: int = 10_000,
        max_evidence_characters: int = 24_000,
        max_consolidation_characters: int = 5_000,
        max_completion_tokens: int = 4_096,
        max_retries: int = 3,
        retry_backoff_seconds: int = 3,
        progress=print,
    ) -> None:
        """Set up prompts, request limits, progress reporting, and model adapter.

        Args:
            llm_client: Async callable that accepts system/user prompts and returns text.
            max_chunk_characters: Maximum size of each page-cited evidence request.
            max_evidence_characters: Limit before extracted evidence is consolidated.
            max_consolidation_characters: Input size for each consolidation request.
            max_completion_tokens: Completion budget sent to the model adapter.
            max_retries: Attempts for a failed model request.
            retry_backoff_seconds: Base delay used for exponential retry backoff.
            progress: Callback that receives human-readable workflow updates.
        """
        self.max_chunk_characters = max_chunk_characters
        self.max_evidence_characters = max_evidence_characters
        self.max_consolidation_characters = max_consolidation_characters
        self.max_retries = max_retries
        self.retry_backoff_seconds = retry_backoff_seconds
        self.progress = progress
        self.request_counter = 0
        self.llm_client = llm_client
        self.max_completion_tokens = max_completion_tokens
        self.prompt_definitions: dict[str, dict[str, str]] = {
            "sustainability": {
                "evidence_prompt": (
                    EVIDENCE_SYSTEM_PROMPT
                    + " For evidence extraction, return at most 150 words of "
                    "compact, decision-relevant notes for each input chunk. "
                    "Retain exact values and citations for included facts."
                ),
                "final_prompt": FINAL_SYSTEM_PROMPT,
            },
            "business_description": {
                "evidence_prompt": (
                    BUSINESS_DESCRIPTION_EVIDENCE_PROMPT
                    + " For evidence extraction, return at most 150 words of "
                    "compact, decision-relevant notes for each input chunk. "
                    "Retain exact values and citations for included facts."
                ),
                "final_prompt": BUSINESS_DESCRIPTION_FINAL_PROMPT,
            },
        }

    def _get_prompt_definition(self, summary_type: str) -> dict[str, str]:
        """Resolve the evidence and final prompts for a summary type.

        Args:
            summary_type: Supported summary type key.

        Returns:
            Evidence and final system prompts used by the selected workflow.

        Raises:
            ValueError: If the summary type is not configured.
        """
        try:
            return self.prompt_definitions[summary_type]
        except KeyError as error:
            valid_types = ", ".join(self.prompt_definitions)
            raise ValueError(
                f"Unknown summary type {summary_type!r}; choose from {valid_types}."
            ) from error

    @staticmethod
    def discover_reports(input_folder: Path) -> list[Path]:
        """Find PDFs recursively, excluding generated summaries and their children.

        Args:
            input_folder: Folder containing source reports.

        Returns:
            Sorted paths to discovered PDF reports.
        """
        output_folder = input_folder / "generated_summaries"
        return sorted(
            (
                path for path in input_folder.rglob("*")
                if path.is_file()
                and path.suffix.casefold() == ".pdf"
                and output_folder not in path.parents
            ),
            key=lambda path: path.name.casefold(),
        )

    def extract_pdf(self, pdf_path: Path) -> tuple[list[dict[str, Any]], dict[str, int]]:
        """Extract selectable text with PyMuPDF and preserve page indices.

        Returns page records containing filename, page number, and normalized text,
        together with counts for all pages, pages with text, and skipped blank pages.
        Scanned pages need OCR; this method extracts embedded selectable text only.

        Args:
            pdf_path: Report to extract.

        Returns:
            A tuple containing page records and extraction statistics.

        Raises:
            pymupdf.FileDataError: If the file cannot be opened as a PDF.
        """
        import pymupdf

        pages = []
        empty_pages = 0
        with pymupdf.open(pdf_path) as document:
            page_count = len(document)
            for page_number, page in enumerate(document, start=1):
                text = _clean_page_text(page.get_text("text"))
                if not text:
                    empty_pages += 1
                    continue
                pages.append(
                    {
                        "filename": pdf_path.name,
                        "page_number": page_number,
                        "text": text,
                    }
                )
        stats = {
            "page_count": page_count,
            "pages_with_text": len(pages),
            "empty_pages_skipped": empty_pages,
        }
        return pages, stats

    def _build_chunks(self, filename: str, pages: list[dict[str, Any]]) -> list[str]:
        """Group page text into bounded chunks with source citations.

        Args:
            filename: Source PDF filename to include in citations.
            pages: Extracted page records.

        Returns:
            Evidence chunks, each retaining the filename and page number of its text.
        """
        fragments = []
        for page in pages:
            header = f"SOURCE: {filename}, p. {page['page_number']}"
            content_limit = self.max_chunk_characters - len(header) - 1
            for text_part in _split_text(page["text"], content_limit):
                fragments.append(f"{header}\n{text_part}")

        chunks: list[str] = []
        current = ""
        for fragment in fragments:
            candidate = f"{current}\n\n{fragment}" if current else fragment
            if len(candidate) > self.max_chunk_characters:
                if current:
                    chunks.append(current)
                current = fragment
            else:
                current = candidate
        if current:
            chunks.append(current)
        return chunks

    @staticmethod
    def _prompt_context(search_results: str, previous_response: str) -> str:
        """Format evidence and prior notes using the shared prompt input labels.

        Args:
            search_results: Current report chunk or consolidated evidence.
            previous_response: Earlier notes to provide as conversational context.

        Returns:
            A labeled context string for the prompt template.
        """
        return (
            f"REPORT EVIDENCE:\n{search_results}\n\n"
            f"PREVIOUS RESPONSE:\n{previous_response}"
        )

    async def _call_with_retry(
        self, system_prompt: str, context: str
    ) -> tuple[str, dict[str, int]]:
        """Call the injected model adapter with retries and count requests.

        Args:
            system_prompt: Instructions for the current model task.
            context: Evidence or summary text supplied as the user prompt.

        Returns:
            The model response and request count for this call.

        Raises:
            RuntimeError: If all attempts fail or the adapter returns invalid text.
            NotImplementedError: If the student adapter has not been implemented.
        """
        requests_before = self.request_counter
        last_error: Exception | None = None
        for attempt in range(self.max_retries):
            self.request_counter += 1
            try:
                result = await self.llm_client(
                    system_prompt=system_prompt,
                    user_prompt=context,
                    max_completion_tokens=self.max_completion_tokens,
                )
                if not isinstance(result, str) or not result.strip():
                    raise RuntimeError("The model adapter returned no text.")
                return result, {"requests": self.request_counter - requests_before}
            except NotImplementedError:
                raise
            except Exception as error:
                last_error = error
                self.progress(
                    f"    Request attempt {attempt + 1}/{self.max_retries} failed: {error}"
                )
                if attempt + 1 < self.max_retries:
                    await asyncio.sleep(self.retry_backoff_seconds * (2**attempt))
        raise RuntimeError(
            f"Model request failed after {self.max_retries} attempts"
        ) from last_error

    async def _extract_evidence(
        self,
        filename: str,
        pages: list[dict[str, Any]],
        evidence_system_prompt: str,
        checkpoint_path: Path | None = None,
    ) -> tuple[str, list[dict[str, Any]]]:
        """Extract cited notes from chunks, resume checkpoints, and compact if needed.

        A checkpoint is reused only when both the PDF filename and chunk signature
        match. Consolidation runs only after extraction exceeds the evidence limit.

        Args:
            filename: PDF filename used to identify source pages.
            pages: Extracted page records to process.
            evidence_system_prompt: Instructions for extracting report evidence.
            checkpoint_path: Optional file used to resume completed chunks.

        Returns:
            Consolidated evidence text and per-request usage records.

        Raises:
            RuntimeError: If a model response is blank or no evidence is produced.
            ValueError: If consolidation fails to reduce the evidence size.
        """
        chunks = self._build_chunks(filename, pages)
        evidence_parts: list[str] = []
        usage_log = []
        chunk_signature = hashlib.sha256(
            "\n".join(chunks).encode("utf-8")
        ).hexdigest()

        if checkpoint_path and checkpoint_path.exists():
            try:
                checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
                if (
                    checkpoint.get("filename") == filename
                    and checkpoint.get("chunk_count") == len(chunks)
                    and checkpoint.get("chunk_signature") == chunk_signature
                ):
                    evidence_parts = list(checkpoint.get("evidence_parts", []))
                    self.progress(
                        "  Resuming from checkpoint: "
                        f"{len(evidence_parts)}/{len(chunks)} evidence chunks saved"
                    )
            except (OSError, json.JSONDecodeError):
                self.progress("  Ignoring unreadable evidence checkpoint.")

        for chunk_index in range(len(evidence_parts), len(chunks)):
            chunk = chunks[chunk_index]
            self.progress(
                f"  Evidence chunk {chunk_index + 1}/{len(chunks)}: sending"
            )
            context = self._prompt_context(
                chunk, "No earlier pages are included in this extraction call."
            )
            response, usage = await self._call_with_retry(
                evidence_system_prompt, context
            )
            if not response.strip():
                raise RuntimeError(
                    "Evidence extraction returned a blank response for "
                    f"chunk {chunk_index + 1}/{len(chunks)}; final summarization was stopped."
                )
            evidence_parts.append(response)
            usage_log.append({"stage": "evidence", "chunk": chunk_index + 1, **usage})
            if checkpoint_path:
                checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
                checkpoint_path.write_text(
                    json.dumps(
                        {
                            "filename": filename,
                            "chunk_count": len(chunks),
                            "chunk_signature": chunk_signature,
                            "evidence_parts": evidence_parts,
                        },
                        ensure_ascii=False,
                    ),
                    encoding="utf-8",
                )
            self.progress(
                f"  Evidence chunk {chunk_index + 1}/{len(chunks)}: received"
            )

        evidence = "\n\n".join(evidence_parts)
        while len(evidence) > self.max_evidence_characters:
            batches = _split_text(evidence, self.max_consolidation_characters)
            next_parts = []
            previous_size = len(evidence)
            for batch_index, batch in enumerate(batches, start=1):
                self.progress(
                    f"  Evidence consolidation batch {batch_index}/{len(batches)}: sending"
                )
                context = self._prompt_context(
                    "Condense these extracted notes into at most 120 words. Keep the "
                    "most important facts, exact values, material inconsistencies, "
                    "and all citations for retained facts. Remove duplication and "
                    "peripheral detail.\n\n" + batch,
                    f"Evidence consolidation batch {batch_index}.",
                )
                response, usage = await self._call_with_retry(
                    evidence_system_prompt, context
                )
                if not response.strip():
                    raise RuntimeError(
                        "Evidence consolidation returned a blank response for "
                        f"batch {batch_index}/{len(batches)}."
                    )
                next_parts.append(response)
                usage_log.append(
                    {"stage": "evidence_consolidation", "chunk": batch_index, **usage}
                )
                self.progress(
                    f"  Evidence consolidation batch {batch_index}/{len(batches)}: received"
                )
            evidence = "\n\n".join(next_parts)
            if len(evidence) >= previous_size:
                raise ValueError("Evidence consolidation did not reduce context size.")
        if not evidence.strip():
            raise RuntimeError(
                "Evidence extraction produced no usable text; final summarization was stopped."
            )
        return evidence, usage_log

    async def run_report(
        self,
        pdf_path: Path,
        output_folder: Path,
        summary_type: str = "sustainability",
    ) -> dict[str, Any]:
        """Extract, summarize, and save one PDF's outputs.

        The final Markdown, evidence JSON, and append-only run record are written
        under ``output_folder``. The temporary evidence checkpoint is removed after
        a successful run.

        Args:
            pdf_path: Source report to summarize.
            output_folder: Destination for the summary and supporting artifacts.
            summary_type: Prompt and validation ruleset to use.

        Returns:
            Report filename and generated summary text.

        Raises:
            ValueError: If the summary type is unsupported or the PDF has no text.
            RuntimeError: If evidence extraction or model requests fail.
        """
        prompt_definition = self._get_prompt_definition(summary_type)
        started = datetime.now(timezone.utc).isoformat()
        pdf_path = pdf_path.resolve()
        self.progress(f"Starting report: {pdf_path.name}")
        pages, extraction_stats = self.extract_pdf(pdf_path)
        self.progress(
            f"PDF extraction complete: {extraction_stats['pages_with_text']}/"
            f"{extraction_stats['page_count']} pages have selectable text; "
            f"{extraction_stats['empty_pages_skipped']} blank pages skipped."
        )
        if not pages:
            raise ValueError("No selectable text found; this report may require OCR.")

        checkpoint_path = (
            output_folder
            / f".{pdf_path.stem}_{summary_type}_evidence_checkpoint.json"
        )
        evidence, usage_log = await self._extract_evidence(
            pdf_path.name,
            pages,
            prompt_definition["evidence_prompt"],
            checkpoint_path,
        )
        self.progress("  Final summary: sending")
        final_context = self._prompt_context(evidence, "No additional prior response.")
        summary, usage = await self._call_with_retry(
            prompt_definition["final_prompt"], final_context
        )
        usage_log.append({"stage": "final_summary", **usage})
        output_folder.mkdir(parents=True, exist_ok=True)
        stem = re.sub(r"[^A-Za-z0-9._-]+", "_", pdf_path.stem).strip("_")
        (output_folder / f"{stem}_{summary_type}.md").write_text(
            summary.strip() + "\n", encoding="utf-8"
        )
        (output_folder / f"{stem}_{summary_type}_evidence.json").write_text(
            json.dumps(
                {
                    "filename": pdf_path.name,
                    "extraction": extraction_stats,
                    "evidence": evidence,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        run_record = {
            "filename": pdf_path.name,
            "summary_type": summary_type,
            "status": "success",
            "started_at": started,
            "finished_at": datetime.now(timezone.utc).isoformat(),
            "extraction": extraction_stats,
            "usage": usage_log,
            "error": None,
        }
        with (output_folder / "run_log.jsonl").open("a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(run_record, ensure_ascii=False) + "\n")
        checkpoint_path.unlink(missing_ok=True)

        self.progress(f"Finished report: {pdf_path.name}")
        return {"filename": pdf_path.name, "summary": summary.strip()}

    async def run_reports(
        self,
        pdf_paths: list[Path],
        output_folder: Path,
        summary_type: str = "sustainability",
    ) -> list[dict[str, Any]]:
        """Process reports sequentially and continue after individual report errors.

        Successful report results are returned; failures are recorded in the shared
        run log and reported through the progress callback.

        Args:
            pdf_paths: Reports to process, in execution order.
            output_folder: Shared destination for generated artifacts and run log.
            summary_type: Prompt and validation ruleset to use for each report.

        Returns:
            Results for reports that completed successfully.
        """
        results = []
        total = len(pdf_paths)
        for report_index, pdf_path in enumerate(pdf_paths, start=1):
            self.progress(f"Report {report_index}/{total}")
            try:
                results.append(
                    await self.run_report(pdf_path, output_folder, summary_type)
                )
            except Exception as error:
                failure = {
                    "filename": pdf_path.name,
                    "summary_type": summary_type,
                    "status": "failed",
                    "finished_at": datetime.now(timezone.utc).isoformat(),
                    "error": f"{type(error).__name__}: {error}",
                }
                output_folder.mkdir(parents=True, exist_ok=True)
                with (output_folder / "run_log.jsonl").open("a", encoding="utf-8") as log_file:
                    log_file.write(json.dumps(failure, ensure_ascii=False) + "\n")
                self.progress(f"Failed report: {pdf_path.name}: {failure['error']}")
        return results

    async def close(self) -> None:
        """Close the injected model adapter.

        Returns:
            None: The adapter's optional external resources are released.
        """
        await self.llm_client.close()