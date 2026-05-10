---
id: paper-2665
title: Multidimensional resource load-aware task migration in mobile edge computing
authors:
- Li, Chuangxin
- Li, Jixiao
- Gao, Yongqiang
- Song, Jiawei
- Wang, Zhigang
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2025.108091
url: https://www.scopus.com/pages/publications/105014610298?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Interdependent subtasks
- Mobile edge computing
- Resource allocation
- Task migration
- Workflows scheduling
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2665 — Multidimensional resource load-aware task migration in mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing demands for low latency, high computational power, and distributed execution in applications such as autonomous driving, augmented reality (AR), and smart manufacturing, Mobile Edge Computing (MEC) has emerged as a solution by bringing computation and storage closer to end users. In MEC environments, complex computational tasks are often structured as workflows, consisting of multiple interdependent subtasks that require distributed execution across multiple MEC servers. However, workflow tasks in MEC environments often involve complex data and temporal dependencies, requiring frequent task migration across multiple MEC servers due to user mobility. Inefficient task migration canlead to increased execution delays, communication overhead, and server overload, ultimately degrading system performance and service quality. Therefore, how to effectively optimize workflow task migration strategies to ensure on-time task completion while achieving balanced resource allocation among edge servers remains a key challenge in workflow scheduling for MEC environments. To address the challenge, this paper proposes a comprehensive strategy integrating user trajectory prediction and federated deep reinforcement learning to jointly optimize workflow migration and resource allocation. A hybrid GRU-2LSTM model predicts user mobility trajectories, while a Federated Multi-Agent Deep Deterministic Policy Gradient (FMADDPG) algorithm optimizes task migration and resource allocation. Simulation results demonstrate that the proposed strategy reduces average load imbalance by 10 %–20 % and lowers workflow timeout rates by 7 %–27 %, highlighting its effectiveness in workflow scheduling, resource optimization, and overall system efficiency in dynamic MEC environments. © 2025 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2665.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
