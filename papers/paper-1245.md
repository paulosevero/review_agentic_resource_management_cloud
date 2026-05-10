---
id: paper-1245
title: Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning
authors:
- Wang, Yi-Xiao
- Tao, Wen-Jian
- Zhao, Shao-Peng
- Zhang, Yan-Ping
venue: Computer-Aided Design and Applications
venue_type: journal
year: 2024
doi: 10.14733/cadaps.2024.S9.265-276
url: https://www.scopus.com/pages/publications/85173561138?origin=resultslist
publisher: CAD Solutions, LLC
pages: 265--276
keywords:
- Computer-Aided Medical Systems
- Loading Balance
- MADDPG
- Multi-Agent Reinforcement Learning
- Service Mesh
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1245 — Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The service mesh is the most well-known framework for developing network applications because it separates governance and business logic in microservices and achieves unified governance of heterogeneous systems. The Service Mesh has a more complicated topology structure than the typical microservice design, which makes it harder to keep the load balance. The present Service Mesh load balancing technique is rather straightforward, merely taking into account the current load status of each individual node and disregarding the mutual load impact across nodes. This paper proposes a load balancing method based on multi-agent reinforcement learning to address the aforementioned issues. This method turns the Service Mesh load balancing problem into a random game process, builds an Actor-Critic network to simulate the service mesh multi-resource scheduling strategy, and uses the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm to determine the best multi-resource scheduling strategy. The Istio framework is utilized in this study to create a service mesh environment, and the test results demonstrate that the suggested approach can produce faster response times. © 2024, CAD Solutions, LLC. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1245.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
