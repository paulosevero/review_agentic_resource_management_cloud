---
id: "paper-2206"
title: "Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF"
authors: ["Tatsumi, Riku", "Mizutani, Kimihiro"]
year: 2025
venue: "2025 IEEE VTS Asia Pacific Wireless Communications Symposium, APWCS 2025"
venue_type: "conference"
doi: "10.1109/APWCS67981.2025.11151933"
url: "https://www.scopus.com/pages/publications/105017688649?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["containerized streaming", "eBPF", "mobile edge computing", "system call monitoring"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2206 — Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF

## Metadata

- **Authors:** Tatsumi, Riku and Mizutani, Kimihiro
- **Year:** 2025
- **Venue:** 2025 IEEE VTS Asia Pacific Wireless Communications Symposium, APWCS 2025
- **DOI:** 10.1109/APWCS67981.2025.11151933
- **URL:** https://www.scopus.com/pages/publications/105017688649?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** containerized streaming; eBPF; mobile edge computing; system call monitoring

### Abstract

Container-based streaming services are increasingly deployed at the mobile edge to deliver low-latency content to users. However, understanding and optimizing their runtime performance remains challenging due to the complexity of system-level interactions in containerized environments. In this paper, we present a lightweight performance analysis framework using eBPF to monitor fine-grained system call metrics in containerized streaming cache servers. Our system collects approximately 360 kernel-level metrics from running containers at one-second intervals and correlates them with chunk-level download time observed at the reverse proxy.We formulate a regression problem to predict download latency using these metrics and evaluate four machine learning approaches: linear regression, ridge regression, random forest regression, and histogram-based gradient boosting regression. Experimental results show that the histogram-based gradient boosting model achieves the highest prediction accuracy with a mean squared error of 2.26 × 10<sup>-4</sup>. Feature importance analysis further reveals that a small subset of system calls contributes most to performance variability, suggesting opportunities for dimensionality reduction and lightweight modeling.Our findings demonstrate that eBPF-based monitoring, combined with regression analysis, offers a practical and accurate solution for understanding the performance behavior of containerized edge streaming systems. The proposed framework is readily extensible to other low-latency services such as LLM inference clusters and GPU-intensive workloads.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
