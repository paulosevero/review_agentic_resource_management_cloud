---
id: paper-2946
title: Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning
authors:
- Zhu, Bincheng
- Zhu, Shaojun
- Chi, Kaikai
- Mumtaz, Shahid
- Bazzi, Wael
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3637266
url: https://www.scopus.com/pages/publications/105023179194?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6596--6613
keywords:
- convex-based critic
- counterfactual baseline
- mobile edge computing
- multi-agent
- NOMA
- Wireless power transfer
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2946 — Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Wireless power transfer enhanced mobile edge computing (WPT-MEC) has emerged as a key technology to support low-latency and energy-efficient computation in wireless networks. With increasing network density, multi-base-station architectures emerge where wireless devices (WDs) offload tasks to distributed base stations (BSs), creating challenges in maintaining quality-of-service fairness during complex resource coordination in multi-BS WPT-MEC networks. To address these challenges, we investigate a non-orthogonal multiple access (NOMA)-enhanced WPT-MEC network comprising multiple WDs and BSs with finite computational capacities. For ensuring fairness, we formulate a max-min problem to maximize the minimum task computation amount by jointly optimizing offloading decisions, NOMA decoding orders, offloading powers and time resource allocation, which results in a challenging mixed integer, sequence and nonlinear programming (MISNLP). To tackle this problem, we propose a two-stage distributed multi-agent algorithm. In the first stage, each BS agent generates offloading preferences based on partial observations, guiding WDs' offloading decisions. In the second stage, given these offloading decisions, we develop an efficient convex-based algorithm to solve the per-BS resource allocation subproblem, jointly optimizing NOMA decoding order, offloading powers and time resource allocation. For effective training, we leverage off-policy training and the centralized training with decentralized execution (CTDE) paradigm with two key innovations: (1) a convex-based critic that evaluates the joint action without bias, and (2) a counterfactual baseline that isolates individual agent credit assignment. The proposed C3MA algorithm achieves six times faster convergence and at least 20% performance improvement when serving more than 20 WDs, compared with existing multi-agent schemes, while maintaining a near-optimal Jain's fairness index of 0.97. Moreover, it sustains an ultra-low execution delay below 5 milliseconds even with 40 WDs, confirming its efficiency and scalability.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2946.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
