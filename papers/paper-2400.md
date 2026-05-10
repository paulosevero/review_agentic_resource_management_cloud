---
id: paper-2400
title: 'Adaptive Incentive and Resource Allocation for Blockchain-Supported Edge Video Streaming Systems: A Cooperative Learning Approach'
authors:
- Yuan, Shijing
- Zhou, Qingshi
- Li, Jie
- Guo, Song
- Chen, Hongyang
- Wu, Chentao
- Yang, Yang
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2024.3437745
url: https://www.scopus.com/pages/publications/85201258893?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 539--556
keywords:
- adaptive incentive
- cooperative processing
- multi-agent reinforcement learning
- Video streaming
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2400 — Adaptive Incentive and Resource Allocation for Blockchain-Supported Edge Video Streaming Systems: A Cooperative Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing significantly enhanced the growth of edge-assistant video streaming applications. However, challenges such as unpredictable wireless conditions, resource constraints, and task redundancy have intertwined impacts on the overall performance of edge video streaming systems (EVS). Therefore, it is essential to have an integrated framework that addresses resource management, computational offloading, and video task preprocessing. Existing optimization strategies often neglect the simultaneous management of computational offloading, resource allocation, and video task preprocessing, leading to a suboptimal system utility. Moreover, they struggle to handle high-dimensional decision variables. On the other hand, learning-based adaptive schemes fall short in integrating distributed decisions and ensuring the scalability of wireless devices. Additionally, current approaches lack adaptive incentives. To bridge these gaps, we propose a novel framework called AIRA, which is based on improved multi-agent reinforcement learning (MARL) and smart contracts. AIRA manages resources, video compression, and adaptive incentives in a distributed manner. It consists of a MARL-driven cooperative learning algorithm (CLA) and a smart contract-guided adaptive incentive mechanism. Leveraging an actor-critic structure, the CLA enables wireless devices to master strategies for resource allocation, video task compression, and offloading, utilizing historical data. Notably, the CLA incorporates an attention mechanism to select pivotal tuples from the observation-action pairings among different agents, ensuring improved scalability and computational prowess. Evaluations based on real-world trajectories demonstrate that AIRA enables adaptive incentives. Compared to state-of-the-art approaches, CLA effectively enhances the long-term system utility and scalability of EVS. © 2002-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2400.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
