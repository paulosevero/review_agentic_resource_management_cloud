---
id: paper-2198
title: 'GRCEM: Generating Optimal Software Rejuvenation Strategies for Cloud-Edge Collaborative Systems Based on MADRL'
authors:
- Tan, Xueyong
- Liu, Jing
venue: Proceedings - 2025 IEEE 49th Annual Computers, Software, and Applications Conference, COMPSAC 2025
venue_type: conference
year: 2025
doi: 10.1109/COMPSAC65507.2025.00170
url: https://www.scopus.com/pages/publications/105016134495?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1360--1369
keywords:
- Cloud-Edge collaboration
- Multi-Agent Deep Reinforcement Learning
- software aging
- software rejuvenation
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
    my_justification: RL
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

# paper-2198 — GRCEM: Generating Optimal Software Rejuvenation Strategies for Cloud-Edge Collaborative Systems Based on MADRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of cloud and edge computing has solidly established the Cloud-Edge collaborative architecture as an essential technology, enabling the deployment of large-scale distributed applications. However, despite the benefits conferred by Cloud-Edge collaborative systems, challenges arise from prolonged operation, rapid evolution, and resource constraints. These challenges may accelerate software aging, resulting in performance degradation, functional disruptions, and increased susceptibility to errors. Software rejuvenation acts as a preemptive and proactive maintenance strategy designed to alleviate the consequences of software aging. Although task migration is a commonly used method for software rejuvenation, addressing software aging in complex Cloud-Edge collaborative systems requires dynamic task migration to adapt to environmental changes. Therefore, to develop a task migration-based rejuvenation strategy with lower latency, energy consumption, and software rejuvenation cost, this paper introduces a method for generating software rejuvenation strategies based on Multi-Agent Deep Reinforcement Learning for Cloud-Edge collaboration systems, named GRCEM. Initially, the environment is modeled to define the state space, action space, and training rewards, meticulously designed to minimize rejuvenation costs for the Cloud-Edge collaborative system. Subsequently, a distributed execution algorithm for deep reinforcement learning is devised, treating each node as an autonomous agent responsible for acquiring knowledge and enhancing rejuvenation strategies through continuous interaction with the system environment. Finally, the rejuvenation strategy is formulated, characterized by its optimal rejuvenation cost. The experimental results demonstrate that the GRCEM method accomplishes software rejuvenation with reduced rejuvenation costs compared to the baseline method. Furthermore, the system's performance transitions from the aging state to the robust state after rejuvenation, thereby significantly enhancing the availability and reliability of the Cloud-Edge collaboration system.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2198.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
