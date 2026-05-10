---
id: paper-1842
title: IBR-MAPPO-based Task Offloading in Space-Air-Ground Integrated Vehicular Networks
authors:
- Liao, Zixuan
- Xu, Bo
- Cao, Haotong
- Shu, Zixuan
- Sun, Jinlong
- Zhao, Haitao
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2025
doi: 10.1109/VTC2025-Fall65116.2025.11310474
url: https://www.scopus.com/pages/publications/105032399929?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- multi-agent proximal policy optimization
- resource allocation
- Space-Air-ground integrated vehicular network
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1842 — IBR-MAPPO-based Task Offloading in Space-Air-Ground Integrated Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Space-Air-ground integrated vehicular network (SAGVN) can provide substantial advantages for the Internet of Vehicles (IoV) with broad coverage and long-distance communications. However, efficient task offloading in SAGVN is difficult due to the dynamic and multi-dimensional characteristics of IoV. In this paper, we address a task offloading problem in SAGVN, where unmanned aerial vehicles (UAVs) and low Earth orbit (LEO) satellites collaborate to offer mobile edge computing (MEC) services to vehicles. Our goal is to jointly design service placement and task offloading strategies for each UAV to minimize overall system latency, subject to mobility, coverage, energy, and bandwidth constraints. The problem can be reformulated as a multi-agent Markov decision process (MAMDP), where each vehicle and UAV can act as an agent, and the actions taken by agents correspond to the optimal UAV trajectory, subchannel selection, task partition ratio, and offloading destination. Then, we decompose the problem into three sub-problems of service placement, task offloading, and subchannel selection. Given the extensive observation and action space, an iterative best response multi-agent proximal policy optimization (IBR-MAPPO) algorithm is proposed. Finally, simulation results show that our approach converges rapidly and achieves lower execution delay than baseline algorithms.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1842.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
