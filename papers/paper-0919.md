---
id: paper-0919
title: Empowering Satellite-UAV MEC Networks via Matching-Aided Multi-Agent Deep Reinforcement Learning
authors:
- Gao, Shuo
- Kang, Hui
- Sun, Geng
- Li, Jiahui
- Wang, Xue
- Wang, Jiacheng
- Niyato, Dusit
venue: Proceedings - 2024 20th International Conference on Mobility, Sensing and Networking, MSN 2024
venue_type: conference
year: 2024
doi: 10.1109/MSN63567.2024.00039
url: https://www.scopus.com/pages/publications/105010319910?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 220--227
keywords:
- anti-jamming
- cognitive radio
- deep reinforcement learning
- matching theory
- satellite communication
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

# paper-0919 — Empowering Satellite-UAV MEC Networks via Matching-Aided Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the sixth generation (6G) era, unmanned aerial vehicle (UAV) and satellite communications offer promising prospects in terms of the increasing demand for network coverage by the explosive growth of Internet of Things (IoT) devices. However, the lack of spectrum resources has become the bottleneck affecting network service performance. In this paper, we seek to use cognitive radio (CR) technology to assist the satellite-UAV networks. Specifically, we consider an integrated satellite-aerial network (SAN) and UAV-enabled MEC system in which CR is applied for the allocation and management of spectrum resources. Then, we formulate an optimization problem to maximize task execution and data transmission in the SAN system and minimize the energy consumption of UAVs by jointly optimizing the UAV trajectory and the strategy of task offloading. The problem is non-convex with high dynamic and hybrid action space, and thus we propose a matching-aided multi-agent deep reinforcement learning (MADRL)-based algorithm to solve the problem. Simulation results show that the proposed algorithm can improve the efficiency of task collection and reduce energy consumption while ensuring the anti-jamming ability.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0919.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
