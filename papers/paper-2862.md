---
id: "paper-2862"
title: "EAT: QoS-Aware Edge-Collaborative AIGC Task Scheduling via Attention-Guided Diffusion Reinforcement Learning"
authors: ["Xu, Zhifei", "Tang, Zhiqing", "Lou, Jiong", "Yao, Zhi", "Xie, Xuan", "Wang, Tian", "Wang, Yinglong", "Jia, Weijia"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3656318"
url: "https://www.scopus.com/pages/publications/105028510356?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AIGC Task", "Attention", "Diffusion", "QoS-aware Scheduling", "Reinforcement Learning"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-2862 — EAT: QoS-Aware Edge-Collaborative AIGC Task Scheduling via Attention-Guided Diffusion Reinforcement Learning

## Metadata

- **Authors:** Xu, Zhifei and Tang, Zhiqing and Lou, Jiong and Yao, Zhi and Xie, Xuan and Wang, Tian and Wang, Yinglong and Jia, Weijia
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3656318
- **URL:** https://www.scopus.com/pages/publications/105028510356?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AIGC Task; Attention; Diffusion; QoS-aware Scheduling; Reinforcement Learning

### Abstract

The growth of Artificial Intelligence (AI) and large language models has enabled the use of Generative AI (GenAI) in cloud data centers for diverse AI-Generated Content (AIGC) tasks. Models like Stable Diffusion introduce unavoidable delays and substantial resource overhead, which are unsuitable for users at the network edge with high QoS demands. Deploying AIGC services on edge servers reduces transmission times but often leads to underutilized resources and fails to optimally balance inference latency and quality. To address these issues, this paper introduces a QoS-aware Edge-collaborative AIGC Task scheduling (EAT) algorithm. Specifically: 1) We segment AIGC tasks and schedule patches to various edge servers, formulating it as a gang scheduling problem that balances inference latency and quality while considering server heterogeneity, such as differing model distributions and cold start issues. 2) We propose a reinforcement learning-based EAT algorithm that uses a cross attention layer to extract load and task queue information from edge servers and employs a diffusion-based policy network for scheduling, efficiently enabling model reuse. 3) We develop an AIGC task scheduling system that uses our EAT algorithm to divide tasks and distribute them across multiple edge servers for processing. Experimental results based on our system and large-scale simulations show that our EAT algorithm reduces the response time by up to 42% compared to baselines. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** EAT: QoS-Aware Edge-Collaborative AIGC Task Scheduling via Attention-Guided Diffusion Reinforcement Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** EAT: QoS-Aware Edge-Collaborative AIGC Task Scheduling via Attention-Guided Diffusion Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** EAT: QoS-Aware Edge-Collaborative AIGC Task Scheduling via Attention-Guided Diffusion Reinforcement Learning
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
