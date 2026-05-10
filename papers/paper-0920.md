---
id: paper-0920
title: Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning
authors:
- Gao, Zhen
- Yang, Lei
- Dai, Yu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3285950
url: https://www.scopus.com/pages/publications/85162722954?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 758--776
keywords:
- Multiaccess edge computing (MEC)
- multiagent reinforcement learning (MARL)
- recurrent graph neural networks (R-GNNs)
- resources allocation
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

# paper-0920 — Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In multiaccess edge computing (MEC), when many mobile devices (MDs) offload their tasks to an edge server (ES), its resources might become constrained. These tasks may take a long time to complete or even be thrown away. Since the unknown information of both the ESs and other MDs, it is difficult for each MD to determine its offloading policy independently. Furthermore, most offloading methods have poor generalization to new environment since they focus on model architecture with a fixed quantity of MDs and ESs, preventing trained models from transferring to other environments. In this article, we provide a full decentralized offloading scheme based on the curriculum attention-weighted graph recurrent network-based multiagent actor-critic (CAGR-MAAC). First, we build MEC as a shared MD agents-ESs graph and an AGR-based message network is designed to enable each MD aggregate the information of ESs and other MDs and solve the partial observability of MD agents for MEC system. Second, a learnable differentiable encoder network is introduced to construct MD agent's local information encoding. Subsequently, the MD agent converts overall the information regarding the MEC system into a fixed-size embedding via an AGR Network to handle different quantity of MDs and ESs. Finally, we introduce curriculum learning to address the huge complexity of the MEC system and the training difficulties induced by the large amounts of MDs and ESs. Experiments demonstrate that compared with existing algorithms, CAGR-MAAC boosts task completion rates and decreases system costs by 13.01%-15.03% and 16.45%-18.56%, and can quickly adapt to the new environment.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0920.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
