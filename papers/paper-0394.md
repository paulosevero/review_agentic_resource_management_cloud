---
id: paper-0394
title: Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks
authors:
- Cheng, Zhipeng
- Liwang, Minghui
- Chen, Ning
- Huang, Lianfen
- Du, Xiaojiang
- Guizani, Mohsen
venue: Computer Communications
venue_type: journal
year: 2022
doi: 10.1016/j.comcom.2022.06.017
url: https://www.scopus.com/pages/publications/85132712026?origin=resultslist
publisher: Elsevier B.V.
pages: 234--244
keywords:
- Laser
- MASAC
- Multi-agent Markov game
- SWIPT
- Task offloading
- UAV
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

# paper-0394 — Deep reinforcement learning-based joint task and energy offloading in UAV-aided 6G intelligent edge networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge networks are expected to play an important role in 6G where machine learning-based methods are widely applied, which promote the concept of Edge Intelligence. Meanwhile, Unmanned Aerial Vehicle (UAV)-enabled aerial network is significant in 6G networks to achieve seamless coverage and super-connectivity. To this end, a joint task and energy offloading problem is studied under a UAV-aided and energy-constrained intelligent edge network, consisting of a high altitude platform (HAP), multiple UAVs, and on-ground fog computing nodes (FCNs). To guarantee the energy supply of UAVs and FCNs, both simultaneous wireless information and power transfer (SWIPT), as well as laser charging techniques are considered. Specifically, we investigate a scenario where each UAV needs to execute a computation-intensive task during each time slot and can be powered by the laser beam transmitted from the HAP. Due to the limited computation resources, each UAV can offload part of the task and energy to the FCNs for collaborative computing, to reduce local energy consumption and the overall task execution delay by adopting SWIPT. Considering the dynamics of the network, e.g., the time-varying locations of UAVs and available computation resources of FCNs, the problem is formulated as a cooperative multi-agent Markov game for UAVs, which aims to maximize the total system utility, by optimizing the task partitioning and power allocation strategies of each UAV, regarding task size, average delay and energy consumption of task execution. To tackle this problem, we propose a multi-agent soft actor–critic (MASAC)-based approach to resolve the problem. Numerical simulation results prove the superiority of our proposed approach as compared with benchmark methods. © 2022 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0394.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
