---
id: paper-2488
title: Joint Optimization of Model Inferencing and Task Offloading for MEC-Empowered Large Vision Model Services
authors:
- Zhuang, Xinyi
- Wu, Jiaqi
- Wu, Hongjia
- Zhang, Tingting
- Gao, Lin
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2025
doi: 10.1109/INFOCOM55648.2025.11044689
url: https://www.scopus.com/pages/publications/105011081575?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Large Vision Model
- Mobile Edge Computing
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

# paper-2488 — Joint Optimization of Model Inferencing and Task Offloading for MEC-Empowered Large Vision Model Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of Large Vision Models (LVMs) such as Sora, the initial comprehension of physical laws by large AI models has garnered significant attention, which enables them to interpret and apply physical principles with increasing accuracy and sophistication. Nevertheless, due to resource limitations and delay constraints, traditional cloud-based LVM services often fail to meet the diverse needs of users, particularly in scenarios requiring real-time responsiveness. In this work, we explore the scenario of Mobile Edge Computing (MEC)-empowered LVM services in wireless networks, where heterogeneous LVMs are deployed on both cloud and edge servers, and LVM Users (LUs) can offload computation task to edge servers to reduce delay and energy consumption. In such a scenario, we focus on the joint optimization of model inferencing and task offloading for LUs, aiming to maximize the total service utility, while minimizing delay and energy consumption. First, to characterize the utility of LVM services, we propose a multi-dimensional video quality metric based on real measurements, which incorporates both the prompt-video alignment and the classic video quality indicators. Then, to solve the problem in a decentralized manner, we propose a two-stage solution based on both learning and optimization techniques. In the first stage, we design a reinforcement learning-based Multi-Agent Proximal Policy Optimization (MAPPO) approach to make the real-time model inferencing and task offloading decisions. In the second stage, we employ the optimization-based Sequential Least Squares Programming (SLSQP) to make the efficient resource allocation decisions. Simulation results show that our proposed solution outperforms other benchmarks, and can reduce delay and energy consumption by up to 17.2% and 21.7%, respectively, while increasing service utility by up to 3%.  © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2488.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
