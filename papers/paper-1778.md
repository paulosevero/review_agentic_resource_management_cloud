---
id: paper-1778
title: A Resource Scheduling Method Based on the Dual Sparse Attention Mechanism A2C Network
authors:
- Li, Xueqian
- Yu, Xiuli
- Wei, Shimin
venue: 2025 13th International Conference on Information and Communication Networks, ICICN 2025
venue_type: conference
year: 2025
doi: 10.1109/ICICN67355.2025.11430409
url: https://www.scopus.com/pages/publications/105035547128?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 269--275
keywords:
- A2C
- cloud computing
- deep reinforcement learning
- resource dispatch
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1778 — A Resource Scheduling Method Based on the Dual Sparse Attention Mechanism A2C Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of high resource demands and low utilization rates in distributed training resources for current embodied intelligence large model training, a cloud computing resource scheduling method based on a dual sparse attention mechanism A2C network is proposed. This method improves resource scheduling efficiency and load balancing in cloud computing environments through multi-agent collaboration. First, the input task set is classified into four major types according to their characteristics: high-CPU tasks, high-MEM tasks, long-time tasks, and balanced tasks. Second, agents based on the dual sparse attention mechanism A2C network are independently designed according to task characteristics. This method considers dual-objective optimization of scheduling time and load balancing during policy updates. A dual sparse attention mechanism is introduced within the critic network to dynamically screen key information from adjacent agents and achieve implicit collaboration. Finally, simulations were conducted on the Alibaba v2018 dataset. Experimental results demonstrate that compared to Random, FirstFit, and Tetris, the proposed method significantly reduces resource scheduling time, increases throughput, and optimizes load balancing. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1778.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
