---
id: paper-2650
title: 'Optimizing Resource Utilization and Performance in LEO Satellite Edge Computing: A Joint Service Deployment and Task Offloading Approach'
authors:
- Lai, Junyu
- Wu, Di
- Chen, Yuhang
- Liu, Huashuo
- Chen, Han
- Jiang, Weiwei
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3668808
url: https://www.scopus.com/pages/publications/105031679756?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge Computing
- LEO Satellite Networks
- Resource Utilization
- Service Deployment
- Task Offloading
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

# paper-2650 — Optimizing Resource Utilization and Performance in LEO Satellite Edge Computing: A Joint Service Deployment and Task Offloading Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> While service-oriented low Earth orbit (LEO) satellite edge computing (LSEC) frameworks enable diverse edge services for user tasks, the heterogeneous distribution of terrestrial users causes substantial imbalance in computational task loads across satellites. This asymmetric workload leads to inefficient resource utilization and degraded edge computing performance. To address these challenges, we propose a joint optimization framework that integrates edge service deployment and task offloading, supported by service popularity analysis and spatiotemporal user-task modeling. The framework employs a two-timescale design: at the large timescale, an improved atomic orbital search (iAOS) heuristic dynamically optimizes service placement, configuration, and resource allocation; at the small timescale, a direction-selective multi-agent double deep Q-network (DS-MDDQN) leverages deep reinforcement learning to route tasks to the most suitable processing nodes. Extensive simulations show that our approach significantly outperforms six representative baselines in both user-perceived performance and system-level efficiency. Replacement studies further verify the effectiveness of each component: iAOS enhances resource utilization and reduces task failure through optimized service deployment, while DS-MDDQN mitigates network dynamics and lowers task completion latency via adaptive task offloading. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2650.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
