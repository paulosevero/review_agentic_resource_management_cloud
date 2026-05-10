---
id: paper-0589
title: A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling
authors:
- Fodor, Balazs
- Jakub, Akos
- Szucs, Gabor
- Sonkoly, Balazs
venue: 2023 IEEE Virtual Conference on Communications, VCC 2023
venue_type: conference
year: 2023
doi: 10.1109/VCC60689.2023.10474695
url: https://www.scopus.com/pages/publications/85190237053?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 139--144
keywords:
- auto-scaling
- cloud computing
- microservice scaling
- multi-agent reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0589 — A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient cloud-based microservice scaling needs to take into account the inter-dependencies between application components to avoid bottlenecks and to swiftly adapt to dynamically changing environments or user demands. Most of today's solutions are not adaptive enough especially to handle large-scale microservices. In this paper, we propose a novel solution leveraging Multi-Agent Deep Reinforcement Learning (MADRL). First, we define our model for horizontal scaling of microservices and formalize the problem. Second, we propose an algorithm based on Multi-Agent Deep Deterministic Policy Gradient (MADDPG) to solve it. Third, a dedicated simulation environment is presented, where arbitrary microservices can be created for testing purposes, and we carry out a comprehensive evaluation. We analyze the performance of the model for microservices of different sizes, investigating its ability to optimize scaling while considering efficient resource utilization and application stability. Results show that our MADDPG-based RL algorithm outperforms the industry standard approach provided by Kubernetes' HPA by at least 14% in terms of resource usage cost.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0589.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
