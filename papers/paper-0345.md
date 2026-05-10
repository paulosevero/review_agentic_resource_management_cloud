---
id: paper-0345
title: 'NITCO: An intelligent agent technique for optimising of resource utilisation in cloud'
authors:
- Singh, Harvinder
- Bhasin, Anshu
- Kaveri, Parag Ravikant
venue: International Journal of Reasoning-based Intelligent Systems
venue_type: journal
year: 2021
doi: 10.1504/IJRIS.2021.114632
url: https://www.scopus.com/pages/publications/85105349931?origin=resultslist
publisher: Inderscience Publishers
pages: 69--75
keywords:
- Cloud computing
- Energy-consumption
- Scheduling
- Service level agreement
- SLA
- Utilisation
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    winning_category: classical_agents
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-0345 — NITCO: An intelligent agent technique for optimising of resource utilisation in cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient task scheduling is significant to meet the quality of service (QoS) requirements in cloud computing. Cloud is a large pool of virtual access resources to perform thousands of computational and storage operations. Task scheduling is an NP-hard problem, unsuitable matching leads to performance degradation and violation of service level agreement (SLA). The growing complexity of cloud services needs an extension of existing scheduling algorithms. In this paper, the scheduling problem has been explored based on growing application trends. Cloud dynamic resource provisioning can satisfy users' requirements if execution of tasks performed: identifying of task requirements; workflow of application scheduling using a sufficient amount of resources. In this research work, we present an intelligent agent technique for optimising resource utilisation named NITCO. NITCO considers the above mentioned challenge, identification of task requirements and configuration of resource. The performance of proposed NITCO has been evaluated on simulated cloud environment and comparison of results show that NITCO performed better in terms of execution cost, execution time, VM utilisation and SLA violation while it delivers quality of service. Copyright © 2021 Inderscience Enterprises Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **winning_category:** 'classical_agents'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0345.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
