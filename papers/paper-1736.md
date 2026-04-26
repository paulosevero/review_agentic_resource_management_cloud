---
id: "paper-1736"
title: "Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster"
authors: ["Kim, Seoyoung", "Ha, Jiwon", "Kim, Yoonhee"]
year: 2025
venue: "Cluster Computing"
venue_type: "journal"
doi: "10.1007/s10586-025-05216-0"
url: "https://www.scopus.com/pages/publications/105014810871?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Affinity-aware", "Deep Learning Inference", "Heterogeneous GPU Cluster", "Machine Learning", "Online-learning", "Resource Scheduling"]
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

# paper-1736 — Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster

## Metadata

- **Authors:** Kim, Seoyoung and Ha, Jiwon and Kim, Yoonhee
- **Year:** 2025
- **Venue:** Cluster Computing
- **DOI:** 10.1007/s10586-025-05216-0
- **URL:** https://www.scopus.com/pages/publications/105014810871?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Affinity-aware; Deep Learning Inference; Heterogeneous GPU Cluster; Machine Learning; Online-learning; Resource Scheduling

### Abstract

With rapid advancements in AI, GPU accelerator technology is evolving, leading to an increase in heterogeneous computing nodes within data centers. This necessitates schedulers that can identify and efficiently manage diverse resources to dynamically meet application demands. For latency-sensitive tasks such as deep learning inference, imprecise GPU scheduling can cause resource interference, degrading both application performance and overall GPU utilization. The rise of NLP and large language models (LLMs) has heightened the focus on balancing throughput and latency. However, dynamic loads on specific resources can lead to performance degradation due to head-of-line blocking. Consequently, proactive resource management is essential to reduce costs while ensuring quality of service (QoS) and maintaining energy efficiency. This paper introduces OLTunes, a cluster-level scheduling system for deep learning inference models that integrates streaming and batch methods to efficiently manage both online and offline models. By leveraging FM-FTML, an online learning technique, OLTunes optimizes runtime environments and resource allocation to meet user SLAs through prediction and optimization. It groups tasks based on their characteristics and model variants to minimize interference, ensuring complementary affinities. It also automatically adjusts resources and configurations to improve performance and reduce resource fragmentation. Performance experiments on a heterogeneous GPU cluster demonstrated a 58% average improvement in GPU utilization, up to 49% reduction in p99 tail latency, and a 61% increase in throughput. It also achieved approximately 84.6% energy savings with a maximum accuracy loss of 4% and reduced latency-sensitive SLO violations by up to 92% compared to other baselines, ensuring end-to-end QoS. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

## 04 — Title Screening

**Title:** Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster
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
