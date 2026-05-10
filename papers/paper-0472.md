---
id: paper-0472
title: Data-aware Hierarchical Federated Learning via Task Offloading
authors:
- Ma, Mulei
- Wu, Liantao
- Liu, Wenxiang
- Chen, Nanxi
- Shao, Ziyu
- Yang, Yang
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2022
doi: 10.1109/GLOBECOM48099.2022.10000924
url: https://www.scopus.com/pages/publications/85146932846?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3011--3016
keywords:
- Deep Reinforcement Learning
- Hierarchical Federated Edge Learning
- Multi-Access Edge Computing
- Resource Allocation
- Task Offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0472 — Data-aware Hierarchical Federated Learning via Task Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To cope with the high communication overhead caused by frequent aggregation of Federated Learning (FL) in Multi-access Edge Computing (MEC) scenarios, Hierarchical Federated Edge Learning (HFEL) is proposed as an evolving framework. HFEL offloads tasks to edge servers for partial model aggregation to reduce network traffic. However, most of the existing research focuses on resource optimization for HFEL without considering the impact of data characteristics and cannot guarantee the quality of FL training. To this end, we propose a task offloading approach based on data and resource heterogeneity under HFEL to improve training performance and reduce system cost. Specifically, we leverage information entropy to incorporate data statistical features into the cost function to reshape edge datasets. In addition, we applied Multi-Agent Deep Deterministic Policy Gradient (MADDPG) with a resource allocation module to generate distributed offloading policy more efficiently. Our algorithm not only adopts local observations to obtain the optimal action but also takes into account device heterogeneity, which can adapt to the unstable edge environment. Extensive experiments under multiple datasets and baselines are carried out, which demonstrate that our algorithm can effectively improve the accuracy of aggregated models while reducing system cost. © 2022 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0472.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
