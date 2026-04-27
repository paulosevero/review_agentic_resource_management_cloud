---
id: "paper-1314"
title: "Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing"
authors: ["You, Feiran", "Du, Hongyang", "Kang, Jiawen", "Ni, Wei", "Niyato, Dusit", "Jamalipour, Abbas"]
year: 2024
venue: "Proceedings - 2024 IEEE Smart World Congress, SWC 2024 - 2024 IEEE Ubiquitous Intelligence and Computing, Autonomous and Trusted Computing, Digital Twin, Metaverse, Privacy Computing and Data Security, Scalable Computing and Communications"
venue_type: "conference"
doi: "10.1109/SWC62898.2024.00337"
url: "https://www.scopus.com/pages/publications/105002235341?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2209--2214"
keywords: ["generative diffusion models", "Multi-access edge computing", "proximal policy optimization", "virtual reality"]
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
    human_decision: "include"
    human_justification: "Tem RL, mas também menciona GenAI. Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-1314 — Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing

## Metadata

- **Authors:** You, Feiran and Du, Hongyang and Kang, Jiawen and Ni, Wei and Niyato, Dusit and Jamalipour, Abbas
- **Year:** 2024
- **Venue:** Proceedings - 2024 IEEE Smart World Congress, SWC 2024 - 2024 IEEE Ubiquitous Intelligence and Computing, Autonomous and Trusted Computing, Digital Twin, Metaverse, Privacy Computing and Data Security, Scalable Computing and Communications
- **DOI:** 10.1109/SWC62898.2024.00337
- **URL:** https://www.scopus.com/pages/publications/105002235341?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2209--2214
- **Language:** English
- **Keywords:** generative diffusion models; Multi-access edge computing; proximal policy optimization; virtual reality

### Abstract

The rapid growth of Artificial Intelligence-Generated Content (AIGC) services has led to increased mobile user participation in related computations and interactions. This development has enabled AI-generated characters to interact with Virtual Reality (VR) users in real time, making the VR experience more interactive and personalized. In this paper, we consider an MEC system where VR users engage in AIGC services, focusing on the Generative Diffusion Model (GDM)based image generation tasks. Specifically, VR users initiate requests for computing resources, while computation offloading distributes the processing load across the MEC system. To manage AIGC edge computation offloading and cloudlet-VR user connections jointly, a Data Center Operator (DCO) employs a centralized Proximal Policy Optimization (PPO) algorithm. To protect VR users' privacy while preserving PPO functionality, we employ the Generative Diffusion Model (GDM), specifically the Denoising Diffusion Implicit Model (DDIM), which first introduces noise to the PPO state, then conducts a denoising process to recover the state information. We further employ Inverse Reinforcement Learning (IRL) to infer rewards for the recovered states, using expert demonstrations trained by the PPO. The similarity between PPO-generated rewards and IRL-inferred rewards is then computed. Simulation results demonstrate that our proposed approach successfully achieves computation offloading while protecting VR users' privacy within the PPO centralized management framework.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing
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
