---
id: paper-2608
title: A Multi-Agent Deep Reinforcement Learning-Based Task Offloading Method for 6G-Enabled Internet of Vehicles with Cloud-Edge-Device Collaboration
authors:
- Hu, Fangxiang
- Fu, Qi
- Zhang, Shiwen
- Huang, Jing
venue: Computers, Materials and Continua
venue_type: journal
year: 2026
doi: 10.32604/cmc.2026.074154
url: https://www.scopus.com/pages/publications/105035886134?origin=resultslist
publisher: Tech Science Press
pages: ''
keywords:
- 6G
- cloud-edge-device collaboration
- high-density vehicle
- multi-agent proximal policy optimization
- resource allocation
- task offloading
- Vehicular edge computing
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

# paper-2608 — A Multi-Agent Deep Reinforcement Learning-Based Task Offloading Method for 6G-Enabled Internet of Vehicles with Cloud-Edge-Device Collaboration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the Internet of Vehicles (IoV) environment, the growing demand for computational resources from diverse vehicular applications often exceeds the capabilities of intelligent connected vehicles. Traditional approaches, which rely on one or more computational resources within the cloud-edge-device computing model, struggle to ensure overall service quality when handling high-density traffic flows and large-scale tasks. To address this issue, we propose a computational offloading scheme based on a cloud-edge-device collaborative 6G IoV edge computing model, namely, Multi-Agent Deep Reinforcement Learning-based and Server-weighted scoring Selection (MADRLSS), which aims to optimize dynamic offloading decisions and resource allocation. The scheme first designs an improved multi-agent proximal policy optimization (MAPPO) algorithm, decoupling centralized training from distributed execution for multiple terminal vehicle agents. Specifically, the centralized training of terminal vehicles is migrated to the high-performance edge layer, while lightweight decision-making networks are retained at the terminal vehicles to enable efficient and dynamic task offloading decisions. Additionally, a server-weighted scoring selection (SS) algorithm is proposed, which integrates two key metrics—short-term server load and geographical proximity—to select the optimal server and allocate communication resources. The proposed scheme improves the quality of experience (QoE) while balancing energy consumption. Simulation results demonstrate that the MADRLSS scheme significantly outperforms existing benchmark methods in terms of task offloading efficiency and stability, maintaining QoE consistently above 82% and effectively enhancing service quality in complex vehicular scenarios. Copyright © 2026 The Authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2608.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
