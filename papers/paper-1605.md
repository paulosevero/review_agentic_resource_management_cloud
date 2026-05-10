---
id: paper-1605
title: Multi-Node Inference Architectures for Low-Latency LLM Serving
authors:
- Gundla, Naresh Kumar
- Atthuluri, Sri Harsha
venue: International Conference on Advanced Computing Technologies, ICoACT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICoACT63339.2025.11004706
url: https://www.scopus.com/pages/publications/105010172638?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Distributed Computing
- Large Language Models
- Low-Latency
- Multi-Node Inference
- Real-World Datasets
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

# paper-1605 — Multi-Node Inference Architectures for Low-Latency LLM Serving

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Over the past few years, large language models have evolved to enable a wide range of applications-from natural language understanding to real-time conversational agents. However, the deployment of LLMs into production presents many significant challenges, especially with regard to low-latency responses that enable real-time interactions. This work investigates multi-node inference architectures for optimized deployment using open-source frameworks with scalability, flexibility, and cost-effectiveness. We investigate various methods, such as microbatching, tensor and pipeline parallelism, and sophisticated load balancing, that effectively distribute inference workloads across multiple nodes. We conduct extensive evaluations using popular open-source tools such as Kubernetes, Ray, and Envoy to benchmark the performance of these architectures in terms of latency, throughput, and resource utilization under diverse workloads. We also analyze model replication versus model partitioning trade-offs, giving insights into the most appropriate configuration for various deployment scenarios. As our results show, a well-orchestrated multi-node setup can be used to greatly reduce inference latency while preserving high throughputs, enabling the deployment of sophisticated LLMs in latencysensitive applications. This paper gives insights with a detailed analysis of multi-node inference strategies and integration into open-source ecosystems, therefore it will be a great guide for practitioners seeking to develop deployments of LLMs at scale. In summary, this work underlines how distributed architectures can overcome some of the inherent limitations imposed by singlenode deployments and are crucial for achieving more efficient and responsive AI-driven services.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1605.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
