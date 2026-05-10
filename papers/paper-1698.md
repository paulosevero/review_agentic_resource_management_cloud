---
id: paper-1698
title: Optimizing the Average Age of Information in Multi-UAV-Assisted MEC Systems with Stochastic Task Arrivals
authors:
- Jia, Yihang
- Yang, Jie
- Ni, Yiyang
- Qiu, Renzhe
- Mo, Zhaoying
- Zhao, Haitao
venue: 2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCC65529.2025.11149089
url: https://www.scopus.com/pages/publications/105017694292?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- average age of information
- Mobile edge computing
- multi-agent actorcritic
- tasks arrive
- unmanned aerial vehicle
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1698 — Optimizing the Average Age of Information in Multi-UAV-Assisted MEC Systems with Stochastic Task Arrivals

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has gained significant attention as an effective solution in real-time mission-critical applications such as emergency response and disaster relief operations to enhance computational capabilities and reduce service latency. This paper proposes a novel multi-UAV cooperative MEC system that addresses the challenges posed by stochastic task arrivals from ground users, while enabling collaborative computing offloading among UAVs. The primary objective is to minimize the overall average age of information (AAoI) for all users under joint constraints on UAV trajectory optimization and computation offloading allocation. Our key innovation lies in the development of a federated learning framework with parameter-sharing mechanisms, where UAVs and ground users operate as heterogeneous multi-agents with in a distributed training architecture. By implementing the multi-agent actor-critic (MAAC) algorithm, the proposed approach enables online optimization of systemwide AAoI through collaborative policy learning. Comprehensive experimental evaluations demonstrate that the proposed scheme achieves lower AAoI and greater stability compared to conventional MAAC (without parameter sharing) and multi-agent deep deterministic policy gradient (MADDPG) approaches, particularly in dynamic environments with high task arrival rates.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1698.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
