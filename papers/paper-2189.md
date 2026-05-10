---
id: paper-2189
title: Reinforcement Learning-based Scheduling for Efficient Edge-IoT Resource Allocation
authors:
- Suresh, M.
- Jayaprakash, M.
venue: Proceedings of the 6th International Conference on Electronics and Sustainable Communication Systems, ICESC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICESC65114.2025.11212313
url: https://www.scopus.com/pages/publications/105022662004?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1354--1360
keywords:
- deep reinforcement learning
- Edge computing
- IoT
- reinforcement learning
- resource allocation
- scheduling
- task optimization
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

# paper-2189 — Reinforcement Learning-based Scheduling for Efficient Edge-IoT Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In contemporary Edge-IoT spaces, IoT devices are propagating at a staggering rate, creating uncontrollable workload, a high power requirement, and the latency is a problem, which makes resource provision difficult. The traditional heuristic scheduling methods like First-Come, First-Served (FCFS) and Round Robin are ineffective since they do not respond to varying network conditions and because of this there is less efficiency and scalability in the system. In order to overcome these shortcomings, the proposed paper suggests a Reinforcement Learning-Based Scheduling Algorithm (RLSA) that implements Deep Reinforcement Learning (DRL) so that the technique is adaptive and priority-aware to perform intelligent resource and task scheduling. Experimental test results on RLSA using different workloads state that RLSA is associated with 20 percent lesser task latency, 15 percent lower energy utilization, and 12 percent increase throughput than baseline approaches, making RLSA an optimal choice in view of execution and sustainability of real-time Edge-IoT systems. In further research, multi-agent reinforcement learning will be researched to address scaling the allocation of resources and solving the conflict in large IoT environments. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2189.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
