---
id: paper-0724
title: Engineering IoT-Based Open MAS for Large-Scale V2G/G2V †
authors:
- Spanoudakis, Nikolaos I.
- Akasiadis, Charilaos
- Iatrakis, Georgios
- Chalkiadakis, Georgios
venue: Systems
venue_type: journal
year: 2023
doi: 10.3390/systems11030157
url: https://www.scopus.com/pages/publications/85151125738?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- digital twin
- engineering multiagent systems (EMASs)
- internet of things (IoT)
- open multiagent systems
- smart grid
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
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
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

# paper-0724 — Engineering IoT-Based Open MAS for Large-Scale V2G/G2V †

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we aimed to demonstrate how to engineer Internet of Things (IoT)-based open multiagent systems (MASs). Specifically, we put forward an IoT/MAS architectural framework, along with a case study within the important and challenging-to-engineer vehicle-to-grid (V2G) and grid-to-vehicle (G2V) energy transfer problem domain. The proposed solution addresses the important non-functional requirement of scalability. To this end, we employed an open multiagent systems architecture, arranging agents as modular microservices that were interconnected via a multi-protocol Internet of Things platform. Our approach allows agents to view, offer, interconnect, and re-use their various strategies, mechanisms, or other algorithms as modular smart grid services, thus enabling their seamless integration into our MAS architecture, and enabling the solution of the challenging V2G/G2V problem. At the same time, our IoT-based implementation offers both direct applicability in real-world settings and advanced analytics capabilities via enabling digital twin models for smart grid ecosystems. We have described our MAS/IoT-based architecture in detail; validated its applicability via simulation experiments involving large numbers of heterogeneous agents, operating and interacting towards effective V2G/G2V; and studied the performance of various electric vehicle charging scheduling and V2G/G2V-incentivising electricity pricing algorithms. To engineer our solution, we used ASEME, a state-of-the-art methodology for multiagent systems using the Internet of Things. Our solution can be employed for the implementation of real-world prototypes to deliver large-scale V2G/G2V services, as well as for the testing of various schemes in simulation mode. © 2023 by the authors.

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
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "MAS" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "MAS" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "MAS" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0724.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
