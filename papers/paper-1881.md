---
id: paper-1881
title: Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning
authors:
- Liu, Qi
- Yang, Jianzheng
- Yan, Zhixian
venue: Knowledge and Information Systems
venue_type: journal
year: 2025
doi: 10.1007/s10115-025-02507-1
url: https://www.scopus.com/pages/publications/105008824769?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 9363--9383
keywords:
- Edge computing
- Multi-agent
- Quality of service
- Reinforcement learning
- Resource orchestration
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

# paper-1881 — Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a dynamic resource orchestration framework for edge computing environments, utilizing multi-agent reinforcement learning (MARL) to enhance resource allocation and task scheduling. The proposed system consists of edge nodes (E), a centralized resource manager (CRM), and communication infrastructure (CI). Edge nodes execute computational tasks at the network’s periphery, while the CRM oversees resource distribution and task assignment using a global system perspective. The CI supports efficient communication among these components. The MARL framework enables collaborative learning among agents, where each agent selects optimal actions—such as resource allocation, task scheduling, and migration—based on system states that include resource availability, task queue lengths, network conditions, and task priorities. A deep Q-network (DQN)-based training approach is employed, allowing agents to maximize cumulative rewards by balancing task completion efficiency, resource utilization, and latency minimization. The proposed framework is evaluated through comprehensive simulations against traditional heuristic-based and static resource allocation methods. Results demonstrate that our MARL-based approach reduces average task completion latency by 12.3% and improves resource utilization by 8.7% compared to heuristic baselines. Additionally, the framework dynamically adapts to variations in network conditions and workload distribution, ensuring consistent quality of service (QoS) under dynamic edge computing scenarios. © The Author(s), under exclusive licence to Springer-Verlag London Ltd., part of Springer Nature 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1881.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
