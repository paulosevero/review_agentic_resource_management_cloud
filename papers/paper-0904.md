---
id: paper-0904
title: Caching Video by Distributed Multi-agent Reinforcement Learning
authors:
- Fang, Lei
- Liu, Wenbin
- Wang, En
- Yang, Funing
venue: 2024 4th International Conference on Neural Networks, Information and Communication Engineering, NNICE 2024
venue_type: conference
year: 2024
doi: 10.1109/NNICE61279.2024.10498437
url: https://www.scopus.com/pages/publications/85192507911?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 170--174
keywords:
- decentralize training
- deep learning
- multi-agent reinforcement learning
- video chching
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0904 — Caching Video by Distributed Multi-agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing is a new paradigm to support video caching, aiming to optimize the user's viewing experience. However, existing works have focused on centralized algorithms, which require a powerful computing center to do scheduling to determine the video content that should be stored on which edge server closest to the user. Therefore, these approach put too much pressure on the backbone network, resulting in increased application costs and reducing its usefulness. To address the above limitation, we consider this scenario without any computing center and propose an innovative distributed video caching algorithm that is different from the previous centralized methods. In our scenario, we no longer need the support of the computing center, but only consider the information interaction between the edge nodes. Our objective is to reduce the average latency to improve the user experience. To this end, we propose a novel decentralized multi-agent reinforcement learning (MARL) algorithm, Distributed Algorithm Without Center (DAWC), implementing in decentralized training and decentralized execution. The main difference between our algorithm and the existing MARL algorithm is that our algorithm is trained distributed, while other algorithms are trained centrally. We further utilize a neural communication protocol to reduce information loss and non-stationary by introducing hidden state and differentiable message encoding and extracting functions. Extensive performance results show that the performance of DAWC is not significantly weaker than that of MARL algorithm with central participation in centralized learning, but other independent learning algorithm and random offloading strategy. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0904.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
