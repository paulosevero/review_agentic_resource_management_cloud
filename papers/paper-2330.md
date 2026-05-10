---
id: paper-2330
title: Accelerating Mobile Edge Generation (MEG) by Constrained Learning
authors:
- Xu, Xiaoxia
- Liu, Yuanwei
- Mu, Xidong
- Xing, Hong
- Nallanathan, Arumugam
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TCCN.2025.3558975
url: https://www.scopus.com/pages/publications/105002678443?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1854--1869
keywords:
- Artificial intelligence generated content (AIGC)
- edge artificial intelligence (AI)
- generative AI (GAI)
- mobile edge generation (MEG)
- reinforcement learning (RL)
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2330 — Accelerating Mobile Edge Generation (MEG) by Constrained Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A novel mobile edge generation (MEG) framework is proposed for low-latency image generation on mobile devices. Exploiting a latent diffusion model (LDM) distributed across the edge server (ES) and the user equipment (UE), only low-dimension features need to be transmitted for creating artificial intelligence generative content (AIGC). Two novel modules, namely dynamic diffusion and feature merging, are conceived to compress the diffusion model and transmitted features, respectively. By jointly optimizing compression rates of denoising steps and feature merging, the image quality maximization problem is formulated subject to latency and energy consumption constraints. To address this problem in dynamic channel conditions, a low-complexity compression protocol is developed. First, a backbone LDM architecture is learned by offline distillation to support various compression options. Then, compression rates are predicted in online environment specific to channel and task features. To solve the resultant constrained Markov Decision Process (MDP), a constrained variational policy optimization (CVPO) based MEG algorithm, MEG-CVPO, is further developed to learn constraint-guaranteed optimization. Numerical results demonstrate that: 1) The proposed framework improves image distortions while reducing over 40% latency compared to conventional generation schemes. 2) MEG-CVPO stringently guarantee constraints and realizes a flexible trade-off between generation qualities and overheads. © 2015 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2330.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
