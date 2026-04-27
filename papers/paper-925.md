---
id: "paper-925"
title: "Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators"
authors: ["Geens, Robin", "Shi, Man", "Symons, Arne", "Fang, Chao", "Verhelst, Marian"]
year: 2024
venue: "International System on Chip Conference"
venue_type: "conference"
doi: "10.1109/SOCC62300.2024.10737844"
url: "https://www.scopus.com/pages/publications/85210589021?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["Computer graphics equipment", "Decoding", "Edge computing", "Graphics processing unit", "Photomapping", "Problem oriented languages", "Cloud-based", "Cost models", "Energy cost", "Energy efficient", "GPU computing", "Hardware accelerators", "Hardware architecture", "High energy consumption", "Language model", "Model inference", "Carbon footprint"]
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
    human_justification: "LLM as workload"

---

# paper-925 — Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators

## Metadata

- **Authors:** Geens, Robin and Shi, Man and Symons, Arne and Fang, Chao and Verhelst, Marian
- **Year:** 2024
- **Venue:** International System on Chip Conference
- **DOI:** 10.1109/SOCC62300.2024.10737844
- **URL:** https://www.scopus.com/pages/publications/85210589021?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** Computer graphics equipment; Decoding; Edge computing; Graphics processing unit; Photomapping; Problem oriented languages; Cloud-based; Cost models; Energy cost; Energy efficient; GPU computing; Hardware accelerators; Hardware architecture; High energy consumption; Language model; Model inference; Carbon footprint

### Abstract

The rise of Large Language Models (LLMs) has significantly escalated the demand for efficient LLM inference, primarily fulfilled through cloud-based GPU computing. This approach, while effective, is associated with high energy consumption resulting in large operating expenses and considerable carbon footprints. In the meantime, growing privacy concerns advocate for inference on edge devices, which are constrained by a limited battery capacity. Both cloud and edge scenarios necessitate energy-efficient LLM inference strategies.This paper addresses the urgent need for energy-efficient inference by proposing an open-source framework designed to model LLM workloads on dedicated accelerators. Our framework facilitates early identification of energy bottlenecks through rapid modeling of the execution efficiency of a wide range of LLMs on diverse hardware architectures. Key innovations include a PyTorch-based generalized LLM template to easily generate custom workload graphs, extensions of the ZigZag design space exploration framework and techniques to significantly speed up simulation time at a negligible loss of accuracy. Using a representative hardware architecture, we conduct three case studies to reveal critical energy bottlenecks in Llama2-7B inference, revealing that 1) memory-bound computing in the decode stage is detrimental not only for the latency, but also for the energy cost; 2) aggressive weight-only quantization can reduce the energy cost by 4.6 × and shift the bottleneck from weight fetching to the attention mechanism; 3) in edge scenarios, the relative energy cost of the prefill stage is more significant, encouraging efforts to optimize both prefill and decode stage. Our framework is available open-source at github.com/KULeuven-MICAS/zigzag-llm.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators
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
