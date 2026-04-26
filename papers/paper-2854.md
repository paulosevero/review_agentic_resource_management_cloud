---
id: "paper-2854"
title: "Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation"
authors: ["Wu, Bing", "Zou, Sai", "Liwang, Minghui", "Ni, Wei", "Wang, Xianbin", "Tian, Youliang"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3678546"
url: "https://www.scopus.com/pages/publications/105034780951?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["6\u00a0G edge intelligence", "application intent", "knowledge distillation", "knowledge graph", "large language model", "network service request"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2854 — Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation

## Metadata

- **Authors:** Wu, Bing and Zou, Sai and Liwang, Minghui and Ni, Wei and Wang, Xianbin and Tian, Youliang
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3678546
- **URL:** https://www.scopus.com/pages/publications/105034780951?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 6 G edge intelligence; application intent; knowledge distillation; knowledge graph; large language model; network service request

### Abstract

Future 6 G networks are envisaged to tightly integrate communication, sensing, and computing, demanding real-time, intent-driven intelligence at the edge. While large language models (LLMs) excel in intent recognition and semantic reasoning, their application to real-time network lifecycle management at the edge is limited by heterogeneous application intents (APPIs), dynamic network conditions, and severe resource constraints. This paper proposes a novel lightweight LLM architecture, KGLlama-KD, that synergizes knowledge graphs (KGs) with knowledge distillation (KD) to enable intent-driven networking and enhance 6 G edge intelligence. Specifically, a KG is constructed to formally describe the relationships among application scenarios, functional primitives, performance requirements within APPIs, and the correspondences between APPIs and network service requests (NSRs), thereby producing a structured intent training dataset. Building upon the Llama 3 foundation model, a two-phase optimization framework is designed to support lightweight edge deployment while preserving translation fidelity. The LLM is first fine-tuned with KG guidance and compressed via KD in the cloud, and then deployed on resource-constrained edge nodes to perform real-time, accurate, and efficient APPIs interpretation. Experiments validate that KGLlama-KD achieves 95% accuracy for APPI understanding, surpassing DeepSeek and Qwen by an average of 8%. The distilled model reduces inference latency by 60% compared to full-scale LLMs, fulfilling the sub-100 ms requirement for 6 G latency-sensitive services. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation
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
