---
id: paper-2395
title: Energy-Efficient Computing Offloading With Trajectory Optimization and Resource Allocation in UAVs Aided Industrial IoT
authors:
- Yu, Zihang
- Zhang, Zhenjiang
- Zeadally, Sherali
- Shen, Bo
- Pei, Xintong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3582091
url: https://www.scopus.com/pages/publications/105010007900?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 34780--34792
keywords:
- Energy
- Industrial IoT (IIoT)
- Internet of Things (IoT)
- resource allocation
- task offloading
- uncrewed aerial vehicle (UAV) trajectories
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2395 — Energy-Efficient Computing Offloading With Trajectory Optimization and Resource Allocation in UAVs Aided Industrial IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, uncrewed aerial vehicle (UAV) assisted mobile-edge computing (MEC) has emerged as a novel paradigm for providing computing services to devices in the Industrial Internet of Things (IIoT) domain. However, due to the constraints of a single UAV’s battery and processing capabilities, it is unable to fulfill the computational and communication requirements of IIoT devices. We presents a multi-UAV-assisted IIoT system wherein computational services for IIoT devices are collaboratively provided by a terrestrial base station (BS) and UAVs. Considering the impact of energy consumption on the environment, we formulate a long-term weighted system energy consumption minimization problem by jointly optimizing UAVs trajectories, offloading and resource allocation decisions while considering the constraints of task deadlines. Due to the network dynamics and complexity of the optimization problem, we reformulate it as a Markov decision process (MDP) and apply a multiagent twin delayed deep deterministic policy gradient (MATD3) approach to solve the problem. The simulation results obtained show that our proposed MATD3-based method achieves 6% higher rewards and 30% faster convergence over previous algorithms, such as multiagent deep deterministic policy gradient and the proximal policy optimization. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2395.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
