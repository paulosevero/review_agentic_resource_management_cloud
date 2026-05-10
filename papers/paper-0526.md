---
id: paper-0526
title: 'DMADRL: A Distributed Multi-agent Deep Reinforcement Learning Algorithm for Cognitive Offloading in Dynamic MEC Networks'
authors:
- Yi, Meng
- Yang, Peng
- Du, Miao
- Ma, Ruochen
venue: Neural Processing Letters
venue_type: journal
year: 2022
doi: 10.1007/s11063-022-10811-y
url: https://www.scopus.com/pages/publications/85129176922?origin=resultslist
publisher: Springer
pages: 4341--4373
keywords:
- Cognitive offloading
- Data transmission rate
- Deep reinforcement learning
- Multi-access edge computing
- The Markov decision process
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

# paper-0526 — DMADRL: A Distributed Multi-agent Deep Reinforcement Learning Algorithm for Cognitive Offloading in Dynamic MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task offloading for mobile devices (MDs) has been extensively studied based on the feature that multi-access edge computing (MEC) can efficiently provide computing and storage resources at the edge of the network. Most existing researches mainly focus on offloading the tasks to the MEC serves to reduce computing energy consumption, while the utilization of idle resources of MDs and the dynamic of users are often ignored. To address this issue, we propose a distributed multi-agent deep reinforcement learning algorithm (DMADRL) with a hybrid cognitive offloading strategy for dynamic MEC networks, in which MDs can use their idle resources to process tasks directly or act as relay nodes to forward tasks to the MEC servers. Taking channel gain and power allocation into account, DMADRL aims to solve an optimal task computation offloading policy in the dynamic MEC network where MDs are moving at a certain rate, and its objective is to maximize the system data transmission rate. Specifically, by modeling this optimal problem as a Markov decision process (MDP), DMADRL integrates two critical phases of centralized training and distributed implementation to overcome the problem that the traditional DRL algorithm cannot converge in multi-agent scenarios. Moreover, DMADRL also considers the experience-sharing mechanism and strategy integration optimization. Simulation results show that our algorithm has excellent convergence, and compared with the other three classical algorithms, our algorithm DMADRL performs better in the cognitive offloading decision. © 2022, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0526.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
