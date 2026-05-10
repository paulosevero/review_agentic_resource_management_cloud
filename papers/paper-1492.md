---
id: paper-1492
title: Multi-Agent-Based Service Composition Using Integrated Particle-Ant Algorithm in the Cloud
authors:
- Cho, Seongsoo
- Lee, Yeonwoo
- Choi, Hanyong
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/app15179603
url: https://www.scopus.com/pages/publications/105015366871?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- cloud service composition
- Integrated Particle-Ant Algorithm
- metaheuristic algorithms
- Multi-Agent System
- Quality of Service Optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1492 — Multi-Agent-Based Service Composition Using Integrated Particle-Ant Algorithm in the Cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing complexity and scale of service-oriented architectures in cloud computing have heightened the demand for intelligent, decentralized, and adaptive service composition techniques. This study proposes an advanced framework that integrates a Multi-Agent System (MAS) with a novel hybrid metaheuristic optimization method, the Integrated Particle-Ant Algorithm (IPAA), to achieve efficient, scalable, and Quality of Service (QoS)-aware service composition. The IPAA dynamically combines the global search capabilities of Particle Swarm Optimization (PSO) with the local exploitation strength of Ant Colony Optimization (ACO), thereby enhancing convergence speed and solution quality. The proposed system is structured into three logical layers—agent, optimization, and infrastructure—facilitating autonomous decision-making, distributed coordination, and runtime adaptability. Extensive simulations using a synthetic cloud service dataset demonstrate that the proposed approach significantly outperforms traditional optimization methods, including standalone PSO, ACO, and random composition strategies, across key metrics such as utility score, execution time, and scalability. Moreover, the framework enables real-time monitoring and automatic re-optimization in response to QoS degradation or Service-Level Agreement (SLA) violations. Through decentralized negotiation and minimal communication overhead, agents exhibit high resilience and flexibility under dynamic service availability. These results collectively suggest that the proposed IPAA-based framework provides a robust, intelligent, and scalable solution for service composition in complex cloud computing environments. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1492.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
