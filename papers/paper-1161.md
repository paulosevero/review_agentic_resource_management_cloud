---
id: paper-1161
title: An Adaptive Energy Orchestrator for Cyberphysical Systems Using Multiagent Reinforcement Learning †
authors:
- Robles-Enciso, Alberto
- Robles-Enciso, Ricardo
- Skarmeta Gómez, Antonio F.
venue: Smart Cities
venue_type: journal
year: 2024
doi: 10.3390/smartcities7060125
url: https://www.scopus.com/pages/publications/85213437141?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: 3210--3240
keywords:
- cyber-physical system
- edge computing
- energy management
- Internet of Things
- reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1161 — An Adaptive Energy Orchestrator for Cyberphysical Systems Using Multiagent Reinforcement Learning †

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Highlights: What are the main findings? A proof of concept of a smart energy management system in a smart home. Using the reinforcement learning technique, we optimise energy use, avoiding non-renewable sources as much as possible and predicting the critical moments of lower energy production. Multiagent reinforcement learning individually manages each of the smart home services (lights, fridge, etc.) so that it is possible to dynamically switch off or shift the period of operation to different slots depending on the energy production. What is the implication of the main finding? The use of intelligent techniques tomanage the services of a smart home allows optimisation of energy use, exploiting peak times of possibly unused energy generation (e.g., PV solar) while minimising the use of non-renewable (petrol generator) or costly (grid peak time, batteries) energy sources. By dynamically determining an optimal schedule for smart home services by prioritising green energy sources, a reduction in carbon emissions is implicitly achieved, since less prioritised (carbon-based) energy sources are exceptionally used. Reducing carbon emissions is a critical issue for the near future as climate change is an imminent reality. To reduce our carbon footprint, society must change its habits and behaviours to optimise energy consumption, and the current progress in embedded systems and artificial intelligence has the potential to make this easier. The smart building concept and intelligent energy management are key points to increase the use of renewable sources of energy as opposed to fossil fuels. In addition, cyber-physical systems (CPSs) provide an abstraction of the management of services that allows the integration of both virtual and physical systems in a seamless control architecture. In this paper, we propose to use multiagent reinforcement learning (MARL) to model the CPS services control plane in a smart house, with the purpose of minimising, by shifting or shutdown services, the use of non-renewable energy (fuel generator) by exploiting solar production and batteries. Furthermore, our proposal dynamically adapts its behaviour in real time according to current and historic energy production, thus being able to handle occasional changes in energy production due to meteorological phenomena or unexpected energy consumption. In order to evaluate our proposal, we have developed an open-source smart building energy simulator and deployed our use case. Finally, several simulations with different configurations are evaluated to verify the performance. The simulation results show that the reinforcement learning solution outperformed the priority-based and the heuristic-based solutions in both power consumption and adaptability in all configurations. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1161.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
