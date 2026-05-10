---
id: paper-2357
title: Resource Allocation for Cooperative Sensing in Fog Computing-Based Vehicular Networks
authors:
- Yan, Shi
- Zhang, Shenhu
- Sun, Zengzhong
- Sun, Yaohua
- Peng, Mugen
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3578321
url: https://www.scopus.com/pages/publications/105008042896?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17445--17460
keywords:
- Cooperative sensing and computing
- fog computing-based vehicular networks
- multi-agent deep reinforcement learning
- resource allocation
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

# paper-2357 — Resource Allocation for Cooperative Sensing in Fog Computing-Based Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cooperative sensing leverages the collaborative exchange of sensing and driving data among vehicles to broaden the sensing range and refine accuracy for autonomous vehicles. However, the substantial surge in shared data has engendered a significant demand for wireless spectrum in vehicular networks (VNETs), rendering the execution of driving safety tasks within tolerable latency more challenging under resource-constrained circumstances. In this study, a cooperative sensing scheme based on clusters in fog computing-based vehicular networks (VNETs) is proposed. Here, vehicles are grouped into collaborative clusters, selectively exchanging sensing messages to enable cooperative computing. To balance communication, sensing, and computing performance in cooperative sensing, a joint problem for vehicle clustering formulation, sensing message selection, radio, and computing resource allocation is established. This problem is subsequently decomposed into two sub-problems due to their non-convex nature. The vehicle clustering formulation alongside sensing message selection sub-problems are redefined into a multi-agent Markov game, addressed via an attention-enhanced multi-agent deep reinforcement learning algorithm. Additionally, the swap matching and interior-point methods are adapted for iterative optimization of sensing, communication, and computing performances. Comprehensive simulation results have validated the superiority of the proposed scheme over existing models across diverse performance metrics. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2357.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
