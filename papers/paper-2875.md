---
id: paper-2875
title: Dynamic Computation Offloading Optimization Based on Meta-Reinforcement Learning in UAV-Assisted MEC Networks
authors:
- Yan, Ming
- Yu, Peiying
- Chen, Junfeng
- Li, Chunguo
- Chih-Lin, I.
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3670318
url: https://www.scopus.com/pages/publications/105031927516?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- computation offloading
- meta-reinforcement learning
- Multi-access edge computing (MEC)
- unmanned aerial vehicle (UAV)
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

# paper-2875 — Dynamic Computation Offloading Optimization Based on Meta-Reinforcement Learning in UAV-Assisted MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Offloading computationally intensive tasks to edge nodes reduces latency and improves user experience. Unmanned aerial vehicle (UAV)-assisted multi-access edge computing (MEC) can effectively address the limitations of the fixed deployment of traditional edge nodes, but the dynamic nature of UAVs brings challenges to the optimization of computation offloading. Methods based on deep reinforcement learning (DRL) can efficiently learn edge network dynamics to optimize computation offloading in UAV-assisted systems. In the system model, different edge nodes such as UAVs, roadside units, and user equipments (UEs) are treated as agents in the reinforcement learning network, so that the optimization of the edge computation offloading strategy can be transformed into a multi-agent optimization problem. In addition, meta-reinforcement learning is introduced into the multi-agent deep deterministic policy gradient (MADDPG) algorithm to cope with the dynamics and uncertainty of the UAV-assisted edge computing network environment. Simulation results show that the computation offloading strategy based on meta-reinforcement learning can not only quickly adapt to the dynamic changes of the network environment but also outperform other benchmark algorithms in terms of network energy efficiency. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2875.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
