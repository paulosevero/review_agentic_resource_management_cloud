---
id: paper-1672
title: Reinforcement Learning-Based Latency Minimization for Vehicular Edge Computing Networks
authors:
- Huang, Qilin
- Liu, Jinyu
venue: 2025 5th International Conference on Intelligent Communications and Computing, ICICC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICICC66840.2025.11199477
url: https://www.scopus.com/pages/publications/105021595775?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 137--142
keywords:
- Markov game
- multiagent deep reinforcement learning
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

# paper-1672 — Reinforcement Learning-Based Latency Minimization for Vehicular Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Pushing computing functions to network edges can save backhaul network bandwidth and meet diverse latency requirements, thus supporting computation-intensive and delaysensitive tasks. However, challenges such as unstable network conditions, vehicle mobility, and strict latency requirements make it crucial to decide on local task provision. This paper focuses on the cloud-edge latency optimization problem (LOP) based on task offloading and resource allocation in the vehicle edge network, taking into account vehicle mobility, time-varying channels, and signal blocking. First, the LOP is formulated as a mixed-integer nonlinear programming (MINLP) model. We reformulate this challenging optimization problem as a Markov game and incorporate a unique delay task dropout penalty mechanism to efficiently tackle this challenging optimization problem. This mechanism effectively reduces the negative impacts of latency on task execution and system performance. Then, we design an intelligent decision-making algorithm based on a multiagent deep deterministic policy gradient. The proposed algorithm doesn't require prior knowledge of uncertain parameters and works without relying on dynamic models. Extensive simulation tests show that our proposed algorithm converges quickly and enhances system performance more effectively than the three alternative solutions. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1672.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
