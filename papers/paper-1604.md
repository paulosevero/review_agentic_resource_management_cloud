---
id: paper-1604
title: Multi-Agent Deep Reinforcement Learning for Optimized Task Offloading in Edge Systems
authors:
- Guizani, Maher
- Khan, Latif U.
- Islam, Mohammad A.
venue: 2025 7th Computing, Communications and IoT Applications Conference, ComComAp 2025
venue_type: conference
year: 2025
doi: 10.1109/ComComAp68359.2025.11353164
url: https://www.scopus.com/pages/publications/105033485124?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 454--459
keywords:
- metaverse
- Multi-agent deep reinforcement learning
- resource optimization
- task offloading
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

# paper-1604 — Multi-Agent Deep Reinforcement Learning for Optimized Task Offloading in Edge Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Next-generation Internet of Things (IoT) wireless systems will rely on metaverse for efficient and effective management of their constrained resources. In a metaverse-enabled IoT wireless system, task offloading is one of the main challenges. Many nodes in the physical space (i.e., physical entities like sensors and mobile devices) of the metaverse will have to offload their tasks to the meta space (i.e., a space that uses a virtual model of the physical world and is deployed at the network edge and cloud). However, task offloading is very challenging due to the limited and constrained resources. Therefore, in this paper, we consider a task offloading problem and try to solve it using an optimization formulation. To solve the formulated problem, we propose a hybrid framework, convex-optimization-assisted multiagent deep reinforcement Learning (MARL) for task offloading. In the proposed solution, we use MARL for task offloading and a convex optimizer for the time interval allocation. It is evident that our proposed solution of using the convex optimization with MARL significantly improved the system performance. Finally, we provide simulation results to support the validity of the proposed solution.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1604.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
