---
id: "paper-841"
title: "Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing"
authors: ["Cai, Fenglong", "Yuan, Dong", "Yang, Zhe", "Cui, Lizhen"]
year: 2024
venue: "Proceedings of the IEEE International Conference on Web Services, ICWS"
venue_type: "conference"
doi: "10.1109/ICWS62655.2024.00099"
url: "https://www.scopus.com/pages/publications/85210263346?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "799--809"
keywords: ["collaborative framework", "edge computing", "large language model", "online scheduling algorithm", "service"]
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
    human_justification: "LLM as workload"

---

# paper-841 — Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing

## Metadata

- **Authors:** Cai, Fenglong and Yuan, Dong and Yang, Zhe and Cui, Lizhen
- **Year:** 2024
- **Venue:** Proceedings of the IEEE International Conference on Web Services, ICWS
- **DOI:** 10.1109/ICWS62655.2024.00099
- **URL:** https://www.scopus.com/pages/publications/85210263346?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 799--809
- **Language:** English
- **Keywords:** collaborative framework; edge computing; large language model; online scheduling algorithm; service

### Abstract

The rapid advancement and extensive implementation of Large Language Models (LLMs) are milestones in the realm of artificial intelligence. Although Parameter-Efficient Transfer Learning (PETL), a.k.a. Adapter, methods have reduced the barrier for fine-tuning and inference on LLMs, it becomes a challenge to efficiently deploy and fine-tuning different adapter models needed for massive AI applications. With the popularity of SoC chips, the computing power of edge devices has improved significantly. To meet the computational resources required by LLM applications and improve quality of service (QoS), we propose Edge-LLM, a server-node collaboration framework for large-scale language model serving, to efficiently utilize edge resources to accelerate LLM fine-tuning and inference in resource-constrained scenarios. In the framework, we implement an adaptive quantization strategy, FM cache mechanism, and value density first (VDF) scheduling algorithm to reduce GPU overhead and accelerate LLM computation. The experimental results demonstrate that Edge-LLM can significantly improve overall computational speed by a factor of 17, decrease the number of tasks experiencing timeouts by 63%, and reduce GPU overhead by up to 43%.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge-LLM: A Collaborative Framework for Large Language Model Serving in Edge Computing
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
