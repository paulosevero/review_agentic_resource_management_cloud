---
id: paper-2514
title: Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA
authors:
- Babu, Anju
- Josemin Bala, G.
venue: Frontiers in Computer Science
venue_type: journal
year: 2026
doi: 10.3389/fcomp.2026.1739223
url: https://www.scopus.com/pages/publications/105031123085?origin=resultslist
publisher: Frontiers Media SA
pages: ''
keywords:
- Bidirectional Successive Halving and Attention Gated Recurrent Unit (BiSHAGRU)
- Exponentially Half-life Weighted Moving Average (EHWMA)
- fog computing
- healthcare platforms
- latency
- Recurrent Tuned Kernel Density Estimation (RTKDE)
- Secretary Halton Sequenced Bird Optimization Algorithm (SHSBOA)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2514 — Dynamic request-aware fog-node deployment for latency reduction using RTKDE and EHWMA

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing integrated with healthcare Internet of Things (IoT) systems enables low-latency processing for time-critical medical applications. However, dynamic request variations, limited fog resources, and node failures can significantly increase latency and reduce system reliability. This paper proposes a dynamic request-aware fog-node deployment framework to mitigate latency in healthcare fog-computing platforms. Recurrent Tuned Kernel Density Estimation (RTKDE) is used to detect dynamic request changes, and Exponentially Half-life Weighted Moving Average (EHWMA) assesses request growth trends. Based on the estimated workload, fog nodes are adaptively scaled and optimally deployed using the Secretary Halton Sequenced Bird Optimization Algorithm (SHSBOA). System reliability is enhanced through faulty fog-node detection using a Bidirectional Successive Halving and Attention Gated Recurrent Unit (BiSHAGRU) model, while redundant fog-to-cloud transmissions are reduced using a Multi-Agent Weighted Reward Reinforcement Learning (MAWRRL) approach. Simulation results using iFogSim demonstrate the effectiveness of the proposed framework. RTKDE achieves a Mean Integrated Square Error (MISE) of 0.042, EHWMA attains a Mean Square Error (MSE) of 0.006, and SHSBOA records a latency of 3,122 ms for 100 requests. BiSHAGRU achieves 99.23% fault detection accuracy, and MAWRRL attains a 93.02% success rate in redundant data handling, confirming improved latency reduction and reliability. Copyright © 2026 Babu and Josemin Bala.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2514.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
