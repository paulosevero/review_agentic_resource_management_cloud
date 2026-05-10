---
id: paper-0383
title: 'Proactive and Reactive Decision Based Agent Placement: Reliability and Latency Perspective'
authors:
- Arzo, Sisay Tadesse
- Esmaeili, Mona
- Worku, Yonatan Melese
- Akhavan, Zeinab
- Devetsikiotis, Michael
- Zarkesh-Ha, Payman
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2022
doi: 10.1109/GLOBECOM48099.2022.10001516
url: https://www.scopus.com/pages/publications/85146923459?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4413--4418
keywords:
- Autonomous agents
- Computer system firewalls
- Deep learning
- Forecasting
- Intelligent agents
- Multi agent systems
- Network architecture
- Agent based
- Cloud data centers
- Decision accuracies
- Decision-based
- Edge clouds
- In networks
- Multi agent
- Network automations
- Network intelligence
- Networks management
- State feedback
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0383 — Proactive and Reactive Decision Based Agent Placement: Reliability and Latency Perspective

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> 6G is aiming at fully incorporating in-network intelligence towards automated network management. In this regard, a multi-agent-based network automation architecture as a service design is proposed. The architecture introduces in-network intelligence, designing intelligent agents as the fundamental unit which is used as a building block in autonomous network system design. This work focuses on the dynamic agent placement problems in edge/cloud data centers. Agents are softwarized and intelligent versions of network functions that are traditionally implemented in hardware such as firewalls, packet gateways, etc. This paper, based on a combination of proactive and reactive solutions, considered decision accuracy in developing an intelligent decision algorithm that can be used in the prediction agent design. The proactive decision is based on a deep learning prediction algorithm using time-series workload forecasting. However, in case of unforeseen events that are missing from the historical dataset, the proactive decisions could be less reliable. Therefore, network-state feedback should be considered to determine the current network conditions using the change in instant arrival rate as a reactive decision. Then combining it with the proactive decision should be able to capture the unpredictable traffic spikes. The result is used to determine the number and type of agents to instantiate at a given time in the edge/cloud data centers. Using a public dataset in our algorithms, we predicted the workload request for a few days. The result shows improved decision accuracy over the existing solutions using the appropriate amount of dataset, machine learning models, and rate estimation. © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0383.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
