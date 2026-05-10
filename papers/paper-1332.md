---
id: paper-1332
title: Distributed Multi-Agent Reinforcement Learning for Cooperative Low-Carbon Control of Traffic Network Flow Using Cloud-Based Parallel Optimization
authors:
- Zhang, Yongnan
- Zhou, Yonghua
- Fujita, Hamido
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2024
doi: 10.1109/TITS.2024.3452430
url: https://www.scopus.com/pages/publications/85210925168?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 20715--20728
keywords:
- Distributed multi-agent reinforcement learning
- graph convolutional network
- low-carbon control
- parallel optimization
- self-attention value decomposition
- traffic network flow
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

# paper-1332 — Distributed Multi-Agent Reinforcement Learning for Cooperative Low-Carbon Control of Traffic Network Flow Using Cloud-Based Parallel Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The escalating air pollution resulting from traffic congestion has necessitated a shift in traffic control strategies towards green and low-carbon objectives. In this study, a graph convolutional network and self-attention value decomposition-based multi-agent actor-critic (GSAVD-MAC) approach is proposed to cooperative control traffic network flow, where vehicle carbon emission and traffic efficiency are considered as reward functions to minimize carbon emissions and traffic congestions. In this method, we design a local coordination mechanism based on graph convolutional network to guide the multi-agent decision-making process by extracting spatial topology and traffic flow characteristics between adjacent intersections. This enables distributed agents to make low-carbon decisions which not only account for their own interactions with the environment but also consider local cooperation with neighboring agents. Further, we design a global coordination mechanism based on self-attention value decomposition to guide multi-agent learning process by assigning various weights to distributed agents with respect to their contribution degrees. This enables distributed agents to learn a globally optimal low-carbon control strategy in a cooperative and adaptive manner. In addition, we design a cloud computing-based parallel optimization algorithm for the GSAVD-MAC model to reduce calculation time costs. Simulation experiments based on real road networks have verified the advantages of the proposed method in terms of computational efficiency and control performance. © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1332.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
