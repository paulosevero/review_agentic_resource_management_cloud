---
id: paper-1257
title: Multi-objective joint optimization of task offloading based on MADRL in internet of things assisted by satellite networks
authors:
- Wang, Houpeng
- Cao, Suzhi
- Li, Huanjing
- Yan, Lei
- Guo, Zhonglin
- Gao, Yu'e
venue: Computer Networks
venue_type: journal
year: 2024
doi: 10.1016/j.comnet.2024.110801
url: https://www.scopus.com/pages/publications/85204491226?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Mobile edge computing
- Multi-agent DRL
- Multi-objective joint optimization
- Satellite network
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1257 — Multi-objective joint optimization of task offloading based on MADRL in internet of things assisted by satellite networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Internet of Things (IoT) integrates a large number of heterogeneous terminals and systems, possessing ubiquitous sensing and computing capabilities. Satellite networks are the crucial supplement to terrestrial networks, particularly in remote areas where network infrastructures are sparingly distributed or unavailable. Combining edge computing with satellite networks provides on-orbit computing capabilities for IoT applications, reducing service delay and enhancing service quality. Due to the resource constraints of satellites, achieving collaborative services through task offloading among multiple satellites becomes essential. Both the privacy leakage risk arising from frequent data interactions and the load imbalance resulting from offloading preferences cannot be overlooked. The key challenge of task offloading is to safeguard the privacy of offloaded data and ensure the system's load balance while minimizing the delay and energy consumption. In this paper, the task offloading problem is formulated as a Partially Observable Markov Decision Process (POMDP), and a task offloading algorithm based on multi-objective joint optimization using multi-agent deep reinforcement learning in a distributed architecture is proposed. The simulation results validate the efficacy of our model and algorithm, demonstrating that our proposed algorithm achieves better performance in minimizing comprehensive offloading costs. © 2024 The Authors

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1257.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
