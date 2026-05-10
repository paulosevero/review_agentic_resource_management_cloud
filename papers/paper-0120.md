---
id: paper-0120
title: 'UAV-enabled mec system: Locations and coverage optimization'
authors:
- Cui, Yan
- Zheng, Jianchao
- Wang, Xiangdong
- Diao, Xianbang
- Cai, Yueming
- Liu, Siyan
venue: IET Conference Publications
venue_type: conference
year: 2019
doi: 10.1049/cp.2019.1142
url: https://www.scopus.com/pages/publications/85090563944?origin=resultslist
publisher: Institution of Engineering and Technology
pages: 12--18
keywords:
- MEC
- Multi-Agent Intelligent-Learning Algorithm
- Potential Game
- UAVs
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0120 — UAV-enabled mec system: Locations and coverage optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) can significantly enhance the computation capability of mobile devices and reduce their energy consumptions. Compared with terrestrial base stations, UAVs are flexible and easy to deploy, so they can provide more flexible and reliable edge computing services for ground users. In this paper, we study an UAV-enabled MEC system, where the UAV group serves as an edge server group to provide computing offloading services for high-density ground users. Ground users within UAV's coverage will choose local computing or offload to UAVs based on the principle of minimizing the weighted sum of their energy consumption and the delay. In order to serve more ground users and control the growth of its own energy consumption, each UAV will find an appropriate hover point and determine the coverage at a fixed height. We model the problem as a game model, and obtain the Nash equilibrium (NE) point by our Multi-agent Intelligent-learning Algorithm (MIA). Simulation results show that our algorithm has better performance, and each UAV can achieve a balance between the number of ground users it serves and its own energy consumption. © 2019 Institution of Engineering and Technology. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0120.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
