---
id: paper-0749
title: Multi-Agent Deep Reinforcement Learning based Collaborative Computation Offloading in Vehicular Edge Networks
authors:
- Wang, Hao
- Zhou, Huan
- Zhao, Liang
- Liu, Xuxun
- Leung, Victor C. M.
venue: Proceedings - 2023 IEEE 43rd International Conference on Distributed Computing Systems Workshops, ICDCSW 2023
venue_type: conference
year: 2023
doi: 10.1109/ICDCSW60045.2023.00027
url: https://www.scopus.com/pages/publications/85178512211?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 151--156
keywords:
- computation offloading
- deep deterministic policy gradient
- markov decision process
- multi-agent
- resource allocation
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

# paper-0749 — Multi-Agent Deep Reinforcement Learning based Collaborative Computation Offloading in Vehicular Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, to cope with the long communication distance and unreliability of cloud-based computing architectures, mobile edge computing has emerged as a solution with great promise. This pattern extends cloud-based services towards the vehicular edge network and enables vehicular tasks to be offloaded to intermediate Roadside Units (RSUs) directly. However, as more and more tasks are offloaded to RSUs, the computation capacity of a single RSU becomes insufficient. Without edge cooperation, overall resource utilization and effectiveness are prone to being underutilized. To address this issue, this paper investigates a collaborative computation offloading scheme where adjacent RSUs can process offloaded tasks collaboratively rather than individually. First, we explore a vehicular edge network where the bilateral synergy between RSUs is leveraged. In particular, we incorporate a price-based incentive mechanism into the resource allocation process to promote overall resource utilization. Second, considering the time-varying system conditions and uncertain resource requirements, the optimization problem is approximated as a Markov Decision Process (MDP) and extended to a multi-agent system. Finally, we propose a Multi-agent Deep deterministic policy gradient-based computation Offloading and resource Allocation scheme (MDOA) to solve the corresponding problem. Simulation results show that the proposed MDOA can not only achieve a higher long-term utility of RSUs but also have better performance than other baselines in different scenarios.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0749.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
