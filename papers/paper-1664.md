---
id: paper-1664
title: Redis-Based High-Concurrency Optimization for a Shooting Results System
authors:
- Hu, Linwei
- Cheng, Meng
- Sun, Weixing
- Fu, Lijun
venue: Proceedings of the IEEE International Conference on Computer and Communications, ICCC
venue_type: conference
year: 2025
doi: 10.1109/ICCC68654.2025.11437585
url: https://www.scopus.com/pages/publications/105035765591?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 348--352
keywords:
- distributed cache
- high concurrency
- hotspot detection
- load balancing
- Redis
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

# paper-1664 — Redis-Based High-Concurrency Optimization for a Shooting Results System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Shooting-event management platforms experience bursty, extremely skewed read traffic during moments such as results release or registration deadlines. Conventional Redis clusters struggle to balance hotspot-slot overload against resource waste. This paper proposes an intelligent cache optimization tailored to periodic high-concurrency scenarios: (1) Hot-cold data identification and prediction via time-series features and a lightweight large language model (LLM) with a federated inference scheme, enabling millisecond-level hotspot-key prediction and prewarming; (2) Access-aware elastic scaling by combining a dynamic hotspot-replica scheduler with a Kubernetes-based Redis Cluster HPA to automatically adjust node scale and topology under load. On a representative shooting dataset, the approach increases peak throughput from 30k to 86k QPS, reduces hotspotread P99 latency by 62%, and saves 43% cache resources during off-peak periods. The study offers an elastic-cache path that jointly optimizes availability and resource efficiency for periodic hotspot workloads. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1664.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
