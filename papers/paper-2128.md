---
id: paper-2128
title: Research on Heterogeneous Computing Energy Efficiency Optimization Strategy for NOMA-MEC System; [面向 NOMA-MEC 系统的异构计算能效优化策略研究]
authors:
- She, Rui
- Cui, Enfang
- Wu, Yuting
- Huang, Zhilan
venue: Beijing Youdian Daxue Xuebao/Journal of Beijing University of Posts and Telecommunications
venue_type: journal
year: 2025
doi: 10.13190/j.jbupt.2024-005
url: https://www.scopus.com/pages/publications/105007714082?origin=resultslist
publisher: Beijing University of Posts and Telecommunications
pages: 133--143
keywords:
- edge computing
- energy efficiency
- heterogeneous computing
- task unloading
language: Chinese
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

# paper-2128 — Research on Heterogeneous Computing Energy Efficiency Optimization Strategy for NOMA-MEC System; [面向 NOMA-MEC 系统的异构计算能效优化策略研究]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of generative artificial intelligence technology, edge machine learning has gradually become a key trend, aiming to use data on edge devices for model training to reduce latency and improve user experience. However, due to the energy and resource limitations of edge devices, especially in executing high-energy learning tasks, improving the energy efficiency of edge devices has become the main challenge at present. This paper proposes an edge energy efficiency optimization model based on heterogeneous computing. On the local computing side, central processing unit and neural network processing unit (CPU-NPU) heterogeneous computing units are configured to reasonably allocate tasks between CPU and NPU to improve carrying capacity and energy utilization. On the transmission side, non orthogonal multiple access transmission is used to offload tasks from edge devices to servers to improve spectrum and energy efficiency. At the same time, in order to maximize the energy efficiency of edge devices, a joint computing and communication resource management optimization strategy is proposed. Based on the joint optimization algorithm, the single objective energy efficiency optimal solution for local heterogeneous computing task allocation, transmission power allocation factor, task offloading delay involving computing and communication sides is jointly optimized to maximize the overall energy efficiency of edge devices. The simulation results show that compared with traditional CPU single computing nodes, the proposed scheme improves spectrum resource utilization while also improving the energy efficiency of Internet of things (IOT) edge user devices by 30%. © 2025 Beijing University of Posts and Telecommunications. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2128.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
