---
id: paper-0966
title: Multi-Device Edge Computing Offload Method in Hybrid Action Space; [混合动作空间下的多设备边缘计算卸载方法]
authors:
- Ji, Zhang
- Guoliang, Qi
- Chunhong, Duo
- Wenwen, Gong
venue: Computer Engineering and Applications
venue_type: journal
year: 2024
doi: 10.3778/j.issn.1002-8331.2304-0194
url: https://www.scopus.com/pages/publications/105007344161?origin=resultslist
publisher: Journal of Computer Engineering and Applications Beijing Co., Ltd.; Science Press
pages: 301--310
keywords:
- hybrid action space
- Internet of things (IoT)
- mobile edge computing
- multi-agent deep determination policy gradient (MADDPG)
language: Chinese
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0966 — Multi-Device Edge Computing Offload Method in Hybrid Action Space; [混合动作空间下的多设备边缘计算卸载方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In order to reduce the total cost of device-level in multi-device multi-edge server scenarios and solve the algorithm limitation of existing deep reinforcement learning (DRL) that only supports a single action space, a hybrid-based multi-agent deep determination policy gradient (H-MADDPG) is proposed. Firstly, the MEC system model is established by considering various complex environmental conditions, such as the dynamic change of computing power of IoT devices/ servers with load, time-varying wireless transmission channel gain, unknown energy harvesting, and the uncertainty of task size. Then, the problem model is established with the minimum total cost of integrated delay and energy consumption in a continuous time slot as the optimization objective. Finally, the problem is delivered to H-MADDPG in the form of Markov decision process (MDP), which trains two parallel policy networks with the assistance of the value network, and outputs discrete server selection and continuous task offload rate. The experimental results show that the H-MADDPG method has good convergence and stability. From different perspectives, such as whether the computing tasks are intensive or delay sensitive, the overall system return of H-MADDPG is better than Local, OffLoad and DDPG. Compared with other methods, it can maintain greater system throughput under the demand of computationally intensive tasks. © 2024 Journal of Computer Engineering and Applications Beijing Co., Ltd.; Science Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0966.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
