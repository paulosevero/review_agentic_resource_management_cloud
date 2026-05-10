---
id: paper-2720
title: 'Joint edge offloading and resource provisioning for SLA-aware MEC: a two-timescale graph-attentive TD3 approach'
authors:
- Mohajer, Amin
- Mirzaei, Abbas
- Bavaghar, Maryam
- Darabi, Mostafa
- Fernando, Xavier
venue: Wireless Networks
venue_type: journal
year: 2026
doi: 10.1007/s11276-026-04117-3
url: https://www.scopus.com/pages/publications/105035298154?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Graph attention network (GAT)
- Multi-access edge computing (MEC)
- Resource provisioning
- SLA-aware orchestration
- Task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2720 — Joint edge offloading and resource provisioning for SLA-aware MEC: a two-timescale graph-attentive TD3 approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> SLA-aware multi-access edge computing (MEC) must jointly decide (i) how much radio/compute capacity to provision per region and (ii) where to execute each task (local edge, neighboring edge, or cloud) under bursty, non-stationary demand. These coupled decisions are difficult because the system is large-scale, partially observable, and has a continuous, high-dimensional action space (per-user bandwidth/CPU shares) while still requiring strict delay compliance. To address this challenge, we propose EdgeMind, a two-timescale orchestration framework. At the long timescale, a Transformer-based traffic predictor forecasts per-service demand and guides slice leasing (bandwidth and CPU) from the infrastructure provider to control cost while preventing congestion. At the short timescale, we design a graph-attentive multi-agent TD3 controller (TD3-GAT) that performs decentralized offloading and fine-grained resource provisioning using centralized training and decentralized execution. A GAT module encodes neighbor states and cooperation opportunities, while TD3’s twin critics and delayed policy updates stabilize learning in continuous control. In addition, we introduce a confidence-aware neighbor policy distillation term that transfers peer behaviors only when the estimated advantage is reliably positive, improving stability and sample efficiency in dense deployments. Extensive simulations in a realistic multi-edge setting with heterogeneous service profiles and non-stationary arrivals show that EdgeMind improves SLA satisfaction, reduces average completion delay, and increases service provider profit compared to representative baselines (DQN, greedy delay minimization, centralized DDPG with static slicing, and FC-MADDPG). © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2720.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
