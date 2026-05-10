---
id: paper-0265
title: Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing
authors:
- Bai, Wenle
- Qian, Cheng
venue: Proceedings of the IEEE International Conference on Software Engineering and Service Sciences, ICSESS
venue_type: conference
year: 2021
doi: 10.1109/ICSESS52187.2021.9522334
url: https://www.scopus.com/pages/publications/85114963754?origin=resultslist
publisher: IEEE Computer Society
pages: 131--134
keywords:
- deep reinforcement learning
- fog computing
- offloading
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

# paper-0265 — Deep Reinforcement Learning for Joint Offloading and Resource Allocation in Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The traditional cloud computing model can no longer satisfy the current demand due to the limitations of backhaul bandwidth and high latency. Therefore, a new fog computing architecture is proposed, which relieves the bandwidth load and energy pressure on the backhaul link by reducing the number of communications between the cloud computing center and the users. The latency is drastically reduced by proximity to the devices. However, the performance of fog computing is highly dependent on a variety of resource allocation strategies. Therefore, task offloading strategies and resource allocation strategies are a great challenge. In this paper, we use the advantage actor-critic (A2C) algorithm in Deep reinforcement learning (DRL) to jointly optimize the offloading strategy, and network resource allocation strategy to reduce latency for dependent computational tasks in fog computing. One of the major challenges of such problems is that there are multiple action dimensions, which makes it difficult to converge the network. Therefore, this paper uses the multi-Agent method to simplify the problem by splitting the complete offload decision action into three sub-Actions. We demonstrate through numerical simulations that the algorithm can effectively reduce the cost and also discuss the effects of the different number of devices and the different number of fog nodes on the cost.  © 2021 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0265.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
