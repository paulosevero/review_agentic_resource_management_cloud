---
id: paper-1851
title: 'IATS: Information-age aware task scheduling for vehicle-road-cloud cooperative systems'
authors:
- Lin, Sijie
- Li, Liying
- Chen, Jining
- Cong, Peijin
- Wang, Tian
- Zhou, Junlong
venue: Journal of Systems Architecture
venue_type: journal
year: 2025
doi: 10.1016/j.sysarc.2025.103480
url: https://www.scopus.com/pages/publications/105008117459?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Age of information
- Multi-agent reinforcement learning
- Task scheduling
- Vehicle-road-cloud
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

# paper-1851 — IATS: Information-age aware task scheduling for vehicle-road-cloud cooperative systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As the Internet of Things (IoT) continues to evolve at an unprecedented pace, smart vehicles can now support various real-time applications like object detection that require timely situational awareness. The freshness of state information is critical for these time-sensitive applications, as it directly affects the timeliness and accuracy of situational awareness. Fresh state information enables smart vehicles to make correct decisions in dynamic environments. However, this aspect is often ignored in prior work. Besides, these applications are typically computation-intensive, posing a challenge to resource-limited smart vehicles. Considering that the state information's freshness can be characterized using the age of information (AoI) and the vehicle-road-cloud computing architecture is effective in integrating the resources of roadside units and the cloud to assist with processing tasks for vehicles, to minimize the system's long-term average AoI without violating delay and energy constraints, this paper explores the AoI-aware task scheduling problem in a vehicle-road-cloud cooperative system. To achieve this goal, we first develop an AoI model tailored for smart vehicles within the cooperative system and formulate an AoI optimization problem. In order to tackle the proposed issue, we design a multi-agent reinforcement learning-based task scheduling method that can perform task scheduling in complex, dynamic, and decentralized decision-making environments. The algorithm iteratively trains the network continuously such that all agents obtain the optimal scheduling strategy. Finally, we implement extensive simulations and testbed-based experiments to validate our method. The results indicate that our method reduces the average AoI by 81.91% on average and 95.23% at the highest compared to benchmarking approaches. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1851.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
