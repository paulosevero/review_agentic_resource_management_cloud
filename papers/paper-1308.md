---
id: "paper-1308"
title: "VELO: A Vector Database-Assisted Cloud-Edge Collaborative LLM QoS Optimization Framework"
authors: ["Yao, Zhi", "Tang, Zhiqing", "Lou, Jiong", "Shen, Ping", "Jia, Weijia"]
year: 2024
venue: "Proceedings of the IEEE International Conference on Web Services, ICWS"
venue_type: "conference"
doi: "10.1109/ICWS62655.2024.00105"
url: "https://www.scopus.com/pages/publications/85210264193?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "865--876"
keywords: ["Edge Computing", "Large Language Model", "Multi-Agent Reinforcement Learning", "Quality of Services", "Request Scheduling", "Vector Database"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1308 — VELO: A Vector Database-Assisted Cloud-Edge Collaborative LLM QoS Optimization Framework

## Metadata

- **Authors:** Yao, Zhi and Tang, Zhiqing and Lou, Jiong and Shen, Ping and Jia, Weijia
- **Year:** 2024
- **Venue:** Proceedings of the IEEE International Conference on Web Services, ICWS
- **DOI:** 10.1109/ICWS62655.2024.00105
- **URL:** https://www.scopus.com/pages/publications/85210264193?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 865--876
- **Language:** English
- **Keywords:** Edge Computing; Large Language Model; Multi-Agent Reinforcement Learning; Quality of Services; Request Scheduling; Vector Database

### Abstract

The Large Language Model (LLM) has gained significant popularity and is extensively utilized across various domains. Most LLM deployments occur within cloud data centers, where they encounter substantial response delays and incur high costs, thereby impacting the Quality of Services (QoS) at the network edge. Leveraging vector database caching to store LLM request results at the edge can substantially mitigate response delays and cost associated with similar requests, which has been overlooked by previous research. Addressing these gaps, this paper introduces a novel Vector database-assisted cloud-Edge collaborative LLM QoS Optimization (VELO) framework. Firstly, we propose the VELO framework, which ingeniously employs vector database to cache the results of some LLM requests at the edge to reduce the response time of subsequent similar requests. Diverging from direct optimization of the LLM, our VELO framework does not necessitate altering the internal structure of LLM and is broadly applicable to diverse LLMs. Subsequently, building upon the VELO framework, we formulate the QoS optimization problem as a Markov Decision Process (MDP) and devise an algorithm grounded in Multi-Agent Reinforcement Learning (MARL) to decide whether to request the LLM in the cloud or directly return the results from the vector database at the edge. Moreover, to enhance request feature extraction and expedite training, we refine the policy network of MARL and integrate expert demonstrations. Finally, we implement the proposed algorithm within a real edge system. Experimental findings confirm that our VELO framework substantially enhances user satisfaction by concurrently diminishing delay and resource consumption for edge users utilizing LLMs.  © 2024 IEEE.

## 04 — Title Screening

**Title:** VELO: A Vector Database-Assisted Cloud-Edge Collaborative LLM QoS Optimization Framework

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** VELO: A Vector Database-Assisted Cloud-Edge Collaborative LLM QoS Optimization Framework
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** VELO: A Vector Database-Assisted Cloud-Edge Collaborative LLM QoS Optimization Framework
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
