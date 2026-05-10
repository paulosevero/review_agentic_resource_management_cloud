---
id: paper-2533
title: Hybrid-Action DRL-Based Resource Allocation for Semantic-Aware Computation Offloading in Vehicular Edge Networks
authors:
- Chen, Quan
- Song, Xiaoqin
- Song, Tiecheng
- Yang, Yang
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2026
doi: 10.1109/TWC.2025.3626670
url: https://www.scopus.com/pages/publications/105021044542?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6790--6805
keywords:
- deep reinforcement learning
- resource allocation
- semantic communication
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2533 — Hybrid-Action DRL-Based Resource Allocation for Semantic-Aware Computation Offloading in Vehicular Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) enhances computational efficiency by strategically offloading tasks from vehicles to edge servers. Integrating semantic communication into vehicular networks introduces further benefits by leveraging semantic information to reduce task transmission delays. However, semantic-aware computation offloading encounters dual challenges: adaptively selecting semantic features to preserve task-critical meaning and dynamically allocating communication and semantic resources under varying network conditions. To cope with these challenges, we propose an importance-based hybrid-action multi-agent proximal policy optimization (I-HAMAPPO) algorithm for the semantic-aware vehicular computation offloading system in this paper. By assessing the importance scores of semantic features, an importance evaluation module (IEM) is designed to selectively transmit task-relevant information. A utility function, integrating task delay, energy consumption, and semantic similarity, is developed to provide a multi-dimensional performance evaluation of the system. Subsequently, the optimization problem is formulated with the objective of maximizing system utility by optimizing communication resources and semantic compression ratios. Considering the presence of mixed decision variables in the formulated problem, we employ the proposed I-HAMAPPO algorithm to optimize the continuous and discrete actions jointly. Based on real-world vehicle trajectories from the highD dataset, extensive experimental results demonstrate the convergence of I-HAMAPPO and its efficacy in maximizing system utility. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2533.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
