---
id: paper-1713
title: Multi-dimensional resource orchestration and scheduling method driven by AI inference services via hypergraph and genetic algorithm; [基于超图和遗传算法的 AI 推理服务驱动的多维资源编排与调度方法]
authors:
- Jing, Chuanfang
- Zhu, Xiaorong
venue: Tongxin Xuebao/Journal on Communications
venue_type: journal
year: 2025
doi: 10.11959/j.issn.1000-436x.2025180
url: https://www.scopus.com/pages/publications/105023446987?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 118--133
keywords:
- 6G network
- AI inference service
- hypergraph
- multi-dimensional resource
- orchestration and scheduling
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1713 — Multi-dimensional resource orchestration and scheduling method driven by AI inference services via hypergraph and genetic algorithm; [基于超图和遗传算法的 AI 推理服务驱动的多维资源编排与调度方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To tackle the stringent performance requirements of AI inference services and the complex coupling of multidimensional (MR) resources in 6G networks, a hypergraph and genetic algorithm-based method for AI inference service-driven MR orchestration and scheduling was proposed. Firstly, hypergraph accurately captured the high-order dependency relationships among AI inference tasks in the service layer, algorithm-data-computing-connection resources in the logical layer, and infrastructure in the physical layer. Secondly, a cross-layer MR dynamic matching optimization problem was formulated. The problem aimed to achieve the best match between service demands and network resources through joint allocation of AI inference tasks, microservices involving MR, and intelligent agents. Meanwhile, an improved non-dominated sorting genetic algorithm-II was proposed. By leveraging the pre-classification characteristics of hyperedges to flexibly reduce the solution dimension, the convergence speed of the algorithm was improved. Simulation results demonstrate that the proposed method outperforms the comparative algorithms in balancing inference latency and inference accuracy, thus validating the effectiveness and practicality of the proposed algorithm. © 2025, Editorial Board of Journal on Communications. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1713.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
