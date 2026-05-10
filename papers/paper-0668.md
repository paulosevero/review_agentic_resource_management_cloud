---
id: paper-0668
title: 'MOBILE EDGE COMPUTING ORIENTED MULTI-AGENT COOPERATIVE ROUTING ALGORITHM: A DRL-BASED APPROACH'
authors:
- Lv, Jianhui
- Zhao, Shen
- Yi, B.O.
- Li, Qing
venue: Fractals
venue_type: journal
year: 2023
doi: 10.1142/S0218348X23400996
url: https://www.scopus.com/pages/publications/85165182918?origin=resultslist
publisher: World Scientific
pages: ''
keywords:
- Cooperative Routing
- DRL
- MEC
- Multi-Agent
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0668 — MOBILE EDGE COMPUTING ORIENTED MULTI-AGENT COOPERATIVE ROUTING ALGORITHM: A DRL-BASED APPROACH

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the era of 5G/B5G, computing-intensive, delay-sensitive applications such as virtual reality inevitably bring huge amounts of data to the network. In order to meet the real-time requirements of applications, Mobile Edge Computing (MEC) pushes computing resources and data from the centralized cloud to the edge network, providing users with computing offload technology. However, the mismatch between the great computing requirements of computing-intensive tasks and the limited computing power of a single edge server poses a great challenge to computing offload technology. In this paper, a multi-agent cooperation mechanism for MEC and a routing mechanism based on deep reinforcement learning (DRL) are proposed. First of all, a multi-agent cooperation mechanism is proposed to realize the cooperative processing of computing-intensive and delay-sensitive applications, and the task unloading decision-making problem based on multi-agent cooperation is studied. Secondly, the cooperative processing of tasks by multi-agents involves data transmission. Considering the real-time requirements of tasks, this paper proposes an intelligent routing mechanism based on DRL to plan the optimal routing path. Finally, the simulation implementation and performance evaluation of the multi-agent cooperation mechanism and routing mechanism for MEC are carried out. The experimental results show that the intelligent routing mechanism based on DRL and graph neural network is superior to the comparison mechanism in terms of network average delay, throughput and maximum link bandwidth utilization. At the same time, the superiority of graph neural network in model generalization is verified on a new network topology National Science Foundation (NSF) Net. The results of route optimization are applied to the multi-agent cooperation mechanism, and the experimental results show that the mechanism is superior to the comparison scheme in terms of task success rate and average task response delay. The combination of these two mechanisms well solves the problem that it is difficult to deal with computing-intensive and delay-sensitive applications in mobile edge computing because of its limited resources.  © 2023 The Author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0668.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
