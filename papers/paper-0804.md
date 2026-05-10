---
id: paper-0804
title: Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing
authors:
- Zhou, Ao
- Li, Sisi
- Ma, Xiao
- Zhang, Yiran
- Wang, Shangguang
venue: Proceedings - 2023 IEEE International Conference on Web Services, ICWS 2023
venue_type: conference
year: 2023
doi: 10.1109/ICWS60048.2023.00047
url: https://www.scopus.com/pages/publications/85173880801?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 278--288
keywords:
- Container image
- Edge computing
- Instance deployment.
- Offloading
- Resource provisioning
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

# paper-0804 — Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Container-enabled serverless computing has become a widely adopted approach for resource provisioning in the edge cloud. However, traffic incurred by container image pulling heavily burdens the already congested back-haul network. To relieve the problem, we do an analysis on Docker Hub, and find that instance deployment strategy has a significant impact on the back-haul traffic due to the varying similarity levels of different images. We incorporate this feature into task offloading decision and resource provisioning, and formulate the problem with a mixed integer non-linear programming (MINLP) problem. To address the challenges arising from the coupling and contradiction of instance deployment, image pulling, offloading decision, and resource allocation, we employ multi-agent deep reinforcement learning to decompose the problem into several simpler sub-problems, and design an algorithm for each sub-problem individually by exploiting convex optimization and fractional programming techniques. Simulations are conducted to validate the effectiveness of the proposed algorithm. The experiment results illustrate that our algorithm outperforms current notable solutions and improves the global utility by 13%-74%. © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0804.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
