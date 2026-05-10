---
id: paper-0593
title: 'Video Content Placement at the Network Edge: Centralized and Distributed Algorithms'
authors:
- Gao, Yanan
- Yang, Song
- Li, Fan
- Trajanovski, Stojan
- Zhou, Pan
- Hui, Pan
- Fu, Xiaoming
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2023
doi: 10.1109/TMC.2022.3200401
url: https://www.scopus.com/pages/publications/85137575983?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6843--6859
keywords:
- mobile edge computing
- multi-agent reinforcement learning
- online optimization
- Video content placement
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0593 — Video Content Placement at the Network Edge: Centralized and Distributed Algorithms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the traditional video streaming service paradigm, content providers typically provision the requested video content to viewers through a central content delivery network (CDN). However, remote viewers usually experience long video streaming delay due to uncertain wide area network delay, which severely affects the quality of experience. Multi-Access Edge Computing (MEC) offers a way to shorten the video streaming delay by building small-scale cloud infrastructures at the network edge, which are in close proximity to the viewers. In this paper, we present novel centralized and distributed algorithms for the video content placement problem in MEC. In the proposed centralized video content placement algorithm, we leverage the Lyapunov optimization technique to formulate the video content placement problem as a series of one-time-slot optimization problems and apply an Alternating Direction Method of Multipliers (ADMM)-based method to solve each of them. We further devise a distributed Multi-Agent Reinforcement Learning (MARL)-based method with value decomposition mechanism and parallelization policy update method to solve the video content placement problem. The value Decomposition mechanism deals with the credit assignment among multiple agents, which promotes the cooperative optimization of the global target and reduces the frequency of information exchange. The parallelization of policy network can speed up the convergence process. Simulation results verify the effectiveness and superiority of our proposed centralized and distributed algorithms in terms of performance.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0593.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
