---
id: "paper-1898"
title: "ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models"
authors: ["Liu, Mingxuan", "Gu, Jianhua", "Zhao, Tianhai"]
year: 2025
venue: "Proceedings of the IEEE International Conference on Web Services, ICWS"
venue_type: "conference"
doi: "10.1109/ICWS67624.2025.00045"
url: "https://www.scopus.com/pages/publications/105018796381?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "305--315"
keywords: ["GPU Management", "Large Language Model", "LLM Inference", "Prefill-Decoding Disaggregation", "RDMA", "Remote Fork", "Serverless Computing"]
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

# paper-1898 — ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models

## Metadata

- **Authors:** Liu, Mingxuan and Gu, Jianhua and Zhao, Tianhai
- **Year:** 2025
- **Venue:** Proceedings of the IEEE International Conference on Web Services, ICWS
- **DOI:** 10.1109/ICWS67624.2025.00045
- **URL:** https://www.scopus.com/pages/publications/105018796381?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 305--315
- **Language:** English
- **Keywords:** GPU Management; Large Language Model; LLM Inference; Prefill-Decoding Disaggregation; RDMA; Remote Fork; Serverless Computing

### Abstract

Large Language Model (LLM) inference suffers from inefficiencies in coupled prefill (P) and decoding (D) phases, leading to resource underutilization and scheduling bottlenecks. While disaggregated P-D architectures address this by isolating phases across asymmetric clusters, serverless deployments introduce critical challenges: cold-start latency during autoscaling and costly intermediate state transfers (e.g., KV cache) between distributed prefill and decoding instances. We present ServerlessPD, a system that co-designs remote fork with RDMA to enable near-instant autoscaling and zero-copy state transferring for serverless LLM inference. ServerlessPD introduces a RDMA-based OS kernel-integrated primitive that remotely forks active prefill instances into decoding instances across machines, bypassing cold starts by reusing pre-materialized GPU states, which grants child containers direct copy-on-write access to parent GPU memory. The system further employs GPU context interception to efficiently capture and replicate execution states, ensuring seamless state transfer. To optimize resource utilization, ServerlessPD integrates a dynamic launch-point algorithm that schedules fork operations based on real-time prefill-decoding dynamics, minimizing idle time and overlapping computation with state transfers. ServerlessPD demonstrates that RDMA-codeigned remote fork can unlock near-instant autoscaling and efficient state disaggregation for LLM serving. © 2025 IEEE.

## 04 — Title Screening

**Title:** ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models
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
