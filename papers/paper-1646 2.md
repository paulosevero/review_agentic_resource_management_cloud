---
id: "paper-1646"
title: "Aging-aware CPU Core Management for Embodied Carbon Amortization in Cloud LLM Inference"
authors: ["Hewage, Tharindu B.", "Ilager, Shashikant", "Read, Maria Rodriguez", "Buyya, Rajkumar"]
year: 2025
venue: "E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems"
venue_type: "conference"
doi: "10.1145/3679240.3734608"
url: "https://www.scopus.com/pages/publications/105016349535?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "43--55"
keywords: ["CPU Aging", "Embodied Carbon Reduction", "LLM Inference", "Sustainable AI"]
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

# paper-1646 — Aging-aware CPU Core Management for Embodied Carbon Amortization in Cloud LLM Inference

## Metadata

- **Authors:** Hewage, Tharindu B. and Ilager, Shashikant and Read, Maria Rodriguez and Buyya, Rajkumar
- **Year:** 2025
- **Venue:** E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems
- **DOI:** 10.1145/3679240.3734608
- **URL:** https://www.scopus.com/pages/publications/105016349535?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 43--55
- **Language:** English
- **Keywords:** CPU Aging; Embodied Carbon Reduction; LLM Inference; Sustainable AI

### Abstract

Broad adoption of Large Language Models (LLM) demands rapid expansions of cloud LLM inference clusters, leading to the accumulation of embodied carbon−the emissions from manufacturing and supplying IT assets−that mostly concentrate on inference server CPU. This paper delves into the challenges of sustainable growth of cloud LLM inference, emphasizing extended amortization of CPU embodied over an increased lifespan. Given the reliability risks of silicon aging, we propose an aging-aware CPU core management technique to delay CPU aging effects, allowing the cluster operator to safely increase CPU life. Our technique exploits CPU underutilization patterns that we uncover in cloud LLM inference by halting aging in unused cores and even-outing aging in active cores via selective deep idling and aging-aware inference task allocation. Through extensive simulations using real-world Azure inference traces and an extended LLM cluster simulator from Microsoft, we show superior performance of our technique over existing methods with an estimated 37.67% reduction in yearly embodied carbon emissions through p99 performance of managing CPU aging effects, a 77% reduction in CPU underutilization, and less than 10% impact to the inference service quality. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Aging-aware CPU Core Management for Embodied Carbon Amortization in Cloud LLM Inference

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Aging-aware CPU Core Management for Embodied Carbon Amortization in Cloud LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Aging-aware CPU Core Management for Embodied Carbon Amortization in Cloud LLM Inference
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
