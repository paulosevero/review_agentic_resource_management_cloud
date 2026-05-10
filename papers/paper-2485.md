---
id: paper-2485
title: Maximizing Long-Term Task Completion Ratio of UAV-Enabled Wirelessly Powered MEC Systems
authors:
- Zhu, Shaojun
- Zhu, Bincheng
- Chi, Kaikai
- Qiu, Jiefan
- Shi, Hailong
- Gao, Xingyu
venue: ACM Transactions on Multimedia Computing, Communications and Applications
venue_type: journal
year: 2025
doi: 10.1145/3712599
url: https://www.scopus.com/pages/publications/105003485151?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- mobile edge computing
- task completion ratio
- Unmanned aerial vehicles
- wirelessly powered transfer
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2485 — Maximizing Long-Term Task Completion Ratio of UAV-Enabled Wirelessly Powered MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicle (UAV)-enabled wirelessly powered Mobile Edge Computing (MEC) is emerging as a powerful technology for boosting computational capability and energy supplementation in Internet of Things (IoT). This work addresses the long-term task completion ratio maximization problem in UAV-enabled wirelessly powered MEC systems. Besides the large number of optimization parameters, the environment can only be partially observed as the UAVs cannot cover the whole network area. Then, it is very challenging to obtain good solutions due to the lack of global information. We introduce a novel distributed Multi-Agent Deep Reinforcement Learning (MADRL) framework for optimizing UAVs' actions and resource allocation, considering the constraints of tasks that vary in size, arrival times, and required computation completion time. To decouple the complicated parameters, we divide the problem into two manageable subproblems - UAVs' action decision and resource allocation under a given UAV's action. We employ a distributed Deep Reinforcement Learning (DRL) scheme for the former subproblem to cope with the partially observable nature. By revealing some important properties of the later subproblem, we design an efficient two-stage optimal algorithm to minimize the total consumed energy of nodes while maximizing the task-completing number. Extensive simulations validate the effectiveness of the proposed framework, achieving over a 50% improvement in task completion ratio compared to baseline schemes in some scenarios.  © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2485.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
