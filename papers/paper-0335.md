---
id: paper-0335
title: Cloud Based Decision Making for Multi-agent Production Systems
authors:
- Rehman, Hamood Ur
- Pulikottil, Terrin
- Estrada-Jimenez, Luis Alberto
- Mo, Fan
- Chaplin, Jack C.
- Barata, Jose
- Ratchev, Svetan
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2021
doi: 10.1007/978-3-030-86230-5_53
url: https://www.scopus.com/pages/publications/85115448778?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 673--686
keywords:
- Cloud computing
- Machine learning
- Multi-agent
- Production systems
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
    my_justification: LLM as workload
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

# paper-0335 — Cloud Based Decision Making for Multi-agent Production Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The use of multi-agent systems (MAS) as a distributed control method for shop-floor manufacturing control applications has been extensively researched. MAS provides new implementation solutions for smart manufacturing requirements such as the high dynamism and flexibility required in modern manufacturing applications. MAS in smart manufacturing is becoming increasingly important to achieve increased automation of machines and other components. Emerging technologies like artificial intelligence, cloud-based infrastructures, and cloud computing can also provide systems with intelligent, autonomous, and more scalable solutions. In the current work, a decision-making framework is proposed based on the combination of MAS cloud computing, agent technology, and machine learning. The framework is demonstrated in a quality control use case with vision inspection and agent-based control. The experiment utilizes a cloud-based machine learning pipeline for part classification and agent technology for routing. The results show the applicability of the framework in real-world scenarios bridging cloud service-oriented architecture with agent technology for production systems. © 2021, Springer Nature Switzerland AG.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0335.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
