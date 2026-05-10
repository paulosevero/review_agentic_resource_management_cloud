---
id: paper-2047
title: Dynamic Multi-Agent Reinforcement Learning Based Load Balancing on Software Defined Networking
authors:
- Prakash, S. Wilson
- Usharani, S.
- Rajesh, R.
- Rajkumar, K.
venue: 2025 International Conference on Networks and Cryptology, NETCRYPT 2025
venue_type: conference
year: 2025
doi: 10.1109/NETCRYPT65877.2025.11102153
url: https://www.scopus.com/pages/publications/105015492669?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 359--364
keywords:
- Cloud Computing
- Load balancing
- Multi-Agent Reinforcement Learning (MARL)
- Software-Defined Networking (SDN)
- Virtual Machine Migration
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2047 — Dynamic Multi-Agent Reinforcement Learning Based Load Balancing on Software Defined Networking

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing provides on-demand access to computing re-sources via the internet, but efficient resource utilization and traffic man-agement remain challenging due to dynamic workloads. This paper proposes a Dynamic Multi-Agent Reinforcement Learning (MARL)-based Load Balancing (DA-LB) algorithm for Software-Defined Networking (SDN)-enabled cloud data centers. Unlike existing heuristic or single-agent reinforcement learning approaches, DA-LB leverages decentralized cooperation among MARL agents to achieve adaptive load balancing, leveraging SDN's global visibility for efficient Virtual Machine (VM) migration. The algorithm dy-namically predicts overloaded VMs, minimizes migration time, and adapts to traffic fluctuations. Experimental results demonstrate a 30% reduction in migration time and 25% improvement in resource utilization compared to Multipath TCP (MPTCP) and heuristic methods. Key innovations include: •A Decentralized Partially Observable Markov Decision Process (Dec-POMDP) framework for scalable multi-agent coordination. •Integration of actor-critic algorithms with epsilon-greedy exploration and parameter sharing for robust policy learning. •SDN-driven global state awareness to optimize VM placement.  © 2025 IEEE.

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
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2047.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
