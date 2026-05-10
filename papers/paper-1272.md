---
id: paper-1272
title: Counterfactual Reward Estimation for Credit Assignment in Multi-agent Deep Reinforcement Learning over Wireless Video Transmission
authors:
- Wenhan, Y.
- Qian, Liangxin
- Chua, Terence Jie
- Zhao, Jun
venue: Proceedings - International Conference on Distributed Computing Systems
venue_type: conference
year: 2024
doi: 10.1109/ICDCS60910.2024.00112
url: https://www.scopus.com/pages/publications/85203146172?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1177--1189
keywords:
- credit assignment
- multi-agent deep reinforcement learning
- Video transmission
- wireless communication
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1272 — Counterfactual Reward Estimation for Credit Assignment in Multi-agent Deep Reinforcement Learning over Wireless Video Transmission

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study investigates frame-wise optimization in Mobile Edge Computing (MEC) for video transmission, emphasizing dynamic adaptation to diverse frame complexities and efficient resource utilization. The comprehensive system model captures the complexities of joint optimizations in MEC for real-time video transmission, addressing challenges associated with error concealment techniques, and enhancing the user experience by addressing successive frame losses. To handle credit assignment in multi-agent scenarios, we integrate counterfactual reward shaping, introducing a counterfactual reward multi-agent proximal policy optimization (CRMAPPO). Results reveal the impact of the credit assignment parameter (β) on algorithm performance, demonstrating a trade-off between accurate credit assignment and policy bias. The study emphasizes CRMAPPO's performance, surpassing traditional MAPPO under optimal β choices, marking a substantial 109.18% improvement in total rewards. This research significantly contributes to optimizing resource allocation in video transmission within MEC frameworks, addressing challenges associated with frame-wise optimization and providing a nuanced understanding of credit assignment dynamics in multi-agent environments.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1272.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
