---
id: "paper-1133"
title: "LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators"
authors: ["Prieto-Sibaja, Luis D.", "Leon-Vega, Luis G.", "Leon-Vega, Indra", "Castro-Godinez, Jorge", "Cozzini, Stefano"]
year: 2024
venue: "Proceedings of the IEEE Central America and Panama Convention, CONCAPAN"
venue_type: "conference"
doi: "10.1109/CONCAPAN63470.2024.10933896"
url: "https://www.scopus.com/pages/publications/105005866600?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Cloud Computing", "Edge Computing", "Field Programmable Gate Arrays", "Hardware Acceleration", "High Performance Computing", "Large Language Models"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1133 — LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators

## Metadata

- **Authors:** Prieto-Sibaja, Luis D. and Leon-Vega, Luis G. and Leon-Vega, Indra and Castro-Godinez, Jorge and Cozzini, Stefano
- **Year:** 2024
- **Venue:** Proceedings of the IEEE Central America and Panama Convention, CONCAPAN
- **DOI:** 10.1109/CONCAPAN63470.2024.10933896
- **URL:** https://www.scopus.com/pages/publications/105005866600?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud Computing; Edge Computing; Field Programmable Gate Arrays; Hardware Acceleration; High Performance Computing; Large Language Models

### Abstract

Large Language Models (LLMs) have emerged as the leading technique in Natural Language Processing due to their remarkable capabilities. These models are exceptionally complex, often utilising billions of parameters and consuming tens of gigabytes of memory unless optimised. Typically, LLMs are trained and accelerated using general-purpose Graphics Processing Units (GPUs), with a single inference potentially occupying an entire GPU. Consequently, cloud services may require hundreds of GPUs to deliver high-quality AI assistant services. This demand for extensive hardware acceleration allows exploring alternative architectures that offer improved execution time and energy efficiency.This study evaluates Field-Programmable Gate Arrays (FP-GAs), renowned for their flexibility and efficiency, to accelerate LLMs. We specifically compare the resource consumption and latency of two distinct architectures: layer and spatial accelerators. Analysing the Llama 2-7B model, we identified potential optimisation opportunities within its composition and operational graphs. Our most successful implementations demonstrate a performance improvement ranging from 1.37× to 10.98× over two AMD EPYC processors with 64 cores each. Moreover, our results indicate that, with further refinement, FPGAs have the potential to surpass GPU performance for LLM inference, showcasing their feasibility as a viable alternative for this demanding application. © 2024 IEEE.

## 04 — Title Screening

**Title:** LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LLM Acceleration on FPGAs: A Comparative Study of Layer and Spatial Accelerators
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
