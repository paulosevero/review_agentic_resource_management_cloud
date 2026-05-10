---
id: paper-1316
title: Joint Cooperative Computation Offloading and Trajectory Optimization in Heterogeneous UAV-Swarm-Enabled Aerial Edge Computing Networks
authors:
- Yu, Hanqing
- Leng, Supeng
- Wu, Fan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3362321
url: https://www.scopus.com/pages/publications/85186983278?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17700--17711
keywords:
- Aerial edge network
- heterogeneous unmanned aerial vehicles (UAVs)
- multiagent deep reinforcement learning
- trajectory planning
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

# paper-1316 — Joint Cooperative Computation Offloading and Trajectory Optimization in Heterogeneous UAV-Swarm-Enabled Aerial Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Aerial edge computing (AEC) networks, which employ multiple unmanned aerial vehicles (UAVs) as mobile-edge computing servers, have emerged as a promising solution to provide computation offloading services, especially in scenarios where the coverage of existing infrastructures is limited for wireless networks. Recently, there has been a growing focus on leveraging UAVs with diverse computing capabilities to enhance the performance of AEC networks through cooperative computing. However, heterogeneity and cooperation introduce a higher degree of coupling between trajectory planning and computing offloading strategy for AEC networks. In particular, the joint decision making in an AEC network needs to balance minimizing the distance between UAVs and access users and enabling collaborative offloading. And this must be done while considering the time-varying computation requirements and the long-term impact on system performance. To address the aforementioned challenges, we formulate an optimization problem to design a joint dynamic cooperative computation offloading and trajectory optimization scheme for the AEC network. The complexity arises from the problem's nature as a mixed-integer nonlinear program. To tackle this challenge, we propose a multiagent deep reinforcement learning algorithm based on QMIX. We leverage both theoretical analysis and an action branching architecture to reduce the complexity of our proposed deep reinforcement algorithm. Simulation results demonstrate a substantial performance improvement over the benchmarks, affirming the effectiveness of our complexity reduction approach.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1316.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
