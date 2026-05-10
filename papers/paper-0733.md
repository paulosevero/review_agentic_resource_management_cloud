---
id: paper-0733
title: Enabling Programmable Deterministic Communications in 6G
authors:
- Thi, Minh-Thuyen
- Said, Siwar Ben Hadj
- Roberty, Adrien
- Chbib, Fadlallah
- Khatoun, Rida
- Linguaglossa, Leonardo
venue: Proceedings of the International Symposium on Mobile Ad Hoc Networking and Computing (MobiHoc)
venue_type: conference
year: 2023
doi: 10.1145/3565287.3617607
url: https://www.scopus.com/pages/publications/85176108807?origin=resultslist
publisher: Association for Computing Machinery
pages: 322--327
keywords:
- 6G
- deterministic communication
- TSN
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-0733 — Enabling Programmable Deterministic Communications in 6G

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Emerging applications and technologies such as vehicle-to-everything (V2X), edge-computing, and artificial intelligence have emphasized the demand for low-latency and deterministic communication. Although the 5G network has taken several efforts to fulfill this demand, such as with 5G-Time-Sensitive Networking (TSN) integration and DetNet, these efforts must be significantly expanded in 6G to fully achieve end-to-end deterministic communication. In this paper, we explore the problem of programmable deterministic communication in the new architecture of 6G. To deal with this problem, we rely on TSN, which has been proven to be a promising solution for deterministic communication. We take V2X as a use case, then investigate the two greatest challenges of this use case: low-latency communication and programmable network management for deterministic communication. To deal with these challenges, we introduce two solutions: (i) TSN low-latency scheduling supported by Multi-Agent Deep Reinforcement Learning, and (ii) programmable network management supported by SDN and joint cloud-infrastructure control. For each solution, detailed architecture and functionality design are presented. We show their high feasibility, applicability, and potentialities through comprehensive definitions, detailed explanations and in-depth qualitative analysis.  © 2023 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0733.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
