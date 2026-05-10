---
id: "paper-2570"
title: "Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning"
authors: ["Farabegoli, Nicolas", "Domini, Davide", "Aguzzi, Gianluca", "Viroli, Mirko"]
year: 2026
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2026.108539"
url: "https://www.scopus.com/pages/publications/105036172040?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Aggregate computing", "Collective adaptive systems", "Edge-cloud computing", "Heterogeneous graph neural networks", "Multi-agent reinforcement learning", "Task offloading"]
language: "English"
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
    human_justification: "RL"

---

# paper-2570 — Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning

## Metadata

- **Authors:** Farabegoli, Nicolas and Domini, Davide and Aguzzi, Gianluca and Viroli, Mirko
- **Year:** 2026
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2026.108539
- **URL:** https://www.scopus.com/pages/publications/105036172040?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Aggregate computing; Collective adaptive systems; Edge-cloud computing; Heterogeneous graph neural networks; Multi-agent reinforcement learning; Task offloading

### Abstract

Task offloading in edge-cloud computing systems requires determining optimal allocation of application components across heterogeneous infrastructure while balancing multiple objectives, like energy consumption, latency, or cost. This problem becomes particularly complex in large-scale deployments (e.g., smart cities, industrial IoT) where existing approaches fail to address collective phenomena, namely emergent system-wide behaviors like network congestion that arise from multi-device interactions, leading to suboptimal offloading decisions in large-scale deployments. To address these challenges this paper introduces a multi-agent learning framework for collective component offloading that decomposes applications into a directed acyclic graph of macro-components, enabling partial offloading where individual components can be selectively executed locally or migrated to edge/cloud servers. Our system model represents the infrastructure as a heterogeneous graph of application devices and infrastructure nodes, supporting decentralized offloading decisions while maintaining component interdependencies. In particular, we propose Informed Deep Hetero Graph Q-Learning (IDHGQL), which combines: (1) Heterogeneous Graph Neural Networks (HeteroGNNs) for policy representation that naturally handle diverse device types and relationships; (2) Aggregate computing to enrich device observations with collective system state information; and (3) a multi-agent Deep Q-Learning algorithm based on centralized training with decentralized execution that balances individual constraints with emergent collective phenomena. Experimental evaluation demonstrates IDHGQL’s effectiveness in multi-objective optimization scenarios, successfully learning policies that balance battery consumption, latency, and infrastructure costs. In density-aware scenarios, agents learn spatially-adaptive strategies that dynamically adjust offloading decisions based on local congestion: favoring local execution in high-density areas to avoid network bottlenecks while leveraging edge/cloud resources in sparse regions. Ablation studies confirm that collective information integration is essential for learning such context-aware policies, with IDHGQL consistently outperforming static baselines across all evaluated metrics. © 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

## 04 — Title Screening

**Title:** Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Heterogeneous GNN for collective-task offloading in cloud-edge via deep Q-learning
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
