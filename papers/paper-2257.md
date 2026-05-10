---
id: paper-2257
title: 'Dependent task offloading for air-ground integrated MEC networks: a multi-agent collaboration approach'
authors:
- Wang, Yuchen
- Wei, Zhongcheng
- Huang, Zishan
- Yang, Jian
- Zhao, Jijun
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-024-04732-9
url: https://www.scopus.com/pages/publications/85210369673?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Air-ground integrated networks
- Dependent task offloading
- Mobile edge computing (MEC)
- Multi-agent deep deterministic policy gradient (MADDPG)
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
    proposed_justification: RL
    winning_category: rl
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

# paper-2257 — Dependent task offloading for air-ground integrated MEC networks: a multi-agent collaboration approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The air-ground integrated mobile edge computing (MEC) network provides an efficient data processing platform for application services with timing-dependent subtasks in the Internet of Things (IoT). Nevertheless, in multi-user concurrency scenarios, due to the unbalanced node load and the complexity of service requests, it may lead to long user response latency. In this paper, we propose the air-ground collaborative task offloading (AGC_TO) scheme, aiming to minimize total task offloading delay and maximize node resource utilization. The approach considers the dynamic resource scenarios in an integrated subtask timing dependency constraints, unmanned aerial vehicles (UAV) flight service range change, offloading location optimization, CPU resource allocation and node load optimization, CPU resource allocation, and node load five key factors. Firstly, We employ a subtask preprocessing (STP) algorithm based on depth-first traversal to analyze the topology of timing-dependent tasks in terms of obtaining different sequences of string parallel divisions for single-user request tasks in a multi-user concurrency scenario. Subsequently, utilizing this sequence with dynamically changing global computational resource information, considering the mobility of the UAV as well as the dynamically available resources among nodes, the optimal offloading location of the subtask can be autonomously determined by the multi-agent collaborative offloading algorithm based on multiagent deep deterministic policy gradient (MADDPG). Numerical results demonstrate that the proposed scheme is significantly better than the representative benchmark in terms of task offloading latency and system resource utilization. Specifically, the proposed scheme outperforms the single agent offloading algorithms double deep-Q network based task offloading (DDQN_TO) and deep Q-network based task offloading (DQN_TO), reducing task offloading latency by 41.4% and 46.4%, and enhancing resource utilization by 8.4% and 8.6%, respectively. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

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
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2257.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
