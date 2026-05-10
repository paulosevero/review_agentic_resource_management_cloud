---
id: paper-2821
title: 'Drone-Aided Secure Task Offloading Optimization for Internet of Vehicles: Review, Challenges and Method'
authors:
- Wang, Ye
- Wang, Jingjing
- Chen, Jianrui
- Hou, Xiangwang
- Wang, Ziyang
- Jiang, Chunxiao
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3641579
url: https://www.scopus.com/pages/publications/105024586945?origin=resultslist
publisher: IEEE Computer Society
pages: 4596--4615
keywords:
- Drone-aided
- Internet of Vehicles
- multi-agent reinforcement learning algorithm
- task offloading optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2821 — Drone-Aided Secure Task Offloading Optimization for Internet of Vehicles: Review, Challenges and Method

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The evolution of the Internet of Vehicles (IoV) has introduced computation-intensive and latency-sensitive applications that challenge traditional cloud architectures. Although drone-aided IoV offers a flexible solution, it presents a complex optimization problem. The core challenge lies in balancing task offloading efficiency with crucial operational safety constraints, such as collision avoidance and battery management, a gap often overlooked in existing research. This paper addresses this problem by first modeling the drone-aided task offloading system as a constrained multi-agent Markov decision process. Based on this framework, we propose a novel safe multi-agent reinforcement learning algorithm (MARL) named Lagrangian-constrained multi-agent policy optimization (LC-MAPO). The LC-MAPO integrates safety constraints into the twin delayed deep deterministic policy gradient (TD3) actor-critic framework using Lagrangian duality theory. The algorithm's effectiveness was validated in three distinct simulation scenarios and compared against an unconstrained multi-agent deep deterministic policy gradient (MADDPG) algorithm and a greedy algorithm. Experimental results demonstrate that LC-MAPO achieves superior performance in both safety adherence and task processing efficiency. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2821.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
