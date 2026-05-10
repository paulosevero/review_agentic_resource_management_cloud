---
id: paper-1122
title: 'Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism'
authors:
- Park, Yu Min
- Hassan, Sheikh Salman
- Tun, Yan Kyaw
- Han, Zhu
- Hong, Choong Seon
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2023.3311537
url: https://www.scopus.com/pages/publications/85171526953?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2003--2016
keywords:
- attention mechanism
- mobile-edge computing
- multi-agent proximal policy optimization
- resource allocation
- sub-terahertz communication
- Unmanned aerial vehicles (UAVs)
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

# paper-1122 — Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The use of Terahertz (THz) technology in sixth-generation (6G) networks will bring high-speed and capacity data services. But limitations like molecular absorption, rain attenuation, and limited coverage range cause communication losses. To overcome these losses and improve coverage in rural areas, a high number of base stations are required. Hence, an aerial communication platform, which uses line-of-sight (LoS) communication to avoid losses, is needed. To address this, we study the deployment and optimization of multi-access edge computing (MEC)-powered unmanned aerial vehicle (UAV) for sub-THz communication in remote areas. To this end, we solve an optimization problem to minimize energy consumption and delay for MEC-UAV and mobile users. The formulated problem is a mixed-integer non-linear programming (MINLP) problem. As the problem is an MINLP, we decompose the main problem into two subproblems. Due to its convex nature, we solve the first subproblem with a standard optimization solver, i.e., CVXPY. To solve the second subproblem, we design a resources-based multi-agent proximal policy optimization (RMAPPO) deep reinforcement learning (DRL) algorithm with an attention mechanism. The considered attention mechanism is utilized for encoding a diverse number of observations. This is designed by the network coordinator to provide a differentiated fit reward to each agent in the network. The simulation results show that the proposed algorithm outperforms the benchmark and yields a network utility that is 2.22%, 15.55%, and 17.77% more than the benchmarks.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1122.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
