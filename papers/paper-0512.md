---
id: paper-0512
title: 'Dynamic Many-to-Many Task Offloading in Vehicular Fog Computing: A Multi-Agent DRL Approach'
authors:
- Wei, Zhiwei
- Li, Bing
- Zhang, Rongqing
- Cheng, Xiang
- Yang, Liuqing
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2022
doi: 10.1109/GLOBECOM48099.2022.10001342
url: https://www.scopus.com/pages/publications/85146948913?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6301--6306
keywords:
- many-to-many
- multi-agent deep reinforcement learning
- POMDP
- task offloading
- vehicular fog computing
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

# paper-0512 — Dynamic Many-to-Many Task Offloading in Vehicular Fog Computing: A Multi-Agent DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Confronted with the increasing computation-intensive requirements of vehicular applications, vehicular fog computing (VFC) has emerged as the promising solution to mitigate the load at the edge of vehicular network. In VFC, vehicles are employed as vehicular fog nodes to provide reliable services with applicability. However, considering the individual serving and offloading intentions of the privately-owned vehicles, the many-to-many task offloading in dynamic vehicular environment becomes a challenging problem. In this paper, we propose a distributed dynamic many-to-many task offloading framework based on vehicle-to-vehicle (V2V) trading paradigm to improve the fog resource utilization in VFC. In order to reach an effective and stable offload-and-serve cooperation between vehicles as service demanders and vehicles as computation providers in the proposed framework, we formulate the trading process as a partially observable Markov decision processes (POMDP) and design a Multi-Agent Gated actor Attention Critic (MA-GAC) approach, leading to an efficient offloading optimization process in a distributed manner. Theoretical analysis and experiments verify the feasibility and efficiency of the proposed framework, and simulation results demonstrate that the proposed MA-GAC approach outperforms other benchmarks in the dynamic environment. © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0512.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
