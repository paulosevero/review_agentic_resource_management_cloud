---
id: paper-0426
title: Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles
authors:
- He, Hang
- Ren, Tao
- Cui, Meng
- Liu, Dong
- Niu, Jianwei
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2022
doi: 10.1007/978-3-031-19211-1_40
url: https://www.scopus.com/pages/publications/85142880064?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 481--494
keywords:
- Computation offloading
- Deep reinforcement learning
- Mobile edge computing
- Proximal policy optimization
- Unmanned aerial vehicle
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

# paper-0426 — Deep Reinforcement Learning Based Computation Offloading in Heterogeneous MEC Assisted by Ground Vehicles and Unmanned Aerial Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Compared with traditional mobile edge computing (MEC), heterogeneous MEC (H-MEC), which is assisted by ground vehicles (GVs) and unmanned aerial vehicles (UAVs) simultaneously, is attracting more and more attention from both academia and industry. By deploying base stations (along with edge servers) on GVs or UAVs, H-MEC is more suitable for access-demand dynamically-changing network environments, e.g., sports matches, traffic management, and emergency rescue. However, it is non-trivial to perform real-time user association and resource allocation in large-scale H-MEC environments. Motivated by this, we propose a shared multi-agent proximal policy optimization (SMAPPO) algorithm based on the centralized training and distributed execution framework. Due to the NP-hard difficulty of jointly optimizing user association and resource allocation for H-MEC, we adopt the actor-critic-based online-policy gradient (PG) algorithm to obtain near-optimal solutions with low scheduling complexities. In addition, considering the low sampling efficiency of PG, we introduce proximal policy optimization to increase the training efficiency by importance sampling. Moreover, we leverage the idea of centralized training and distributed execution to improve the training efficiency and reduce scheduling complexity, so that each mobile device makes decisions based only on local observation and learns other MDs’ experience from a shared replay buffer. Extensive simulation results demonstrate that SMAPPO can achieve more satisfactory performances than traditional algorithms. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0426.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
