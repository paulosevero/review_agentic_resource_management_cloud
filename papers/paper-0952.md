---
id: paper-0952
title: Hierarchical Task Offloading for Vehicular Fog Computing Based on Multi-Agent Deep Reinforcement Learning
authors:
- Hou, Yukai
- Wei, Zhiwei
- Zhang, Rongqing
- Cheng, Xiang
- Yang, Liuqing
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2023.3305321
url: https://www.scopus.com/pages/publications/85168667065?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3074--3085
keywords:
- counterfactual multi-agent
- hierarchical task offloading
- multi-agent reinforcement learning
- Vehicular fog computing
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

# paper-0952 — Hierarchical Task Offloading for Vehicular Fog Computing Based on Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular fog computing (VFC) has been expected as a promising architecture that can make full use of computing resources of idle vehicles to increase computing capability. However, most current VFC architectures only focus on the local region and ignore the spatio-temporal heterogeneity of computing resources, resulting in that some regions have idle computing resources while others cannot satisfy the requirements of tasks. To further improve the overall computing resource utilization in the whole network, in this work, we propose a hierarchical VFC architecture, where neighboring regions can share their idle computing resources. Considering the high complexity of both inter- and intra-region cooperative task offloading in such a hierarchical VFC architecture, we put forward a distributed task offloading strategy based on multi-agent reinforcement learning in which the multi-agent reinforcement learning method is designed to learn each task vehicle's offloading strategy in a distributed manner. Moreover, to tackle the inefficiency caused by the multi-agent credit assignment problem, we provide the counterfactual multi-agent reinforcement learning approach which exploits a counterfactual baseline to evaluate the action of each agent. Simulation results validate that the proposed hierarchical VFC architecture can effectively improve the global task computing efficiency and the proposed mechanism outperforms the baseline algorithms.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0952.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
