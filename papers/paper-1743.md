---
id: paper-1743
title: Development of Distributed Digital Twins of Complex Technical Objects Based on an Agent-Oriented Software Architecture
authors:
- Kovtunenko, Alexey
- Freint, Sofia
- Shundeev, Artem
- Vaganova, Darya
- Bagautdinov, Sergey
venue: Communications in Computer and Information Science
venue_type: conference
year: 2025
doi: 10.1007/978-3-031-89211-0_10
url: https://www.scopus.com/pages/publications/105013080375?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 129--145
keywords:
- Agent-based architecture
- Complex technical object
- Digital twin
- Distributed computing environment
- Edge computing
- Predictive analytics
- Software architecture
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1743 — Development of Distributed Digital Twins of Complex Technical Objects Based on an Agent-Oriented Software Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article presents the development of a digital twin of a complex technical object based on a distributed computing environment using an agent-oriented software architecture. The use of the distributed agent-oriented ABSynth platform allows for the integration of heterogeneous resources from cyber-physical system networks (including edge devices and high-performance computing (HPC)) into a unified computing environment. The components of the simulation model, as well as predictive analytics and fault detection, are implemented and operate in real-time, based on a library of the agent platform. A prototype of the software component of the digital twin for the wind turbine nacelle has been created. The test results have demonstrated the effectiveness of the agent-based approach in creating flexible, scalable, and fault-tolerant digital twins of complex technical objects and systems. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

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
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1743.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
