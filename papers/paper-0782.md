---
id: paper-0782
title: An Energy Saving Control Strategy Based on Multi-Agent Q-Learning Algorithm for Data Center
authors:
- Yu, Hui
- Xia, Ying
venue: 'Journal of Physics: Conference Series'
venue_type: conference
year: 2023
doi: 10.1088/1742-6596/2517/1/012018
url: https://www.scopus.com/pages/publications/85164934048?origin=resultslist
publisher: Institute of Physics
pages: ''
keywords:
- Customer satisfaction
- Energy conservation
- Energy utilization
- Learning algorithms
- Multi agent systems
- Optimal systems
- Quality of service
- Reinforcement learning
- Software agents
- Control strategies
- Datacenter
- Energy supplies
- Energy-consumption
- Energy-saving control
- Green renewable energy
- Multi-agent Q-learning
- Q-learning algorithms
- Renewable energies
- Total energy
- Scheduling algorithms
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0782 — An Energy Saving Control Strategy Based on Multi-Agent Q-Learning Algorithm for Data Center

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, the application of green renewable energy to data centers has become an important trend. Traditional solutions lack the consideration of matching tasks to renewable energy supplies. Therefore, in the face of diverse real-time computing tasks, how to reduce the total energy cost while ensuring the quality of service is an important challenge for the data center in the future. In this paper, our focus is on using the information on renewable energy supply and task characteristics as input states to assign tasks that maximize user satisfaction while meeting the minimum total cost of energy consumption. We consider the diversity of real-time tasks and design three different task types: the most crucial task, the crucial task and the non-crucial task. According to the different characteristics of these tasks, we propose a scheduling algorithm based on multi-agent, which uses multiple sets of agents with different initial positions to parallel search in different dimensions of the parameter space to find the optimal solution. To further optimize the algorithm, we eliminate the centralized noise solution based on the Pareto sorting method and sort the multiple optimal solutions to highlight the most suitable solution. The experimental results show that the proposed algorithm compared with other algorithms can reduce the total energy consumption by 11% and increase the customer satisfaction by 13% on average, and has better performance and applicability. © Published under licence by IOP Publishing Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0782.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
