---
id: paper-2479
title: A Trajectory Planning and Task Offloading Collaborative Optimization Method for Multi-UAV Assisted MEC
authors:
- Zhu, Bowen
- Zhang, Ran
- Ma, Fubao
- Yang, Xirui
venue: Proceedings of 2025 IEEE International Conference on Unmanned Systems, ICUS 2025
venue_type: conference
year: 2025
doi: 10.1109/ICUS66297.2025.11294262
url: https://www.scopus.com/pages/publications/105031904993?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 425--432
keywords:
- Markov decision process
- MATD3
- mobile edge computing
- multi-UAV
- task offloading
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

# paper-2479 — A Trajectory Planning and Task Offloading Collaborative Optimization Method for Multi-UAV Assisted MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In multi Unmanned Aerial Vehicle (UAV) assisted Mobile Edge Computing (MEC) systems, there are difficulties in balancing user coverage, task delay, and energy consumption for collaborative trajectory planning and task offloading. To address these problems, a collaborative optimization method based on improved Multi-Agent Twin Delayed Deep Deterministic Policy Gradient (MATD3) algorithm is proposed in this research. This method models the system's complex interactions as a Multi-agent Markov Decision Process (MMDP), and designs an enhanced state representation integrating service association matrices, to enhance the fine-grained perception capability of UAVs towards service topology. Besides, a global reward mechanism based on system-level pheromone signals is constructed to organically integrate multiple objectives such as coverage, delay, energy consumption and flight safety, guiding multi-UAV to efficiently learn collaborative decision-making strategies. Experimental results show that the proposed method can achieve autonomous optimization of flight trajectory and resource allocation strategies for UAVs under dynamic user demands and environmental constraints, effectively improving user coverage, reducing task processing latency, and optimizing system energy consumption. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2479.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
