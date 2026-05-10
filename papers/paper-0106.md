---
id: paper-0106
title: Multi Agents to Search and Rescue Based on Group Intelligent Algorithm and Edge Computing
authors:
- Yang, Tingting
- Jiang, Zhi
- Dong, Jie
- Feng, Hailong
- Yang, Chengming
venue: 'Proceedings - IEEE 2018 International Congress on Cybermatics: 2018 IEEE Conferences on Internet of Things, Green Computing and Communications, Cyber, Physical and Social Computing, Smart Data,
  Blockchain, Computer and Information Technology, iThings/GreenCom/CPSCom/SmartData/Blockchain/CIT 2018'
venue_type: conference
year: 2018
doi: 10.1109/Cybermatics_2018.2018.00092
url: https://www.scopus.com/pages/publications/85067889394?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 389--394
keywords:
- Ant colony optimization
- Blockchain
- Boats
- Cluster computing
- Cooperative communication
- Decision making
- Distributed parameter control systems
- Edge computing
- Green computing
- Internet of things
- Multi agent systems
- Software agents
- Autonomous decision
- Distributed clusters
- Distributed task allocation
- Hierarchical control
- Improved ant colony algorithm
- Intelligent Algorithms
- Safety of navigation
- Search and rescue operations
- Search engines
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    proposed_justification: Out of scope
    winning_category: out_of_scope
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0106 — Multi Agents to Search and Rescue Based on Group Intelligent Algorithm and Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing number of maritime trade activities, carrying out rapid and effective maritime search and rescue operation has become an urgent need for research in order to ensure the safety of navigation at sea. Now, we mainly rely on artificial decision making, artificial distribution of search and rescue area, and artificial driving ship to complete search and rescue operation. The distribution, synergy, parallelism, robustness and intelligence of unmanned boat and UAV provide a new idea for the development of search and rescue work at sea. The marine search and rescue system under the new situation can be regarded as a hierarchical control network system composed of multi agents. And in this paper, a new fast search and rescue system is proposed by using the improved ant colony algorithm and the independent calculation decision of the agents. The system adopts the edge computing, relies on the information sharing and the cooperative decision between the search and rescue agent groups. And finally it achieves the independent synchronous search and rescue. Distributed task allocation solutions break through the limitations of centralized hierarchical task allocation based on manpower. Edge computing requires all distributed control nodes to make autonomous decisions in the task process. Based on the distributed cluster control of unmanned boat and UAVs, this paper combines edge computing, cooperative communication, centralized task allocation and decision making together. © 2018 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **regex_justification:** "Out of scope"
- **winning_category:** 'out_of_scope'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: out_of_scope, pattern_id: oos_maritime_sar, matched_substring: "maritime search and rescue" }`
  - `{ category: out_of_scope, pattern_id: oos_sar_network, matched_substring: "search and rescue operation ha" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi Agents" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agents" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0106.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
