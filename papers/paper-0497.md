---
id: paper-0497
title: 'Distributed Task Scheduling in Serverless Edge Computing Networks for the Internet of Things: A Learning Approach'
authors:
- Tang, Qinqin
- Xie, Renchao
- Yu, Fei Richard
- Chen, Tianjiao
- Zhang, Ran
- Huang, Tao
- Liu, Yunjie
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2022.3167417
url: https://www.scopus.com/pages/publications/85128313161?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19634--19648
keywords:
- Deep reinforcement learning (DRL)
- distributed task scheduling
- Internet of Things (IoT)
- serverless edge computing
- stochastic game
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Learning approach talvez indique LLM/agents
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

# paper-0497 — Distributed Task Scheduling in Serverless Edge Computing Networks for the Internet of Things: A Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> By delegating the infrastructure management, such as provisioning or scaling to third-party providers, serverless edge computing has recently been widely adopted in several applications, especially Internet of Things (IoT) applications. Task scheduling is a critical issue in serverless edge computing as it significantly impacts the quality of user experience. In contrast to the centralized scheduling in the cloud center, serverless edge task scheduling is more challenging due to the heterogeneous and resource-constrained nature of edge resources. This article aims to study the distributed task scheduling for the IoT in serverless edge computing networks, in which heterogeneous serverless edge computing nodes are rational individuals with interests to optimize their own scheduling utility while the nodes only have access to local observations. The task scheduling competition process is formulated as a partially observable stochastic game (POSG) to enable serverless edge computing nodes to noncooperatively schedule tasks and allocate computing resources depending on their locally observed system state, which takes into account the associated task generation state, data queue state, communication channel state, and previous computing resource allocation state. To solve the proposed POSG and deal with the partial observability, a multiagent task scheduling algorithm based on the dueling double deep recurrent $Q$ -network (D3RQN) method is developed to approximate the optimal task scheduling and resource allocation solution. Finally, extensive simulation experiments are conducted to validate the effectiveness and superiority of the proposed scheme. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Learning approach talvez indique LLM/agents"
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
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0497.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
