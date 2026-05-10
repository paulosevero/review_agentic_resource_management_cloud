---
id: paper-1818
title: Reinforcement learning based offloading and resource allocation for multi-intelligent vehicles in green edge-cloud computing
authors:
- Li, Liying
- Gao, Yifei
- Xia, Peiwen
- Lin, Sijie
- Cong, Peijin
- Zhou, Junlong
venue: Computer Communications
venue_type: journal
year: 2025
doi: 10.1016/j.comcom.2025.108051
url: https://www.scopus.com/pages/publications/85215068093?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- GECC
- Intelligent transportation system
- Multi-agent reinforcement learning
- Task offloading and resource allocation
- Time and energy
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

# paper-1818 — Reinforcement learning based offloading and resource allocation for multi-intelligent vehicles in green edge-cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Green edge-cloud computing (GECC) collaborative service architecture has become one of the mainstream frameworks for real-time intensive multi-intelligent vehicle applications in intelligent transportation systems (ITS). In GECC systems, effective task offloading and resource allocation are critical to system performance and efficiency. Existing works on task offloading and resource allocation for multi-intelligent vehicles in GECC systems focus on designing static methods, which offload tasks once or a fixed number of times. This offloading manner may lead to low resource utilization due to congestion on edge servers and is not suitable for ITS with dynamically changing parameters such as bandwidth. To solve the above problems, we present a dynamic task offloading and resource allocation method, which allows tasks to be offloaded an arbitrary number of times under time and resource constraints. Specifically, we consider the characteristics of tasks and propose a remaining model to obtain the states of vehicles and tasks in real-time. Then we present a task offloading and resource allocation method considering both time and energy according to a designed real-time multi-agent deep deterministic policy gradient (RT-MADDPG) model. Our approach can offload tasks in arbitrary number of times under resource and time constraints, and can dynamically adjust the task offloading and resource allocation solutions according to changing system states to maximize system utility, which considers both task processing time and energy. Extensive simulation results indicate that the proposed RT-MADDPG method can effectively improve the utility of ITS compared to 2 benchmarking methods. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1818.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
