---
id: paper-2914
title: Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information
authors:
- Zhang, Jing
- Shen, Fei
- Yan, Feng
- Li, Jie
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3634598
url: https://www.scopus.com/pages/publications/105022251819?origin=resultslist
publisher: IEEE Computer Society
pages: 3499--3515
keywords:
- Multi-agent reinforcement learning
- Nash equilibrium
- partially observable Markov decision process (POMDP)
- stochastic game
- vehicular edge offloading
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

# paper-2914 — Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing provides low-latency computational services for task offloading in vehicular networks. However, challenges such as dynamic transmission rates, resource limitations, and information-sharing constraints impede efficient offloading. Few studies address these issues concurrently in designing dynamic offloading strategies, often resulting in sub-optimal system utility. This paper aims to achieve efficient vehicular task offloading via an idleness-aware edge server (ES) from a game theory perspective. We propose a Gated Recurrent Unit (GRU) prediction model with an attention mechanism to guide vehicles to the nearest idle ES. The offloading decision process is modeled as a stochastic game, proving the existence of a Nash equilibrium (NE). Additionally, we model it as a multi-agent partially observable Markov decision process (POMDP) to account for limited information access among vehicles. To solve the POMDP and achieve near-optimal NE, we introduce a Multi-Agent Reinforcement Learning-based Task Offloading (MATO) algorithm, combining a Differentiable Neural Computer (DNC) and an Advantageous Actor-Critic (A2C) framework. The DNC’s external memory stores structured representations of past information, enabling deeper exploration of the strategy space. Adjusting the reward representation enhances training efficiency. Experimental results driven by real-world datasets demonstrate that MATO effectively improves the computing offloading utility while increasing the convergence speed compared to existing schemes. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2914.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
