---
id: paper-2678
title: 'AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach'
authors:
- Liu, Xiaoying
- Zheng, Junhao
- Zheng, Kechen
- Liu, Jia
- Taleb, Tarik
- Shiratori, Norio
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3674155
url: https://www.scopus.com/pages/publications/105033470100?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Age of information
- federated learning
- heterogeneous network
- mobile edge computing
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2678 — AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates a dynamic heterogeneous mobile edge computing network (HMECN), where mobile devices (MDs) could offload their full tasks to a small base station (SBS) directly or the macro base station (MBS) in direct or relay mode. As age of information (AoI) is a comprehensive and accurate metric to capture the freshness of computation results, we formulate a long-term weighted sum AoI (LWSA) minimization problem in the HMECN by jointly optimizing the offloading decisions of MDs as well as the bandwidth and computation resource allocation of all base stations, subject to energy, delay and peak AoI constraints. To address the formulated non-convex mixed integer nonlinear programming problem, we decompose it into the offloading decision optimization (ODO) top-problem and the resource allocation optimization (RAO) sub-problem. Based on the decomposition, we propose a federated learning (FL)-assisted hybrid DRL and convex approach that is comprised of a safe multi-agent DRL algorithm, convex optimization and FL. The ODO top-problem is solved by the safe multi-agent DRL algorithm, which strictly ensures that the actions of each agent do not exceed its energy constraint and then paves the way for using convex optimization to solve the RAO sub-problem. FL is used to alleviate the training instability problem aggravated by multi agent settings via breaking the limitation of partial knowledge for each individual agent. Simulation results demonstrate the superiority of the proposed approach in terms of the LWSA, convergence, scalability and robustness in dynamic environments. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2678.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
