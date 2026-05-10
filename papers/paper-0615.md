---
id: paper-0615
title: Cooperative Multi-Agent Deep Reinforcement Learning for Computation Offloading in Digital Twin Satellite Edge Networks
authors:
- Ji, Zhe
- Wu, Sheng
- Jiang, Chunxiao
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2023
doi: 10.1109/JSAC.2023.3313595
url: https://www.scopus.com/pages/publications/85171523894?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3414--3429
keywords:
- computation offloading
- digital twin
- multi-Agent reinforcement learning
- Satellite edge computing
- twin delayed deterministic policy gradient
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

# paper-0615 — Cooperative Multi-Agent Deep Reinforcement Learning for Computation Offloading in Digital Twin Satellite Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of commercial off-The-shelf hardware, low Earth orbit (LEO) satellites are promising to provide flexible edge computing services. In this paper, we investigate a digital twin (DT)-empowered satellite-Terrestrial cooperative edge computing network, where computation tasks from terrestrial users can be partially offloaded to the associated base station (BS) edge server, the associated LEO satellite edge server, and an adjacent LEO satellite edge server. We formulate a multi-Tier computation offloading optimization problem to minimize the weighted sum of total system delay and satellite energy consumption, where a LEO-layer problem and a DT-layer problem are involved. The LEO-layer problem optimizes the three-Tier computation resource allocation and task splitting ratio. From the multi-satellite network perspective, the DT-layer problem optimizes how many resources will be shared between adjacent satellites. We then propose a multi-Agent double actors twin delayed deterministic policy gradient (MA-DATD3) algorithm to optimize the LEO-layer problem, and adopt a centralized training and decentralized execution (CTDE) paradigm. The proposed MA-DATD3 algorithm is extended to solve the DT-layer problem in a centralized way, and the resource sharing between adjacent satellites is optimized to maximize the time-Averaged reward. Simulation results show that our algorithm achieves a better performance than the MADDPG algorithm, and effectively improves the computation offloading performance while balancing the energy consumption and the total delay.  © 1983-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0615.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
