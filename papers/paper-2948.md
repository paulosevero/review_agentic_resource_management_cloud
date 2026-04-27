---
id: "paper-2948"
title: "Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing"
authors: ["Zuo, Wendong", "Liao, Siteng", "Cui, Yangguang", "Liu, Tong", "Cai, Hui", "Wan, Shaohua"]
year: 2026
venue: "IEEE Transactions on Cloud Computing"
venue_type: "journal"
doi: "10.1109/TCC.2026.3668236"
url: "https://www.scopus.com/pages/publications/105031650676?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["deep reinforcement learning", "Edge computing", "multi-unmanned aerial vehicle cooperation", "task assignment"]
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

# paper-2948 — Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing

## Metadata

- **Authors:** Zuo, Wendong and Liao, Siteng and Cui, Yangguang and Liu, Tong and Cai, Hui and Wan, Shaohua
- **Year:** 2026
- **Venue:** IEEE Transactions on Cloud Computing
- **DOI:** 10.1109/TCC.2026.3668236
- **URL:** https://www.scopus.com/pages/publications/105031650676?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning; Edge computing; multi-unmanned aerial vehicle cooperation; task assignment

### Abstract

Leveraging flexible deployment and wide-area coverage, Unmanned Aerial Vehicles (UAVs) assisted edge computing (EC) extends computation capability to the network edge and has become a key paradigm for improving the quality of service in the Internet of Things. However, constrained by onboard resources, UAVs struggle to independently process massive heterogeneous tasks in real time. Existing studies mainly focus on cooperation between UAVs and ground devices or the cloud, while the coupled cooperative relationships among UAVs and the performance scalability in large-scale UAV networks remain insufficiently characterized. To this end, we propose a distributed task assignment framework for a multi-UAV cooperative EC system, where each UAV explicitly accounts for cooperation with other UAVs and, leveraging controllable mobility, assigns a portion of local tasks to other UAVs or base stations to minimize the long-term system-wide total latency. To address the resulting joint trajectory control and task assignment optimization problem, we first formulate it as a Markov decision process. We then propose a Multi-head self-Attention critic-assisted MADDPG (MA<sup>2</sup> DDPG) algorithm to train local online decision models for UAVs. Under the fully cooperative setting, we employ a centralized Critic to exploit global information and reduce parameter redundancy; concurrently, a multi-head self-attention mechanism is incorporated into the Critic to aggregate multi-UAV interaction information, delineate implicit cooperative dependencies, and alleviate the network input dimensionality curse arising from increasing UAV scale. Finally, extensive simulation experiments validate the effectiveness of the proposed method. © 2013 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
