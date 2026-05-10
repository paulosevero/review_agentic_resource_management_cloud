---
id: paper-1690
title: 'FlowTracer: A Tool for Uncovering Network Path Usage Imbalance in AI Training Clusters'
authors:
- Jamil, Hasibul
- Alim, Abdul
- Schares, Laurent
- Maniotis, Pavlos
- Schour, Liran
- Sydney, Ali
- Kayi, Abdullah
- Kosar, Tevfik
- Karacali, Bengi
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11160830
url: https://www.scopus.com/pages/publications/105018463532?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6988--6993
keywords:
- cloud networking
- load balancing
- Network monitoring
- network visibility
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: AI é workload não tomador de decisão
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

# paper-1690 — FlowTracer: A Tool for Uncovering Network Path Usage Imbalance in AI Training Clusters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing complexity of AI workloads, especially distributed Large Language Model (LLM) training, places significant strain on the networking infrastructure of parallel data centers and supercomputing systems. While Equal-Cost Multi-Path (ECMP) routing distributes traffic over parallel paths, hash collisions often lead to imbalanced network resource utilization and performance bottlenecks. This paper presents FlowTracer, a tool designed to analyze network path utilization and evaluate different routing strategies. Unlike tools that introduce additional traffic, FlowTracer aids in debugging network inefficiencies by passively monitoring and correlating user workload flows. As a result, FlowTracer does not interfere with ongoing data transfers, enabling analysis with minimal overhead, which is an important factor when debugging and fine-tuning routing schemes in production systems. FlowTracer can provide detailed insights into traffic distribution and can help identify the root causes of performance degradation, such as hash collisions. With FlowTracer's flow-level insights, system operators can optimize routing, reduce congestion, and improve the performance of distributed AI workloads. We use a RoCEv2-enabled cluster with a leaf-spine network and 16 400-Gbps nodes to demonstrate how FlowTracer can be used to compare the flow imbalances of ECMP routing against a statically configured network. The example showcases a 30% reduction in imbalance, as measured by a new metric we introduce.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "AI é workload não tomador de decisão"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1690.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
