---
id: paper-0570
title: Edge Computing Resource Allocation Algorithm for NB-IoT Based on Deep Reinforcement Learning
authors:
- Chu, Jiawen
- Pan, Chunyun
- Wang, Yafei
- Yun, Xiang
- Li, Xuehua
venue: IEICE Transactions on Communications
venue_type: journal
year: 2023
doi: 10.1587/transcom.2022EBP3076
url: https://www.scopus.com/pages/publications/85159767465?origin=resultslist
publisher: Institute of Electronics Information Communication Engineers
pages: 439--447
keywords:
- Compute offload
- Deep reinforcement learning
- Mobile edge computing
- Narrowband Internet of Things
- Resource allocation
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

# paper-0570 — Edge Computing Resource Allocation Algorithm for NB-IoT Based on Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) technology guarantees the privacy and security of large-scale data in the Narrowband-IoT (NB-IoT) by deploying MEC servers near base stations to provide sufficient computing, storage, and data processing capacity to meet the delay and energy consumption requirements of NB-IoT terminal equipment. For the NB-IoT MEC system, this paper proposes a resource allocation algorithm based on deep reinforcement learning to optimize the total cost of task offloading and execution. Since the formulated problem is a mixed-integer non-linear programming (MINLP), we cast our problem as a multi-Agent distributed deep reinforcement learning (DRL) problem and address it using dueling Q-learning network algorithm. Simulation results show that compared with the deep Q-learning network and the all-local cost and all-offload cost algorithms, the proposed algorithm can effectively guarantee the success rates of task offloading and execution. In addition, when the execution task volume is 200 KBit, the total system cost of the proposed algorithm can be reduced by at least 1.3%,and when the execution task volume is 600 KBit, the total cost of system execution tasks can be reduced by 16.7% at most. © 2023 The Institute of Electronics, Information and Communication Engineers.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0570.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
