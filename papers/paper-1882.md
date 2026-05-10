---
id: paper-1882
title: Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing
authors:
- Liu, Zhicheng
- Wang, Yilan
- Zhao, Yunfeng
- Qiu, Chao
- Zhang, Cheng
- Wang, Xiaofei
- Dong, Mianxiong
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3588142
url: https://www.scopus.com/pages/publications/105012290036?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12784--12801
keywords:
- mobile edge computing
- model inference
- object detection
- task offloading
- Video detection
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1882 — Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Real-time video detection is essential for many mobile visual applications, which brings the heavy computational burden of deep neural networks. Mobile edge computing offers a promising solution by deploying computational resources near mobile devices. However, achieving efficient video detection on mobile devices requires addressing challenges such as different performance requirements, diverse computing and network conditions, and system dynamics. We propose a real-time video detection framework in mobile edge computing, where multiple video streams from mobile devices are processed while balancing key performance metrics with consideration of grouping. A joint optimization problem of task scheduling, model selection, and resource provisioning is formulated for the system, where decisions are made on two timescales. To this end, we propose a window controller to unify decision-making at the time-slot level. We design an online scheduling algorithm based on multi-agent deep reinforcement learning to enable adaptive and distributed scheduling, while a masking-enhanced attention mechanism enables efficient explicit information exchange between mobile devices. Experimental evaluations across different numbers of mobile devices demonstrate that, in terms of average reward, the proposed algorithm outperforms local processing by 14.600%, fixed offloading by 10.007%, and four learning-based scheduling baselines by an average of 2.267%.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1882.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
