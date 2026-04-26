---
id: "paper-2726"
title: "Transformer-Based Resource and Stage-Aware Scheduling for Model-Parallel LLM Inference"
authors: ["Naeem, Rami", "Buyantogtokh, Tengis", "Rizk, Hamada", "Amano, Tatsuya", "Yamaguchi, Hirozumi"]
year: 2026
venue: "ICDCN 2026 - Companion Proceedings of the International Conference on Distributed Computing and Networking 2026"
venue_type: "conference"
doi: "10.1145/3737611.3776613"
url: "https://www.scopus.com/pages/publications/105029245060?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "72--77"
keywords: ["Communication overhead", "Continuous batching", "Distributed LLM inference", "Imitation learning", "Pipeline parallelism", "Scheduling", "Tensor parallelism", "Transformer scheduler"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2726 — Transformer-Based Resource and Stage-Aware Scheduling for Model-Parallel LLM Inference

## Metadata

- **Authors:** Naeem, Rami and Buyantogtokh, Tengis and Rizk, Hamada and Amano, Tatsuya and Yamaguchi, Hirozumi
- **Year:** 2026
- **Venue:** ICDCN 2026 - Companion Proceedings of the International Conference on Distributed Computing and Networking 2026
- **DOI:** 10.1145/3737611.3776613
- **URL:** https://www.scopus.com/pages/publications/105029245060?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 72--77
- **Language:** English
- **Keywords:** Communication overhead; Continuous batching; Distributed LLM inference; Imitation learning; Pipeline parallelism; Scheduling; Tensor parallelism; Transformer scheduler

### Abstract

Current large language model (LLM) serving systems face three key limitations in distributed scheduling. First, most parallelization strategies are not stage-aware: they treat prefill and decode as uniform workloads despite their distinct compute and communication profiles. Second, many assume homogeneous hardware and ignore resource diversity in memory and bandwidth across nodes. Third, they overlook network congestion, as they are primarily designed for data-center environments with abundant interconnect bandwidth. We address these gaps with a resource- and stage-aware scheduler that models heterogeneous GPU clusters, communication costs, and per-stage characteristics. We compare three approaches: a heuristic stage-based policy, a continuous-batching (vLLM-style) baseline, and a transformer-based scheduler trained by imitation to replicate and improve the heuristic. Our evaluation spans eight representative scenarios covering large models that exceed a single GPU, prefill-dominant and mixed workloads, heterogeneous and bandwidth-limited clusters, strict SLO constraints, and multi-tenant or elastic deployments. The learned scheduler reduces latency by up to 50% under bandwidth-constrained or heterogeneous conditions while maintaining throughput within 20-30% of vLLM. It further improves latency by 3-17% over its heuristic teacher while preserving 100% feasibility. Continuous batching remains superior on high-bandwidth fabrics. These results identify bandwidth as a first-order determinant of optimal scheduling and demonstrate that learned schedulers can unify heuristic feasibility with adaptive, resource-aware optimization.  © 2026 Copyright held by the owner/author(s).

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
