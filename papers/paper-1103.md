---
id: paper-1103
title: A Task Offloading Optimization Scheme Combining V2I and V2V
authors:
- Ni, Sujie
- Chen, Bing
- Shi, You
venue: Jisuanji Gongcheng/Computer Engineering
venue_type: journal
year: 2024
doi: 10.19678/j.issn.1000-3428.0068415
url: https://www.scopus.com/pages/publications/85216314206?origin=resultslist
publisher: Editorial Office of Computer Engineering
pages: 174--183
keywords:
- multi-agent deep reinforcement learning
- task division
- task offloading
- V2I and V2V joint offloading
- vehicle edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1103 — A Task Offloading Optimization Scheme Combining V2I and V2V

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In vehicle edge computing systems, individual vehicles frequently encounter difficulties in executing computation-intensive tasks due to their constrained processing capacities. Furthermore, the highly dynamic nature of the Internet of Vehicles (IoV) environment exacerbates the challenge, as vehicles struggle to gather comprehensive global information about their surroundings and the task offloading behaviors of neighboring vehicles. This complexity hampers effective decision-making in task offloading. To mitigate these challenges—limited computational resources, fluctuating environmental conditions, and restricted observational capabilities—this study introduces an online algorithm based on the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) framework. The proposed approach synergistically integrates both Vehicle-to-Infrastructure (V2I) and Vehicle-to-Vehicle (V2V) offloading mechanisms while also incorporating task division to optimize overall system performance. First, by considering vehicle location, connection duration, and available computational resources, the vehicle with the highest service performance value is selected as the candidate service vehicle. Second, an optimization problem is formulated to minimize the system's average task offloading delay, and this problem is modeled as a Markov decision process. Through centralized training, vehicles are able to obtain information from other vehicles, enabling them to adjust their own policies accordingly. In the online execution phase, vehicles can make rapid task offloading decisions based on local observations. Finally, the proposed algorithm is compared against benchmark algorithms. The experimental results demonstrate that, compared to the deep deterministic policy gradient method and the equal task division method, the proposed task offloading algorithm reduces the average task offloading delay by 75% and 66%, respectively, and exhibits a faster convergence rate, validating the algorithm's effectiveness. © 2024, Editorial Office of Computer Engineering. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1103.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
