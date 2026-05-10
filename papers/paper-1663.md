---
id: paper-1663
title: 'QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems'
authors:
- Hu, Miao
- He, Qi
- Wu, Di
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2025
doi: 10.1109/INFOCOM55648.2025.11044591
url: https://www.scopus.com/pages/publications/105011046553?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- heterogeneous edge servers
- LLM
- partially in-formed
- Quantization
- scheduling
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

# paper-1663 — QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The quantization technologies have enabled the practical deployment of large language models (LLMs) at the edge, however, current edge scheduling and quantization selection are separately designed. Furthermore, partially informed edge processing performance further exacerbates these challenges. To address these issues, we introduce QLLMS, a joint quantization-adaptive scheduling scheme for large language models tailored to partially informed edge serving systems. The primary objective of our approach is to reduce GPU rental costs by strategically orchestrating both quantization options and heterogeneous resources. The QLLMS algorithm first determines the available quantization set (AQS) to optimize the LLM inference performance within limited edge resources. To address the unpredictable nature of edge computing performance, we present a low-rank property-driven recovery approach, which can reconstruct complete AQS matrices using only partial samples. Subsequently, we devise a novel many-to-one matching algorithm that aims to strike a balance between efficient utilization of edge resources and optimal model inference performance, factoring in the available quantization options. We prove that QLLMS yields a stable matching without blocking pairs that could lead to inefficiencies. Experiment results show that QLLMS achieves a reduction of up to 22.36% in rental costs compared to state-of-the-art baselines in partially informed edge serving systems while simultaneously improving the task completion rate on edge servers.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1663.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
