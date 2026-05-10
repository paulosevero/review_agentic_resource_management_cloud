---
id: paper-2458
title: Towards Profits Optimization in LLM Inference Model Deployment at the Network Edge
authors:
- Zhang, Yuqi
- Zheng, Danyang
- Xing, Huanlai
- Xu, Honghui
- Peng, Chengzong
- Wang, Chao
- Cao, Xiaojun
venue: Conference Proceedings of the IEEE International Performance, Computing, and Communications Conference
venue_type: conference
year: 2025
doi: 10.1109/IPCCC66453.2025.11304692
url: https://www.scopus.com/pages/publications/105032370158?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- edge computing
- heuristic algorithm
- inference chain deployment
- large language model
- Profit optimization
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

# paper-2458 — Towards Profits Optimization in LLM Inference Model Deployment at the Network Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent advances in large language models (LLMs) have empowered robots and drones with autonomous decision-making capabilities. Due to the stringent real-Time requirements of these applications, LLM inference must be performed at the network edge. However, hosting high-precision LLMs on a single edge server is often infeasible, creating challenges in efficiently distributing LLM deployments across edge networks. This work addresses these challenges by formulating and solving the profit maximization problem for distributed LLM inference deployment. We first formally define the Profit-Centric Inference Chain Deployment (PC-InCD) problem. To solve PC-InCD, we introduce a novel Local Maximal Profit (LMP) factor that enables effective edge server selection for hosting LLM sub-modules, and we propose the LMP-based Inference Chain Deployment (LMP-InCD) algorithm. Extensive simulations demonstrate that LMP-InCD significantly outperforms benchmark methods in maximizing profit across diverse network conditions. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2458.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
