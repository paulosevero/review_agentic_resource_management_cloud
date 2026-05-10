---
id: "paper-2677"
title: "ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices"
authors: ["Lin, Yufei", "Xu, Tianxiang", "Ye, Chengwei", "Zhang, Huanzhen", "Wang, Kangsheng"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-95-3055-7_1"
url: "https://www.scopus.com/pages/publications/105023163358?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "1--11"
keywords: ["Adaptive Partitioning", "Automotive Edge Devices", "Inference Optimization", "Large Language Models", "Latency Reduction"]
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
    human_justification: "LLM as workload"

---

# paper-2677 — ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices

## Metadata

- **Authors:** Lin, Yufei and Xu, Tianxiang and Ye, Chengwei and Zhang, Huanzhen and Wang, Kangsheng
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-95-3055-7_1
- **URL:** https://www.scopus.com/pages/publications/105023163358?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 1--11
- **Language:** English
- **Keywords:** Adaptive Partitioning; Automotive Edge Devices; Inference Optimization; Large Language Models; Latency Reduction

### Abstract

Large language models (LLMs) increasingly drive intelligent services within automotive edge computing. However, deploying these models efficiently remains challenging due to diverse hardware setups and limited computational resources typical of automotive edge environments. Existing deployment strategies often disregard hardware diversity, resulting in suboptimal resource use and compromised performance, particularly under peak inference workloads. Consequently, computing elements like CPUs and integrated GPUs are frequently idle, with tasks excessively dependent on discrete GPUs. To address this, we propose a dynamic inference partitioning strategy named Hardware-Aware Dynamic Scheduling (ACL), tailored specifically for automotive edge computing. Our approach leverages the inherent distinction between initial token-processing phases (prefill) and subsequent token generation phases (decode) within LLM inference. By adaptively distributing these phases across heterogeneous hardware units, ACL maximizes resource utilization and balances workloads effectively. Empirical evaluations indicate that ACL significantly enhances inference performance. Furthermore, our framework demonstrates robust efficiency improvements consistently across various LLM architectures, highlighting its adaptability and effectiveness in heterogeneous automotive computing scenarios. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

## 04 — Title Screening

**Title:** ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices
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
