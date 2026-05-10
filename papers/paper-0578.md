---
id: paper-0578
title: Optimization of Cloud Datacenters’ Benefit Using Monte Carlo Algorithm
authors:
- Darshi, Razieh
- Shamaghdari, Saeed
- Nasiri, Ali Akbar
venue: Lecture Notes in Electrical Engineering
venue_type: conference
year: 2023
doi: 10.1007/978-981-99-0416-7_47
url: https://www.scopus.com/pages/publications/85161410113?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 472--479
keywords:
- Cloud datacenter
- Monte Carlo
- Optimization
- Renewable energy
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0578 — Optimization of Cloud Datacenters’ Benefit Using Monte Carlo Algorithm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data centers are very rapid growing structures with outstanding contribution to the world’s energy generation and consumption. The use of renewable energy sources to supply power has received much attention due to their many environmental benefits. However due to the variable nature of the output power of renewable energy sources, providing reliable and stable power for the data center faces many challenges. Therefore, in this paper, an intelligent energy scheduling approach for providing reliable power for datacenters using renewable energy resources is proposed. The purpose of the proposed intelligent algorithm is to minimize datacenters’ expenses and to maximize the benefit of all renewable and non-renewable energy resources and the battery energy storage system. To manage the load demand of the datacenter and all the distributed energy resources optimally, the multi-agent hour-ahead energy scheduling problem is modeled as a finite Markov decision process (MDP). The entities of the grid comprising datacenters and power resources are considered as intelligent agents. The scheduling decisions of the agents are obtained through the newly developed framework of the model-free reinforcement algorithm to compute an optimal policy. Based on the observation of the system using a non-optimal policy, the optimal policy is achieved. Finally, the performance of the proposed algorithm is verified using real power-grid data. Moreover, the simulation results indicate the presented framework can significantly improve the benefit of the cloud data center and can be applied in real-time. © 2023, The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0578.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
