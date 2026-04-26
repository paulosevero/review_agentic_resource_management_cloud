---
id: "paper-2330"
title: "Accelerating Mobile Edge Generation (MEG) by Constrained Learning"
authors: ["Xu, Xiaoxia", "Liu, Yuanwei", "Mu, Xidong", "Xing, Hong", "Nallanathan, Arumugam"]
year: 2025
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2025.3558975"
url: "https://www.scopus.com/pages/publications/105002678443?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1854--1869"
keywords: ["Artificial intelligence generated content (AIGC)", "edge artificial intelligence (AI)", "generative AI (GAI)", "mobile edge generation (MEG)", "reinforcement learning (RL)"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2330 — Accelerating Mobile Edge Generation (MEG) by Constrained Learning

## Metadata

- **Authors:** Xu, Xiaoxia and Liu, Yuanwei and Mu, Xidong and Xing, Hong and Nallanathan, Arumugam
- **Year:** 2025
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2025.3558975
- **URL:** https://www.scopus.com/pages/publications/105002678443?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1854--1869
- **Language:** English
- **Keywords:** Artificial intelligence generated content (AIGC); edge artificial intelligence (AI); generative AI (GAI); mobile edge generation (MEG); reinforcement learning (RL)

### Abstract

A novel mobile edge generation (MEG) framework is proposed for low-latency image generation on mobile devices. Exploiting a latent diffusion model (LDM) distributed across the edge server (ES) and the user equipment (UE), only low-dimension features need to be transmitted for creating artificial intelligence generative content (AIGC). Two novel modules, namely dynamic diffusion and feature merging, are conceived to compress the diffusion model and transmitted features, respectively. By jointly optimizing compression rates of denoising steps and feature merging, the image quality maximization problem is formulated subject to latency and energy consumption constraints. To address this problem in dynamic channel conditions, a low-complexity compression protocol is developed. First, a backbone LDM architecture is learned by offline distillation to support various compression options. Then, compression rates are predicted in online environment specific to channel and task features. To solve the resultant constrained Markov Decision Process (MDP), a constrained variational policy optimization (CVPO) based MEG algorithm, MEG-CVPO, is further developed to learn constraint-guaranteed optimization. Numerical results demonstrate that: 1) The proposed framework improves image distortions while reducing over 40% latency compared to conventional generation schemes. 2) MEG-CVPO stringently guarantee constraints and realizes a flexible trade-off between generation qualities and overheads. © 2015 IEEE.

## 04 — Title Screening

**Title:** Accelerating Mobile Edge Generation (MEG) by Constrained Learning

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Accelerating Mobile Edge Generation (MEG) by Constrained Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Accelerating Mobile Edge Generation (MEG) by Constrained Learning
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
