---
id: paper-1711
title: Review of the developments of cooperative operation technologies for agricultural machinery in field operation scenarios; [大田作业场景中农机协同作业技术发展综述]
authors:
- Jin, Chengqian
- Chen, Junlong
- Liu, Zheng
- Yang, Tengxiang
- Liu, Gangwei
venue: Nongye Gongcheng Xuebao/Transactions of the Chinese Society of Agricultural Engineering
venue_type: journal
year: 2025
doi: 10.11975/j.issn.1002-6819.202412064
url: https://www.scopus.com/pages/publications/105014503433?origin=resultslist
publisher: Chinese Society of Agricultural Engineering
pages: 1--13
keywords:
- agricultural machinery
- control execution
- cooperative operation
- decision planning
- perception and communiccrtion
- unmanned farm
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1711 — Review of the developments of cooperative operation technologies for agricultural machinery in field operation scenarios; [大田作业场景中农机协同作业技术发展综述]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Agricultural machinery cooperative operation can greatly contribute to fully autonomous unmanned farms. However, some critical challenges still remain in modern agriculture, such as labor shortages, high physical demands, redundant workflows, and resource inefficiency. Multi-machine collaboration can be expected to integrate to significantly improve operational efficiency, cost-saving, and productivity with less environmental impact. This study aims to systematically categorize the agricultural machinery cooperative operation technologies into three key components: sensing and communication, decision-making and planning, and control execution. A critical review was then performed on the advancements in field scenarios. Specifically, 1) sensing and communication were formed as the foundational layer, thus enabling real-time data acquisition and information exchange. Current implementations rely heavily on global navigation satellite systems (GNSS), light detection and ranging (LiDAR), and vision-based sensors. However, the GNSS-dependent systems were limited to the accuracy and reliability under signal-interference scenarios. The communication protocols were also required to update the efficient multi-machine coordination. Consequently, the multi-sensor fusion (e.g., integrating GNSS, LiDAR, cameras, and inertial measurement units) was prioritized to enhance the environmental perception accuracy and robustness. Additionally, low-latency, high-bandwidth communication frameworks (such as 5G or dedicated agricultural IoT networks) were adopted to improve real-time data synchronization and collaborative decision-making. 2) Decision-making and planning also included task allocation, strategic optimization, and path coordination. While the centralized decision architectures dominated the existing systems, among which the predefined static environments were limited to scalability and real-time adaptability. Current path-planning algorithms were predominantly optimized for single-machine operations, difficult to the multi-agent conflicts in dynamic field conditions. The emerging frameworks of distributed decision-making also enabled decentralized task allocation using edge computing and swarm intelligence. Traditional algorithms (e.g., A*, and Dijkstra) were often combined with machine learning (e.g., reinforcement learning, and genetic algorithms). Hybrid path-planning models were obtained to balance the computational efficiency and collision avoidance for large-scale multi-machine operations. Therefore, the context-aware decision systems can be expected to dynamically adjust the operation strategies in the future, according to the real-time field data, weather conditions, and machine status. 3) Control execution was used to realize the precise machinery operation using advanced control models. Generic control strategies are often employed at present, such as proportion-integration-differentiation (PID) or model predictive control. It was still lacking in the adaptability to the heterogeneous agricultural environments. The hybrid control architectures were proposed to integrate the model-based controllers with the data-driven techniques (e.g., neural networks, and adaptive sliding mode control). The high accuracy was improved to solve the terrain variability, actuator delays, and mechanical wear. The path-tracking stability was also enhanced using sensor-feedback adaptive control. Among them, the trajectory execution was refined using real-time LiDAR, vision, and proprioceptive data. Nevertheless, some challenges still remain so far. Perception systems remained vulnerable to GNSS signal degradation. Communication infrastructures lacked standardization, thus leading to interoperability issues. Centralized decision-making frameworks were required for high scalability. The single-machine-centric path-planning approaches failed to solve the multi-agent coordination complexities. Furthermore, the overly generalized control models resulted in suboptimal performance under dynamic field conditions. Three strategic recommendations were proposed to overcome these limitations: 1) Robust platforms of multi-sensor fusion can be developed to mitigate the GNSS dependency for high perception accuracy in complex environments. 2) Distributed decision-making architectures can be expected to be implemented with real-time trajectory coordination algorithms for collision-free multi-machine operations. 3) Hybrid control systems can be designed to combine PID, MPC, and machine learning for high path-tracking precision and adaptability. A cross-disciplinary integration of robotics, AI, and agronomy can be expected to advance autonomous farming in the future. Key directions also include edge-AI-empowered real-time perception, blockchain-based secure machine-to-machine communication, and digital twin-assisted cooperative planning. Agricultural machinery cooperative systems can be expected to achieve higher autonomy, efficiency, and scalability, ultimately driving the sustainable intensification of food production. This finding can provide a comprehensive roadmap to advance the cooperative operation, with emphasis on its transformative potential for unmanned farms. © 2025 Chinese Society of Agricultural Engineering. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1711.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
