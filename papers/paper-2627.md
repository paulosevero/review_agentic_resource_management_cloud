---
id: paper-2627
title: 'Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads'
authors:
- Kaarat, Arjun
- Reddy Batthula, Venkata Jaipal
- Segall, Richard
venue: Proceedings - 5th International Conference on Informatics and Software Engineering, IISEC 2026
venue_type: conference
year: 2026
doi: 10.1109/IISEC69317.2026.11418430
url: https://www.scopus.com/pages/publications/105036000174?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 555--560
keywords:
- Cosine Similarity
- Generative AI
- Geometric Scheduling
- GPU Clusters
- Kubernetes
- Resource Fragmentation
- Vector Bin Packing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2627 — Fitting the Void: Residual-Aware Geometric Packing for GenAI Workloads

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Generative AI workloads demand heterogeneous resources (GPUs, CPU cores, and high-bandwidth memory) in highly variable combinations. Current cluster schedulers, including Kubernetes, largely treat placement as scalar capacity packing (e.g., average utilization), which can mask infeasible nodes-servers may appear partially utilized while having no free GPUs, leaving CPUs or memory stranded. We propose Residual-Aware Geometric Packing (RAGP), a scheduling approach that matches each workload to a node's residual multi-resource capacity. RAGP represents workload demand and server residual capacity as multi-dimensional vectors and uses cosine similarity to quantify alignment between a workload's resource profile and a node's remaining capacity.This geometric matching preferentially places CPU-intensive workloads on CPU-rich nodes, memory-intensive workloads on memory-rich nodes, and complementary workloads together, reducing fragmentation and improving effective utilization. To address bursty inference behavior, RAGP incorporates a predictive buffer: it forecasts short-horizon resource demand (including memory growth with longer conversations) and reserves headroom proactively rather than relying on instantaneous measurements. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2627.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
