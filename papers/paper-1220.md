---
id: paper-1220
title: 'Toward Optimal Resource Allocation: A Multi-Agent DRL Based Task Offloading Approach in Multi-UAV-Assisted MEC Networks'
authors:
- Tariq, Muhammad Naqqash
- Wang, Jingyu
- Raza, Salman
- Siraj, Mohammad
- Altamimi, Majid
- Memon, Saifullah
venue: IEEE Access
venue_type: journal
year: 2024
doi: 10.1109/ACCESS.2024.3411022
url: https://www.scopus.com/pages/publications/85195372501?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 81428--81440
keywords:
- DRL
- MEC
- resource allocation
- task offloading
- UAV
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

# paper-1220 — Toward Optimal Resource Allocation: A Multi-Agent DRL Based Task Offloading Approach in Multi-UAV-Assisted MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The application of UAV-aided MEC well-suited for the execution of the data-intensive and latency-sensitive tasks in the infrastructure-deprived regions. However, the growing number of UAVs and smart devices causing a major difficulty in the devising an effective scheme for the task offloading and resource allocation in multi-UAV-aided MEC networks. Furthermore, the resource deficient environments unable to sustain prolonged resource-intensive activities, additional complexities are posed on the optimum utilization of the resources. In this paper, we introduced a multi-agent deep reinforcement learning scheme for the task offloading in the multi-UAV-assisted networks (MUAVDRL). In this configuration, the mobile users fetch computational resources from the UAVs with the goal of minimizing the computation cost which incorporates both the energy consumption and the computation delay. Initially, we start with the optimization problem which is defined as the minimizing the computational costs. Through modelling it as MDP, we aim to reduce the computational costs for mobile users. Leveraging the dynamic and high-dimensional nature of the challenge, the MUAVDRL algorithm solves this problem efficiently. Comprehensive simulation results exhibit the efficacy and superiority of our projected framework when compared to existing state-of-the-art methods, illustrating its potential in the practice.  © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1220.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
