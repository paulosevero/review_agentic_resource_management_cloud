---
id: paper-1568
title: 'DAPO: Mobility-Aware Joint Optimization of Model Partitioning and Task Offloading for Edge LLM Inference'
authors:
- Feng, Hao
- Huang, Gan
- Zhou, Nian
- Zhang, Feng
- Liu, Yuming
- Zhou, Xiumin
- Liu, Junchen
venue: Electronics (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/electronics14193929
url: https://www.scopus.com/pages/publications/105019044202?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- collaborative inference
- Large Language Models (LLMs)
- Mobile Edge Intelligence (MEI)
- model partitioning
- user mobility
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
    my_justification: LLM as workload
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

# paper-1568 — DAPO: Mobility-Aware Joint Optimization of Model Partitioning and Task Offloading for Edge LLM Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying Large Language Models (LLMs) in edge environments faces two major challenges: (i) the conflict between limited device resources and high computational demands, and (ii) the dynamic impact of user mobility on model partitioning and task offloading decisions. To address these challenges, this paper proposes the Dynamic Adaptive Partitioning and Offloading (DAPO) framework, an intelligent solution for multi-user, multi-edge Mobile Edge Intelligence (MEI) systems. DAPO employs a Deep Deterministic Policy Gradient (DDPG) algorithm to jointly optimize the model partition point and the task offloading destination. By mapping continuous policy outputs onto valid discrete actions, DAPO efficiently addresses the high-dimensional hybrid action space and dynamically adapts to user mobility. Through extensive simulations, we demonstrate that DAPO outperforms baseline strategies and mainstream RL methods, achieving up to 27% lower latency and 18% lower energy consumption compared to PPO and A2C, while maintaining fast convergence and scalability in dynamic mobile environments. © 2025 by the authors.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1568.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
