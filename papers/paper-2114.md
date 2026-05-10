---
id: paper-2114
title: 'ADDAPT6G: Advanced Double Dueling Architecture for Proactive Tuning in 6G Networks'
authors:
- Selis, Dimitrios
- Ramantas, Kostas
- Alonso, Luis
- Vardakas, John S
- Verikoukis, Christos
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11160944
url: https://www.scopus.com/pages/publications/105018463059?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1857--1862
keywords:
- 6G Mobile Communications
- Cloud Network Function (CNF)
- Container Migration
- Deep Reinforcement Learning
- Double Deep Q-Networks (DDQN)
- Dueling Architecture (DA)
- Multi-agent Reinforcement Learning (MARL)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2114 — ADDAPT6G: Advanced Double Dueling Architecture for Proactive Tuning in 6G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The continuous advancement in Beyond 5G (B5G) networks demands innovative solutions to address the increasingly complex requirements of network service distribution, considering latency, bandwidth and throughput. In particular, the non-convex nature of the associated challenges makes them difficult to tackle as a single well-defined optimal solution can not be easily identified. This paper introduces a novel framework that employs Dueling Double Deep Q-Networks (Dueling DDQN) within a distributed architecture to optimize Cloud-native Network Function (CNF) migration and service distribution. By leveraging the cutting-edge capabilities of Deep Reinforcement Learning (DRL), our approach autonomously detects, predicts and rectifies placement inefficiencies, thereby enhancing the overall network service quality. Finally, we demonstrate the practical applicability of our proposed solution through testbed experimentation using a multi-node server setup to benchmark our system's capability to efficiently mitigate performance constraints within a distributed environment.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2114.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
