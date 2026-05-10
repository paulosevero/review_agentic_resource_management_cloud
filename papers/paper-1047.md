---
id: paper-1047
title: A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control
authors:
- Lin, Wenjun
- Lin, Weiwei
- Lin, Jianpeng
- Zhong, Haocheng
- Wang, Jiangtao
- He, Ligang
venue: 'Sustainable Computing: Informatics and Systems'
venue_type: journal
year: 2024
doi: 10.1016/j.suscom.2024.100977
url: https://www.scopus.com/pages/publications/85184797831?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- DVFS
- Multi-agent
- Reinforcement learning
- Server fan
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1047 — A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of the digital economy and intelligent industry, the energy consumption of data centers (DCs) has increased significantly. Various optimization methods are proposed to improve the energy efficiency of servers in DCs. However, existing solutions usually adopt model-based heuristics and best practices to select operations, which are not universally applicable. Moreover, existing works primarily focus on the optimization methods for individual components, with a lack of work on the joint optimization of multiple components. Therefore, we propose a multi-agent reinforcement learning-based method, named MRDF, combining DVFS and dynamic fan control to achieve a trade-off between power consumption and performance while satisfying thermal constraints. MRDF is model-free and learns by continuously interacting with the real server without prior knowledge. To enhance the stability of MRDF in dynamic environments, we design a data-driven baseline comparison method to evaluate the actual contribution of a single agent to the global reward. In addition, an improved Q-learning is proposed to deal with the large state and action space of the multi-core server. We implement MRDF on a Huawei Taishan 200 server and verify the effectiveness by running benchmarks. Experimental results show that the proposed method improves energy efficiency by an average of 3.9% compared to the best baseline solution, while flexibly adapting to different thermal constraints. © 2024

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1047.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
