---
id: paper-1046
title: 'MAARS: Multiagent Actor–Critic Approach for Resource Allocation and Network Slicing in Multiaccess Edge Computing'
authors:
- Lim, Ducsun
- Joe, Inwhee
venue: Sensors
venue_type: journal
year: 2024
doi: 10.3390/s24237760
url: https://www.scopus.com/pages/publications/85211792115?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- multiaccess edge computing
- network slicing
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

# paper-1046 — MAARS: Multiagent Actor–Critic Approach for Resource Allocation and Network Slicing in Multiaccess Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a novel algorithm to address resource allocation and network-slicing challenges in multiaccess edge computing (MEC) networks. Network slicing divides a physical network into virtual slices, each tailored to efficiently allocate resources and meet diverse service requirements. To maximize the completion rate of user-computing tasks within these slices, the problem is decomposed into two subproblems: efficient core-to-edge slicing (ECS) and autonomous resource slicing (ARS). ECS facilitates collaborative resource distribution through cooperation among edge servers, while ARS dynamically manages resources based on real-time network conditions. The proposed solution, a multiagent actor–critic resource scheduling (MAARS) algorithm, employs a reinforcement learning framework. Specifically, MAARS utilizes a multiagent deep deterministic policy gradient (MADDPG) for efficient resource distribution in ECS and a soft actor–critic (SAC) technique for robust real-time resource management in ARS. Simulation results demonstrate that MAARS outperforms benchmark algorithms, including heuristic-based, DQN-based, and A2C-based methods, in terms of task completion rates, resource utilization, and convergence speed. Thus, this study offers a scalable and efficient framework for resource optimization and network slicing in MEC networks, providing practical benefits for real-world deployments and setting a new performance benchmark in dynamic environments. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1046.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
