---
id: paper-2560
title: 'ReToCue: Reliability-Aware Task Offloading and Caching in UAV-assisted LEO Satellite Edge Computing'
authors:
- Dong, Chongwu
- Li, Weidong
- Xin, Yao
- Chen, Donglong
- Wang, Yi
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2026.3668646
url: https://www.scopus.com/pages/publications/105031751504?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- edge caching
- reliability analysis
- SAGIN
- task offloading
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

# paper-2560 — ReToCue: Reliability-Aware Task Offloading and Caching in UAV-assisted LEO Satellite Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of Space-Air-Ground Networks with mobile edge computing represents a key 6G paradigm enabled by advances in low Earth orbit (LEO) satellites, unmanned aerial vehicles (UAVs), and terrestrial networks. However, several critical challenges emerge when handling delay-sensitive services in rescue missions and infrastructure-less scenarios, where terrestrial network layers are absent. In such scenarios, the limited battery capacity of UAVs and satellites can be exhausted quickly. These factors jointly increase the probability of task delay violations and degrade the quality of service. To address these challenges, our work first investigates the joint optimization of edge caching and computation offloading in the UAV-assisted LEO Satellite edge computing (UAV-LEC) system. The primary objective in our formulation is to minimize total energy consumption while maintaining strict service reliability requirements. Given the distributed and stochastic characteristics of the UAVLEC system, we utilize a partially observable Markov decision process (POMDP) to model the system. Furthermore, martingale theory is incorporated to analyze the service reliability bounds of the tandem queue in the proposed framework. Building on these theoretical foundations, we propose a novel asynchronous interactive multi-agent reinforcement learning algorithm to address the distributed caching and computation optimization problem in the UAV-LEC system. Finally, we conduct comprehensive simulations to demonstrate that the proposed algorithm achieves significant improvements compared to the baseline. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2560.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
