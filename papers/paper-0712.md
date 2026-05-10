---
id: paper-0712
title: A federated multi-agent deep reinforcement learning for vehicular fog computing
authors:
- Shabir, Balawal
- Rahman, Anis U.
- Malik, Asad Waqar
- Buyya, Rajkumar
- Khan, Muazzam A.
venue: Journal of Supercomputing
venue_type: journal
year: 2023
doi: 10.1007/s11227-022-04911-8
url: https://www.scopus.com/pages/publications/85140976388?origin=resultslist
publisher: Springer
pages: 6141--6167
keywords:
- A3C
- Advantage function
- Computation offloading
- Deep reinforcement learning
- Federated learning
- Residence time
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0712 — A federated multi-agent deep reinforcement learning for vehicular fog computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular fog computing is an emerging paradigm for delay-sensitive computations. In this highly dynamic resource-sharing environment, optimal offloading decision for effective resource utilization is a challenging task. In recent years, deep reinforcement learning has emerged as an effective approach for dealing with resource allocation problems because of its self-adapting nature in a large state space scenario. However, due to high mobility and rapid changes in the network topology cause fluctuating task arrival rate. Similarly, the data sharing between the vehicles and the fog nodes raises a variety of security and privacy concerns. Therefore, the proposed system is based on local and global model training approaches. In this paper, we propose a federated multi-agent deep reinforcement learning solution that efficiently learns task-offloading decisions at multiple tiers i.e. locally and globally. The proposed work results in fast convergence due to its collaborative learning model among vehicles and fog servers. The local model runs at the vehicular nodes, and the global model runs at the fog servers. To reduce network overhead, the models are learned locally; thus, limited information is shared across the network this reduces the communication overhead and improves the privacy of the agents. The proposed system is compared with the greedy and stochastic approaches in terms of residence times, cost, delivery rate, and utilization ratio. We observed that the proposed approach has significantly reduced the task residence time, end-to-end delay and overall system cost. © 2022, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0712.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
