---
id: paper-0677
title: A Genetic Programming-based Framework for Semi-automated Multi-agent Systems Engineering
authors:
- Mc Donnell, Nicola
- Duggan, Jim
- Howley, Enda
venue: ACM Transactions on Autonomous and Adaptive Systems
venue_type: journal
year: 2023
doi: 10.1145/3584731
url: https://www.scopus.com/pages/publications/85177814867?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- Bin Packing Problem
- Genetic Programming
- multi-agent systems
- Nature-inspired computing
- operations research
- optimisation problems
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0677 — A Genetic Programming-based Framework for Semi-automated Multi-agent Systems Engineering

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rise of new technologies, such as Edge computing, Internet of Things, Smart Cities, and Smart Grids, there is a growing need for multi-agent systems (MAS) approaches. Designing multi-agent systems is challenging, and doing this in an automated way is even more so. To address this, we propose a new framework, Evolved Gossip Contracts (EGC). It builds on Gossip Contracts (GC), a decentralised cooperation protocol that is used as the communication mechanism to facilitate self-organisation in a cooperative MAS. GC has several methods that are implemented uniquely, depending on the goal the MAS aims to achieve. The EGC framework uses evolutionary computing to search for the best implementation of these methods. To evaluate EGC, it was used to solve a classical NP-hard optimisation problem, the Bin Packing Problem (BPP). The experimental results show that EGC successfully discovered a decentralised strategy to solve the BPP, which is better than two classical heuristics on test cases similar to those on which it was trained; the improvement is statistically significant. EGC is the first framework that leverages evolutionary computing to semi-automate the discovery of a communication protocol for a MAS that has been shown to be effective at solving an NP-hard problem.  © 2023 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0677.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
