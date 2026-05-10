---
id: paper-2590
title: Carbon-Aware Spatial-Temporal Scheduling for Multiple AI Data Center Parks with Training and Inference Workloads Characteristics
authors:
- Han, Jianpei
- Du, Ershun
- Du, Bojun
- Li, Yaowang
- Zhang, Ning
- Kang, Chongqing
venue: IEEE Transactions on Industry Applications
venue_type: journal
year: 2026
doi: 10.1109/TIA.2026.3678569
url: https://www.scopus.com/pages/publications/105034643717?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AIDC park
- continuity-constraints
- inference workloads
- optimal scheduling
- spatial-temporal flexibility
- training workloads
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2590 — Carbon-Aware Spatial-Temporal Scheduling for Multiple AI Data Center Parks with Training and Inference Workloads Characteristics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The explosion of large models and generative artificial intelligence (AI) applications has led to the rapid development of AI data center (AIDC), raising significant concerns over their energy consumption and carbon emissions. Furthermore, AIDC's workload, divergent in its training and inference phases, introduces novel challenges that are not adequately addressed by conventional optimization techniques. In this regard, this study focuses on multiple geographically distributed AIDC parks, and a carbon-aware spatial-temporal scheduling strategy is proposed with detailed training and inference workloads characteristics. Firstly, the system architecture and the carbon-aware scheduling framework of multiple AIDC parks are presented. Secondly, the power consumption and carbon emission models of the AIDC park are established, which incorporate the differentiated characteristics of training and inference workloads. Subsequently, the continuity-constrained workload migration mechanism is developed, and the spatial-temporal flexibility models of the AIDC park are established. Then, the carbon-aware spatial-temporal scheduling strategy with chance constraints is formulated via the multi-objective optimization framework, wherein the -constraint method and Big-M linearization technique are synergistically integrated for model transformation and dimensionality reduction solution. Finally, the case study based on a simplified urban computing power network with three AIDC parks is conducted. Numerical results demonstrate that the proposed strategy reduces operating costs by at least 1.69% and carbon emissions by 4.5% compared with four alternative schemes, while maintaining computational tractability. © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2590.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
