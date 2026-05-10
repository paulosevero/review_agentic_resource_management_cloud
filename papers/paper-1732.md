---
id: paper-1732
title: 'Swarm Intelligence for Edge Microservices: Bio-Inspired Algorithms for Dynamic Service Distribution'
authors:
- Khanna, Abhirup
- Negi, Dakshita
- Sah, Anushree
- Rawat, Saurabh
- Maheshwari, Piyush
venue: 2025 International Conference on Computational Intelligence and Knowledge Economy, ICCIKE 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCIKE67021.2025.11318214
url: https://www.scopus.com/pages/publications/105032702815?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 536--541
keywords:
- Bio-inspired Algorithms
- Edge Computing
- Microservice Placement
- Multi-objective Optimization
- Swarm Intelligence
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1732 — Swarm Intelligence for Edge Microservices: Bio-Inspired Algorithms for Dynamic Service Distribution

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The paper presents an edge computing framework of dynamic microservice location using swarm intelligence that focuses on addressing interdependent challenges facing resource heterogeneity, latency sensitivity, network variability, and fault tolerance. Unlike classic centralized or non-adaptive strategies that use only one general purpose scheme, the proposed one incorporates four specially designed algorithms: a multi-objective placement model that balances cost, energy and latency; a decentralized Swarm Utility Convergence (SUC) implementation that provides malleable agent coordination; a Stochastic Service Availability (SSA) amelioration that assures reliability through optimum replica placement, and a hybrid bio inspired metaheuristic method that combines an ant colony optimization and a particle swarm optimization technique. All of these models combined enable the real-time adaptivity, resilience to node failures and optimal use of resources. The simulation outcomes under different weighting schemes, environmental dynamics and node densities exhibit in general considerably quicker convergence, would be the agent utility, the location efficiency, and available services than benchmarks. The main findings are that optimization benchmarks can be reached faster when energy efficient is chosen as the priority, dynamic optimization strategies perform better than others under scalability diversion, and service availability becomes a plateau at some replication level. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1732.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
