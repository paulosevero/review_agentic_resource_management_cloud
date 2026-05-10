---
id: paper-1303
title: Global optimization strategy of prosumer data center system operation based on multi-agent deep reinforcement learning
authors:
- Yang, Dongfang
- Wang, Xiaoyuan
- Shen, Rendong
- Li, Yang
- Gu, Lei
- Zheng, Ruifan
- Zhao, Jun
- Tian, Xue
venue: Journal of Building Engineering
venue_type: journal
year: 2024
doi: 10.1016/j.jobe.2024.109519
url: https://www.scopus.com/pages/publications/85193460813?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- D3QN
- Data center system
- Global cooperative optimization
- VDN
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

# paper-1303 — Global optimization strategy of prosumer data center system operation based on multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The escalating issues of high energy consumption and carbon emissions in data centers (DCs) necessitate the optimization of system operations. However, early optimization strategies were overly simplistic and lacked automated updating and iterative capabilities. With the evolution of artificial intelligence (AI), researchers have applied deep reinforcement learning (DRL) algorithms to system operations. However, the optimization focus has been limited to the internal systems, lacking global optimization. In this paper, a global optimization control strategy based on the Dueling double-deep Q network (D3QN) and value decomposition network (VDN) algorithms is proposed to make the DCs system operate more closely with the upstream, midstream, and downstream. By adjusting battery charging/discharging capacity, computational workload, and waste heat utilization heating temperature global synergistic optimization is achieved. Compared with without optimization, renewable energy waste, operation cost, total electricity consumption, and grid electricity consumption are reduced by 18.37%, 9.78%, 4.01%, and 29.74%, respectively. Additionally, a detailed comparison between non-algorithmic optimization and algorithmic optimization is provided, offering valuable insights for substantial energy savings and emissions reduction in DCs. The results demonstrate the importance of fully exploring the interactive potential between upstream energy supply, midstream computational workload, and downstream waste heat recovery to achieve synergistic global optimization of “computing power", “thermal energy" and “electrical energy" for the sustainable and green development of DCs or other prosumer buildings. © 2024 Elsevier Ltd

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1303.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
