---
id: paper-1367
title: 'Fairness-Aware Personalized Pricing: A Simulation Study of Trade-offs Across Behavioral, Group, and Envy-Based Constraints'
authors:
- Aggarwal, Anmol
venue: ICSEC 2025 -  29th International Computer Science and Engineering Conference 2025
venue_type: conference
year: 2025
doi: 10.1109/ICSEC67360.2025.11298102
url: https://www.scopus.com/pages/publications/105032729082?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 478--483
keywords:
- Agent-Based Simulation
- Algorithmic Fairness
- Behavioral Fairness
- Envy-Freeness
- Fairness Constraints
- Multi-Objective Optimization
- Personalized Pricing
- Price Discrimination
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

# paper-1367 — Fairness-Aware Personalized Pricing: A Simulation Study of Trade-offs Across Behavioral, Group, and Envy-Based Constraints

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As dynamic pricing becomes increasingly personalized through machine learning, concerns about fairness have moved to the forefront of algorithmic pricing design. While traditional fairness definitions in automated decision systems have focused on group parity or individual similarity, pricing introduces domain-specific challenges such as loyalty penalties, behavioral exploitation, and price envy. This paper proposes a unified framework that quantifies and balances four fairness notions in personalized pricing: group fairness, individual consistency, behavioral (loyalty-based) fairness, and envy-freeness. The approach integrates these soft constraints into a multi-objective optimization model that augments the standard revenue maximization objective.We simulate a heterogeneous population of agents with distinct behavioral traits and compare four policies: unconstrained pricing, group fairness-constrained pricing, loyalty fairness, and a combined multi-fair policy. Results show that fairness-Aware pricing substantially reduces loyalty gaps and envy violations while maintaining over 96% of unconstrained revenue. The multi-fair policy achieves the most balanced performance across fairness dimensions, demonstrating that equity and efficiency can be jointly realized in algorithmic pricing systems. The findings provide a theoretical and empirical basis for fairness-Aware pricing with implications for SaaS, marketplaces, and digital services. © 2025 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1367.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
