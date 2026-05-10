---
id: paper-0498
title: DRL-based Distributed Resource Allocation for Edge Computing in Cell-Free Massive MIMO Network
authors:
- Tilahun, Fitsum Debebe
- Abebe, Ameha Tsegaye
- Kang, Chung G.
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2022
doi: 10.1109/GLOBECOM48099.2022.10000910
url: https://www.scopus.com/pages/publications/85146938679?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3845--3850
keywords:
- cell-free massive MIMO
- deep reinforcement learning (DRL)
- edge computing
- joint communication and computing resource allocation
- multi-agent reinforcement learning
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
  04-title-screening: exclude
  05-abstract-screening: pending
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
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
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

# paper-0498 — DRL-based Distributed Resource Allocation for Edge Computing in Cell-Free Massive MIMO Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, with the aim of addressing the stringent computing and quality-of-service (QoS) requirements of recently introduced advanced multimedia services, we consider a cell-free massive MIMO-enabled mobile edge network. In particular, benefited from the reliable cell-free links to offload intensive computation to the edge server, resource-constrained end-users can augment on-board (local) processing with edge computing. To this end, we formulate a joint communication and computing resource allocation (JCCRA) problem to minimize the total energy consumption of the users, while meeting the respective user-specific deadlines. To tackle the problem, we propose a distributed solution approach based on cooperative multi-agent reinforcement learning framework, wherein each user is implemented as a learning agent to make joint resource allocation relying on local information only. The simulation results demonstrate that the performance of the proposed distributed approach outperforms the heuristic baselines, converging to a centralized target benchmark, without resorting to large over-head. Moreover, we showed that the proposed algorithm has performed significantly better in cell-free system as compared with the cellular MEC systems, e.g., a small cell-based MEC system. © 2022 IEEE.

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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0498.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
