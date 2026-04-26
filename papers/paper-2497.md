---
id: "paper-2497"
title: "From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection"
authors: ["Adjewa, Fr\u00e9d\u00e9ric", "Esseghir, Moez", "Merghem-Boulahia, Le\u00efla"]
year: 2026
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s26020356"
url: "https://www.scopus.com/pages/publications/105028792177?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["artificial intelligence of things", "BERT", "computation offloading", "edge computing", "efficient intrusion detection", "semantic embeddings"]
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

# paper-2497 — From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection

## Metadata

- **Authors:** Adjewa, Frédéric and Esseghir, Moez and Merghem-Boulahia, Leïla
- **Year:** 2026
- **Venue:** Sensors
- **DOI:** 10.3390/s26020356
- **URL:** https://www.scopus.com/pages/publications/105028792177?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** artificial intelligence of things; BERT; computation offloading; edge computing; efficient intrusion detection; semantic embeddings

### Abstract

The convergence of Artificial Intelligence (AI) and the Internet of Things (IoT) is enabling a new class of intelligent applications. Specifically, Large Language Models (LLMs) are emerging as powerful tools not only for natural language understanding but also for enhancing IoT security. However, the integration of these computationally intensive models into resource-constrained IoT environments presents significant challenges. This paper provides an in-depth examination of how LLMs can be adapted to secure IoT ecosystems. We identify key application areas, discuss major challenges, and propose optimization strategies for resource-limited settings. Our primary contribution is a novel collaborative embeddings offloading mechanism for IoT intrusion detection named SEED (Semantic Embeddings for Efficient Detection). This system leverages a lightweight, fine-tuned BERT model, chosen for its proven contextual and semantic understanding of sequences, to generate rich network embeddings at the edge. A compact neural network deployed on the end-device then queries these embeddings to assess network flow normality. This architecture alleviates the computational burden of running a full transformer on the device while capitalizing on its analytical performance. Our optimized BERT model is reduced by approximately 90% from its original size, now representing approximately 41 MB, suitable for the Edge. The resulting compact neural network is a mere 137 KB, appropriate for the IoT devices. This system achieves 99.9% detection accuracy with an average inference time of under 70 ms on a standard CPU. Finally, the paper discusses the ethical implications of LLM-IoT integration and evaluates the resilience of LLMs in dynamic and adversarial environments. © 2026 by the authors.

## 04 — Title Screening

**Title:** From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection
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
