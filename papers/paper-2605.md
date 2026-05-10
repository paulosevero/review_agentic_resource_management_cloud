---
id: paper-2605
title: Dynamic Multi-Layer Aerial System for Latent Diffusion-Based Generative AI Inference at the Edge
authors:
- Hiep, Dao Quang
- Cong Luong, Nguyen
- Gong, Shimin
- Li, Xingwang
- Nguyen, Ngoc Hung
- Niyato, Dusit
- Kim, Dong In
venue: IEEE Transactions on Communications
venue_type: journal
year: 2026
doi: 10.1109/TCOMM.2026.3662093
url: https://www.scopus.com/pages/publications/105030651465?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4461--4476
keywords:
- AI inference
- edge computing
- Latent diffusion models
- reinforcement learning
- unmanned aerial vehicle
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2605 — Dynamic Multi-Layer Aerial System for Latent Diffusion-Based Generative AI Inference at the Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we investigate a Multi-layer Aerial system for GenAI inference at the Edge (MAGE). Therein, ground user equipments (UEs) request image synthesis services from a remote base station (BS) that leverages the Latent Diffusion Model (LDM) for image generation. Multiple Unmanned Aerial Vehicles (UAVs) are deployed to serve the UEs for relaying their images and prompts to the BS. To reduce the communication cost and the computation burden at the BS, the UAVs can partially execute the LDM inference, i.e., an image autoencoder and prompt encoder, and offload the diffusion process task to the BS. In this work, we aim to minimize the BRISQUE scores across all the UEs by jointly optimizing the UAVs' positions, UE-UAV associations, the number of denoising steps at the BS, and offloading strategies of the UAVs. The optimization problem is non-convex, in which the objective function based on BRISQUE scores has no closed-form expression. Due to the fixed exploration strategy of Proximal Policy Optimization (PPO), which limits the policy's adaptability in dynamic environments, this leads to sub-optimal solutions. To address these potential drawbacks, we propose an adaptive exploration strategy that dynamically adjusts the exploration rate based on observed improvements in rewards. Specifically, the exploration capability is controlled by modulating the influence of the entropy bonus according to recent reward gains. Simulations based on the COCO-Stuff datasets show that the proposed scheme outperforms baseline schemes in different terms of BRISQUE score, UAVs' energy consumption, and inference latency. In particular, the proposed scheme reduces the BRISQUE score by up to 20-28.57%, inference energy consumption up to 15.98-30.17%, transmission energy consumption by 15.4-18.5%, and the latency by up to 33.33-43.28% compared to the baseline methods, resulting in higher image quality with a noticeably improved level of perceptual naturalness, improved energy efficiency, as well as substantially faster performance.  © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2605.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
