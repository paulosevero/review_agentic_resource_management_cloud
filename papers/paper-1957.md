---
id: paper-1957
title: 'Self-adaptive Multi-Access Edge Architectures: A Robotics Case'
authors:
- Moghaddam, Mahyar T.
- Leed, Joakim V.
- Frandsen, Anders Q.
venue: Proceedings - 2025 IEEE Conference on Cloud and Big Data Computing, CBDCom 2025
venue_type: conference
year: 2025
doi: 10.1109/CBDCOM68404.2025.00029
url: https://www.scopus.com/pages/publications/105033530493?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 157--164
keywords:
- Computing Offloading
- Energy Efficiency
- Neural Networks
- Performance
- Robotics
- Software Architecture
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1957 — Self-adaptive Multi-Access Edge Architectures: A Robotics Case

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growth of compute-intensive AI tasks highlights the need to mitigate the processing costs and improve performance and energy efficiency. This necessitates the integration of intelligent agents as architectural adaptation supervisors tasked with adaptive scaling of the infrastructure and efficient offloading of computation within the continuum. This paper presents a self-adaptation approach for an efficient computing system of a mixed human-robot environment. The computation task is associated with a Neural Network algorithm that leverages sensory data to predict human mobility behaviors, to enhance mobile robots’ proactive path planning, and ensure human safety. To streamline neural network processing, we built a distributed edge offloading system with heterogeneous processing units, orchestrated by Kubernetes. By monitoring response times and power consumption, the MAPE-K-based adaptation supervisor makes informed decisions on scaling and offloading. Results show notable improvements in service quality over traditional setups, demonstrating the effectiveness of the proposed approach for AI-driven systems. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1957.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
