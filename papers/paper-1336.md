---
id: paper-1336
title: Offloading algorithm for multi-agent and double-layer offloading in internet of vehicle
authors:
- Zhang, Ji
- Gong, Wenwen
- Duo, Chunhong
- Qi, Guoliang
venue: Jisuanji Gongcheng/Computer Engineering
venue_type: journal
year: 2024
doi: 10.19678/j.issn.1000-3428.0068262
url: https://www.scopus.com/pages/publications/85203806193?origin=resultslist
publisher: Editorial Office of Computer Engineering
pages: 182--197
keywords:
- Double-layer offloading mechanism
- Edge computing
- Internet of Vehicle(IoV)
- Monotonic value function factorization
- Non-task vehicle cloud
language: Chinese
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Review
    winning_category: review
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

# paper-1336 — Offloading algorithm for multi-agent and double-layer offloading in internet of vehicle

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the edge computing environment of the Internet of Vehicles (IoV), with the aim of efficiently offloading tasks and allocating resources to alleviate the limited storage and computing power of vehicles, this study proposes a offloading algorithm based on multi-agent and double-layer offloading in IoV. A three-layer network model consisting of a Mobile Edge Computing (MEC) server, Vehicles, and Non-Task Vehicle Cloud(MEC-VNTVC) interconnection is first proposed. Additionally, task, judgment, and calculation models are established. Second, the computational offloading and resource allocation of task vehicles are abstracted into a Partially Observable Markov Decision Process (POMDP), and a double-layer offloading mechanism is proposed to minimize the system cost. Applying a double-layer offloading mechanism and monotonic value function factorization for deep multi-agent reinforcement learning QMIX, a deep reinforcement learning offloading algorithm DLSQMIX based on the double-layer offloading mechanism is proposed, which coordinates task vehicles, non-task vehicles, and state information, considering the time constraint and cooperates with the computation power of the MEC and the nontask vehicle cloud, to learn optimal offloading decisions. The system overhead and latency are compared and explained in terms of the computing power of edge servers and non-task vehicles, number of task vehicles and nontask vehicles, and average task volume. The simulation experiment results demonstrate that the DLSQMIX algorithm can effectively solve the task-offloading problem. Compared with the Genetic Algorithm (GA), Particle Swarm Optimization (PSO) algorithm, and QMIX algorithm, the proposed algorithm reduces the system overhead by 2.52%-3.91% and latency by 3.50%-6.59%. © 2024, Editorial Office of Computer Engineering. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_editorial, matched_substring: "Editorial" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "In the edge computing environm" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1336.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
