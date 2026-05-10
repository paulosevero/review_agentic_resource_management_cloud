---
id: paper-1709
title: An effective method for prospective scheduling of tasks in cloud-fog computing with an energy consumption management approach based on Q-learning
authors:
- Jin, Yan
venue: Engineering Applications of Artificial Intelligence
venue_type: journal
year: 2025
doi: 10.1016/j.engappai.2025.110705
url: https://www.scopus.com/pages/publications/105001311827?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Cloud computing
- Energy consumption
- Prospective task scheduling
- Reinforcement learning
- Response time
- Task scheduling
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

# paper-1709 — An effective method for prospective scheduling of tasks in cloud-fog computing with an energy consumption management approach based on Q-learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing energy consumption in cloud computing data centers has become a significant concern due to the expanding scale of computational demands. Efficient task scheduling is crucial to optimizing resource utilization while reducing operational costs and energy consumption. This study proposes a Multi-Agent Reinforcement Learning (MARL)-based scheduling framework that enhances system efficiency by dynamically allocating tasks based on environmental variations and workload fluctuations. Unlike conventional methods, MARL allows multiple intelligent agents to collaboratively optimize scheduling decisions, leading to superior adaptability and performance. The proposed approach consists of two steps: first, a centralized task dispatcher assigns incoming tasks to cloud servers using a queuing model. Second, an MARL-based scheduler on each server prioritizes and allocates tasks to virtual machines while continuously updating scheduling policies to maximize efficiency. The framework is evaluated using a CloudSim-based simulation environment to ensure a realistic and controlled assessment. Experimental results demonstrate that the proposed method reduces energy consumption by an average of 51.34 %, improves CPU utilization efficiency, and decreases response time by 44.35 % compared to traditional scheduling techniques, including First In-First Out (FIFO), Greedy, and Queue-based Scheduling (Q-sch). By leveraging MARL, the scheduler effectively minimizes waiting times and optimizes task completion rates, ensuring a balance between energy efficiency and system performance. This work highlights the advantages of reinforcement learning in cloud-fog computing and underscores its potential for intelligent resource management. © 2025 Elsevier Ltd

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1709.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
