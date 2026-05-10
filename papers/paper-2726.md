---
id: paper-2726
title: Transformer-Based Resource and Stage-Aware Scheduling for Model-Parallel LLM Inference
authors:
- Naeem, Rami
- Buyantogtokh, Tengis
- Rizk, Hamada
- Amano, Tatsuya
- Yamaguchi, Hirozumi
venue: ICDCN 2026 - Companion Proceedings of the International Conference on Distributed Computing and Networking 2026
venue_type: conference
year: 2026
doi: 10.1145/3737611.3776613
url: https://www.scopus.com/pages/publications/105029245060?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 72--77
keywords:
- Communication overhead
- Continuous batching
- Distributed LLM inference
- Imitation learning
- Pipeline parallelism
- Scheduling
- Tensor parallelism
- Transformer scheduler
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2726 — Transformer-Based Resource and Stage-Aware Scheduling for Model-Parallel LLM Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Current large language model (LLM) serving systems face three key limitations in distributed scheduling. First, most parallelization strategies are not stage-aware: they treat prefill and decode as uniform workloads despite their distinct compute and communication profiles. Second, many assume homogeneous hardware and ignore resource diversity in memory and bandwidth across nodes. Third, they overlook network congestion, as they are primarily designed for data-center environments with abundant interconnect bandwidth. We address these gaps with a resource- and stage-aware scheduler that models heterogeneous GPU clusters, communication costs, and per-stage characteristics. We compare three approaches: a heuristic stage-based policy, a continuous-batching (vLLM-style) baseline, and a transformer-based scheduler trained by imitation to replicate and improve the heuristic. Our evaluation spans eight representative scenarios covering large models that exceed a single GPU, prefill-dominant and mixed workloads, heterogeneous and bandwidth-limited clusters, strict SLO constraints, and multi-tenant or elastic deployments. The learned scheduler reduces latency by up to 50% under bandwidth-constrained or heterogeneous conditions while maintaining throughput within 20-30% of vLLM. It further improves latency by 3-17% over its heuristic teacher while preserving 100% feasibility. Continuous batching remains superior on high-bandwidth fabrics. These results identify bandwidth as a first-order determinant of optimal scheduling and demonstrate that learned schedulers can unify heuristic feasibility with adaptive, resource-aware optimization.  © 2026 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2726.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
