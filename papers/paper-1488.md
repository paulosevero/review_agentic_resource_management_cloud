---
id: paper-1488
title: 'IFresher: Information Freshening for Mobile Augmented Reality With Multi-Agent Reinforcement Learning in Edge Computing'
authors:
- Cheng, Shuang
- Wang, Zhaoyang
- Feng, Fangzheng
- Zhang, Yu
- Bi, Ting
- Jiang, Tao
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3581523
url: https://www.scopus.com/pages/publications/105008938138?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11703--11716
keywords:
- age of information
- bandwidth allocation
- Mobile augmented reality
- multi-agent deep reinforcement learning
- video configuration adaptation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1488 — IFresher: Information Freshening for Mobile Augmented Reality With Multi-Agent Reinforcement Learning in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we propose the IFresher framework to improve the timeliness of multi-agent mobile augmented reality (MAR) systems. Existing works have made strides in accuracy-latency trade-offs, but fail to directly address real-time task responsiveness and multi-agent contention challenges. To bridge this gap, we introduce the concept of the age of analytics information (AoAI), which quantifies the combined impact of video analytics (VA) accuracy, transmission delay, and computational efficiency. By deriving a closed-form expression for AoAI, IFresher establishes a central control mechanism that jointly optimizes bandwidth allocation and video configuration to minimize AoAI while ensuring accuracy. Due to the mixed-integer nonlinear characteristics of the problem and the fact that each agent only has local observations, the problem is reformulated into a decentralized partially observable Markov decision process (Dec-POMDP). We propose a multi-agent reinforcement learning (MARL) algorithm, named convex-embedded transformer QMIX (CTQMIX), using the centralized training and decentralized execution (CTDE) framework for agent collaboration. Specifically, the convex optimization ensures optimal bandwidth distribution, and the transformer captures temporal dependencies between observations and actions across time steps to improve decision-making in dynamic environments. Evaluations with real-world experiments show that the CTQMIX outperforms state-of-the-art (SOTA) algorithms. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1488.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
