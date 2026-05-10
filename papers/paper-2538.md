---
id: paper-2538
title: Model Migration in Digital Twin-Empowered Vehicular Edge Computing With AoI-Aware Decentralized Bilevel Learning
authors:
- Chen, Xiangyi
- Bi, Yuanguo
- Xing, Huanlai
- Zheng, Danyang
- Marina, Mahesh K.
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3621052
url: https://www.scopus.com/pages/publications/105018766277?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3953--3968
keywords:
- age-of-information
- bilevel learning
- Digital twin migration
- vehicular edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2538 — Model Migration in Digital Twin-Empowered Vehicular Edge Computing With AoI-Aware Decentralized Bilevel Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The accuracy of digital twin models hinges on the prompt collection of information from the vehicular environment. However, the high mobility of vehicles and the dynamically changing network environment pose significant challenges. Dynamic twin model migration can reduce the Age of Information (AoI) by bringing twin models closer to their vehicles. Existing works rarely consider the inherent differences in optimization cycles between digital twin model migration and data upload, which potentially leads to suboptimal cost efficiency and information freshness. Specifically, real-time vehicular data must be rapidly uploaded to edge servers to ensure the accuracy and timeliness of digital twin models, while frequent migration of twin models over short periods incurs substantial costs. Therefore, we propose a dual-timescale bilevel learning approach, where the upper-layer learning optimizes twin model migration decisions on a long timescale to achieve forward-looking model migration, and the lower-layer learning optimizes data upload and resource allocation decisions on a short timescale to ensure the accuracy and timeliness of digital twin models. Then, we design a multi-agent selective parameter sharing approach based on spatiotemporal dependency correlations to accelerate model convergence and reduce communication costs among agents. Furthermore, through a rigorous theoretical analysis, we prove the convergence of the dual-timescale bilevel learning with broad applicability. Finally, numerical results demonstrate that our algorithm outperforms comparison algorithms in terms of convergence, AoI, and system cost, achieving at least a 21.30% reduction in AoI and a 14.58% reduction in system cost compared to the benchmark algorithms. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2538.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
