---
id: paper-1754
title: 'Multi-Agent Multi-Objective Reinforcement Learning for Intelligent Cloud Migration Planning: A Comprehensive Framework with Explainable Decision Support'
authors:
- Kuppala, Nandini
- Monish, G.V.
- Nivedha, V.
- Pinnenti, Balu
venue: 2025 17th IEEE International Conference on Computational Intelligence and Communication Networks, CICN 2025
venue_type: conference
year: 2025
doi: 10.1109/CICN67655.2025.11368234
url: https://www.scopus.com/pages/publications/105034686299?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 567--573
keywords:
- Cloud computing
- Explainable artificial intelligence
- Migration planning
- Multi-agent systems
- Multi-objective optimization
- Reinforcement learning
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
    my_justification: RL
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

# paper-1754 — Multi-Agent Multi-Objective Reinforcement Learning for Intelligent Cloud Migration Planning: A Comprehensive Framework with Explainable Decision Support

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud migration planning requires simultaneous optimization of multiple conflicting objectives such as cost, performance, risk, and compliance under constraints of complex system interdependencies. Conventional methodologies are based on static heuristics and manual intervention which fail to adapt to dynamic enterprise environments. This paper introduces a Multi-Agent Multi-Objective Reinforcement Learning (MAMORL) framework using three specialized agents: Migration Sequencer for dependency-aware system ordering, Resource Optimizer for cost-performance trade-offs, and Risk Manager for compliance and downtime mitigation. Each agent utilizes multi-objective neural networks with separate value heads for conflicting objectives, coordinating with shared environment interactions. The framework was tested with enterprise migration scenarios modeling 50 systems of various criticality levels and 1000 migration cases following organizational complexity patterns. Experimental results show substantial improvements compared to baseline methods: 85-95% completion rates, 1525 % cost optimization, and 20-30% risk reduction. The system incorporates explainable AI components using surrogate models and feature importance analysis to provide transparent decision rationale. Multi-objective learning successfully balances competing priorities while maintaining interpretable policies through weighted scalarization techniques. The framework addresses critical gaps in automated migration planning by combining agent specialization, multi-objective optimization, and decision transparency in an enterprise-grade system. Outcomes demonstrate effective coordination across specialized agents while discovering Pareto-optimal solutions across objective trade-offs, contributing to AI-driven infrastructure management with practical enterprise applicability. © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1754.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
