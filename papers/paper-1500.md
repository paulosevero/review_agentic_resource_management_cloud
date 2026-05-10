---
id: paper-1500
title: Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing
authors:
- Cui, Hanshuai
- Tang, Zhiqing
- Wu, Yuan
- Jia, Weijia
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3583153
url: https://www.scopus.com/pages/publications/105009746660?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12314--12328
keywords:
- Container update
- edge computing
- edge-cloud collaboration
- layer sharing
- reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1500 — Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Containers have become popular for deploying applications in Edge Computing (EC) for their seamless integration and easy deployment. Frequent container updates are essential to enhance performance and introduce new challenges for cutting-edge applications such as large language models and digital twins. However, traditional container update methods result in substantial download costs and task interruptions, which are unacceptable for latency-sensitive tasks in resource-constrained EC. Existing work has largely overlooked the layered structure of container images. By leveraging this layered structure, duplicate downloads can be reduced, and various layers can be transferred from other edges, reducing burden on the remote cloud. In this paper, we model the layer-aware container update problem with edge-cloud collaboration to minimize update and scheduling costs. We present the Layer-aware Edge-cloud collaborative Container Update (LECU) algorithm based on reinforcement learning to make container update decisions. Moreover, a task scheduling algorithm is devised to schedule tasks affected by container updates to other edges, minimizing the impact of task interruptions. We implement our LECU algorithm on an edge system with real-world data traces to demonstrate its effectiveness and conduct larger-scale simulations to evaluate its scalability. Results demonstrate that our algorithms reduce container update and task scheduling costs by 14% and 19%, respectively, compared to baselines. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1500.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
