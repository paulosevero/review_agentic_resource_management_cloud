---
id: paper-1712
title: 'SEROS: Shared exploration and reward optimization task scheduling strategy for multi-agent collaboration in edge computing networks'
authors:
- Jin, Lei
- Chen, Junyan
- Yao, Rui
- Chen, Jiahao
- Li, Xinmei
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2025.103992
url: https://www.scopus.com/pages/publications/105018080442?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computational task scheduling
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Offloading strategy
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1712 — SEROS: Shared exploration and reward optimization task scheduling strategy for multi-agent collaboration in edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of mobile edge computing (MEC) into dynamic wireless ad hoc networks has intensified the challenges of computational resource scheduling, particularly under queue load constraints. Current research primarily focuses on global average metrics while neglecting fairness in resource allocation among devices across cross-time slot task scenarios. This oversight leads to significant disparities in the resources allocated to different devices, with some devices consistently lacking computational resources due to imbalanced scheduling. To address these limitations, we propose SEROS (Shared Exploration and Reward Optimization Strategy), a multi-agent reinforcement learning framework designed for cross-timeslot task scheduling in MEC environments. The method dynamically balances local optimization objectives with global collaboration through a weighted shared reward mechanism while enhancing training efficiency via hybrid sample trajectory utilization, enabling adaptive task offloading decisions. First, we construct a mobile edge computing model incorporating queue load constraints to address cross-timeslot task scheduling challenges, improving resource utilization for time-sensitive workloads through delayed optimization objectives. Second, we design a collaborative incentive mechanism based on global–local reward balancing and develop a sample trajectory-sharing scheme to accelerate policy convergence while preserving agent specialization. Simulation experiments validate the effectiveness of SEROS, demonstrating that compared with baseline methods, the proposed approach exhibits superior comprehensive performance in task completion rate improved by 7% and inter-device completion rate concentration enhanced by 40%, along with stability and task completion time. © 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1712.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
