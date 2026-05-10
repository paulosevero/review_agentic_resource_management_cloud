---
id: "paper-2472"
title: "Enabling Distributed Generative Artificial Intelligence in 6G: Mobile-Edge Generation"
authors: ["Zhong, Ruikang", "Mu, Xidong", "Jaber, Mona", "Liu, Yuanwei"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2024.3493611"
url: "https://www.scopus.com/pages/publications/86000437753?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6607--6620"
keywords: ["Deep learning (DL)", "generative artificial intelligence (GAI)", "image generation", "mobile-edge generation (MEG)"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2472 — Enabling Distributed Generative Artificial Intelligence in 6G: Mobile-Edge Generation

## Metadata

- **Authors:** Zhong, Ruikang and Mu, Xidong and Jaber, Mona and Liu, Yuanwei
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2024.3493611
- **URL:** https://www.scopus.com/pages/publications/86000437753?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6607--6620
- **Language:** English
- **Keywords:** Deep learning (DL); generative artificial intelligence (GAI); image generation; mobile-edge generation (MEG)

### Abstract

Mobile-edge generation (MEG) is an emerging technology that allows the network to meet the challenging traffic load expectations posed by the rise of generative artificial intelligence (GAI). A novel MEG model is proposed for deploying GAI models on edge servers (ESs) and user equipment (UE) to jointly complete text-to-image generation tasks. In the generation task, the ES and UE will cooperatively generate the image according to the text prompt given by the user. To enable the MEG, a pretrained latent diffusion model (LDM) is invoked to generate the latent feature, and an edge-inferencing MEG protocol is employed for data transmission exchange between the ES and the UE. A compression coding technique is proposed for compressing the latent features to produce seeds. Based on the above seed-enabled MEG model, an image quality optimization problem with energy constraint is formulated. The transmitting power of the seed is dynamically optimized by a deep reinforcement learning (DRL) agent over the fading channel. The proposed MEG-enabled text-to-image generation system is evaluated in terms of image quality and transmission overhead. The numerical results indicate that, compared to the conventional centralized generation-and-downloading scheme, the symbol number of the transmission of MEG is materially reduced. In addition, the proposed compression coding approach can improve the quality of generated images under low signal-to-noise ratio (SNR) conditions, and the DRL-enabled dynamic power control further improves the image quality under the energy constraint compared to static transmit power control.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Enabling Distributed Generative Artificial Intelligence in 6G: Mobile-Edge Generation

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Enabling Distributed Generative Artificial Intelligence in 6G: Mobile-Edge Generation
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Enabling Distributed Generative Artificial Intelligence in 6G: Mobile-Edge Generation
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
