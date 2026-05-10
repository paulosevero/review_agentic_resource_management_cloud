---
id: paper-2365
title: Diffusion-Based Multi-Agent Reinforcement Learning for Semantic Vehicular Edge Computing
authors:
- Yang, Yi
- Ma, Wenqiang
- Sun, Wen
- He, Jianhua
- Fu, Yaru
- Yuen, Chau
- Zhang, Yan
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2025
doi: 10.1109/TSC.2025.3618082
url: https://www.scopus.com/pages/publications/105018091288?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3668--3681
keywords:
- deep reinforcement learning
- diffusion model
- resource allocation
- semantic communication
- task offloading
- Vehicular edge computing (VEC)
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

# paper-2365 — Diffusion-Based Multi-Agent Reinforcement Learning for Semantic Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is critical for the safe and efficient driving of intelligent vehicles, by which they can offload computation-intensive tasks (such as driving environment perception) to edge servers to overcome the limitations of onboard computational resources and cooperate with others. One of the major challenges faced by VEC is that the offloaded intelligent driving tasks generally generate large amounts of data, which can easily stretch and congest the vehicle communication channels. To address the above challenges, we first propose a novel semantic VEC (SVEC) architecture, which can extract the semantic information of tasks and offload them to edge servers, thereby achieving reliable and efficient offloaded task communication and computation adaptively. Considering the scarce channel resources of vehicles and the intelligent tasks with different priorities and modalities, we define a novel user utility model for SVEC and transform the problem of maximizing user utility into a joint optimization problem of semantic feature extraction, task offloading and resource allocation. Furthermore, to cope with the complexity of the solution space of the optimization problem, we propose a diffusion-based multi-agent reinforcement learning algorithm, which improves the ability of agents to explore the solution space through the diffusion process, thereby achieving optimal decisions for semantic feature extraction, task offloading and resource allocation. Simulation results show that the proposed scheme improves the overall performance of SVEC while reducing offload latency and average system cost.  © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2365.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
