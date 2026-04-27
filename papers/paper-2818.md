---
id: "paper-2818"
title: "AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units"
authors: ["Wang, Xinkai", "Zhuansun, Yiming", "Li, Chao", "Wang, Jing", "Hou, Xiaofeng", "Sun, Lingyu", "Wang, Luping", "Guo, Minyi"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-95-1021-4_17"
url: "https://www.scopus.com/pages/publications/105022150272?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "231--245"
keywords: ["CPU Efficiency", "Intel AMX", "LLM Serving"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2818 — AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units

## Metadata

- **Authors:** Wang, Xinkai and Zhuansun, Yiming and Li, Chao and Wang, Jing and Hou, Xiaofeng and Sun, Lingyu and Wang, Luping and Guo, Minyi
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-95-1021-4_17
- **URL:** https://www.scopus.com/pages/publications/105022150272?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 231--245
- **Language:** English
- **Keywords:** CPU Efficiency; Intel AMX; LLM Serving

### Abstract

Current data centers are accommodating more AI-based workloads, especially large-language model (LLM) training and serving in recent years. Given the limited count and significant energy consumption of expensive GPUs, cloud providers tend to utilize more cost-efficient processors for LLM serving, such as Intel scalable CPU equipped with acceleration units AMX. To understand the improvements, bottlenecks, and opportunities on this new platform, we first undertake a comprehensive characterization of LLM serving using AMX on two generations of modern CPUs with various memory devices. Our characterization reveals that the hardware and software behaviors of LLM serving on CPU are distinct from conventional cloud workloads and vary greatly. In this paper, we propose AsymServe to maximize LLM serving efficiency on scalable CPU platforms via handling software and hardware asymmetry. It adjusts hardware allocation and software configurations adaptively to maximize CPU performance-per-watt. Through extensive evaluation, we show that AsymServe improves LLM serving performance. Specifically, it achieves up to 1.71x faster first-token generation, 3.13x greater throughput, and 11.09x better energy efficiency. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

## 04 — Title Screening

**Title:** AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units
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
