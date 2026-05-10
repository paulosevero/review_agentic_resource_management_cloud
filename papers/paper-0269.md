---
id: paper-0269
title: Engineering approaches for programming agent-based iot objects using the resource management architecture
authors:
- Brandão, Fabian Cesar
- Lima, Maria Alice Trinta
- Pantoja, Carlos Eduardo
- Zahn, Jean
- Viterbo, José
venue: Sensors
venue_type: journal
year: 2021
doi: 10.3390/s21238110
url: https://www.scopus.com/pages/publications/85120604304?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- Edge computing
- Embedded multi-agent systems
- IoT
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
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
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

# paper-0269 — Engineering approaches for programming agent-based iot objects using the resource management architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Internet of Things (IoT) allows the sharing of information among devices in a network. Hardware evolutions have enabled the employment of cognitive agents on top of such devices, which could help to adopt pro-active and autonomous IoT systems. Agents are autonomous entities from Artificial Intelligence capable of sensing (perceiving) the environment where they are situated. Then, with these captured perceptions, they can reason and act pro-actively. However, some agent approaches are created for a specific domain or application when dealing with embedded systems and hardware interfacing. In addition, the agent architecture can compromise the system’s performance because of the number of perceptions that agents can access. This paper presents three engineering approaches for creating IoT Objects using Embedded Multi-agent systems (MAS)—as cognitive systems at the edge of an IoT network—connecting, acting, and sharing information with a re-engineered IoT architecture based on the Sensor as a Service model. These engineering approaches use Belief-Desire-Intention (BDI) agents and the JaCaMo framework. In addition, it is expected to diversify the designers’ choice in applying embedded MAS in IoT systems. We also present a case study to validate the whole re-engineered architecture and the approaches. Moreover, some performance tests and comparisons are also presented. The study case shows that each approach is more or less suitable depending on the domain tackled. The performance tests show that the re-engineered IoT architecture is scalable and that there are some trade-offs in adopting one or another approach. The contributions of this paper are an architecture for sharing resources in an IoT network, the use of embedded MAS on top IoT Objects, and three engineering approaches considering agent and artifacts dimensions. © 2021 by the authors. Licensee MDPI, Basel, Switzerland.

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
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "MAS" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0269.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
