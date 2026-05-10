---
id: paper-2646
title: 'MAG-Q: Multi-agent Actor-Critic based GRL with Quantum inspired Forwarding for Enhanced Task Offloading in Clustered Fog Computing environment'
authors:
- Kumar Verma, Nilesh
- Naik, K. Jairam
venue: Expert Systems with Applications
venue_type: journal
year: 2026
doi: 10.1016/j.eswa.2026.132044
url: https://www.scopus.com/pages/publications/105034619588?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Fog computing
- Graph attention network
- Multi-agent actor-critic
- Quantum-inspired optimization
- Task offloading
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

# paper-2646 — MAG-Q: Multi-agent Actor-Critic based GRL with Quantum inspired Forwarding for Enhanced Task Offloading in Clustered Fog Computing environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The exponential growth of latency-sensitive applications and the proliferation of Internet of Things (IoT) devices have intensified the need for efficient task offloading in the edge-fog-cloud continuum. Responding to this evolving landscape, the current study introduces MAG-Q, a hybrid task-offloading framework for clustered fog computing environment, that integrates Graph Attention Network (GAT) encoded Multi-Agent Actor-Critic model (MAAC) for intra-cluster placement with a Quantum-Inspired Forwarding (QIF) method for inter-cluster routing. MAG-Q employs Graph Attention to model heterogeneous nodes and links along with a reward that optimizing latency and energy efficiency while ensuring scalability in multi-agent environments, in comparison to previous MARL techniques that employ uniform graph encoders or single-policy control to improve decision-making. To achieve cross-cluster robust task forwarding and optimal load balancing, the QIF module utilizes quantum-inspired annealing strategies by formulating the problem as Quadratic Unconstrained Binary Optimization (QUBO) and mapping it to an Ising model; we demonstrate that this objective is NP-hard and illustrate that the hybrid design scales with the number of clusters. Extensive experimental evaluations demonstrate that MAG-Q significantly reduces task completion latency up to 35%, enhances energy efficiency up to 25%, and improves offloading gain up to 32% compared to state-of-the-art approaches. The results emphasize the scalability and adaptability of the proposed framework, making it a feasible solution for next-generation fog computing applications in dynamic and resource-constrained environments. © 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2646.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
