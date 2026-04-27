---
id: "paper-760"
title: "Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems"
authors: ["Xiong, Jianyu", "Guo, Peng", "Wang, Yi", "Meng, Xiangyin", "Zhang, Jian", "Qian, Linmao", "Yu, Zhenglin"]
year: 2023
venue: "Engineering Applications of Artificial Intelligence"
venue_type: "journal"
doi: "10.1016/j.engappai.2022.105710"
url: "https://www.scopus.com/pages/publications/85144058485?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Cloud computing", "Group distributed manufacturing system", "Multi-agent deep reinforcement learning", "Near-real-time optimization", "Task offloading"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-760 — Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems

## Metadata

- **Authors:** Xiong, Jianyu and Guo, Peng and Wang, Yi and Meng, Xiangyin and Zhang, Jian and Qian, Linmao and Yu, Zhenglin
- **Year:** 2023
- **Venue:** Engineering Applications of Artificial Intelligence
- **DOI:** 10.1016/j.engappai.2022.105710
- **URL:** https://www.scopus.com/pages/publications/85144058485?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud computing; Group distributed manufacturing system; Multi-agent deep reinforcement learning; Near-real-time optimization; Task offloading

### Abstract

The rapid development of cloud computing and the Internet of Things (IoT) have facilitated near real-time optimization of the group distributed manufacturing systems. Currently, the most common technique to accomplish near-real-time optimization is cloud–edge cooperation for offloading optimization tasks. The tasks are partially offloaded to the cloud to be completed, and the remaining are kept at the edge. Due to the complexity of task offloading, such as capacity restrictions of cloud and edge computing resources, or task deadlines, unbalanced or insufficient tasks are offloaded to cloud and edge, causing time delay. To address the imbalance and insufficiency in the task offloading process, a mixed-integer programming model was developed to reduce the latency of task calculation. The task offloading problem is decomposed into two sub-problems: 1) Defining priorities for the tasks in near real-time. 2) Determining if the task is offloaded to the cloud. A multi-agent deep reinforcement learning with attention mechanism (MaDRLAM) framework is proposed to solve the two-step decision problem. The MaDRLAM framework consists of two agents, and each agent corresponds to a sub-problem. Each agent comprises an encoder and a decoder, and the two agents cooperate in devising an offloading strategy for the tasks. The Encoder and Decoder built for each agent are based on the Transformer structure. Unlike the traditional Transformer, we added the Pointer networks to the Transformer to solve the proposed decision problem. Besides, an improved multi-actor and single-critic strategy based on the REINFORCE algorithm is designed to train the proposed MaDRLAM. Finally, Extensive computational experiments are conducted on instances with a varying number of tasks, different task data sizes, and different cloud computing capacities. Computational results show that the proposed framework can find a solution with a GAP value of less than 1% within 1 s for each instance. The proposed framework is competitive in both solution accuracy and solution time compared with other offloading strategies. © 2022 Elsevier Ltd

## 04 — Title Screening

**Title:** Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
