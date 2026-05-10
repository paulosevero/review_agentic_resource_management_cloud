---
id: paper-2267
title: Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]
authors:
- Wang, Ruyan
- Yang, Anqi
- Wu, Dapeng
- Tang, Tong
- Zhu, Zhiyuan
venue: Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
venue_type: journal
year: 2025
doi: 10.11999/JEIT240685
url: https://www.scopus.com/pages/publications/105000908007?origin=resultslist
publisher: Science Press
pages: 470--479
keywords:
- Asynchronous Mobile Edge Computing (MEC)
- Average Age of Information (AoI)
- Average energy consumption
- Hybrid action reinforcement learning
- Wireless Sensor Networks (WSNs)
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

# paper-2267 — Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Objective Mobile Edge Computing (MEC) is a key technology for addressing the limited computing capabilities and energy constraints of wireless devices. MEC improves local computing performance and extends battery life by offloading computationally intensive tasks from sensors to nearby edge servers. However, in dynamic environments such as anomaly detection, environmental monitoring, and vehicle positioning, task heterogeneity becomes a significant factor limiting performance. For example, the asynchrony of task generation times can result in issues such as low communication efficiency and increased latency. Furthermore, traditional latency measurement techniques often fail to accurately assess task timeliness. To address these challenges, this paper proposes a strategy for the joint optimization of task scheduling and computational resource allocation in asynchronous MEC networks. The proposed strategy adaptively optimizes task scheduling and resource allocation, minimizing the average information age and energy consumption, thereby enhancing overall system performance. Methods This paper focuses on age-aware asynchronous MEC offloading and resource allocation. Specifically, a mathematical model is formulated based on the First Come First Served (FCFS) queuing principle, considering the order of asynchronous task arrivals. This model optimizes task scheduling and computational resource allocation in asynchronous MEC offloading, with the goal of minimizing the Average Age of Information (AoI) and average energy consumption. In dynamic asynchronous MEC, optimization problems are inherently complex. When these tasks involve both binary offloading decisions and continuous resource allocation, the combination of actions further complicates problem-solving, transforming it into a non-convex optimization challenge. Additionally, the actor network of the Actor-Critic algorithm (A2C) adapts its output layer to either a Categorical or Gaussian distribution, depending on whether the action space is discrete or continuous. This paper proposes a Hybrid Advantage Actor-Critic (HA2C) Deep Reinforcement Learning (DRL) algorithm, which effectively optimizes dynamic task scheduling and computational resource allocation strategies as tasks are generated. Results and Discussions In the simulations, the performance of the algorithm is evaluated by comparing four different strategies: random strategy, DRL strategy, delay strategy, and synchronous strategy. The following conclusions are drawn: 1. Average AoI is more sensitive to task timeliness than latency metrics. It not only accounts for the time interval between task generation and reception but also considers the intervals between task generations, offering a better measure of task timeliness. Moreover, the HA2C algorithm effectively balances the timeliness of information and energy consumption, achieving optimal average AoI and energy consumption (Figure 4). 2. The hybrid action space of the HA2C algorithm is better suited for adapting to a growing number of devices. As the number of devices increases, HA2C significantly outperforms multi-agent algorithms and traditional A2C algorithms (Figure 5). This is because the number of actions in a discrete action space grows exponentially with the device count, ultimately leading to the curse of dimensionality, which degrades the performance of discrete DRL algorithms. 3. In the asynchronous MEC model, task generation occurs instantaneously and asynchronously. This setup allows a large amount of computational resources to be concentrated on tasks that arrive earlier, maximizing the utilization of MEC resources. As a result, asynchronous models outperform synchronous models in terms of both average AoI and average energy consumption (Figure 6). In conclusion, these experiments confirm that, compared to synchronous models, asynchronous models not only significantly improve computational efficiency but also effectively reduce energy consumption. Furthermore, the proposed HA2C algorithm proves to be highly effective in solving the asynchronous edge offloading and resource allocation problems, maintaining efficient performance even as the number of devices increases. Conclusions This paper leverages MEC to address the limited computational capacity and energy of wireless devices. Specifically, the paper considers scenarios where Wireless Sensor Network (WSN) edge computing systems continuously collect and process data to monitor real-time changes in the detection environment. In these contexts, the paper focuses on the heterogeneous generation times of sensor tasks deployed at different locations. The optimization goal is to minimize both average information age and energy consumption, achieved through task scheduling and adaptive resource allocation. The HA2C algorithm is designed to handle dynamic and unpredictable system changes while simultaneously managing both continuous and discrete actions. Simulation results demonstrate that the algorithm significantly reduces average information age and energy consumption in asynchronous offloading networks, while meeting the timeliness requirements of tasks in WSNs. © 2025 Science Press. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2267.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
