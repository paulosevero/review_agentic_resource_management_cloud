---
id: paper-0954
title: Multiagent Deep Deterministic Policy Gradient-Based Computation Offloading and Resource Allocation for ISAC-Aided 6G V2X Networks
authors:
- Hu, Bintao
- Zhang, Wenzhang
- Gao, Yuan
- Du, Jianbo
- Chu, Xiaoli
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3432728
url: https://www.scopus.com/pages/publications/85199513630?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 33890--33902
keywords:
- Computation offloading
- deep reinforcement learning (DRL)
- edge intelligence
- integrated sensing and communications (ISACs)
- resource allocation
- vehicle-to-everything (V2X) communications
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

# paper-0954 — Multiagent Deep Deterministic Policy Gradient-Based Computation Offloading and Resource Allocation for ISAC-Aided 6G V2X Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular communications in future sixth-generation (6G) networks are expected to leverage integrated sensing and communications (ISACs) and mobile edge computing (MEC) techniques. However, the rapid proliferation of vehicle user equipment (V-UE) and the diversity of ISAC-aided and MEC-empowered vehicular communication and computation services demand a more intelligent and efficient resource allocation framework for the next-generation vehicular networks. To address this issue, we propose a comprehensive ISAC-aided vehicle-to-everything (V2X) MEC framework, where the V-UEs can offload their tasks to the edge server collocated at the roadside unit (RSU). We aim to minimize the long-term average total service delay of all the V-UEs by jointly optimizing the offloading decisions of all the V-UEs, the computation resource allocation at the ISAC-aided RSU, the transmission power, and the allocation of resource blocks for all the V-UEs, where the total service delay of a V-UE includes the task processing delay and the transmission delay if the V-UE offloads its task to the RSU. To solve the formulated mixed integer nonlinear programming problem, we design a multiagent deep deterministic policy gradient (MADDPG)-based offloading optimization and resource allocation algorithm (MADDPG-O2RA2). Simulation results demonstrate that our proposed algorithm outperforms the benchmarks in terms of convergence and the long-term average delay among all the V-UEs.  © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

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
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0954.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
