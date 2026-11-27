# Annual Report Summary Examples

This folder contains a small, editable workflow for generating annual-report summaries and intentionally corrupted examples for classroom discussion. It is a basis for inspiration, not a required design or a complete production system. Students should adapt the approach, prompts, evaluation criteria, and implementation to their own project.

## What Is Included

- `summarize_annual_reports.ipynb` provides a notebook interface for selecting a report, summary type, task, corruption types, and severity.
- `annual_report_summarizer.py` extracts selectable PDF text, preserves page numbers, prepares evidence chunks, calls the configured language model, and saves summaries and run information.
- `summary_corruptor.py` asks the selected model adapter to make realistic corruptions to an existing good summary. It marks the resulting Markdown as intentionally corrupted.
- `student_llm_client.py` contains a provider-neutral async callable placeholder for students to connect to a model they are allowed to use.
- `business_reports/` and `sustainability_reports/` contain the source PDFs listed below. Add further reports to these folders to include them in a run.
- `generated_summaries/business/` and `generated_summaries/sustainability/` hold good summaries and their supporting run artifacts.
- `corrupted_examples/business/` and `corrupted_examples/sustainability/` hold intentionally corrupted Markdown examples. They are kept outside `generated_summaries` so they cannot be confused with good outputs.

The corruption workflow keeps the model's change descriptions in memory while the notebook is running. It saves the marked Markdown example, but does not write a separate JSON manifest for each corrupted example. The good-summary workflow has its own evidence and run-log artifacts under `generated_summaries`.

## Source Reports

The source PDFs are included in this folder, so no download is needed. Business report filenames match the summaries in `generated_summaries/business/`, so each summary can be checked against its source. The original links are listed for reference; some open a report webpage rather than a direct PDF download.

### Business Reports

