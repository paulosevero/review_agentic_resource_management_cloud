---
id: paper-1012
title: 'Computation Offloading and Trajectory Planning of Multi-UAV-Enabled MEC: A Knowledge-Assisted Multiagent Reinforcement Learning Approach'
authors:
- Li, Xulong
- Qin, Yunhui
- Huo, Jiahao
- Huangfu, Wei
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2023.3338612
url: https://www.scopus.com/pages/publications/85179796925?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7077--7088
keywords:
- computation offloading
- Mobile edge computing (MEC)
- multi-agent reinforcement learning (MARL)
- trajectory planning
- unmanned aerial vehicle (UAV)
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

# paper-1012 — Computation Offloading and Trajectory Planning of Multi-UAV-Enabled MEC: A Knowledge-Assisted Multiagent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Compared with centralized cloud computing, mobile edge computing (MEC) enables Internet of Things (IoT) devices to offload computation-intensive tasks to the edge of the network closer to them for processing, which can effectively save energy consumption of IoT devices and alleviate network congestion and high latency problems. However, the traditional terrestrial MEC system cannot adapt to scenarios such as rapid network recovery after disasters and emergency rescue due to its poor flexibility and high deployment cost, and assembling edge servers to unmanned aerial vehicles (UAVs) to assist in rapidly building mobile edge networks is a feasible solution. Therefore, this paper considers a multi-UAV-enabled MEC network with the optimization objectives of maximizing the processing success rate of computational tasks and fairness of system, while minimizing the processing delay of computational tasks. We investigate the computation offloading problem and the trajectory planning problem from the perspectives of IoT devices and UAVs, respectively. Then model them as Markov decision processes (MDPs) and propose a joint optimization scheme based on expert knowledge-assisted multi-agent reinforcement learning algorithms. Simulation results show that the proposed algorithm has significant advantages over baseline algorithms in terms of processing success rate and delay of computational tasks as well as fairness of the system. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1012.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
