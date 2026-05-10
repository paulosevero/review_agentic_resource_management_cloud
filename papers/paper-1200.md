---
id: paper-1200
title: Split task offloading algorithm for satellite-ground integrated networks based on deep deterministic policy gradient; [基于深度确定性策略梯度的星地融合网络可拆分任务卸载算法]
authors:
- Song, Xiaoqin
- Wu, Zhihao
- Lai, Haiguang
- Lei, Lei
- Zhang, Lijuan
- Lyu, Danyang
- Zheng, Chenghui
venue: Tongxin Xuebao/Journal on Communications
venue_type: journal
year: 2024
doi: 10.11959/j.issn.1000-436x.2024181
url: https://www.scopus.com/pages/publications/85209245789?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 116--128
keywords:
- deep deterministic policy gradient
- multi-access edge computing
- resource allocation
- satellite-ground integrated network
language: Chinese
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1200 — Split task offloading algorithm for satellite-ground integrated networks based on deep deterministic policy gradient; [基于深度确定性策略梯度的星地融合网络可拆分任务卸载算法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the prolonged task offloading delay in low earth orbit satellite networks, a split task offloading algorithm based on deep deterministic policy gradient (DDPG) was proposed for satellite-ground integrated networks. A multi-access edge computing structural model of the satellite-ground integrated network was established for users in different regions. By applying a multi-agent DDPG algorithm, the objective of minimizing total system service delay was transformed into maximizing agent reward returns. Under the constraints of sub-task offloading, service delay, and other task offloading conditions, the user task splitting ratio was optimized. Simulation results indicate that the proposed algorithm outperforms baseline algorithms in terms of user service delay and the number of benefited users. © 2024 Editorial Board of Journal on Communications. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1200.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
