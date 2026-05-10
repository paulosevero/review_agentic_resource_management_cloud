---
id: paper-1836
title: 'GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks'
authors:
- Liang, Ruihuai
- Yang, Bo
- Chen, Pengyu
- Cao, Xuelin
- Yu, Zhiwen
- Debbah, Merouane
- Niyato, Dusit
- Poor, H. Vincent
- Yuen, Chau
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3568248
url: https://www.scopus.com/pages/publications/105005424986?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10264--10277
keywords:
- computation offloading
- generative AI
- graph diffusion
- Multi-access edge computing
- network optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1836 — GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Optimization is crucial for the efficiency and reliability of multi-access edge computing (MEC) networks. Many optimization problems in this field are NP-hard and do not have effective approximation algorithms. Consequently, there is often a lack of optimal (ground-truth) data, which limits the effectiveness of traditional deep learning approaches. Most existing learning-based methods require a large amount of optimal data and do not leverage the potential advantages of using suboptimal data, which can be obtained more efficiently. To illustrate this point, we focus on the multi-server multi-user computation offloading (MSCO) problem, a common issue in MEC networks that lacks efficient optimal solution methods. In this paper, we introduce the graph diffusion-based solution generator (GDSG), designed to work with suboptimal datasets while still achieving convergence to the optimal solution with high probability. We reformulate the network optimization challenge as a distribution-learning problem and provide a clear explanation of how to learn from suboptimal training datasets. We develop GDSG, a multi-task diffusion generative model that employs a graph neural network (GNN) to capture the distribution of high-quality solutions. Our approach includes a straightforward and efficient heuristic method to generate a sufficient amount of training data composed entirely of suboptimal solutions. In our implementation, we enhance the GNN architecture to achieve better generalization. Moreover, the proposed GDSG can achieve nearly 100% task orthogonality, which helps prevent negative interference between the discrete and continuous solution generation training objectives. We demonstrate that this orthogonality arises from the diffusion-related training loss in GDSG, rather than from the GNN architecture itself. Finally, our experiments show that the proposed GDSG outperforms other benchmark methods on both optimal and suboptimal training datasets. Regarding the minimization of computation offloading costs, GDSG achieves savings of up to 56.62% on the ground-truth training set and 41.06% on the suboptimal training set compared to existing discriminative methods. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1836.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
