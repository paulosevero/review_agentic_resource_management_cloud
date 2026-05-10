---
id: paper-1901
title: Task Offloading and Resource Allocation for MEC-Assisted Consumer Internet of Vehicle Systems
authors:
- Liu, Yanheng
- Li, Dalin
- Wu, Hao
- Sun, Zemin
- Qin, Weihong
- Li, Jun
- Du, Hongyang
- Sun, Geng
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2025
doi: 10.1109/TCE.2025.3599198
url: https://www.scopus.com/pages/publications/105013303269?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10937--10949
keywords:
- consumer Internet of Vehicle
- Mobile edge computing
- multi-agent deep deterministic policy gradient learning
- resource allocation
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

# paper-1901 — Task Offloading and Resource Allocation for MEC-Assisted Consumer Internet of Vehicle Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC)-assisted Internet of vehicle (IoV) is emerging as a promising paradigm to provide computing services for vehicles. However, meeting the computing-sensitive and computation-intensive demands of vehicles poses several challenges, including the discrepancy between the limited resource provision and stringent computing requirement, the difficulty in capturing and integrating the intricate features of the MEC-assisted IoV system into the problem formulation, and the need for real-time processing and efficient resource management in the dynamic environment. In this work, we explore the AI-enabled task offloading and resource allocation for MEC-assisted consumer IoV systems. Specifically, we first present a multi-MEC-assisted consumer IoV architecture that leverages the computational resources of MEC servers to provide offloading services close to vehicles. Subsequently, we formulate a system cost minimization optimization problem (SCMOP) by integrating the service delay and energy consumption. To efficiently solve this problem, we design a joint task offloading and computing resource allocation approach (JTOCRA) by applying the multi-agent deep deterministic policy gradient (MADDPG) algorithm. Finally, simulation results demonstrate that the proposed JTOCRA can achieve superior system performances and exhibits better scalability compared to other alternative approaches. © 1975-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1901.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
