---
id: paper-1951
title: A joint optimization of resource allocation management and multi-task offloading in high-mobility vehicular multi-access edge computing networks
authors:
- Min, Hong
- Rahmani, Amir Masoud
- Ghaderkourehpaz, Payam
- Moghaddasi, Komeil
- Hosseinzadeh, Mehdi
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2024.103656
url: https://www.scopus.com/pages/publications/85203646191?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Double Deep Q-Network
- Multi-access edge computing
- Resource allocation
- Task offloading
- Vehicular communication
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

# paper-1951 — A joint optimization of resource allocation management and multi-task offloading in high-mobility vehicular multi-access edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular communications have advanced data exchange and real-time services in intelligent transportation systems by exploiting advanced communication between vehicles and infrastructure. The emergence of Multi-access Edge Computing (MEC) has further elevated this field by utilizing distributed edge resources near vehicles for low-latency data processing and high-reliability communication. In this dynamic environment, adequate resource allocation and task offloading are pivotal to ensure superior performance, lower latency, and efficient network resource utilization, enhancing Quality of Service (QoS) and overall driving experience and safety. This paper presents a developed vehicular network and offloading mechanism, introducing a resource management model with real-time allocation and load balancing. The proposed method integrates task prioritization, multi-agent collaboration, context-aware decision-making, and distributed learning to optimize network performance. The introduced optimized algorithm initializes Q-networks and target networks, sets up an experience replay buffer, and configures agents with local state representations. Agents use an ε-greedy policy for action selection, update Q-values through experience replay, and prioritize tasks based on urgency while sharing state information for collaborative decision-making. Evaluations through simulation demonstrate optimized performance, enhancing efficiency in vehicular MEC networks compared to baseline and the other well-known algorithms. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1951.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
