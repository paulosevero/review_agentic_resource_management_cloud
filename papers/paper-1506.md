---
id: paper-1506
title: Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs
authors:
- Darzi, Erfan
- Balija, Sree Bhargavi
- Demir, Buse
venue: WoSC11 2025 - Proceedings of the 11th International Workshop on Serverless Computing, Part of Middleware Conference
venue_type: conference
year: 2025
doi: 10.1145/3774899.3775014
url: https://www.scopus.com/pages/publications/105029344902?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 20--25
keywords:
- elastic resource allocation
- GPU multi-tenancy
- LLM inference
- pay-as-you-go GPUs
- serverless computing
- SLO compliance
- TTFT
- vLLM
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1506 — Elastic MIG Reconfiguration with PCIe-Aware Placement for Multi-Tenant GPUs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-tenant LLM inference platforms face unpredictable tail latency from noisy-neighbor interference, violating service-level objectives (SLOs) critical for serverless and elastic cloud workloads. We present a VM-deployable controller that enables fine-grained, dynamic resource allocation by combining Multi-Instance GPU (MIG) reconfiguration, PCIe-aware placement, and lightweight isolation guardrails. The controller samples per-tenant tail latency (including time-to-first-token for autoregressive serving), correlates system signals to detect interference, and adaptively adjusts isolation using host-only controls deployable in cloud environments without fabric privileges. Evaluated on vLLM serving OLMo 2 7B Instruct across a 16-GPU cluster, our approach reduces SLO miss-rate by ≈32% and improves TTFT p99 by ≈10-15% with ≤5% throughput cost, demonstrating practical elastic GPU allocation for serverless LLM inference.  © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1506.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
