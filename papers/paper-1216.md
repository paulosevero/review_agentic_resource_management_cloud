---
id: paper-1216
title: Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning
authors:
- Tan, Jing
- Khalili, Ramin
- Karl, Holger
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2024
doi: 10.1109/TITS.2024.3378007
url: https://www.scopus.com/pages/publications/85189566821?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10777--10789
keywords:
- distributed systems
- multi-objective
- reinforcement learning
- V2X
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1216 — Multi-Objective Optimization Using Adaptive Distributed Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Intelligent Transportation System (ITS) environment is known to be dynamic and distributed, where participants (vehicle users, operators, etc.) have multiple, changing and possibly conflicting objectives. Although Reinforcement Learning (RL) algorithms are commonly applied to optimize ITS applications such as resource management and offloading, most RL algorithms focus on single objectives. In many situations, converting a multi-objective problem into a single-objective one is impossible, intractable or insufficient, making such RL algorithms inapplicable. We propose a multi-objective, multi-agent reinforcement learning (MARL) algorithm with high learning efficiency and low computational requirements, which automatically triggers adaptive few-shot learning in a dynamic, distributed and noisy environment with sparse and delayed reward. We test our algorithm in an ITS environment with edge cloud computing. Empirical results show that the algorithm is quick to adapt to new environments and performs better in all individual and system metrics compared to the state-of-the-art benchmark. Our algorithm also addresses various practical concerns with its modularized and asynchronous online training method. In addition to the cloud simulation, we test our algorithm on a single-board computer and show that it can make inference in 6 milliseconds.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1216.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
