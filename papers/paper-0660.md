---
id: paper-0660
title: 'SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization'
authors:
- Liu, Pengtao
- An, Kang
- Lei, Jing
- Liu, Wei
- Sun, Yifu
- Zheng, Gan
- Chatzinotas, Symeon
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2023.3242422
url: https://www.scopus.com/pages/publications/85148425842?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7987--8003
keywords:
- binary offloading
- Internet of things
- multi-access edge computing (MEC)
- partial offloading
- resource management
- sparse code multiple access (SCMA)
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

# paper-0660 — SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) is regarded as a promising approach for providing resource-constrained mobile devices with computing resources through task offloading. Sparse code multiple access (SCMA) is a code-domain non-orthogonal multiple access (NOMA) scheme that can meet the demands of multi-cell MEC networks for high data transmission rates and massive connections. In this paper, we propose an optimization framework for SCMA-enabled multi-cell MEC networks. The joint resource allocation and computation offloading problem is formulated to minimize the system cost, which is defined as the weighted energy cost and latency. Due to the nonconvexity of the proposed optimization problem induced by the coupled optimization variables, we first propose an algorithm based on the block coordinate descent (BCD) method to iteratively optimize the transmit power and edge computing resources allocation by deriving closed-form solutions, and further develop an improved low-complexity simulated annealing (SA) algorithm to solve the computation offloading and multi-cell SCMA codebook allocation problem. To solve the problem of partial state observation and timely decision-making in long-term optimization environment, we put forward a multiagent deep deterministic policy gradient (MADDPG) algorithm with centralized training and distributed execution. Furthermore, we extend the framework to the partial offloading case and propose an algorithm based on alternating convex search for solving the task offloading ratio. Numerical results show that the proposed multi-cell SCMA-MEC scheme achieves lower energy consumption and system latency in comparison to the orthogonal frequency division multiple access (OFDMA) and power-domain (PD) NOMA techniques.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0660.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
