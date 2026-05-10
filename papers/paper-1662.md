---
id: paper-1662
title: Joint Optimization of Resource Allocation and Task Offloading Strategies in Multi-Cell Dynamic MEC Systems Using Multi-Agent DRL
authors:
- Hu, Yuntao
- Chen, Ming
- Sun, Haowen
- Wang, Yinlu
- Cang, Yihan
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3584471
url: https://www.scopus.com/pages/publications/105009978077?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 118933--118943
keywords:
- centralized training and decentralized execution (CTDE)
- embedding method
- Long-term multi-cell MEC systems
- multi-agent deep reinforcement learning (MADRL)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1662 — Joint Optimization of Resource Allocation and Task Offloading Strategies in Multi-Cell Dynamic MEC Systems Using Multi-Agent DRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper focuses on minimizing the total energy consumption of a long-term delay-sensitive multi-cell mobile edge computing (MEC) system that serves continuously arriving mobile devices (MDs). The energy consumption minimization is achieved by jointly optimizing the task offloading proportions, transmit power allocations, and computational resource distributions while ensuring the overall deadline constraints and the minimum processing size requirements in each scheduling cycle. The optimization problem is then formulated as a multi-agent Markov decision process (MAMDP) to enable sequential optimization across multiple scheduling cycles. To efficiently solve the formulated problem, we develop a multi-agent deep reinforcement learning (MADRL) algorithm that integrates the actor-critic (AC) framework, the embedding techniques, and the centralized training and decentralized execution (CTDE) framework. Simulation results show that the proposed algorithm converges 14%-23% faster than benchmark methods and significantly outperforms benchmark methods in reducing the total energy consumption under specific constraints by up to 10%. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1662.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
