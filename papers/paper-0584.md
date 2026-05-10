---
id: paper-0584
title: A Joint Trajectory and Computation Offloading Scheme for UAV-MEC Networks via Multi-Agent Deep Reinforcement Learning
authors:
- Du, Xinyang
- Li, Xuanheng
- Zhao, Nan
- Wang, Xianbin
venue: IEEE International Conference on Communications
venue_type: conference
year: 2023
doi: 10.1109/ICC45041.2023.10278822
url: https://www.scopus.com/pages/publications/85178274320?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5438--5443
keywords:
- computation offloading
- deep reinforcement learning
- mobile edge computing
- trajectory design
- Unmanned aerial vehicle
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

# paper-0584 — A Joint Trajectory and Computation Offloading Scheme for UAV-MEC Networks via Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicle (UAV)-assisted mobile edge computing (MEC) has emerged as a promising solution to support the computation-intensive tasks in the Internet of Things (IoT) networks. As for the operation of UAV-assisted MEC, jointly design of the UAV trajectory control and computation offloading strategies becomes the key for achieving high offloading efficiency, which is extremely challenging due to the uncertain and dynamic demands in the network. In this paper, aiming at maximizing the offloading task amount, we propose an Multi-Agent joint TrAjectory and Computation Offloading (MA-TACO) scheme, where all related factors including task type variety, quality of service (QoS) guarantee, and service fairness are taken into account. To facilitate each UAV to obtain the best joint strategy under dynamic network environment, considering the complex decisions with both continuous and discrete variables, we develop an Optimization-oriented Multi-Agent Deep Reinforcement Learning approach (OMADRL), where each UAV could autonomously learn the trajectory decision to adapt to the dynamic demands, and the offloading decision would be made by solving a mixed-integer programming problem based on the observations, which would be utilized to guide the trajectory learning. Comparing with solely relying on learning, such an optimization-oriented way could reduce the action space dimension and make each UAV achieve the best strategy faster. The simulation results indicate the effectiveness of the proposed scheme.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0584.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
