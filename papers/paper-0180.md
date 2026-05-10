---
id: paper-0180
title: Smart design for resources allocation in IoT application service based on multi-agent system and DCSP
authors:
- Bali, Mouadh
- Tari, Abdelkamel
- Almutawakel, Abdallah
- Kazar, Okba
venue: Informatica (Slovenia)
venue_type: journal
year: 2020
doi: 10.31449/INF.V44I3.2962
url: https://www.scopus.com/pages/publications/85096302234?origin=resultslist
publisher: Slovene Society Informatika
pages: 373--386
keywords:
- Cloud computing
- Distributed constraints satisfaction problems
- IoT
- IoT service
- Multi agent system
- Resource allocation
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
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

# paper-0180 — Smart design for resources allocation in IoT application service based on multi-agent system and DCSP

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the present paper, we aim at solving two problems; the first problem occurring in the transformation of the IoT devices (sensors, actuators, ) to cloud service. Therefore, we work on maintaining a smooth and efficient data transmission for the cloud and support customer applications like: Data sharing, storage and processing. The second problem has two dimensions. In the first dimension, the problem is arisen in the submission of cloudlets (customer requested jobs) to Virtual Machines (VMs) in the hosts. To solve this problem, we propose scheduling algorithm for resource allocation according to the lowest cost and load. In the second dimension, the problem lies in the hosting of new VMs in the hosts. To overcome this problem, we need take into account the loads when housing new VMs in different datacenters. In this work, we suggest a resource allocation approach for services oriented IoT applications. The architecture of this approach is based on two technics: Multi Agent System (MAS) and Distributed Constraint Satisfaction Problems (DCSP). The MAS manages the physical resources, making decision and the communication between datacenters, while DCSP used to simplify the policy of the resources provisioning in Datacenters. Variables and constraints are distributed among multiple agents in different layers. The experimental results show that the efficiency of our approach is manifested in: Average System Load, Cost augmentation Rate and Available Mips. © 2020 Slovene Society Informatika. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
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
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "MAS" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "MAS" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0180.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
