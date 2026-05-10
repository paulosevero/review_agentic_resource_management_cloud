---
id: paper-0491
title: Distributed Training for Deep Learning Models On An Edge Computing Network Using Shielded Reinforcement Learning
authors:
- Sen, Tanmoy
- Shen, Haiying
venue: Proceedings - International Conference on Distributed Computing Systems
venue_type: conference
year: 2022
doi: 10.1109/ICDCS54860.2022.00062
url: https://www.scopus.com/pages/publications/85140890520?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 581--591
keywords:
- Deep learning
- Distributed cloud
- Edge computing
- Fertilizers
- Learning systems
- Multi agent systems
- Centralised
- Cluster nodes
- Cluster-heads
- Edge computing
- Edge nodes
- Learning models
- Multi-agent reinforcement learning
- Reinforcement learnings
- Resources utilizations
- Training time
- Reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0491 — Distributed Training for Deep Learning Models On An Edge Computing Network Using Shielded Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of edge devices along with their local computation advantage over the cloud, distributed deep learning (DL) training on edge nodes becomes promising. In such a method, the cluster head of a cluster of edge nodes schedules all the DL training jobs from the cluster nodes. Using such a centralized scheduling method, the cluster head knows all the loads of the cluster nodes, which can avoid overloading the cluster nodes, but the head itself may become overloaded. To handle this problem, we first propose a multi-agent RL (MARL) system that enables each edge node to schedule its own jobs using RL. However, without the coordination between the nodes, action collision may occur, in which multiple nodes may schedule tasks to the same node and make it overloaded. To avoid these problems, we propose a system called Shielded ReinfOrcement learning (RL) based DL training on Edges (SROLE). In SROLE, each edge node schedules its own jobs using multi-agent RL. The shield deployed in a node checks action collisions and provides alternative actions to avoid the collisions. As the central shield node for the entire cluster may become a bottleneck, we further propose a decentralized shielding method, in which different shields are responsible for different regions in the cluster and they coordinate to avoid action collisions on the region boundaries. Our container-based emulation experiments show that SROLE reduces training time by up to 59% with 29% lower median resource utilization and reduces the number of action collisions by up to 48% compared to multi-agent RL and the centralized RL. Our real device experiments show that SROLE still reduces the training time by up to 53% with 28% lower median resource utilization than multi-agent RL and the centralized RL.  © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0491.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
