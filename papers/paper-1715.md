---
id: paper-1715
title: Intelligent Auto-scaling in Cloud Infrastructure Using Machine Learning and Reinforcement Learning
authors:
- Joshi, Vedant
- Patel, Pratham
- Chandwani, Navroop
- Bhatia, Jitendra
- Kumhar, Malaram
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-4536-7_17
url: https://www.scopus.com/pages/publications/105018796282?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 217--239
keywords:
- Auto-scaling
- Cloud computing
- Federated learning
- Machine learning
- Quality of service
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1715 — Intelligent Auto-scaling in Cloud Infrastructure Using Machine Learning and Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The application deployment scenario has changed due to cloud computing, which makes effective resource management. For performance optimization and cost reduction, auto-scaling, or the dynamic adjustment of resources in response to workload variations, is essential. Reinforcement learning, in particular, is a promising machine learning technique that offers answers to this problem. This paper thoroughly analyzes reinforcement learning-based auto-scaling in cloud computing. It introduces reinforcement learning, cloud computing, and auto-scaling, laying the groundwork for how these three concepts will come together. The paper examines reinforcement learning algorithm types such as deep reinforcement learning and extensively used policy gradient approaches for cloud auto-scaling and machine learning alternatives. The main issues of reinforcement learning-based auto-scaling systems with state representations, incentive schemes, and scalability are highlighted. Training reinforcement learning agents for efficient auto-scaling, the importance of simulation setup, and historical data are examined. The paper discusses technical and financial ramifications while showcasing successful reinforcement learning-based and ML-based auto-scaling case studies in web services, data analytics, and container orchestration. Future research areas include explainable AI integration and multi-agent reinforcement learning. This study addresses important technical issues such as scalability, incentive structures, and state representation in relation to RL-based auto-scaling frameworks in cloud computing. It looks at how RL agents are trained, focusing on the use of historical data and simulation setups. In this work, the methodologies of deep reinforcement learning and policy gradient are reviewed and their applications in data analytics, container orchestration, and web services auto-scaling are demonstrated. Important contributions include discussing the financial and technical ramifications, providing case examples, and making recommendations for future multi-agent RL and explainable AI research. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1715.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
