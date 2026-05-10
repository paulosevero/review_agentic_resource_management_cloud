---
id: paper-1536
title: Discretized Distributed Optimization over Dynamic Digraphs
authors:
- Doostmohammadian, Mohammadreza
- Jiang, Wei
- Liaquat, Muwahida
- Aghasi, Alireza
- Zarrabi, Houman
venue: IEEE Transactions on Automation Science and Engineering
venue_type: journal
year: 2025
doi: 10.1109/TASE.2024.3383894
url: https://www.scopus.com/pages/publications/85190169910?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2758--2767
keywords:
- consensus constraint
- Distributed optimization
- dynamic digraphs
- matrix perturbation theory
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1536 — Discretized Distributed Optimization over Dynamic Digraphs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We consider a discrete-time model of continuous-time distributed optimization over dynamic directed-graphs (digraphs) with applications to distributed learning. Our optimization algorithm works over general strongly connected dynamic networks under switching topologies, e.g., in mobile multi-agent systems and volatile networks due to link failures. Compared to many existing lines of work, there is no need for bi-stochastic weight designs on the links. The existing literature mostly needs the link weights to be stochastic using specific weight-design algorithms needed both at the initialization and at all times when the topology of the network changes. This paper eliminates the need for such algorithms and paves the way for distributed optimization over time-varying digraphs. We derive the bound on the gradient-tracking step-size and discrete time-step for convergence and prove dynamic stability using arguments from consensus algorithms, matrix perturbation theory, and Lyapunov theory. This work, particularly, is an improvement over existing stochastic-weight undirected networks in case of link removal or packet drops. This is because the existing literature may need to rerun time-consuming and computationally complex algorithms for stochastic design, while the proposed strategy works as long as the underlying network is weight-symmetric and balanced. The proposed optimization framework finds applications to distributed classification and learning. Note to Practitioners - Inspired by recent advances in cloud-computing and distributed and parallel processing along with embedded low-cost CPUs and wireless communications, this paper considers distributed algorithms for optimization and machine learning over wireless-connected autonomous multi-agent systems (MASs). In contrast to the classical centralized learning methods, which are prone to single-point-of-failure and centralized processing, in cooperative optimization the learning is distributed among a group of data-processing agents (e.g. robots) with communication units. This article provides an efficient algorithm to enable MASs to collaboratively optimize a cost function, e.g., for binary classification and distributed support vector machine (D-SVM). Sampled data systems related to MASs and robotic networks, due to digital communications and discretized control models, use discrete-time algorithms that need to account for intermittent communications and dynamic networking. This requires discretized algorithms over dynamic digraphs, practical in the presence of packet drops (or lost communication channels). Most existing distributed algorithms either are susceptible to change in the communication network or impose computationally inefficient stochastic design. These algorithms need to be rerun, for example, whenever the mobile robotic network changes due to limited communication range. This makes most existing algorithms infeasible in real-time applications. Our proposed method outperforms similar algorithms over dynamic robotic networks and in the presence of link removal (packet drops). We show this efficiency of our distributed optimization method by simulation.  © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1536.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
