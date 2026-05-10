---
id: paper-1844
title: A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers
authors:
- Lin, Wenjun
- Lin, Weiwei
- Lin, Jianpeng
- He, Ligang
- Wang, Jiangtao
- Jiang, Hongliang
venue: Journal of Building Engineering
venue_type: journal
year: 2025
doi: 10.1016/j.jobe.2025.112811
url: https://www.scopus.com/pages/publications/105005082223?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Cooling system
- Data center
- Energy optimization
- Multi-agent reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1844 — A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cooling systems within data centers (DCs) have attracted significant attention due to their high energy consumption. Existing optimization methods for cooling systems typically follow a two-stage process: first, constructing the simulation model of data centers based on physical laws; subsequently, applying optimization algorithms to determine the optimal cooling operations. However, purely physical models rely heavily on extensive underlying parameters and often lose accuracy when dealing with complex systems. Moreover, conventional optimization algorithms are usually based on best practices or heuristics, encountering challenges in generalization due to their reliance on prior knowledge specific to individual data centers. To address these problems, this paper applies a data-driven approach to develop simulation models for the air–liquid hybrid cooling system in data centers. Then, a multi-agent reinforcement learning-based method is proposed to achieve the joint control optimization of air-cooled and liquid-cooled equipment, aiming to reduce total energy consumption without thermal risks. Furthermore, to tackle the inherent challenge of credit assignment in the multi-agent system, a rewarding mechanism based on baseline comparison is designed to allocate the global reward according to each agent's actual contribution to the environment, thereby facilitating efficient learning. Numerical experiments conducted on the Marconi-100 dataset verify the effectiveness of the proposed method, achieving an average energy saving (RCI) of 7.7% while maintaining the rack cooling index above 99%. © 2025 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1844.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
