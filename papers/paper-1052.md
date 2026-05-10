---
id: paper-1052
title: A Multi-Agent DRL-Based Computation Offloading and Resource Allocation Method With Attention Mechanism in MEC-Enabled IIoT
authors:
- Ling, Chengfang
- Peng, Kai
- Wang, Shangguang
- Xu, Xiaolong
- Leung, Victor C. M.
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2024
doi: 10.1109/TSC.2024.3466852
url: https://www.scopus.com/pages/publications/85206250782?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3037--3051
keywords:
- attention mechanism
- IIoT
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

# paper-1052 — A Multi-Agent DRL-Based Computation Offloading and Resource Allocation Method With Attention Mechanism in MEC-Enabled IIoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The widespread adoption of Industrial Internet of Things (IIoT) has significantly transformed various aspects of industrial manufacturing. However, the massive volume and complexity of IIoT data highlight the need for innovative solutions to enhance the overall performance of IIoT systems. In this regard, mobile edge computing, assisted by deep reinforcement learning, can alleviate the burden on IIoT systems through computation offloading. Nevertheless, in increasingly digitized industrial environments, how to make real-time, efficient task offloading decisions remains a subject of deep exploration. To address this issue, we propose a two-stage resource allocation and task offloading method, named MCORM. In the first stage, we use the Combinatorial Upper Confidence Bound algorithm, based on the combinatorial multi-armed bandit problem, to solve the resource allocation problem. In the second stage, the Multi-Agent Proximal Policy Optimization algorithm is employed to determine the approximate optimal offloading strategy. Specifically, the Convolutional Block Attention Module is utilized to process observation information, focusing on important features. Finally, extensive experiments are conducted using both simulated and real datasets. The results demonstrate that our proposed algorithm MCORM can reduce latency and energy consumption effectively, promoting efficient industrial production.  © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1052.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
