---
id: paper-2082
title: Towards Expert Models Deployment Cost Optimization in Edge Computing Networks
authors:
- Ren, Jiaqi
- Wang, Chao
- Zhong, Yihan
- Cao, Shaohua
- Zheng, Danyang
- Cao, Xiaojun
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11161045
url: https://www.scopus.com/pages/publications/105018462498?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 838--843
keywords:
- Cost optimization
- Expert model deployment
- Mixture of experts
- Network for AI
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2082 — Towards Expert Models Deployment Cost Optimization in Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the widespread adoption of large language models (LLMs) like GPT, user experiences in various interactive applications have significantly improved. However, reports from OpenAI highlight that GPT clients are now facing high response delays and frequent interruptions, particularly during peak usage hours, due to limited computation resources. This challenge is expected to escalate as machines are interacting with GPT models at higher frequencies, with greater data volumes, and over longer lifecycles. A promising solution is to deploy LLMs across edge networks to efficiently distribute the huge resource demands. This work presents the very first efforts at exploring how to cost-effectively deploy expert models from a mixture of experts (MoE) LLM within edge networks. We introduce the expert models deployment in edge networks (EMD-EN) problem, focusing on optimizing deployment costs. To address this, we propose a novel least cost gain (LCG) measure for selecting appropriate physical nodes to host expert models and present a corresponding LCG-based expert models deployment (LCGEMD) algorithm. Extensive simulations show that our approach outperforms the benchmarks by an average of 17.31% and 36.98% in terms of deployment cost reduction.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2082.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
