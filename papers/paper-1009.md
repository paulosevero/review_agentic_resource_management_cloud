---
id: paper-1009
title: 'Caching on the Sky: A Multiagent Federated Reinforcement Learning Approach for UAV-Assisted Edge Caching'
authors:
- Li, Xuanheng
- Liu, Jiahong
- Chen, Xianhao
- Wang, Jie
- Pan, Miao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3401219
url: https://www.scopus.com/pages/publications/85193247249?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 28213--28226
keywords:
- Deep reinforcement learning
- federated learning
- mobile edge caching
- unmanned aerial vehicle (UAV) networks
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

# paper-1009 — Caching on the Sky: A Multiagent Federated Reinforcement Learning Approach for UAV-Assisted Edge Caching

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a promising solution to alleviate network congestion, mobile edge caching based on unmanned aerial vehicles (UAVs) has emerged and received intensive research interests, where users could download their desired contents from UAVs with much lower latency. As for the UAV-assisted edge caching, to improve the users' Quality of Experience while reducing the cost on content updating, how to jointly design the trajectory and caching strategy for UAVs is critical. However, considering the dynamics and uncertainty on the traffic environment, as well as the mutual effect among different UAVs, such joint design is nontrivial. In this article, we propose a collaborative joint trajectory and caching scheme for UAV-assisted networks under the dynamic and uncertain traffic environment. Unlike most existing work relying on model-based or single-agent methods, we develop a multiagent deep reinforcement learning (MADRL) approach to obtain the solution, where the specific content demand model is not needed and each UAV would learn the best decision autonomously based on its local observations. It can achieve the adaptive cooperation among different UAVs, while optimizing the overall network performance. Moreover, standing from the perspective on swarm intelligence, we further develop a dynamic clustering federated learning framework on the MADRL algorithm. By performing parameter fusion, each UAV can improve the learning efficiency.  © 2014 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1009.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
