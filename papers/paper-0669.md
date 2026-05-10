---
id: paper-0669
title: 'Optimal Computation Offloading in Collaborative LEO-IoT Enabled MEC: A Multiagent Deep Reinforcement Learning Approach'
authors:
- Lyu, Yifeng
- Liu, Zhi
- Fan, Rongfei
- Zhan, Cheng
- Hu, Han
- An, Jianping
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2023
doi: 10.1109/TGCN.2022.3186792
url: https://www.scopus.com/pages/publications/85133797200?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 996--1011
keywords:
- data offloading
- LEO-IoT
- mobile-edge computing
- reinforcement learning
- resource allocation
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

# paper-0669 — Optimal Computation Offloading in Collaborative LEO-IoT Enabled MEC: A Multiagent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, Low Earth Orbit (LEO) satellite-based Internet of Things (LEO-IoT) becomes attractive for computation offloading in mobile-edge computing (MEC) since it can overcome terrain obstacles, such as in depopulated villages and disaster sites. However, it is extremely hard to allocate bandwidth and power resources jointly with multiple users and satellites. In this paper, we study offloading in collaborative LEO-IoT where satellites forward data from users to the MEC server, with the goal of making offloading fast and energy efficient. To achieve this goal, we first define the data offloading in collaborative LEO-IoT as an optimization problem with resource constraints. Then we formulate the optimization problem as a Partially Observable Markov Decision Processes (POMDP), which differs from the existing Markov Decision Processes (MDP) work for the offloading scenario. We further propose a novel Multi-Agent Information Broadcasting and Judging (MAIBJ) algorithm to allocate resources in a collaborative manner. Finally, extensive experiments are conducted with various configurations and the results show that MAIBJ can shorten at least 33% of transmission latency and save at least 42% of energy consumption compared with several baseline algorithms.  © 2017 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0669.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
