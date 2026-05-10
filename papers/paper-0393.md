---
id: paper-0393
title: Multi-Slot Dynamic Computing Resource Optimization in Edge Computing
authors:
- Chen, Pengyu
- Xu, Han
- Fan, Xingwang
- Hu, Jing
- Song, Tiecheng
venue: 2022 IEEE 14th International Conference on Wireless Communications and Signal Processing, WCSP 2022
venue_type: conference
year: 2022
doi: 10.1109/WCSP55476.2022.10039042
url: https://www.scopus.com/pages/publications/85149101472?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 160--165
keywords:
- computing resource allocation
- edge computing
- modified genetic algorithm
- multi-slot dynamic optimization
- users task scheduling
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

# paper-0393 — Multi-Slot Dynamic Computing Resource Optimization in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates multi-slot dynamic computing resource optimization in the scenario of edge computing. A cloud-edge-user optimization system is established which targets to supply users low-delay services through users task scheduling and ensures energy consumption as little as possible. Considering large-scale fading and location information, we model the channel between the users and the edge nodes (eNodes) to calculate the offloading rate. In order to quantify the delay cost, a penalty factor is introduced to characterize the service quality of users. Unrestricted data offloading contributes to excessive energy consumption while delay cost does not decrease much, so energy consumption is also considered as an optimized target. We propose a modified genetic algorithm to solve the multi-slot dynamic optimization problem which presents better convergence than conventional genetic algorithm. A multi-agent greedy algorithm with low time complexity is also designed to compare with the modified genetic algorithm. Via simulation, the effectiveness of two proposed algorithms in reducing the delay cost and the energy consumption is verified and the modified genetic algorithm shows competitive performance. In addition, we also analyze the changes in offloading decisions caused by different weights of energy consumption. © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0393.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
