---
id: "paper-2504"
title: "Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence"
authors: ["Algawiaz, Danah"]
year: 2026
venue: "Scientific Reports"
venue_type: "journal"
doi: "10.1038/s41598-026-42981-3"
url: "https://www.scopus.com/pages/publications/105035879811?origin=resultslist"
publisher: "Nature Research"
pages: ""
keywords: ["Attention mechanism", "Edge computing", "Hallucination detection", "Knowledge distillation", "Latency reduction", "Real-time inference", "Transformer optimisation"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-2504 — Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence

## Metadata

- **Authors:** Algawiaz, Danah
- **Year:** 2026
- **Venue:** Scientific Reports
- **DOI:** 10.1038/s41598-026-42981-3
- **URL:** https://www.scopus.com/pages/publications/105035879811?origin=resultslist
- **Publisher:** Nature Research
- **Pages:** 
- **Language:** English
- **Keywords:** Attention mechanism; Edge computing; Hallucination detection; Knowledge distillation; Latency reduction; Real-time inference; Transformer optimisation

### Abstract

Transformer architectures and large language models remain competitive across a broad range of AI tasks, making them challenging to deploy in resource-constrained edge computing environments due to high resource demands and the generation of erroneous or fake outputs (hallucinations). In this paper, a single scheme, HALL-OPT, is proposed to address both latency detection and reduction in hallucination for real-time edge intelligence. The paper presents three main elements of the framework, namely, (1) a dual-stream hallucination detector that analyses internal attention behaviour, (2) an adaptive token-pruning system, which decodes and extracts the necessary context at minimal computation, and (3) a lightweight edge-optimized transformer obtained by knowledge distillation. On SQuAD 2.0 and CNN/DailyMail, HALL-OPT detects hallucinations accurately at 94.3% and achieves a 67.8% reduction in inference latency with only a 2.1% decrease in accuracy compared to the BERT-base model. The system (when deployed on edge hardware) provides sub-50 ms response times while consuming 43% less energy. It is appropriate for real-time applications in industrial IoT, autonomous systems, healthcare monitoring, and other applications where low latency is critical. Existing transformer optimisation and hallucination mitigation approaches treat reliability and Efficiency as separate objectives, limiting their applicability in real-time edge environments. HALL-OPT uniquely integrates hallucination-aware attention, adaptive pruning, and edge-oriented optimisation into a single unified framework, enabling simultaneous reductions in hallucination, latency, and energy consumption. This integrated design distinguishes HALL-OPT from prior work that optimises accuracy or Efficiency in isolation. © The Author(s) 2026.

## 04 — Title Screening

**Title:** Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence
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
