---
id: paper-1361
title: Multi-Agent Reinforcement Learning Based Energy Consumption Minimization with Virtualization in Maritime UAVs-Assisted MEC Network
authors:
- Zou, Haozheng
- Wang, Luyao
- Zhang, Wenqian
- Zhang, Guanglin
venue: Proceedings - 2024 International Conference on Cloud and Network Computing, ICCNC 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCNC63989.2024.00016
url: https://www.scopus.com/pages/publications/85201953924?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 42--48
keywords:
- maritime mobile edge computing
- multi-Agent
- resource management
- trajectory planning
- virtual machine
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

# paper-1361 — Multi-Agent Reinforcement Learning Based Energy Consumption Minimization with Virtualization in Maritime UAVs-Assisted MEC Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The flexibility and efficiency of unmanned aerial vehicles (UAVs) have been recognized as a viable solution to address the deficiency of deployment on the maritime mobile edge computing (MEC) networks. However, the limited computing resources of edge servers cannot support parallel processing tasks without performance loss. In this paper, we use virtual machine (VM) multiplexing technology to consider the performance degradation of parallel processing tasks in the UAVs-Assisted MEC network. To ensure efficient task offloading, we focus on the trajectory planning and resource management for UAVs. Our objective is to minimize overall energy consumption while ensuring that time delays for all tasks are within tolerable limits. We first transform the joint optimization problem into a Markov Decision Process (MDP), then propose a Multi-Agent deep reinforcement learning-based Resource Management and Trajectory Planning (MA-RMTP) algorithm to solve the problem. The simulation results show that our proposed approach can significantly reduce the overall energy consumption compared to other benchmarks.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1361.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
