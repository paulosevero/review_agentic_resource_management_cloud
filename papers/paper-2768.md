---
id: paper-2768
title: Optimization of Edge Offloading for Centralized Controllers Through Dynamic Computational Resource Allocation
authors:
- Seisa, Achilleas Santi
- Velhal, Shridhar
- Kotpalliwar, Shruti
- Satpute, Sumeet
- Nikolakopoulos, George
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3650978
url: https://www.scopus.com/pages/publications/105027996933?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11068--11087
keywords:
- Application platform
- centralized control
- edge computing
- edge robotics
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

# paper-2768 — Optimization of Edge Offloading for Centralized Controllers Through Dynamic Computational Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article presents a novel framework based on edge computing, implemented using Kubernetes (k8s) orchestration, to optimally offload the computational tasks required for centralized control of multiple robotic agents. Edge-based centralized control architectures are prone to failure due to communication delays. The proposed framework computes the maximum round-trip time delay for which the system remains stable and modifies the controller parameters to ensure the control computation within the critical time. For higher processing and communication delays, the complexity of the controller needs to be reduced by reducing the number of agents, the prediction horizon, and the efficient use of edge resources. The edge resources are dynamic, and the controller needs to be designed to guarantee the online computation within a desired time. A dynamic resource allocation method (based on an approximate function of the controller parameters, complexity, and computational resources) is proposed to design the controller parameters to ensure the bounded computation time. To validate the effectiveness of the proposed approach, we conduct experimental evaluations that analyze system behavior under various conditions, providing valuable insights into the performance, scalability, and robustness of multiagent control systems deployed on edge infrastructure. © 2026 IEEE. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2768.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
