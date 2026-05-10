---
id: paper-0540
title: Average Age of Information Optimization in Mobile Edge Computing Networks
authors:
- Zheng, Huiji
- Yu, Sicong
- Qiu, Xinyuan
- Cui, Xiaolong
- Zhu, Li
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2022
doi: 10.1117/12.2639193
url: https://www.scopus.com/pages/publications/85136966374?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- Deep reinforcement learning
- Federated learning
- Mobile edge computing
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

# paper-0540 — Average Age of Information Optimization in Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Age of Information(AoI) is a novel metric to measure freshness of data in status update scenarios proposed by academia in recent years. Real-time applications need to transmit data packets for status update to the target node as soon as possible. However, due to the data density, the limited computing capacity of edge devices and the influence of the environment, the problems of intensive computation and high delay are caused. Mobile edge computing (MEC) is a new computing mode that extends cloud computing power closer to the user, where computing offloading and other technologies promise to solve those problems. We mainly studies the AoI optimization in MEC networks, in which data freshness and offloading strategy play an important role. Firstly, we propose the average AoI minimization problem for MEC network scenarios, and propose a multi-agent deep reinforcement learning(DRL) algorithm called Federated Multi-Agent Actor-Critic (Fed-MAAC). Federated learning is used to train agents to improve algorithm performance and data security. At the same time, we conducted experiments in gym, a popular simulation environment in reinforcement learning, and compared Fed-MAAC with baseline algorithm. The simulation results show that this algorithm is superior to other algorithms in average AoI optimization performance. © 2022 SPIE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0540.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
