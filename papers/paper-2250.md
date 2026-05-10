---
id: paper-2250
title: A Survey on Trajectory Planning and Resource Allocation in Unmanned Aerial Vehicle-assisted Edge Computing Networks; [无人机辅助边缘计算网络轨迹规划与资源分配研究综述]
authors:
- Wang, Kan
- Cao, Tielin
- Li, Xujie
- Li, Hongyan
- Li, Meng
- Zhou, Momiao
venue: Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
venue_type: journal
year: 2025
doi: 10.11999/JEIT241071
url: https://www.scopus.com/pages/publications/105007512025?origin=resultslist
publisher: Science Press
pages: 1266--1281
keywords:
- Mobile Edge Computing (MEC)
- Offline optimization
- Online optimization
- Trajectory optimization
- Unmanned Aerial Vehicle (UAV)
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
    my_justification: Review
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

# paper-2250 — A Survey on Trajectory Planning and Resource Allocation in Unmanned Aerial Vehicle-assisted Edge Computing Networks; [无人机辅助边缘计算网络轨迹规划与资源分配研究综述]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Significance Unmanned Aerial Vehicle-assisted Mobile Edge Computing (UAV-MEC) is recognized for its flexible deployment, rapid response, wide-area coverage, and distributed computing capabilities, demonstrating significant potential in smart cities, environmental monitoring, and emergency rescue. Traditional ground-based MEC systems, constrained by fixed edge server deployments, are inadequate for dynamic user distributions and remote area demands. The integration of UAVs with MEC is a critical advancement, where dynamic trajectory planning and resource allocation enhance network energy efficiency, computational efficiency, and service quality, supporting the development of low-altitude intelligent networking. This integration addresses the efficient offloading and real-time processing of computation-intensive tasks through air-ground collaborative optimization, providing foundational technical support for future 6G networks and low-altitude economies. Existing surveys in this field predominantly focus on the integration of UAVs and MEC from a resource allocation perspective, while trajectory planning and its joint optimization with resource allocation are largely overlooked. Furthermore, the distinctions between online and offline optimization are insufficiently addressed in existing surveys, necessitating a systematic analysis of current theories and methods to guide future research. Progress In UAV-MEC, joint optimization of trajectory planning and resource allocation has progressed in both online and offline domains. Algorithm frameworks, including alternating optimization and reinforcement learning, have been shown to effectively balance computational complexity with optimization performance. (1) Offline optimization: (a) Energy efficiency optimization: Existing studies employ alternating optimization methods, such as Block Coordinate Descent (BCD) and Successive Convex Approximation (SCA), as well as heuristic algorithms, including differential evolution and dynamic programming, to jointly optimize trajectories, task offloading, and resource allocation, minimizing energy consumption for both users and UAVs. Further reductions in system energy consumption are achieved by integrating Wireless Power Transfer (WPT) and Reconfigurable Intelligent Surfaces (RIS). (b) Latency optimization: Non-Orthogonal Multiple Access (NOMA) and task scheduling strategies are utilized to minimize user-perceived latency. A multi-UAV collaborative framework based on game theory and reinforcement learning is proposed. (c) Multi-objective optimization: The Dinkelbach method is introduced to address fractional programming problems, facilitating joint optimization of computational efficiency, throughput, and secure capacity. Digital Twin (DT) technology is integrated to approximate global optimality. (2) Online optimization: (a) Lyapunov framework: Long-term stochastic problems are decoupled into per-slot optimizations through temporal decomposition. Convex optimization is combined with dynamic trajectory and resource allocation adjustments to adapt to time-varying channels and user mobility. (b) Reinforcement learning: Multi-Agent Deep Reinforcement Learning (MADRL) is applied to multi-UAV collaboration, with expert knowledge guidance and noise injection incorporated to accelerate algorithm convergence. (3) Hybrid optimization: A “pre-planning + online adjustment” strategy is proposed. In the offline phase, clustering algorithms and particle swarm optimization are used to generate high-quality samples for training Deep Neural Networks (DNNs). In the online phase, incremental learning is applied to dynamically fine-tune DNNs for unknown scenarios, balancing global planning with real-time responsiveness. Conclusions Despite notable advancements, several critical challenges in UAV-assisted MEC remain unresolved: (1) Incomplete future state information: The formulation of offline optimization problems typically assumes full knowledge of environmental state information over future time horizons. However, in multi-UAV scenarios involving multi-dimensional parameters, acquiring complete and accurate state information across extended periods remains difficult, limiting the applicability of offline methods. (2) Real-time multi-UAV coordination: Enhancing system efficiency and task completion quality requires real-time coordination among UAVs. This process demands extensive information exchange within UAV swarms, complex obstacle avoidance, and high-dimensional control adjustments. Collaborative computation offloading and multi-UAV trajectory planning remain challenging due to their inherent complexity. (3) Security vulnerabilities in air-ground links: The line-of-sight propagation and open transmission environment of UAV-assisted MEC networks expose offloaded data to risks such as eavesdropping, data tampering, and signal interference. Current approaches predominantly rely on physical-layer security, whereas active defense mechanisms against emerging threats, including deep-fake signal attacks, are still underdeveloped. (4) Lack of integration across air-space-ground networks: The absence of standardized interfaces and unified cross-domain resource scheduling protocols hinders the coordination of spectrum, computing, and caching resources between satellites and UAV-MEC systems. This limitation restricts the realization of globally orchestrated heterogeneous networks. (5) Energy constraints and service quality tradeoff: UAV endurance directly affects service coverage and operational sustainability. Although energy efficiency is emphasized in both offline and online optimization strategies, a fundamental tradeoff persists between energy consumption and edge service quality. These technical bottlenecks continue to restrict the transition of UAV-MEC from theoretical frameworks to large-scale real-world deployment. Prospects Future research is expected to progress in the following directions: (1) Intelligent environmental perception will advance through the integration of Gated Recurrent Units (GRUs) or Temporal Convolutional Networks (TCNs) for dynamic parameter prediction, while Generative Adversarial Networks (GANs) will be leveraged to complement incomplete environmental state information. (2) Multi-UAV collaboration and energy efficiency will be enhanced through the development of service migration mechanisms and DT-driven MADRL frameworks, combined with solar/WPT technologies to improve UAV endurance. (3) Secure communication mechanisms will evolve with the combination of beamforming, physical-layer security techniques, and homomorphic encryption-based task offloading protocols to address eavesdropping and data tampering in air-ground channels. (4) Heterogeneous network integration will focus on exploring a “cloud-edge-device-satellite” architecture to expand UAV-MEC coverage and robustness in 6G networks, with the development of satellites-assisted cross-domain resource scheduling algorithms. (5) Green computing paradigms will emerge through the integration of energy harvesting and service migration mechanisms to reduce computing loads, promoting sustainable low-altitude intelligent computing ecosystems. © 2025 Science Press. All rights reserved.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2250.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
