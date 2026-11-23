# Team Collaboration Agreement

> **Project:** Evaluation of AI-generated summaries — *Trust, Check or Reject*  
> **Programme:** Master Applied Artificial Intelligence (MAAI), Block 2 · Academic year 2026–2027  
> **Institution:** Amsterdam University of Applied Sciences (Hogeschool van Amsterdam)  
> **Repository:** [wanderwerkhoven-afk/MAAIblok2](https://github.com/wanderwerkhoven-afk/MAAIblok2)  
> **Version:** 1.0 · **Last updated:** 23 November 2026  
> **Status:** Draft for collective review and sign-off

## 1. Project Information

### Project title

**Evaluating AI-generated summaries for analyst decision support**

### Value proposition

> We help analysts decide whether to **trust, check or reject AI-generated summaries** by providing evaluation checks, scores and routing—so they can review summaries faster and consistently while keeping control of the final decision.

### Project context

Analysts review AI-generated summaries of long, information-dense documents, such as annual reports, credit reports and dossiers. A plausible-looking summary can still omit essential facts, contain unsupported claims, misrepresent figures or conceal uncertainty. This project explores how a transparent evaluation layer can help an analyst decide how to proceed.

The intended workflow is:

```text
Long source document
        |
        v
AI-generated summary
        |
        v
Evaluation checks + evidence + scores
        |
        v
Suggested review route
        |
        v
Analyst: TRUST / CHECK / REJECT
        |
        v
Recorded human decision and rationale
```

**The application supports decisions; it does not replace the analyst's judgement.** A score or recommendation is not proof that a summary is factually correct.

### Project period

**Block 2, academic year 2026–2027.** Exact start, end and assessment dates are maintained in the [project planning](../../wiki/Planning.md) once confirmed.

### Team members

- Wander Werkhoven
- Shereen
- Sebas
- Sebastiaan
- Lei

**Team coach:** Renata

> Full names, precise role allocations and confirmation dates will be completed by the team. No individual is considered to have signed this agreement until they explicitly confirm it.

---

## 2. Purpose of This Agreement

This agreement defines how we collaborate during research, prototyping, AI evaluation, software development, user testing, documentation and reporting.

We commit to:

- Fair and visible contributions, with clear ownership and peer review.
- Open communication, realistic planning and early reporting of blockers.
- Evidence-based design and technical choices.
- Traceable research, datasets, experiments and project decisions.
- Responsible handling of documents, user information and AI output.
- Shared responsibility for an integrated, demonstrable and explainable final product.

We assess both **the quality of the application** and **the quality of the evidence supporting its behaviour**.

---

## 3. General Responsibilities

Every team member agrees to:

1. Complete assigned tasks by the agreed internal deadlines and keep their status up to date.
2. Raise blockers or capacity problems early rather than silently delaying delivery.
3. Review other members' work and contribute to integration and testing.
4. Join agreed project meetings, prepare where needed and participate constructively.
5. Keep code, research notes, test cases, findings and sources organised in the repository.
6. Explain and substantiate methodological, interface and technical decisions.
7. Document meaningful changes in assumptions, requirements, model behaviour and thresholds.
8. Handle sensitive data and AI tools according to institutional rules and applicable agreements.
9. Contribute to final demonstrations, reporting, reflection and quality assurance.

### Project-specific quality responsibilities

We jointly ensure that:

- **Factuality:** summary claims can be checked against the original document.
- **Coverage:** relevant omissions and missing context are considered during evaluation.
- **Traceability:** findings point to a source location or a reproducible test.
- **Explainability:** analysts can understand why a check failed or why a route was suggested.
- **Uncertainty:** limitations and unsupported conclusions are communicated without false certainty.
- **Human oversight:** the analyst can inspect, override and record the final decision.

---

## 4. Division of Work

Tasks are allocated based on skill, interest, learning objectives and available capacity. Roles are **workstreams**, not exclusive ownership of knowledge: every member should understand the end-to-end product and review adjacent work.

### Proposed workstreams

| Workstream | Typical responsibilities | Owner | Reviewer |
|---|---|---|---|
| Project coordination & integration | Backlog, dependencies, architecture alignment, sprint coordination | To agree | To agree |
| Research & requirements | Stakeholders, interview protocol, acceptance criteria, ethics | To agree | To agree |
| UX/UI & usability | Design patterns, prototype, status messaging, questionnaires, user tests | To agree | To agree |
| AI evaluation & data | Evaluation checks, reference annotations, scoring experiments, error analysis | To agree | To agree |
| Engineering & validation | Document pipeline, interface integration, automated tests, deployment | To agree | To agree |

These are **suggested workstreams**. The team confirms actual owners and reviewers during planning; one member may cover multiple workstreams. Wander may coordinate technical integration if the team agrees.

### Task management

Each substantial task is recorded as a GitHub Issue (or a linked team-tracker item) with:

- **Task and intended outcome:** what will be delivered?
- **Owner and reviewer:** who implements and who checks?
- **Acceptance criteria:** how do we know it is done?
- **Deadline and priority:** when is it needed?
- **Status:** Backlog / In progress / Review / Blocked / Done.
- **Evidence:** related commit, pull request, experiment, user-test record or report section.

The detailed backlog and deadlines belong in the [planning page](../../wiki/Planning.md).

### Fair contribution

Fair contribution does not imply identical tasks or identical hours. We consider effort, difficulty, reliability, initiative, review work and project-wide support. Distribution of work is reviewed regularly and adjusted if one member becomes overloaded or cannot access a meaningful learning opportunity.

---

## 5. Work Method and Version Control

### Repository and branches

- **GitHub repository:** [MAAIblok2](https://github.com/wanderwerkhoven-afk/MAAIblok2).
- **Integration branch:** `main`; it should remain demonstrable and as stable as possible.
- **Task branches:** `feature/<issue-number>-short-description`, `fix/<issue-number>-short-description` or `docs/<issue-number>-short-description`.
- **Review:** changes normally enter `main` through a pull request (PR) linked to their issue.
- **Urgent changes:** any exceptional direct commit to `main` must be communicated and documented.
- **Production/deployment branch:** only introduced if the team decides that a separate release branch is useful.
- **GitLab mirror:** if used, the team documents the source of truth and the sync procedure to avoid diverging histories.

### Development workflow

```text
Issue + acceptance criteria
          |
          v
Branch from main
          |
          v
Implementation + tests + documentation
          |
          v
Pull Request -> peer review
          |
          +-- Changes requested --> revise
          |
          v
Approved and checks passed
          |
          v
Merge to main
          |
          v
Update issue, wiki and demo if relevant
```

### Pull-request expectations

A PR should describe the change, linked issue, test evidence, assumptions and remaining limitations. At least one other team member reviews meaningful changes where practical. Authors do not self-approve substantial methodological changes.

We avoid committing credentials, API tokens, private documents, identifiable user research or unnecessarily large datasets. Environment secrets are stored outside version control; use example configuration files where needed.

### Definition of Done

A task is done when its agreed acceptance criteria are met, relevant tests or checks are recorded, the reviewer has had the opportunity to assess it, documentation is updated and the result is usable within the current prototype.

---

## 6. AI Evaluation and Decision Rules

Because the project evaluates *AI-generated summaries*, we apply additional safeguards to our own development and research.

### Checks and scores

We distinguish between:

1. **Source-grounded factual checks:** whether a claim is supported or contradicted by source passages.
2. **Coverage checks:** whether important source information has been omitted.
3. **Numerical and entity checks:** whether amounts, dates, names and relationships are represented accurately.
4. **Uncertainty and consistency checks:** whether ambiguous statements, contradictions and unavailable evidence are surfaced.

Each check should have a documented goal, inputs, output meaning, limitations, test cases and responsible reviewer. We do not label heuristic scores as calibrated probabilities unless that has been demonstrated.

### Trust / Check / Reject routing

These labels represent **review routes**, not automatic truth judgements:

| Route | Intended meaning | Analyst action |
|---|---|---|
| **TRUST** | No material issues were found by the implemented checks; limitations remain | Review evidence and decide whether the summary is usable |
| **CHECK** | One or more claims, omissions or uncertain findings require closer inspection | Open flagged claims and compare with cited passages |
| **REJECT** | Material contradictions, unsupported claims or evaluation failures make the summary unsuitable without correction | Reject or request revision and record the reason |

Routing thresholds, wording and visual status indicators are **design hypotheses until tested**. They must be documented and empirically reviewed. A green or positive score may never imply a guarantee of accuracy; a detected failure should be explained in actionable language.

The analyst retains the final decision and can override a recommendation with a recorded rationale. If the evidence is insufficient, the interface must say so rather than pretending a definitive answer is available.

### Evaluation discipline

- Define success metrics and a simple baseline before claiming improvement.
- Separate development, validation and final test examples as appropriate.
- Keep annotated test documents, expected outcomes and error taxonomies traceable.
- Report false positives, false negatives, disagreements and difficult edge cases.
- Evaluate whether the proposed UI helps users understand findings and choose the correct next action.
- Record model versions, prompts, settings, sampling choices and relevant dependencies for reproducibility.
- Do not claim validated accuracy, time savings or consistency without supporting measurements.

### Sensitive or confidential documents

Use publicly available, synthetic or explicitly authorised source documents. Do not upload confidential financial, legal, client or personal documents to third-party AI services without permission and appropriate safeguards. Minimise collected data and anonymise user-research notes where possible.

---

## 7. Communication

### Channels

| Purpose | Channel |
|---|---|
| Quick coordination and short questions | WhatsApp |
| Formal discussions, meetings and shared institutional communication | Microsoft Teams |
| Issues, PR discussions and technical decisions | GitHub |
| Long-lived research, design and project documentation | [Project wiki](../../wiki/README.md) |

### Response expectations

During agreed working days, each member checks the relevant project channels at the beginning and end of their work period when reasonably possible. Urgent blockers should be clearly marked with the impact and required decision. Team members communicate extended unavailability in advance where feasible.

We distinguish between a message that needs a quick acknowledgement and a task that requires dedicated work.

### Communication principles

We communicate respectfully, clarify assumptions, challenge ideas with reasons and avoid silently making major scope or technical changes.

---

## 8. Meetings and Decision-Making

### Proposed meeting rhythm

- **Weekly team planning/review:** Friday during scheduled project hours, subject to team confirmation.
- **Coach meeting:** at the time arranged with Renata; record actions afterwards.
- **Midweek check-in:** Wednesday when needed to remove blockers or review a prototype.
- **Additional working sessions:** as required for experiments, usability tests and integration.

### Meeting practice

**Before:** share the agenda and relevant material.  
**During:** review progress, demo completed work, discuss blockers and hear all perspectives.  
**After:** assign action owners and deadlines, update issues and record substantive decisions.

For significant design, research or model decisions, document the question, alternatives, evidence, trade-offs and outcome in [Decisions and Changes](../../wiki/Besluiten-en-wijzigingen.md). Seek consensus; if consensus is not achievable, the team documents competing views and asks the coach for guidance where appropriate.

---

## 9. Availability, Deadlines and Accountability

We plan around actual study schedules, competing commitments and agreed project time. Everyone communicates illness, holidays, conflicting obligations or substantial changes in capacity as soon as practicable.

Internal deadlines should precede university deadlines to leave time for review, testing and integration.

If a deadline is at risk, the owner will:

1. Alert the team as early as possible.
2. Explain the remaining work and the effect on dependencies.
3. Propose a realistic revised date or reduced scope.
4. Request support or redistribution where needed.

Repeated problems are discussed as a team with evidence and with the goal of restoring a workable plan. No one is expected to make up indefinitely for another person's uncommunicated absence.

---

## 10. Feedback, User Research and Quality Assurance

### Peer feedback

Feedback should be specific, constructive, respectful and linked to requirements or evidence. Reviewers identify the problem, explain the impact and suggest a test or improvement. Authors respond to the substance rather than treating critical feedback as personal criticism.

### Prototype and user testing

We test design assumptions with intended users or realistic representatives, including questions such as:

- Can users distinguish the meanings of TRUST, CHECK and REJECT?
- Do they know which claim or document section to inspect next?
- Can they explain a score and find the evidence behind it?
- Do they understand that the decision is theirs, not the application's?
- Do colour, buttons and notifications support rather than bias their judgement?

Methods, sample limitations, observed interactions, findings and resulting design changes are recorded in the [Evaluation wiki](../../wiki/Evaluatie.md). Participation should be voluntary and relevant privacy obligations respected.

### Academic integrity and GenAI use

We disclose consequential AI assistance and record its purpose, tools and verification steps in [GenAI Use](../../wiki/GenAI-gebruik.md). Generated text, references, code or test results must be checked before they are submitted or presented as evidence. We do not fabricate interviews, research results, citations, model performance or user feedback.

---

## 11. Disagreements and Conflict Resolution

If disagreement occurs:

1. Discuss it directly, calmly and respectfully.
2. Focus on observable work, decisions and consequences.
3. Let each person explain their reasoning.
4. Identify options, supporting evidence and trade-offs.
5. Agree on a next step and document it.

If the issue persists, involve team coach **Renata**. Serious or repeated issues concerning contribution, conduct, confidentiality or academic integrity are documented and escalated through the appropriate university process if needed.

---

## 12. Changes to the Agreement

Changes require discussion and collective acceptance. Material changes should be recorded with a date and short rationale in the repository history or project decision log.

**Current version:** 1.0  
**Last updated:** 23 November 2026  
**Next review:** At the first team meeting after publication, and whenever collaboration needs change.

---

## 13. Agreement and Sign-Off

By signing or explicitly confirming this agreement, each member acknowledges the working principles, project-specific quality rules and shared accountability described above.

| Team member | Confirmation / initials | Date |
|---|---|---|
| Wander Werkhoven | Pending | — |
| Shereen | Pending | — |
| Sebas | Pending | — |
| Sebastiaan | Pending | — |
| Lei | Pending | — |

**Note:** Names are copied from the repository's current team list. Confirmation is intentionally left pending until each person approves.

---

## 14. Quick Reference

### Team checklist

- [ ] We agree on workstream ownership, reviewers and workload.
- [ ] We keep tasks and deadlines visible.
- [ ] We use issues, branches and PRs for meaningful development work.
- [ ] We review each other's code, research and design decisions.
- [ ] We report blockers and absences early.
- [ ] We document assumptions, results, tests and changes.
- [ ] We ground evaluation findings in source-document evidence.
- [ ] We do not confuse a score with verified factual correctness.
- [ ] We keep TRUST / CHECK / REJECT understandable and under human control.
- [ ] We protect confidential information and follow institutional AI rules.
- [ ] We test the prototype with users and use findings to improve it.
- [ ] We contribute to the integrated final product and its documentation.

### Key details

| Item | Agreement |
|---|---|
| Quick communication | WhatsApp |
| Formal communication | Microsoft Teams |
| Source repository | [GitHub — MAAIblok2](https://github.com/wanderwerkhoven-afk/MAAIblok2) |
| Shared documentation | [Project wiki](../../wiki/README.md) |
| Task tracking | GitHub Issues |
| Working branch | `main` + task-specific branches |
| Team coach | Renata |
| Regular meeting | Friday (proposed; confirm with team) |
| Final decisions about summaries | Always made by the human analyst |

---

[Back to project home](../../README.md) · [Project planning](../../wiki/Planning.md) · [Decisions](../../wiki/Besluiten-en-wijzigingen.md)
