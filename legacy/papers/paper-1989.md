---
id: "paper-1989"
title: "Generative AI on the Edge: Architecture and Performance Evaluation"
authors: ["Nezami, Zeinab", "Hafeez, Maryam", "Djemame, Karim", "Zaidi, Syed Ali Raza"]
year: 2025
venue: "IEEE International Conference on Communications"
venue_type: "conference"
doi: "10.1109/ICC52391.2025.11161569"
url: "https://www.scopus.com/pages/publications/105018453107?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4595--4602"
keywords: ["6G", "Edge AI", "GenAI", "Kubernetes", "Large Language Model"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1989 — Generative AI on the Edge: Architecture and Performance Evaluation

## Metadata

- **Authors:** Nezami, Zeinab and Hafeez, Maryam and Djemame, Karim and Zaidi, Syed Ali Raza
- **Year:** 2025
- **Venue:** IEEE International Conference on Communications
- **DOI:** 10.1109/ICC52391.2025.11161569
- **URL:** https://www.scopus.com/pages/publications/105018453107?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4595--4602
- **Language:** English
- **Keywords:** 6G; Edge AI; GenAI; Kubernetes; Large Language Model

### Abstract

6G's AI native vision of embedding advance intelligence in the network while bringing it closer to the user requires a systematic evaluation of Generative AI (GenAI) models on edge devices. Rapidly emerging solutions based on Open RAN (ORAN) and Network-in-aBox strongly advocate the use of low-cost, off-the-shelf components for simpler and efficient deployment, for example, in provisioning rural connectivity. In this context, conceptual architecture, hardware testbeds, and precise performance quantification of Large Language Models (LLMs) on off-theshelf edge devices remain largely unexplored. This research investigates computationally demanding LLM inference on a single commodity Raspberry Pi serving as an edge testbed for ORAN. We investigate various LLMs, including small, medium, and large models, on a Raspberry Pi 5 Cluster using a lightweight Kubernetes distribution (K3s) with modular prompting implementation. We study its feasibility and limitations by analyzing throughput, latency, accuracy, and efficiency. Our findings indicate that CPU-only deployment of lightweight models, such as Yi, Phi, and Llama3, can effectively support edge applications, achieving a generation throughput of 5 to 12 tokens per second with less than 50% CPU and RAM usage. We conclude that GenAI on the edge offers localized inference in remote or bandwidthconstrained environments in 6 G networks without reliance on cloud infrastructure.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Generative AI on the Edge: Architecture and Performance Evaluation

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Generative AI on the Edge: Architecture and Performance Evaluation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Generative AI on the Edge: Architecture and Performance Evaluation
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