- [Rabobank (EN), Annual Report 2025](https://media.rabobank.com/asset/a35a8d2d-dbcf-4145-ba0a-7c9f2841d052/Annual-Report-2025.pdf): `Rabobank_Annual_Report_2025_EN.pdf`
- [VDL (NL), Jaarverslag 2025](https://vdl.files.prepr.io/2r684y25deun/vdl-jaarverslag-2025-binnenwerk-nl-web-035.pdf): `VDL-jaarverslag-2025_NL.pdf`
- [ING (EN), Annual Report 2025](https://ing.com/binaries/content/assets/documents/annual-reports/2025-ing-groep-nv-annual-report.pdf): `ING_groep_2025_annual_report_EN.pdf`
- [Coolblue (EN), Yearbook 2025](https://aboutcoolblue.com/documents/37/Yearbook_Holding_fulldoc_EN_2025_aboutcoolblue.pdf): `Coolblue_yearbook_2025_EN.pdf`
- [a.s.r. (EN), Annual Report 2025](https://downloads.asr.nl/files/2025-annual-report-asr.pdf?name=Annual%20report%202025): `ASR_2025_annual_report_EN.pdf`

### Sustainability Reports

More report links are available from [Duurzaamheidsverslag.nl](https://www.duurzaamheidsverslag.nl/bedrijf/). Included:

- [Albert Heijn (EN), Impact Report 2025](https://data.maglr.com/3671/issues/62868/746664/downloads/impact-report-2025-english.pdf): `AlbertHeijn_Impact_Report_2025_EN.pdf`
- [HEMA (NL), Duurzaamheidsverslag 2025](https://hema.h5mag.com/hema/edit-duurzaamheidsverslag_2025/over_dit_verslag/53807/HEMA_s_duurzaamheidsverslag_2025.pdf): `HEMA_duurzaamheidsverslag_2025_NL.pdf`
- [Lyreco (EN), Sustainability Report 2025](https://marketing.lyreco.nl/ga-voor-een-groenere-werkplek/duurzaamheidsverslag-2025/?page=1): `Lyreco_Sustainability_Report_2025_EN.pdf`
- [Rabobank (EN), Our Impact in 2025](https://media.rabobank.com/m/6374b3ea1f24d397/original/Our-Impact-in-2025.pdf): `Rabobank_Our_Impact_2025_EN.pdf`
- [Tony's Chocolonely (EN), Annual Fair Report 2024-2025](https://nl.tonyschocolonely.com/en/pages/annual-fair-report-2024-2025): `Tonys_Annual_Fair_Report_2024-2025_EN.pdf`

To generate new summaries, connect `StudentLLMClient` to a language-model provider as described below. To use other reports, download them into `business_reports/` or `sustainability_reports/`.

## Summary Types

The business summaries already included in `generated_summaries/business/` were generated with the **Business description** prompt. The **Sustainability performance assessment** prompt is also available as an optional summary type; no completed sustainability summaries are currently included.

The notebook supports two kinds of output:

- **Sustainability performance assessment:** a concise five-paragraph assessment focused on disclosed sustainability performance and related credit risks.
- **Business description:** an educational company overview with introductory bullets and sections on operations, markets and strategy, and disclosed risks and responses. It is not a lender's credit memo and should not make unsupported bankability or project-finance judgments.

The summarisation prompts are similar in purpose and analytical style to prompts used for credit report generation: they emphasize evidence-grounded analysis, citations during evidence extraction, and avoiding unsupported assumptions. However, the implementation of summarisation here is different. This workflow extracts text locally from PDFs, processes page-cited chunks, and then generates a summary; it does not use the credit-report-generation pipeline itself. The summary prompts are defined in `annual_report_summarizer.py` and are separate from the corruption prompt.

## Corruption Examples

One or more corruption types can be selected. The language model edits the saved good summary and returns a marked Markdown result.

- **Irrelevance:** makes the summary less focused using peripheral details already present in the summary, rather than unrelated report-layout commentary.
- **Hallucination:** adds plausible but unsupported claims within the subject of the summary.
- **Citation failure:** removes required citations from business descriptions or adds inappropriate source commentary to sustainability summaries.
- **Instruction failure:** introduces a lapse in the requested format or citation instructions.
- **Content omission:** removes relevant details.

**Light** corruption means a subtle but recognizable lapse. **Heavy** corruption means a more substantial lapse while keeping the result readable and recognizably based on its source. Corrupted files include a visible warning in a Markdown comment; treat them as teaching examples, never as factual guidance.

## Running the Notebook

This project supports macOS and Windows. PDF text extraction uses PyMuPDF, so Swift and Apple's PDFKit are not required. Image-only scanned pages may require OCR and are not transcribed by this workflow.

Prerequisites:

- Python 3.12.
- `uv` installed on your operating system.
- Access to a language-model provider, if you want to run generation rather than inspect or adapt the workflow.

From a terminal opened in this project folder, run:

```shell
uv sync
```

This creates the project environment and installs the dependencies declared in `pyproject.toml`. In VS Code, select the Python interpreter in this project's `.venv`, then open `summarize_annual_reports.ipynb` and select that environment as the notebook kernel. Run the notebook cells from top to bottom. The workflow initializes `StudentLLMClient`, which is intentionally a placeholder and does not connect to any provider by default.

To enable generation, implement `StudentLLMClient.__call__` in `student_llm_client.py`. It receives a system prompt, a user prompt, and a completion-token limit; it should asynchronously call a provider and return the generated text as a string. Add the provider's SDK to `pyproject.toml` and install it with `uv sync`. Keep API keys in local environment variables or an untracked `.env` file, never in the notebook or source control. Until implemented, the placeholder raises a clear `NotImplementedError` at the first model call; batch summary mode records that failure in the run log and continues to the next report.

Use the selectors to choose a summary type and either generate good summaries or create corrupted examples from summaries that already exist. Batch mode processes all PDFs found for that summary type.

Once connected, model requests use the provider and deployment configured by the student adapter. Corruption generation sends the saved good summary, not the source PDF, to the model.

## How the Summary Workflow Works

1. PyMuPDF extracts text page by page and skips pages with no selectable text.
2. Extracted text is split into bounded chunks. Each chunk carries the PDF filename and page number so evidence can retain source citations.
3. The model extracts concise evidence notes. A checkpoint allows a matching extraction run to resume if interrupted.
4. If the evidence is too long, it is consolidated before the final summary request.
5. The final summary is saved as Markdown with its evidence and run records.

The exact summary requirements differ by summary type and are specified in the prompts. Review generated content against the source report before using it.

## Customizing the Example

Students can explore changes such as adjusting evidence chunk sizes, designing new corruption categories, changing how severity is defined, comparing model-generated and deterministic corruptions, or evaluating outputs against a rubric. Keep the distinction between supported report facts and intentionally unsupported training content explicit, and independently verify any generated result.
