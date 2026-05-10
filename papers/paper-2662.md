---
id: paper-2662
title: Exploring Image Similarity to Optimize Resource Provisioning in Container-Enabled Edge Computing
authors:
- Li, Sisi
- Zhou, Ao
- Ma, Xiao
- Zhang, Yiran
- Wen, Jinfeng
- Wang, Shangguang
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3668419
url: https://www.scopus.com/pages/publications/105031942629?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1234--1247
keywords:
- Container
- edge computing
- resource provisioning
- service deployment
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

# paper-2662 — Exploring Image Similarity to Optimize Resource Provisioning in Container-Enabled Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Containerization offers great flexibility and agility for resource provisioning in edge clouds. However, this benefit is not freely available, as substantial network traffic incurred by container image pulling heavily burdens the back-haul networks. Our in-depth measurements on 516.3 GB images from Docker Hub reveal that many similar images share identical layers, with only 11.21% having no shared layers. Building on this, we investigate the resource provisioning problem by leveraging image similarity to avoid repeated layer transmissions, aiming to reduce network traffic and improve overall performance. We formulate resource provisioning as a mixed-integer non-linear programming problem, which is challenging due to the coupling of four issues and their conflicting effects on overall performance, including offloading decisions, container instance deployment, image pulling, and resource allocation. To tackle these complexities, we propose a novel Similarity-Aware Resource Provisioning approach, which decomposes the problem into independent sub-problems using counterfactual multi-agent deep reinforcement learning and then solves sub-problems individually with convex optimization and fractional programming techniques. We conduct extensive evaluations with images from Docker Hub. The results show that our approach enables up to 32.6% traffic reduction and 19.9% utility improvement, outperforming the state-of-the-art solutions. © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2662.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
