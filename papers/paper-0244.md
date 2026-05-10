---
id: paper-0244
title: Temporal Fusion Pointer network-based Reinforcement Learning algorithm for Multi-Objective Workflow Scheduling in the cloud
authors:
- Wang, Binyang
- Li, Huifang
- Lin, Zhiwei
- Xia, Yuanqing
venue: Proceedings of the International Joint Conference on Neural Networks
venue_type: conference
year: 2020
doi: 10.1109/IJCNN48605.2020.9207151
url: https://www.scopus.com/pages/publications/85093816795?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud computing
- Multi-objective workflow scheduling
- Neural networks
- Reinforcement Learning
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

# paper-0244 — Temporal Fusion Pointer network-based Reinforcement Learning algorithm for Multi-Objective Workflow Scheduling in the cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is emerging as a deployment promising environment for hosting exponentially increasing scientific and social media applications, but how to manage and execute these applications efficiently depends mainly on workflow scheduling. However, scheduling workflows in the cloud is an NP-hard problem and its existing solutions have certain limitations when applied to real-world scenarios. In this paper, a Temporal Fusion Pointer network-based Reinforcement Learning algorithm for multi-objective workflow scheduling (TFP-RL) is proposed. Through adopting reinforcement learning, our algorithm can discover its heuristics over time by continuous learning according to the rewards resulting from good scheduling solutions. To make more comprehensive scheduling decisions as the influence of historical actions, a novel temporal fusion pointer network (TFP) is designed for the reinforcement learning agent, which can improve the quality of our resulting solutions and the ability of our algorithm in dealing with versatile workflow applications. To decrease convergence time, we train the proposed TFP-RL model independently by the Asynchronous Advantage Actor-Critic method and use its resulting model for scheduling workflows. Finally, under a multi-agent reinforcement learning framework, a Pareto dominance-oriented criterion for reasonable action selection is established for a multi-objective optimization scenario. We first train our TFP-RL model by taking randomly generated workflows as inputs to validate its effectiveness in scheduling, then compare our trained model with other existing scheduling approaches through practical compute- and data-intensive workflows. Experimental results demonstrate that our proposed algorithm outperforms the benchmarking ones in terms of different metrics. © 2020 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0244.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
