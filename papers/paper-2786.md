---
id: paper-2786
title: 'Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning'
authors:
- Sun, Yunhe
- Wang, Yu
- Hawbani, Ammar
- Hao, Fei
- Othman, Wajdy
- Yang, Dongsheng
- Zhao, Liang
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112282
url: https://www.scopus.com/pages/publications/105035101196?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Energy optimization
- Satellite edge computing
- Task offloading
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2786 — Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low Earth orbit (LEO) satellite constellations face stringent constraints on energy and computational resources during long-term operation. Among these constraints, the lifetime of onboard batteries is a key factor limiting satellite service duration. As the intensity of computational tasks increases, onboard data processing has become a major source of energy consumption, further exacerbating battery energy constraints. To this end, this paper proposes a three-layer heterogeneous Satellite Mobile Edge Computing (SMEC) architecture to address these challenges, integrating Ground Stations (GS), Remote Sensing Satellites (RSS), and Computing Satellites (CS). The proposed architecture minimizes local computational load while extending battery lifespan. A joint optimization model incorporates key performance indicators including energy consumption, latency, task loss, and battery Depth of Discharge (DoD). Based on this model, and considering the dynamic complexity of satellite networks, we develop a computation offloading strategy using the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm. This strategy enables RSS to autonomously determine optimal offloading decisions in dynamic environments, facilitating multi-agent collaborative optimization. Simulation results confirm the proposed method's superior prformance over benchmark algorithms in task latency, energy efficiency, task loss rate, and DoD management, while significantly extending satellite lifespan. © 2026

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2786.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
