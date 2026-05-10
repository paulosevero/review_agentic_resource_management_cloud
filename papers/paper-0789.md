---
id: paper-0789
title: 'DeepMECagent: multi-agent computing resource allocation for UAV-assisted mobile edge computing in distributed IoT system'
authors:
- Zhang, Xiangxiang
- Wang, Yichao
venue: Applied Intelligence
venue_type: journal
year: 2023
doi: 10.1007/s10489-022-03482-8
url: https://www.scopus.com/pages/publications/85128820879?origin=resultslist
publisher: Springer
pages: 1180--1191
keywords:
- Mobile edge computing
- Resource allocation
- UAV
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_justification: RL
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

# paper-0789 — DeepMECagent: multi-agent computing resource allocation for UAV-assisted mobile edge computing in distributed IoT system

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The proliferation of Internet-of-Things (IoTs) devices provides a promising platform for various intelligent applications such as virtual reality. However, because of the limited onboard computation resource of IoT devices, the computation task suffers from long latency. Mobile edge computing (MEC), which is a critical technology, allows offloading the computation tasks to an edge server to alleviate the shortage of computation resources and accelerate the computation tasks of IoT devices. Owing to the flexibility and mobility advantages of unmanned aerial vehicles (UAVs), UAV-assisted MEC has been widely researched. However, existing studies mostly explore a centralized offloading strategy. Therefore, when the number of IoT devices increases, the performance of the centralized strategy is reduced. The present study explores an intelligent strategy to minimize computation latency using a distributed algorithm. We develop a distributed algorithm named DeepMECagent based on deep reinforcement learning to optimize the computation offloading with minimum computation latency. In the considered scenario, a UAV functions as an aerial edge server to collect and process the computation tasks offloaded by ground IoT devices.The simulation results demonstrate the effective-ness of the proposed approach for minimizing the computation latency, where the computation latency of the proposed algorithm improves 39.71%,87.42%, and 88.55%, respectively, while compared with the centralized-DQN, Q-table, and the random algorithm. Given the expiration time as 1 second, the number of completed tasks within the expiration time of the proposed DeepMECagent is around 2 × and 1.25 × compared with the random algorithm and the Q-table algorithm, respectively. © 2022, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0789.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
