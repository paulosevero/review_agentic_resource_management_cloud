---
id: paper-0555
title: Admission Control for Games with a Dynamic Set of Players
authors:
- Bistritz, Ilai
- Bambos, Nicholas
venue: Proceedings of the IEEE Conference on Decision and Control
venue_type: conference
year: 2023
doi: 10.1109/CDC49753.2023.10383907
url: https://www.scopus.com/pages/publications/85184813126?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1219--1224
keywords:
- Distributed computer systems
- Learning algorithms
- Multi agent systems
- Online systems
- Admission-control
- Best response
- Cloud-computing
- Continous time
- Exponentials
- Nash equilibria
- Online marketplaces
- Open multi-agent system
- Performance guarantees
- Poisson process
- Continuous time systems
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0555 — Admission Control for Games with a Dynamic Set of Players

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We consider open games where players arrive according to a Poisson process with rate λ and stay in the game for an exponential random duration with rate μ. The game evolves in continuous time where each player n sets an exponential random clock and updates her action an ∈ {0,⋯, K} when it expires. The players take independent best-response actions that, uninterrupted, can converge to a Nash Equilibrium (NE). This models open multiagent systems such as wireless networks, cloud computing, and online marketplaces. When λ is small, the game spends most of the time in a (time-varying) equilibrium. This equilibrium exhibits predictable behavior and can have performance guarantees by design. However, when λ is too small, the system is under-utilized since not many players are in the game on average. Choosing the maximal λ that the game can support while still spending a target fraction 0 < ρ < 1 of the time at equilibrium requires knowing the reward functions. To overcome that, we propose an online learning algorithm that the gamekeeper uses to adjust the probability θ to admit an incoming player. The gamekeeper only observes whether an action was changed, without observing the action or who played it. We prove that our algorithm learns, with probability 1, a θ∗ such that the game is at equilibrium for at least ρ fraction of the time, and no more than ρ+ϵ(μ,ρ) < 1, where we provide an analytic expression for ϵ(μ,ρ). Our algorithm is a black-box method to transfer performance guarantees of distributed protocols from closed systems to open systems.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0555.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
