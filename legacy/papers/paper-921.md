---
id: "paper-921"
title: "Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning"
authors: ["Gao, Zhen", "Yang, Lei", "Dai, Yu"]
year: 2024
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2023.3292387"
url: "https://www.scopus.com/pages/publications/85164391192?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2303--2321"
keywords: ["Curriculum learning", "multiaccess edge computing (MEC)", "reinforcement learning (RL)", "resource allocation", "task offloading"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-921 — Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning

## Metadata

- **Authors:** Gao, Zhen and Yang, Lei and Dai, Yu
- **Year:** 2024
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2023.3292387
- **URL:** https://www.scopus.com/pages/publications/85164391192?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2303--2321
- **Language:** English
- **Keywords:** Curriculum learning; multiaccess edge computing (MEC); reinforcement learning (RL); resource allocation; task offloading

### Abstract

In multiaccess edge computing (MEC) systems, existing task offloading methods have provided ultrashort latency services for heterogeneous tasks on mobile devices (MDs). Nevertheless, the complexity of MEC systems grows exponentially with the number of MDs or edge servers (ESs), so learning a good offloading policy is a huge challenge when the number of MDs or ESs is large. Moreover, MDs are often unable to find optimal ESs for offloading since the restricted ESs infrastructures and the spatiotemporally imbalanced task offloading requirements. To solve these problems, we propose a curriculum spatiotemporal multiagent actor-critic (CSTMAAC)-based task offloading method. Each ES is regarded as an agent and the problem is formulated as a multiobjective optimization task. To adapt to the large-scale MEC systems, we first introduce an evolutionary curriculum learning by gradually raising the number of trained ES agents in a phased way. Second, to facilitate the coordination of the offloading policies among geographically distributed ESs, we design an attention-based centralized critic-network. Besides, a delayed access mechanism is introduced that uses information about future task processing competition to capture the impact of potential future task processing contention and help ES agents obtain a better offloading strategy. Finally, critic-network is expanded to multicritics and a dynamic weight mechanism is designed to adaptively optimize multiobjectives and obtain a good balance for multiple objectives. Real-world data sets used in experiments demonstrate that CSTMAAC raises task completion rates and total utility by 13.01%-15.21% and 16.89%-18.32% compared with the existing algorithms.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning
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
