---
id: paper-2777
title: Optimal deployment decision-making of unmanned platforms in space-air-ground-sea integrated network scenarios
authors:
- Sifeng, Zhu
- Jiaxu, Zhang
- Zonghui, Zhang
- Lei, Bao
- Zhipeng, Hao
- Qinghua, Zhang
- Guoqiang, Chen
- Rui, Qiao
- Mengmeng, Xu
- Hai, Zhu
venue: Expert Systems with Applications
venue_type: journal
year: 2026
doi: 10.1016/j.eswa.2026.131630
url: https://www.scopus.com/pages/publications/105034543448?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Clustering algorithm
- Dynamic deployment of unmanned platforms
- Edge computing
- Multi-agent reinforcement learning
- Space-air-ground-sea integrated network architecture
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2777 — Optimal deployment decision-making of unmanned platforms in space-air-ground-sea integrated network scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates the optimal deployment of unmanned platform (UP) nodes within the space-air-ground-sea integrated network (SAGSIN) architecture for maritime scenarios. To address key challenges including three-dimensional dynamic coverage optimization and collaborative edge computing service provisioning for multi-UP systems, the original deployment problem is decomposed into two interdependent sub-problems: user clustering and dynamic deployment optimization. For the user clustering task, a satellite-executed Weight-k-means++ algorithm is adopted to achieve efficient user categorization based on fine-grained user characteristic analysis. For the dynamic deployment optimization task, a multi-agent proximal policy optimization driven decision-making (R-MAPPO) scheme is proposed for UP nodes. Specifically, UP nodes dynamically adjust their spatial positions and movement velocities by fusing user clustering results and real-time offshore environmental perception data, thereby ensuring full coverage of all users while minimizing two core performance metrics: latency and energy consumption. Extensive experimental results verify that the reward value (comprehensive evaluation of latency and energy consumption) of R-MAPPO algorithm scheme improved by 10.20%, 10.32%, and 25.12% compared to MAPPO, MADDPG, and MADQN, respectively, while also demonstrating robust adaptability and scalability in complex, dynamic maritime network environments. © 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2777.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
