---
id: paper-1313
title: DNN distributed inference offloading scheme based on transfer reinforcement learning in metro optical networks
authors:
- Yin, Shan
- Liu, Lihao
- Cai, Mengru
- Chai, Yutong
- Jiao, Yurong
- Duan, Zheng
- Li, Yian
- Huang, Shanguo
venue: Journal of Optical Communications and Networking
venue_type: journal
year: 2024
doi: 10.1364/JOCN.533206
url: https://www.scopus.com/pages/publications/85201072448?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 852--867
keywords:
- 5G mobile communication systems
- Blocking probability
- Cooperative communication
- Deep neural networks
- Fiber optic networks
- Mobile edge computing
- Multi agent systems
- Optical communication
- Resource allocation
- Communication overheads
- Communication resources
- Distributed inference
- Metro Optical Network
- Multi agent
- Network inference
- Performance
- Reinforcement learnings
- Resource allocation problem
- Single-agent
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1313 — DNN distributed inference offloading scheme based on transfer reinforcement learning in metro optical networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of 5G and mobile edge computing, deep neural network (DNN) inference can be distributed at the edge to reduce communication overhead and inference time, namely, DNN distributed inference. DNN distributed inference will pose challenges to the resource allocation problem in metro optical networks (MONs). Efficient cooperative allocation of optical communication and computational resources can facilitate high-bandwidth and low-latency applications. However, it also introduces greater complexity to the resource allocation problem. In this study, we propose a joint resource allocation method using high-performance transfer deep reinforcement learning (T-DRL) to maximize network throughput. When the topologies or characteristics of MONs change, T-DRL requires only a small amount of transfer training to re-converge. Considering that the generalizability of conventional methods is inversely related to optimization performance, we develop two deployment schemes (i.e., single-agent and multi-agent) based on the T-DRL method to explore the performance of T-DRL. Simulation results demonstrate that T-DRL greatly reduces the blocking probability and average inference time of DNN inference requests. Besides, the multi-agent scheme can maintain a lower blocking probability of requests in MONs, while the single-agent has a shorter convergence time after network changes.  © 2024 Optica Publishing Group.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1313.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
