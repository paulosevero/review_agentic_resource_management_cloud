---
id: "paper-2267"
title: "Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]"
authors: ["Wang, Ruyan", "Yang, Anqi", "Wu, Dapeng", "Tang, Tong", "Zhu, Zhiyuan"]
year: 2025
venue: "Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology"
venue_type: "journal"
doi: "10.11999/JEIT240685"
url: "https://www.scopus.com/pages/publications/105000908007?origin=resultslist"
publisher: "Science Press"
pages: "470--479"
keywords: ["Asynchronous Mobile Edge Computing (MEC)", "Average Age of Information (AoI)", "Average energy consumption", "Hybrid action reinforcement learning", "Wireless Sensor Networks (WSNs)"]
language: "Chinese"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2267 — Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]

## Metadata

- **Authors:** Wang, Ruyan and Yang, Anqi and Wu, Dapeng and Tang, Tong and Zhu, Zhiyuan
- **Year:** 2025
- **Venue:** Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
- **DOI:** 10.11999/JEIT240685
- **URL:** https://www.scopus.com/pages/publications/105000908007?origin=resultslist
- **Publisher:** Science Press
- **Pages:** 470--479
- **Language:** Chinese
- **Keywords:** Asynchronous Mobile Edge Computing (MEC); Average Age of Information (AoI); Average energy consumption; Hybrid action reinforcement learning; Wireless Sensor Networks (WSNs)

### Abstract

Objective Mobile Edge Computing (MEC) is a key technology for addressing the limited computing capabilities and energy constraints of wireless devices. MEC improves local computing performance and extends battery life by offloading computationally intensive tasks from sensors to nearby edge servers. However, in dynamic environments such as anomaly detection, environmental monitoring, and vehicle positioning, task heterogeneity becomes a significant factor limiting performance. For example, the asynchrony of task generation times can result in issues such as low communication efficiency and increased latency. Furthermore, traditional latency measurement techniques often fail to accurately assess task timeliness. To address these challenges, this paper proposes a strategy for the joint optimization of task scheduling and computational resource allocation in asynchronous MEC networks. The proposed strategy adaptively optimizes task scheduling and resource allocation, minimizing the average information age and energy consumption, thereby enhancing overall system performance. Methods This paper focuses on age-aware asynchronous MEC offloading and resource allocation. Specifically, a mathematical model is formulated based on the First Come First Served (FCFS) queuing principle, considering the order of asynchronous task arrivals. This model optimizes task scheduling and computational resource allocation in asynchronous MEC offloading, with the goal of minimizing the Average Age of Information (AoI) and average energy consumption. In dynamic asynchronous MEC, optimization problems are inherently complex. When these tasks involve both binary offloading decisions and continuous resource allocation, the combination of actions further complicates problem-solving, transforming it into a non-convex optimization challenge. Additionally, the actor network of the Actor-Critic algorithm (A2C) adapts its output layer to either a Categorical or Gaussian distribution, depending on whether the action space is discrete or continuous. This paper proposes a Hybrid Advantage Actor-Critic (HA2C) Deep Reinforcement Learning (DRL) algorithm, which effectively optimizes dynamic task scheduling and computational resource allocation strategies as tasks are generated. Results and Discussions In the simulations, the performance of the algorithm is evaluated by comparing four different strategies: random strategy, DRL strategy, delay strategy, and synchronous strategy. The following conclusions are drawn: 1. Average AoI is more sensitive to task timeliness than latency metrics. It not only accounts for the time interval between task generation and reception but also considers the intervals between task generations, offering a better measure of task timeliness. Moreover, the HA2C algorithm effectively balances the timeliness of information and energy consumption, achieving optimal average AoI and energy consumption (Figure 4). 2. The hybrid action space of the HA2C algorithm is better suited for adapting to a growing number of devices. As the number of devices increases, HA2C significantly outperforms multi-agent algorithms and traditional A2C algorithms (Figure 5). This is because the number of actions in a discrete action space grows exponentially with the device count, ultimately leading to the curse of dimensionality, which degrades the performance of discrete DRL algorithms. 3. In the asynchronous MEC model, task generation occurs instantaneously and asynchronously. This setup allows a large amount of computational resources to be concentrated on tasks that arrive earlier, maximizing the utilization of MEC resources. As a result, asynchronous models outperform synchronous models in terms of both average AoI and average energy consumption (Figure 6). In conclusion, these experiments confirm that, compared to synchronous models, asynchronous models not only significantly improve computational efficiency but also effectively reduce energy consumption. Furthermore, the proposed HA2C algorithm proves to be highly effective in solving the asynchronous edge offloading and resource allocation problems, maintaining efficient performance even as the number of devices increases. Conclusions This paper leverages MEC to address the limited computational capacity and energy of wireless devices. Specifically, the paper considers scenarios where Wireless Sensor Network (WSN) edge computing systems continuously collect and process data to monitor real-time changes in the detection environment. In these contexts, the paper focuses on the heterogeneous generation times of sensor tasks deployed at different locations. The optimization goal is to minimize both average information age and energy consumption, achieved through task scheduling and adaptive resource allocation. The HA2C algorithm is designed to handle dynamic and unpredictable system changes while simultaneously managing both continuous and discrete actions. Simulation results demonstrate that the algorithm significantly reduces average information age and energy consumption in asynchronous offloading networks, while meeting the timeliness requirements of tasks in WSNs. © 2025 Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Task Scheduling and Computing Resource Allocation Optimization Strategy in Asynchronous Mobile Edge Computing Networks; [异步移动边缘计算网络中的联合任务调度与计算资源分配优化策略]
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
