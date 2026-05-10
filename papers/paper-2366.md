---
id: paper-2366
title: Dual-Layer Optimization Scheduling of Data Center Based on Multi-Agent Proximal Strategy Network; [基 于 多 智 能 体 近 端 策 略 网 络 的 数 据 中 心 双 层 优 化调 度]
authors:
- Yang, Xiu
- Zhang, Xiangyin
- Huang, Haitao
- Yu, Wenchang
- Chen, Yonggang
- Cao, Junbo
venue: Southern Power System Technology
venue_type: journal
year: 2025
doi: 10.13648/j.cnki.issn1674-0629.2025.04.009
url: https://www.scopus.com/pages/publications/105007736249?origin=resultslist
publisher: Editorial Department of Southern Power System Technology
pages: 107--121and131
keywords:
- data center
- multi-agent
- proximal strategy optimization
- spatiotemporal scheduling
- workload allocation
language: Chinese
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Review
    winning_category: review
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-2366 — Dual-Layer Optimization Scheduling of Data Center Based on Multi-Agent Proximal Strategy Network; [基 于 多 智 能 体 近 端 策 略 网 络 的 数 据 中 心 双 层 优 化调 度]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous evolution of new generation information and communication technologies such as 5G, cloud comput⁃ ing, and artificial intelligence, the world is rapidly entering the fast lane of the digital economy. A dual-layer optimization scheduling method for data centers based on multi-agent proximal strategy network is proposed to address the uncertainty of renewable energy and workload prediction in data centers. Firstly, a dual-layer spatiotemporal optimization scheduling framework for data centers is established, which provides detailed modeling of data center workloads, IT equipment, and air conditioning equipment; On this basis, a dual-layer optimization scheduling model for data centers is proposed. The upper layer schedules the time dimension with the goal of minimizing the total operating cost of IDC operators, while the lower layer schedules the space dimension with the goal of minimiz⁃ ing the operating cost of each IDC. Then, the principle of multi-agent proximal strategy network algorithm is introduced, and the state space, action space, and reward function of the dual-layer optimization scheduling model for data centers are designed. Finally, of⁃ fline training and online scheduling decisions are conducted for the examples. Simulation results show that the proposed model and method can effectively reduce system costs and energy consumption, achieve optimal workload allocation, and have good economy and robustness. © 2025 Editorial Department of Southern Power System Technology. All rights reserved.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_editorial, matched_substring: "Editorial" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2366.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
