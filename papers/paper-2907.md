---
id: paper-2907
title: 'Digital Twin-Enabled Vehicular Edge Computing in Satellite-Terrestrial Network: A Combined DRL and Optimization Approach'
authors:
- Zhang, Hongxia
- Xi, Shiyu
- Cao, Luyao
- Wang, Wenjie
- Zhang, Peiying
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2026.3670437
url: https://www.scopus.com/pages/publications/105032784638?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- digital twin
- satellite-terrestrial network
- Vehicle network
- vehicular edge computing
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
    my_justification: RL
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

# paper-2907 — Digital Twin-Enabled Vehicular Edge Computing in Satellite-Terrestrial Network: A Combined DRL and Optimization Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of generative AI technologies, vehicle intelligence devices (VIDs) are being deployed on a large scale. However, VIDs are typically computationally intensive and require frequent interactions. The limited energy and computational resources of vehicles restrict the performance of VIDs, making it challenging to meet users' demands. In this paper, we propose a vehicle edge computing system supported by a digital twin and a satellite-terrestrial network, where low earth orbit (LEO) satellites and roadside units (RSUs) provide computational services for VIDs. First, we formulate an optimization objective to minimize system costs, defined as the weighted sum of energy consumption and latency. Then, given the problem's non-convex nature and the interactions among multiple variables, we decompose it into two phases. In the first phase, we develop a multi-agent deep reinforcement learning- based algorithm to optimize offloading decisions, association variables, task ratios, and computational resource allocation and reduce system cost. In the second phase, we focus on the convex bandwidth assignment subproblem. We apply the convex optimization to derive closed-form solutions for the bandwidth assignments of LEO satellites and RSUs, which simplifies the solution process. Finally, the simulation results verify that our proposed scheme achieves an average system cost saving of 32.7% compared to benchmark schemes. © 1967-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2907.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
