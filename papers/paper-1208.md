---
id: paper-1208
title: 'EDQD: An Edge-Driven Multi-Agent DRL Solution for Improving Joint QoE in DASH-based Rich Media Content Delivery'
authors:
- Subhan, Fazal E.
- Yaqoob, Abid
- Muntean, Cristina Hava
- Muntean, Gabriel-Miro
venue: IEEE International Symposium on Broadband Multimedia Systems and Broadcasting, BMSB
venue_type: conference
year: 2024
doi: 10.1109/BMSB62888.2024.10608238
url: https://www.scopus.com/pages/publications/85201542671?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Bitrate adaptation
- Deep Reinforcement Learning
- Edge Computing
- MPEG DASH
- QoE Fairness
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

# paper-1208 — EDQD: An Edge-Driven Multi-Agent DRL Solution for Improving Joint QoE in DASH-based Rich Media Content Delivery

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the realm of adaptive video streaming, ensuring high Quality of Experience (QoE) across multiple clients in heterogeneous network environments stands as a significant challenge. This paper delves into the augmentation of QoE fairness and adaptive bitrate aggregation in Dynamic Adaptive Streaming over HTTP (DASH), particularly tailored for multiple rich media clients. This study proposes an edge-driven MultiAgent Deep Reinforcement Learning (MADRL) solution for improving joint QoE in DASH-based rich media content delivery (EDQD) to orchestrate QoE-centric video streaming framework. In order to address the complexities of network conditions at the edge for optimal media streaming bitrate allocation the cooperative strategies among agents are of great importance. Therefore, the EDQD objective is to training agents in such a way to learn policies that optimize not only individual client QoE but also ensure fairness among clients to enhance the overall rich streaming experience. Here, in comparison with previously utilized Asynchronous Advantage Actor-Critic (A3C) algorithm, the Counterfactual Multi-Agent Policy Gradients (COMA) experimentation and training based on 5G network traces has the potential to demonstrate substantial improvements in joint QoE by efficiently allocating bitrate across multiple client in the edgedriven scenario. This research provides a major contribution to the emerging field of QoE-driven rich video streaming by highlighting the effectiveness of novel MADRL-based approach in edge-driven architectures that is designed to provide immersive and high-fidelity rich media experiences. In terms of average QoE, the experimental findings reported in this work outperform other state-of-the-art adaptive edge driven bitrate algorithms by 6.9% and 16.8%. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1208.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
