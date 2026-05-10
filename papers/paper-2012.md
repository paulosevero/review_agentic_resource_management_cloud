---
id: paper-2012
title: 'Burst-Aware Weighted Fair Queueing for Serverless Inference: Mitigating Noisy Neighbor Effects in Multi-Tenant Systems'
authors:
- Pandey, Rajesh Kumar
- Soni, Jubin Abhishek
- Anand, Amit
venue: Journal of Soft Computing and Data Mining
venue_type: journal
year: 2025
doi: 10.30880/jscdm.2025.06.03.022
url: https://www.scopus.com/pages/publications/105027645350?origin=resultslist
publisher: Penerbit UTHM
pages: 356--369
keywords:
- fair queueing
- machine learning inference
- multi-tenancy
- resource scheduling
- Serverless computing
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

# paper-2012 — Burst-Aware Weighted Fair Queueing for Serverless Inference: Mitigating Noisy Neighbor Effects in Multi-Tenant Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-tenant serverless inference often devolves into noisy-neighbor scenarios where a single tenant’s bursty LLM batch floods the fleet, pushing interactive calls beyond their latency budgets. We propose Burst-Aware Weighted Fair Queueing (BWFQ), a scheduler that requires only two counters per tenant (tokens earned, tokens spent) and a constant-time heap pop to select the next invocation. In BWFQ, we use a token bucket in which tokens accumulate at a tenant-specific base rate and are depleted on each dispatch. When a tenant exhausts all its tokens, its requests are queued, giving chances to other quieter tenants to run. Techniques described in other papers, such as Dominant-Resource Fairness and BWFQ, require neither per-invocation resource profiling nor multi-dimensional share accounting, making them easy to integrate with existing Lambda-style dispatchers. To evaluate our algorithm, we built a prototype using AWS Lambda and observed that BWFQ reduces the P99 latency gap between interactive and batch tenants from 8.5s to 2.1s; a 4.0X improvement, while preserving 94% of the throughput achieved by First-Come-First-Serve. The algorithm adds only 35 µs of scheduling overhead per decision and fits in approximately 150 lines of Go code. These results demonstrate that token-bucket fair queueing provides a practical, immediately deployable solution for production serverless inference. © 2025, Penerbit UTHM. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2012.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
