---
id: paper-1888
title: 'Joint Task Offloading and Resource Allocation for Vehicle Platoon: A Nested Algorithm Based on Stackelberg Game'
authors:
- Liu, Jiahui
- Du, Guodong
- Zou, Yuan
- Zhang, Xudong
- Wu, Jinming
- Sun, Wenjing
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3616134
url: https://www.scopus.com/pages/publications/105017587986?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 53288--53307
keywords:
- Dynamic priority
- mobile edge computing (MEC)
- multiagent proximal policy optimization (MAPPO)
- Stackelberg game
- vehicle platoon
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
    my_justification: Game theory
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

# paper-1888 — Joint Task Offloading and Resource Allocation for Vehicle Platoon: A Nested Algorithm Based on Stackelberg Game

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing computational demands of intelligent connected vehicles (ICVs), traditional roadside mobile edge computing (MEC) faces resource and coverage limitations. As a mobile computing entity, a vehicle platoon enables coordinated resource scheduling and low-latency communication, serving as an effective supplement to edge computing. However, limited onboard resources make vehicle platoons insufficient for handling heavy task loads. This study focuses on the joint task offloading and resource allocation between vehicle platoons and MEC servers. An MEC-assisted vehicle platoon computing network (MVPCN) is constructed, where both platoon vehicles (PVs) and MEC servers serve as computing nodes. We formulate a joint optimization problem of task offloading and resource allocation in the vehicle platoon, aiming to minimize the long-term weighted cost of time and energy consumption. Given the complexity of the problem and the limitations of conventional solution methods, we design a discrete two-stage Stackelberg game (DTSG) to decompose the problem into two subproblems: leader [platoon leader (PL)] level and follower (computing nodes) level and prove the existence of a Stackelberg equilibrium (SE). Based on the game model, we propose a nested platoon task offloading and resource-allocation (NPTORA) algorithm. The leader employs the multiagent proximal policy optimization (MAPPO) to generate offloading decisions for the platoon, while the followers allocate computational resources using a dynamic priority-based hybrid optimization (DPHO) algorithm based on the received offloading decisions. Simulation results show that NPTORA outperforms baseline methods in task success, cost efficiency, and adaptability, demonstrating strong performance and practical potential. © 2014 IEEE.

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
- **my_justification:** "Game theory"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1888.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
