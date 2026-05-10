---
id: paper-2377
title: A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems
authors:
- Yazdanian, Peyman
- Liu, Yan
- Li, Zheng
venue: Proceedings - Asia-Pacific Software Engineering Conference, APSEC
venue_type: conference
year: 2025
doi: 10.1109/APSEC66846.2025.00077
url: https://www.scopus.com/pages/publications/105035220121?origin=resultslist
publisher: IEEE Computer Society
pages: 761--772
keywords:
- llm-based multi agent systems
- microservice systems
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2377 — A Comparative Study Towards Designing a Hybrid Architecture of Microservices and LLM-based Multi-Agent Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> LLM-based Multi-Agent Systems (LLM-MAS) present an emerging paradigm for constructing intelligent and adaptive applications that enable autonomous reasoning and collaborative problem-solving. Empirical studies show that current LLM-MAS still suffers from overlapping agent roles, unclear capabilities, and goal misalignment. In contrast, Microservice Systems (MS) are designed with modularity, and each service encapsulates a well-defined context and interface with structured and deterministic execution. From the system architecture principles, these paradigms demonstrate parallel attributes and complementary strengths that lead to a synthesized hybrid architecture. In this paper, we analyze the design factors of hybrid MS and LLM-MAS, as well as the main challenges, through a comparative study across eight architectural dimensions, including function encapsulation, orchestration, API design, auto-correction, data communication, operations, quality attributes, and environment awareness. The analysis reveals critical mismatches, design synergies, and transferable best practices. To motivate future work, we define four research questions to categorize the challenges. The goal is to create a converging design space for exploring architecture design towards intelligent, autonomous, modular, and adaptive systems. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2377.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
