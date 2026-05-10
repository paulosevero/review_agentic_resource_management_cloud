---
id: paper-1289
title: Learning to Schedule Online Tasks with Bandit Feedback
authors:
- Xu, Yongxin
- Wang, Shangshang
- Guo, Hengquan
- Liu, Xin
- Shao, Ziyu
venue: Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems, AAMAS
venue_type: conference
year: 2024
doi: ''
url: https://www.scopus.com/pages/publications/85196365672?origin=resultslist
publisher: International Foundation for Autonomous Agents and Multiagent Systems (IFAAMAS)
pages: 1975--1983
keywords:
- Double-Optimistic learning
- Online scheduling
- Robbins-Monro method
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1289 — Learning to Schedule Online Tasks with Bandit Feedback

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Online task scheduling serves an integral role for task-intensive applications in cloud computing and crowdsourcing. Optimal scheduling can enhance system performance, typically measured by the reward-to-cost ratio, under some task arrival distribution. On one hand, both reward and cost are dependent on task context (e.g., evaluation metric) and remain black-box in practice. These render reward and cost hard to model thus unknown before decision making. On the other hand, task arrival behaviors remain sensitive to factors like unpredictable system fluctuation whereby a prior estimation or the conventional assumption of arrival distribution (e.g., Poisson) may fail. This implies another practical yet often neglected challenge, i.e., uncertain task arrival distribution. Towards effective scheduling under a stationary environment with various uncertainties, we propose a double-optimistic learning based Robbins-Monro (DOL-RM) algorithm. Specifically, DOL-RM integrates a learning module that incorporates optimistic estimation for reward-to-cost ratio and a decision module that utilizes the Robbins-Monro method to implicitly learn task arrival distribution while making scheduling decisions. Theoretically, DOL-RM achieves a sub-linear regret of O(T<sup>3</sup>/<sup>4</sup>), which is the first result for online task scheduling under uncertain task arrival distribution and unknown reward and cost. Our numerical results in a synthetic experiment and a real-world application demonstrate the effectiveness of DOL-RM in achieving the best cumulative reward-to-cost ratio compared with other state-of-the-art baselines. © 2024 International Foundation for Autonomous Agents and Multiagent Systems.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1289.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
