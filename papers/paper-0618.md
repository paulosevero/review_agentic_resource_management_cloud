---
id: paper-0618
title: Multi-Agent Deep Reinforcement Learning for Efficient Computation Offloading in Mobile Edge Computing
authors:
- Jiao, Tianzhe
- Feng, Xiaoyue
- Guo, Chaopeng
- Wang, Dongqi
- Song, Jie
venue: Computers, Materials and Continua
venue_type: journal
year: 2023
doi: 10.32604/cmc.2023.040068
url: https://www.scopus.com/pages/publications/85174390562?origin=resultslist
publisher: Tech Science Press
pages: 3585--3603
keywords:
- Computation offloading
- energy efficiency
- latency
- mobile-edge computing
- multi-agent deep reinforcement learning
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

# paper-0618 — Multi-Agent Deep Reinforcement Learning for Efficient Computation Offloading in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile-edge computing (MEC) is a promising technology for the fifth-generation (5G) and sixth-generation (6G) architectures, which provides resourceful computing capabilities for Internet of Things (IoT) devices, such as virtual reality, mobile devices, and smart cities. In general, these IoT applications always bring higher energy consumption than traditional applications, which are usually energy-constrained. To provide persistent energy, many references have studied the offloading problem to save energy consumption. However, the dynamic environment dramatically increases the optimization difficulty of the offloading decision. In this paper, we aim to minimize the energy consumption of the entire MEC system under the latency constraint by fully considering the dynamic environment. Under Markov games, we propose a multi-agent deep reinforcement learning approach based on the bi-level actor-critic learning structure to jointly optimize the offloading decision and resource allocation, which can solve the combinatorial optimization problem using an asymmetric method and compute the Stackelberg equilibrium as a better convergence point than Nash equilibrium in terms of Pareto superiority. Our method can better adapt to a dynamic environment during the data transmission than the single-agent strategy and can effectively tackle the coordination problem in the multi-agent environment. The simulation results show that the proposed method could decrease the total computational overhead by 17.8% compared to the actor-critic-based method and reduce the total computational overhead by 31.3%, 36.5%, and 44.7% compared with random offloading, all local execution, and all offloading execution, respectively. © 2023 Tech Science Press. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0618.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
