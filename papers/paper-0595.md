---
id: paper-0595
title: 'DiviML: A Module-based Heuristic for Mapping Neural Networks onto Heterogeneous Platforms'
authors:
- Ghannane, Yassine
- Abdelfattah, Mohamed S.
venue: IEEE/ACM International Conference on Computer-Aided Design, Digest of Technical Papers, ICCAD
venue_type: conference
year: 2023
doi: 10.1109/ICCAD57390.2023.10323712
url: https://www.scopus.com/pages/publications/85181398739?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computer hardware
- Integer programming
- Mapping
- Program processors
- Video signal processing
- Datacenter
- Heterogeneous platforms
- Heterogeneous servers
- Mixed integer linear
- Module-based
- Networking video
- Neural-networks
- Solution quality
- Specialized hardware
- Video processing
- Deep neural networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: NN
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

# paper-0595 — DiviML: A Module-based Heuristic for Mapping Neural Networks onto Heterogeneous Platforms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Datacenters are increasingly becoming heterogeneous, and are starting to include specialized hardware for networking, video processing, and especially deep learning. To leverage the heterogeneous compute capability of modern datacenters, we develop an approach for compiler-level partitioning of deep neural networks (DNNs) onto multiple interconnected hardware devices. We present a general framework for heterogeneous DNN compilation, offering automatic partitioning and device mapping. Our scheduler integrates both an exact solver, through a mixed integer linear programming (MILP) formulation, and a modularity-based heuristic for scalability. Furthermore, we propose a theoretical lower bound formula for the optimal solution, which enables the assessment of the heuristic solutions' quality. We evaluate our scheduler in optimizing both conventional DNNs and randomly-wired neural networks, subject to latency and throughput constraints, on a heterogeneous system comprised of a CPU and two distinct GPUs. Compared to naively running DNNs on the fastest GPU, the proposed framework can achieve more than 3× lower latency and up to 2.9× higher throughput by automatically leveraging both data and model parallelism to deploy DNNs on our sample heterogeneous server node. Moreover, our modularity-based 'splitting' heuristic improves the solution runtime up to 395× without noticeably sacrificing solution quality compared to an exact MILP solution, and outperforms all other heuristics by 30-60% solution quality. Finally, our case study shows how we can extend our framework to schedule large language models across multiple heterogeneous servers by exploiting symmetry in the hardware setup. Our code can be easily plugged in to existing frameworks, and is available at https://github.com/abdelfattah-lab/diviml.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "NN"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0595.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
