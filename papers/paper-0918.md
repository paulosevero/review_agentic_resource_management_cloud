---
id: paper-0918
title: 'EdgeVision: Towards Collaborative Video Analytics on Distributed Edges for Performance Maximization'
authors:
- Gao, Guanyu
- Dong, Yuqi
- Wang, Ran
- Zhou, Xin
venue: IEEE Transactions on Multimedia
venue_type: journal
year: 2024
doi: 10.1109/TMM.2024.3385678
url: https://www.scopus.com/pages/publications/85193529393?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9083--9094
keywords:
- Edge intelligence
- edge/cloud computing
- multi-edge collaborative learning
- video analytics
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

# paper-0918 — EdgeVision: Towards Collaborative Video Analytics on Distributed Edges for Performance Maximization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deep Neural Network (DNN)-based video analytics significantly improves recognition accuracy in computer vision applications. Deploying DNN models at edge nodes, closer to end users, reduces inference delay and minimizes bandwidth costs. However, these resource-constrained edge nodes may experience substantial delays under heavy workloads, leading to imbalanced workload distribution. While previous efforts focused on optimizing hierarchical device-edge-cloud architectures or centralized clusters for video analytics, we propose addressing these challenges through collaborative distributed and autonomous edge nodes. Despite the intricate control involved, we introduce EdgeVision, a Multiagent Reinforcement Learning (MARL)-based framework for collaborative video analytics on distributed edges. EdgeVision enables edge nodes to autonomously learn policies for video preprocessing, model selection, and request dispatching. Our approach utilizes an actor-critic-based MARL algorithm enhanced with an attention mechanism to learn optimal policies. To validate EdgeVision, we construct a multi-edge testbed and conduct experiments with real-world datasets. Results demonstrate a performance enhancement of 33.6% to 86.4% compared to baseline methods.  © 1999-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0918.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
