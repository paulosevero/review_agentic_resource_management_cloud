---
id: "paper-2881"
title: "LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things"
authors: ["Yang, Qingwen", "Li, Zhi", "Tang, Jiawei", "Liu, Yanyi", "Guo, Tiezheng", "Wen, Yingyou"]
year: 2026
venue: "Computers, Materials and Continua"
venue_type: "journal"
doi: "10.32604/cmc.2025.074384"
url: "https://www.scopus.com/pages/publications/105032721172?origin=resultslist"
publisher: "Tech Science Press"
pages: ""
keywords: ["edge computing", "Industrial internet of things", "LLM-based agents", "small language models"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2881 — LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things

## Metadata

- **Authors:** Yang, Qingwen and Li, Zhi and Tang, Jiawei and Liu, Yanyi and Guo, Tiezheng and Wen, Yingyou
- **Year:** 2026
- **Venue:** Computers, Materials and Continua
- **DOI:** 10.32604/cmc.2025.074384
- **URL:** https://www.scopus.com/pages/publications/105032721172?origin=resultslist
- **Publisher:** Tech Science Press
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; Industrial internet of things; LLM-based agents; small language models

### Abstract

Deploying Large Language Model (LLM)-based agents in the Industrial Internet of Things (IIoT) presents significant challenges, including high latency from cloud-based APIs, data privacy concerns, and the infeasibility of deploying monolithic models on resource-constrained edge devices. While smaller models (SLMs) are suitable for edge deployment, they often lack the reasoning power for complex, multi-step tasks. To address these issues, this paper introduces LEAF, a Lightweight Edge Agent Framework designed for efficiently executing complex tasks at the edge. LEAF employs a novel architecture where multiple expert SLMs—specialized for planning, execution, and interaction—work in concert, decomposing complex problems into manageable sub-tasks. To mitigate the resource overhead of this multi-model approach, LEAF implements an efficient parameter-sharing scheme based on Scalable Low-Rank Adaptation (S-LoRA). We introduce a two-stage training strategy combining Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) to significantly enhance each expert’s capabilities. Furthermore, a Finite State Machine (FSM)-based decision engine orchestrates the workflow, uniquely balancing deterministic control with intelligent flexibility, making it ideal for industrial environments that demand both reliability and adaptability. Experiments across diverse IIoT scenarios demonstrate that LEAF significantly outperforms baseline methods in both task success rate and user satisfaction. Notably, our fine-tuned 4-billion-parameter model achieves a task success rate over 90% in complex IIoT scenarios, demonstrating LEAF’s ability to deliver powerful and efficient autonomy at the industrial edge. Copyright © 2026 The Authors.

## 04 — Title Screening

**Title:** LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things
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
