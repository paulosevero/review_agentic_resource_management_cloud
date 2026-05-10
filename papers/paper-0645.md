---
id: paper-0645
title: Heuristically Assisted Multiagent RL-Based Framework for Computation Offloading and Resource Allocation of Mobile-Edge Computing
authors:
- Li, Xulong
- Qin, Yunhui
- Huo, Jiahao
- Huangfu, Wei
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3264253
url: https://www.scopus.com/pages/publications/85153333218?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15477--15487
keywords:
- Computational offloading
- heuristic algorithm
- mobile-edge computing (MEC)
- reinforcement learning (RL)
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

# paper-0645 — Heuristically Assisted Multiagent RL-Based Framework for Computation Offloading and Resource Allocation of Mobile-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile-edge computing (MEC) as a promising technology enables it to satisfy ever-increasing demands for low-latency and ultrareliable services. However, due to the limitations of computing capability and the dynamic network environment, it is challenging to process massive data with low latency. In this article, we consider a dynamic MEC network with a high-performance edge server, multiple time-varying channels, and multiple mobile devices. We aim to find a policy that can maximize the processing success rate of computational tasks and the fairness index of the system while minimizing the process delays. To this end, we propose a heuristic-assisted multiagent reinforcement learning (RL)-based framework to realize the joint optimization of computation offloading and resource allocation. On the one hand, heuristic search is introduced in this framework to find a better resource allocation policy in edge servers and further assist the multiagent RL algorithm to determine offloading policy in mobile devices. On the other hand, a novel parameterized multiagent RL algorithm based on soft actor-critic (SAC) is also proposed to broaden the effectiveness and availability of the proposed framework. Simulation results of the average cumulative reward, success rate, processing delay, and fairness index fully verify the superiority of the proposed framework and algorithm for supporting this problem.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0645.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
