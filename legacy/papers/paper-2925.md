---
id: "paper-2925"
title: "AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training"
authors: ["Zhao, Boran", "Liu, Hetian", "Yuan, Zihang", "Zhu, Li", "Yang, Fan", "Xie, Lina", "Xia, Tian", "Zhao, Wenzhe", "Ren, Pengju"]
year: 2026
venue: "IEEE Transactions on Circuits and Systems I: Regular Papers"
venue_type: "journal"
doi: "10.1109/TCSI.2026.3667183"
url: "https://www.scopus.com/pages/publications/105032857105?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Dataset sampling", "DNN training", "edge computing", "hardware/software co-design", "parallel circuits"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2925 — AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training

## Metadata

- **Authors:** Zhao, Boran and Liu, Hetian and Yuan, Zihang and Zhu, Li and Yang, Fan and Xie, Lina and Xia, Tian and Zhao, Wenzhe and Ren, Pengju
- **Year:** 2026
- **Venue:** IEEE Transactions on Circuits and Systems I: Regular Papers
- **DOI:** 10.1109/TCSI.2026.3667183
- **URL:** https://www.scopus.com/pages/publications/105032857105?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Dataset sampling; DNN training; edge computing; hardware/software co-design; parallel circuits

### Abstract

Training deep neural networks (DNNs) on edge devices faces challenges due to the large-scale datasets required, which are costly for edge devices, especially in large language model (LLM) tasks. To address this, a DNN-free method called Near-Memory Sampling (NMS) has been introduced. NMS reduces dimensionality and performs exemplar sampling in the reduced space, avoiding architectural bias and improving generalization. However, NMS has two limitations: 1) The mismatch between the search method and the non-monotonic property of the perplexity error function leads to the emergence of outliers; 2) Key parameter (i.e., target perplexity) is selected empirically, introducing arbitrariness and leading to uneven sampling. These two issues lead to representative bias of exemplars, resulting in degraded accuracy. To overcome these, we propose AdapSNE, which integrates the Fireworks Algorithm (FWA) for efficient non-monotonic search to avoid outliers and uses entropy-guided optimization for uniform sampling, ensuring representative training samples. To reduce the cost of iterative computations, we design an accelerator with custom dataflow and time-multiplexing mechanisms. Experimental results show that AdapSNE outperforms state-of-the-art methods, including both DNN-based (DQAS) and DNN-free (NMS) approaches, across small-scale image datasets, large-scale datasets, and the MMLU benchmark for LLM tasks. © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** AdapSNE: Adaptive Fireworks-Optimized and Entropy-Guided Dataset Sampling for Edge DNN Training
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
