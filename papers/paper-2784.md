---
id: paper-2784
title: 'EDGE360: Edge-Enabled Multi-Agent DRL for Region-Aware Rate Adaptation Solution to Enhance Quality of 360° Video Streaming'
authors:
- Subhan, Fazal E.
- Yaqoob, Abid
- Muntean, Cristina Hava
- Muntean, Gabriel-Miro
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3605849
url: https://www.scopus.com/pages/publications/105015086469?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1918--1935
keywords:
- bitrate adaptation
- deep reinforcement learning
- edge computing
- MPEG DASH
- QoE fairness
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
    my_justification: RL
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

# paper-2784 — EDGE360: Edge-Enabled Multi-Agent DRL for Region-Aware Rate Adaptation Solution to Enhance Quality of 360° Video Streaming

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Optimal tile-based bitrate allocation improves the Quality of Experience (QoE) for adaptive 360° video streaming across multiple clients in heterogeneous network environments; however, it is challenging as it implies accurate viewport prediction, finest tile-based bitrate reservation, and maintaining QoE fairness, particularly under constrained network conditions. This paper proposes a strategy named EDGE360, that employs an edge-driven Multi-Agent Deep Reinforcement Learning (MADRL) solution for rate adaptation to improve the joint QoE in DASH-based rich media content delivery based on adaptive viewport prediction and Video Multi-method Assessment Fusion (VMAF) corresponding tiling granularity selection. Cooperative strategies among agents in the central critic network are crucial for addressing the complexity of network instances at the edge and optimizing media streaming bitrate assignment in multiple-client scenarios. Therefore, EDGE360 aims to implement the Counterfactual Multi-Agent Policy Gradients (COMA) based on 5 G network traces to train agents in policies that optimize individual client QoE and fairness among clients, resulting in an improved rich streaming experience. At the edge, a tile-based quality monitor evaluates viewport trajectories, buffer status, and network throughput, employing deep learning to forecast optimal tile bitrate allocation, which is formulated as an MDP and solved with MADRL. Based on extensive experimentation, EDGE360 surpasses state-of-the-art adaptive bitrate algorithms by achieving the highest average reward, outperforming RAPT360, 360SRL, and BOLA360 by 8.12%, 11.86%, and 18.00%, respectively, demonstrating superior convergence and refinement. © 2002-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2784.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
