---
id: paper-2398
title: A GAN-Enhanced Multi-Agent Deep Reinforcement Learning for Digital Twin-Driven Edge Inference and Heterogeneous Resource Co-Optimization; [数字孪生架构下基于 GAN 增强的多智能体深度强化学习边缘推理与异构资源协同优化]
authors:
- Yuan, Xiao-Ming
- Tian, Han-Sen
- Huang, Kun-Da
- Deng, Qing-Xu
- Kang, Jia-Wen
- Li, Chang-Le
- Duan, Xu-Ting
venue: Jisuanji Xuebao/Chinese Journal of Computers
venue_type: journal
year: 2025
doi: 10.11897/SP.J.1016.2025.01763
url: https://www.scopus.com/pages/publications/105014141998?origin=resultslist
publisher: Science Press
pages: 1763--1780
keywords:
- digital twin
- edge-based large models
- federated learning
- generative adversarial network
- mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2398 — A GAN-Enhanced Multi-Agent Deep Reinforcement Learning for Digital Twin-Driven Edge Inference and Heterogeneous Resource Co-Optimization; [数字孪生架构下基于 GAN 增强的多智能体深度强化学习边缘推理与异构资源协同优化]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deployment of large models at the edge has emerged as a pivotal enabler for the intelligent and digital transformation across various domains, including smart healthcare and urban systems. However, the heterogeneity of massive intelligent tasks and the unpredictability of high-dynamic networks pose significant challenges in the limited computational resources of edge devices to meet the demands of complex inference tasks for efficient and reliable Quality of Service (QoS). Therefore, this paper proposes an edge inference and heterogeneous resource collaborative optimization method based on Generative Adversarial Network (GAN) -enhanced Multi-Agent Deep Reinforcement Learning (MADRL), aiming to achieve dynamic load balancing of heterogeneous resources in Digital Twin (DT) -driven edge large model-enabled systems, ensuring the efficiency and reliability of inference tasks. First, this paper analyzes the physical network layer and twin network layer of the DT-driven edge large model system, and leverages GAN for twin mapping, enabling distributed processing, generation, and optimization of massive heterogeneous data. Next, the MADRL algorithm is applied to the comprehensive quantification and collaborative optimization of heterogeneous resources, with the edge inference data being fed back into the MADRL algorithm to reduce the data communication overhead during centralized training. Meanwhile, the framework utilizes federated learning, allowing for multi-party knowledge sharing, effectively improving model training speed and performance. Finally, simulation results demonstrate that the proposed algorithm reduces inference task delay and energy consumption, optimally utilizes system resources, and improves intelligent service quality in dynamic edge environments. © 2025 Science Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2398.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
