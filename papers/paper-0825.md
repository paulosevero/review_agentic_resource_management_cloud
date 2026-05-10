---
id: paper-0825
title: 'Dynamic and efficient resource allocation for 5G end-to-end network slicing: A multi-agent deep reinforcement learning approach'
authors:
- Asim Ejaz, Muhammad
- Wu, Guowei
- Iqbal, Tahir
venue: International Journal of Communication Systems
venue_type: journal
year: 2024
doi: 10.1002/dac.5916
url: https://www.scopus.com/pages/publications/85200025703?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- maximize profit
- mobile edge computing
- multi-agent algorithm
- network slicing
- online resource allocation
- secure admission control
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0825 — Dynamic and efficient resource allocation for 5G end-to-end network slicing: A multi-agent deep reinforcement learning approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid evolution of user equipment (UE) and 5G networks drives significant transformations, bringing technology closer to end-users. Managing resources in densely crowded areas such as airports, train stations, and bus terminals poses challenges due to diverse user demands. Integrating mobile edge computing (MEC) and network function virtualization (NFV) becomes vital when the service provider's (SP) primary goal is maximizing profitability while maintaining service level agreement (SLA). Considering these challenges, our study addresses an online resource allocation problem in an MEC network where computing resources are limited, and the SP aims to boost profit by securely admitting more UE requests at each time slot. Each UE request arrival rate is unknown, and the requirement is specific resources with minimum cost and delay. The optimization problem objective is achieved by allocating resources to requests at the MEC network in appropriate cloudlets, utilizing abandoned instances, reutilizing idle and soft slice instances to shorten delay and reduce costs, and immediately scaling inappropriate instances, thus minimizing the instantiation of new instances. This paper proposes a deep reinforcement learning (DRL) method for request prediction and resource allocation to mitigate unnecessary resource waste. Simulation results demonstrate that the proposed approach effectively accepts network slice requests to maximize profit by leveraging resource availability, reutilizing instantiated resources, and upholding goodwill and SLA. Through extensive simulations, we show that our proposed DRL-based approach outperforms other state-of-the-art techniques, namely, MaxSR, DQN, and DDPG, by 76%, 33%, and 23%, respectively. © 2024 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0825.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
