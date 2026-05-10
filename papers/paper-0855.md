---
id: paper-0855
title: 'Deep Reinforcement Learning for Multi-UAV MEC System Trajectory Optimization: Minimizing Energy Consumption'
authors:
- Chen, Zonghui
- Xu, Huahu
- Cheng, Chen
venue: Proceedings of 2024 2nd International Conference on Internet of Things and Cloud Computing Technology, IoTCCT 2024
venue_type: conference
year: 2024
doi: 10.1145/3702879.3702884
url: https://www.scopus.com/pages/publications/85216412663?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 24--30
keywords:
- Mobile Edge Computing (MEC)
- Mobility
- Multi-Agent Deep Deterministic Policy Gradient (MADDPG)
- Trajectory Optimization
- Unmanned Aerial Vehicles (UAV)
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0855 — Deep Reinforcement Learning for Multi-UAV MEC System Trajectory Optimization: Minimizing Energy Consumption

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC) systems, unmanned aerial vehicles (UAVs) have garnered significant research and application attention due to their high flexibility and ease of deployment. However, given the limited energy resources carried by UAVs, a critical challenge is how to reduce system energy consumption while ensuring service delivery to users. Additionally, the dynamic nature of MEC network resources makes energy optimization even more challenging. Therefore, this study constructs an optimization objective in a disaster scenario involving multiple UAVs and multiple users by building energy consumption model. Based on this optimization objective, the study fully considers user mobility and proposes the MU-MADDPG algorithm to address this issue. In this system, each UAV acts as an independent agent, collaborating to optimize UAV flight paths. Furthermore, to accelerate the learning process and improve its efficiency, this study introduces a prioritized experience replay (PER) mechanism. Experimental results demonstrate that the proposed algorithm outperforms other algorithms in terms of convergence speed and system energy consumption. © 2024 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0855.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
