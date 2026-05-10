---
id: paper-2282
title: 'WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving'
authors:
- Wang, Tianyu
- Rattihalli, Gourav
- Dhakal, Aditya
- Tang, Xulong
- Milojicic, Dejan
venue: Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops
venue_type: conference
year: 2025
doi: 10.1145/3731599.3767396
url: https://www.scopus.com/pages/publications/105023404126?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 508--515
keywords:
- energy efficiency
- LLM serving
- serverless
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

# paper-2282 — WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless LLM serving reduces operational costs by elastically provisioning GPUs and charging users only for actual usage. However, existing systems mainly optimize cold-start latency while overlooking two inefficiencies: (i) static, exclusive GPU allocation that over-provisions compute resources, lowering utilization and inflating hardware costs, and (ii) reliance on hardware-controlled clock frequencies, wasting energy. Our measurements show that many LLM workloads can meet SLOs with partial SM allocations and reduced clock speeds, enabling opportunities for GPU multiplexing and dynamic clock scaling to reduce energy consumption. We propose WAGES, a workload-aware GPU-sharing system for energy-efficient serverless LLM serving. WAGES uses NVIDIA MPS to co-locate multiple LLMs on a single GPU, dynamically tuning SM partitions and clock speeds to match workload demands while preserving SLOs. A two-tier scheduling framework coordinates global GPU consolidation and local SLO-aware scheduling with on-the-fly tuning. It also overlaps model/KV migration with execution to reduce reconfiguration overheads. On real-world LLM traces, WAGES improves SLO attainment by up to 4% over state-of-the-art GPU sharing while cutting energy use by up to 26%, showing that fine-grained, workload-aware sharing can improve SLO attainment and reduce energy consumption simultaneously. © 2025 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2282.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
