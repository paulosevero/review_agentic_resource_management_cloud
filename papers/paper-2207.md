---
id: "paper-2207"
title: "Twill: Scheduling Compound AI Systems on Heterogeneous Mobile Edge Platforms"
authors: ["Taufique, Zain", "Vyas, Aman", "Miele, Antonio", "Liljeberg, Pasi", "Kanduri, Anil"]
year: 2025
venue: "IEEE/ACM International Conference on Computer-Aided Design, Digest of Technical Papers, ICCAD"
venue_type: "conference"
doi: "10.1109/ICCAD66269.2025.11240767"
url: "https://www.scopus.com/pages/publications/105029389333?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Deep Neural Networks", "Inference and Compound AI", "Large Language Models", "transformers"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2207 — Twill: Scheduling Compound AI Systems on Heterogeneous Mobile Edge Platforms

## Metadata

- **Authors:** Taufique, Zain and Vyas, Aman and Miele, Antonio and Liljeberg, Pasi and Kanduri, Anil
- **Year:** 2025
- **Venue:** IEEE/ACM International Conference on Computer-Aided Design, Digest of Technical Papers, ICCAD
- **DOI:** 10.1109/ICCAD66269.2025.11240767
- **URL:** https://www.scopus.com/pages/publications/105029389333?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Deep Neural Networks; Inference and Compound AI; Large Language Models; transformers

### Abstract

Compound AI (cAI) systems chain multiple AI models to solve complex problems. cAI systems are typically composed of deep neural networks (DNNs), transformers, and large language models (LLMs), exhibiting a high degree of computational diversity and dynamic workload variation. Deploying cAI services on mobile edge platforms poses a significant challenge in scheduling concurrent DNN-transformer inference tasks, which arrive dynamically in an unknown sequence. Existing mobile edge AI inference strategies manage multi-DNN or transformer-only workloads, relying on design-time profiling, and cannot handle concurrent inference of DNNs and transformers required by cAI systems. In this work, we address the challenge of scheduling cAI systems on heterogeneous mobile edge platforms. We present Twill, a run-time framework to handle concurrent inference requests of cAI workloads through task affinity-aware cluster mapping and migration, priority-aware task freezing/unfreezing, and Dynamic Voltage/Frequency Scaling (DVFS), while minimizing inference latency within power budgets. We implement and deploy our Twill framework on the Nvidia Jetson Orin NX platform. We evaluate Twill against state-of-the-art edge AI inference techniques over contemporary DNNs and LLMs, reducing inference latency by 54% on average, while honoring power budgets.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Twill: Scheduling Compound AI Systems on Heterogeneous Mobile Edge Platforms

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Twill: Scheduling Compound AI Systems on Heterogeneous Mobile Edge Platforms
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Twill: Scheduling Compound AI Systems on Heterogeneous Mobile Edge Platforms
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
