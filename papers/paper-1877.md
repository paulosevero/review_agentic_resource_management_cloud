---
id: paper-1877
title: Distributed Computation Offloading for Energy Provision Minimization in WP-MEC Networks With Multiple HAPs
authors:
- Liu, Xiaoying
- Chen, Anping
- Zheng, Kechen
- Chi, Kaikai
- Yang, Bin
- Taleb, Tarik
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2024.3502004
url: https://www.scopus.com/pages/publications/86000734380?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2673--2689
keywords:
- energy provision minimization
- Mobile edge computing
- multi-agent deep reinforcement learning
- wireless power transfer
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1877 — Distributed Computation Offloading for Energy Provision Minimization in WP-MEC Networks With Multiple HAPs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates a wireless powered mobile edge computing (WP-MEC) network with multiple hybrid access points (HAPs) in a dynamic environment, where wireless devices (WDs) harvest energy from radio frequency (RF) signals of HAPs, and then compute their computation data locally (i.e., local computing mode) or offload it to the chosen HAPs (i.e., edge computing mode). In order to pursue a green computing design, we formulate an optimization problem that minimizes the long-term energy provision of the WP-MEC network subject to the energy, computing delay and computation data demand constraints. The transmit power of HAPs, the duration of the wireless power transfer (WPT) phase, the offloading decisions of WDs, the time allocation for offloading and the CPU frequency for local computing are jointly optimized adapting to the time-varying generated computation data and wireless channels of WDs. To efficiently address the formulated non-convex mixed integer programming (MIP) problem in a distributed manner, we propose a Two-stage Multi-Agent deep reinforcement learning-based Distributed computation Offloading (TMADO) framework, which consists of a high-level agent and multiple low-level agents. The high-level agent residing in all HAPs optimizes the transmit power of HAPs and the duration of the WPT phase, while each low-level agent residing in each WD optimizes its offloading decision, time allocation for offloading and CPU frequency for local computing. Simulation results show the superiority of the proposed TMADO framework in terms of the energy provision minimization.  © 2024 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1877.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
