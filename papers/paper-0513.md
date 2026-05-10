---
id: paper-0513
title: Cooperative Offloading and Resource Allocation with Multi-Agent Deep Reinforcement Learning in MEC; [MEC系统中基于多智能体深度增强学习的协作式任务卸载和资源分配]
authors:
- Xia, Bingsen
- Tang, Yuanchun
- Li, Cui
venue: Bandaoti Guangdian/Semiconductor Optoelectronics
venue_type: journal
year: 2022
doi: 10.16818/j.issn1001-5868.2022030601
url: https://www.scopus.com/pages/publications/85133647517?origin=resultslist
publisher: China National Publishing Industry Trading Corporation
pages: 602--608
keywords:
- Cooperative computation offloading
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Resource allocation
language: Chinese
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

# paper-0513 — Cooperative Offloading and Resource Allocation with Multi-Agent Deep Reinforcement Learning in MEC; [MEC系统中基于多智能体深度增强学习的协作式任务卸载和资源分配]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) has emerged as a key technology to alleviate the computation workloads and decrease service latency for computation-intensive applications by offloading the tasks to MEC servers. However, the existing computation offloading and resource allocation studies present some several problems: poor collaboration between edge servers; mismatch between the computational task arrival and the dynamic characteristics in the real environment; and the dynamic joint optimization problem of the collaborative task unload and resource allocation. To solve such issues, based on the collaborative MEC framework, a multi-agent based deep deterministic policy gradient (MADDPG) is proposed for task unloading and resource allocation to minimize the overall long-term average cost. Simulation results reveal that the proposed scheme can reduce the delay and energy consumption. © 2022, Editorial Office of Semiconductor Optoelectronics. All right reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0513.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
