---
id: "paper-1765"
title: "Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System"
authors: ["Latif, Imran", "Newkirk, Alex C.", "Carbone, Matthew R.", "Munir, Arslan", "Lin, Yuewei", "Koomey, Jonathan", "Yu, Xi", "Dong, Zhihua"]
year: 2025
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2025.3554728"
url: "https://www.scopus.com/pages/publications/105003088186?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "61740--61747"
keywords: ["AI training", "GPU power measurements", "large language models", "sustainable computing"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1765 — Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System

## Metadata

- **Authors:** Latif, Imran and Newkirk, Alex C. and Carbone, Matthew R. and Munir, Arslan and Lin, Yuewei and Koomey, Jonathan and Yu, Xi and Dong, Zhihua
- **Year:** 2025
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2025.3554728
- **URL:** https://www.scopus.com/pages/publications/105003088186?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 61740--61747
- **Language:** English
- **Keywords:** AI training; GPU power measurements; large language models; sustainable computing

### Abstract

The expansion of artificial intelligence (AI) applications has driven substantial investment in computational infrastructure, especially by cloud computing providers. Quantifying the energy footprint of this infrastructure requires models parameterized by the power demand of AI hardware during training. In this work, we measured the instantaneous power draw of an 8-GPU NVIDIA H100 HGX node during the training of open-source image classifier (ResNet) and large-language models (Llama2-13b). We characterize power demand for a single node configuration, providing foundational data for future multi-node studies. The maximum observed power draw was approximately 8.4 kW, 18% lower than the manufacturer-rated 10.2 kW, even with GPUs near full utilization. Holding model architecture constant, increasing batch size from 512 to 4096 images for ResNet reduced total training energy consumption by a factor of 4. These findings can inform capacity planning for data center operators and energy use estimates by researchers. Future work will investigate the impact of cooling technology and carbon-aware scheduling on AI workload energy consumption. © 2013 IEEE.

## 04 — Title Screening

**Title:** Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Single-Node Power Demand During AI Training: Measurements on an 8-GPU NVIDIA H100 System
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
