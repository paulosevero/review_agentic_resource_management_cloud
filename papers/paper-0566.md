---
id: paper-0566
title: An O-MAPPO scheme for joint computation offloading and resources allocation in UAV assisted MEC systems
authors:
- Cheng, Ming
- Zhu, Canlin
- Lin, Min
- Wang, Jun-Bo
- Zhu, Wei-Ping
venue: Computer Communications
venue_type: journal
year: 2023
doi: 10.1016/j.comcom.2023.06.008
url: https://www.scopus.com/pages/publications/85163183886?origin=resultslist
publisher: Elsevier B.V.
pages: 190--199
keywords:
- Energy efficiency
- Mobile edge computing
- Online multi-agent proximal policy optimization (O-MAPPO)
- Unmanned aerial vehicle
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0566 — An O-MAPPO scheme for joint computation offloading and resources allocation in UAV assisted MEC systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The combination of mobile edge computing (MEC) systems with unmanned aerial vehicle (UAV) has gained a high profile in recent years due to its high flexibility and ability to handle intensive tasks. The computation offloading strategy and the resource allocation scheme affect the system performance significantly. Moreover, the system complexity increases with the numbers of users and servers exponentially. It is challenging to consider jointly the computation offloading and the resource allocation in MEC systems that have multiple users and multiple servers. This paper formulates the joint resources management in the UAV assisted MEC network as a partially observable markov decision process and proposes an online multi-agent proximal policy optimization (O-MAPPO) scheme to improve the energy efficiency while guaranteeing the requirements in task, power consumption, computation, and time. Specifically, users and servers are set as agents. All agents cooperatively make decisions of computation offloading and resource allocation to maximize the energy efficiency. Simulation results show that the O-MAPPO scheme significantly outperforms benchmark algorithms in robustness and stability. © 2023 Elsevier B.V.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0566.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
