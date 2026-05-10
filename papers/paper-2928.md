---
id: paper-2928
title: Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers
authors:
- Zhao, Yu
- Wang, Cheng
- Yan, Chungang
- Li, Xiaoli
- Jiang, Changjun
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3656552
url: https://www.scopus.com/pages/publications/105028437042?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computing service scheduling
- data augmentation
- distributed data centers
- heuristic guidance
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2928 — Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid growth of computing services in distributed data centers, efficient scheduling needs to consider workload dynamics, resource fluctuations, and diverse optimization preferences while maintaining service quality and system efficiency. Multi-Agent Deep Reinforcement Learning (MADRL) offers a decentralized and adaptive paradigm that enables agents to learn local scheduling policies aligned with individual objectives while collectively improving global performance. However, existing MADRL approaches often suffer from low sample efficiency and limited generalization under dynamic and heterogeneous conditions. This paper proposes a Heuristic-guided Multi-Agent deep Reinforcement learning (H-MAR) approach for computing service scheduling. H-MAR is a novel multi-agent learning framework where heuristic functions act as structured priors to guide personalized policy optimization, and data augmentation is employed to enhance experience coverage and policy robustness. Moreover, we provide a modified Decentralized Partially Observable Markov Decision Process (Dec-POMDP) formulation to support the theoretical analysis of H-MAR. Experiments on real-world Alibaba cluster traces show that H-MAR outperforms representative baselines in the success rate of instance creation, load balancing, and energy consumption, validating its effectiveness for adaptive and robust computing service delivery. © 2008-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2928.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
