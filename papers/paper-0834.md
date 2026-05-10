---
id: paper-0834
title: Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints
authors:
- Ben Sada, Abdelkarim
- Khelloufi, Amar
- Naouri, Abdenacer
- Ning, Huansheng
- Aung, Nyothiri
- Dhelim, Sahraoui
venue: Electronics (Switzerland)
venue_type: journal
year: 2024
doi: 10.3390/electronics13132580
url: https://www.scopus.com/pages/publications/85198348261?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning
- edge AI
- Internet of Things
- task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0834 — Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The journey towards realizing real-time AI-driven IoT applications is facing a significant hurdle caused by the limited resources of IoT devices. Particularly for battery-powered edge devices, the decision between performing task inference locally or by offloading to edge servers, all while ensuring timely results and conserving energy, is a critical issue. This problem is further complicated when an edge device houses multiple local inference models. The challenge of effectively allocating inference models to tasks between local models and edge server models under strict time and energy constraints while maximizing overall accuracy is recognized as a strongly NP-hard problem and has not been addressed in the literature. Therefore, in this work we propose MASITO, a novel multi-agent deep reinforcement learning framework designed to address this intricate problem. By dividing the problem into two sub-problems namely task scheduling and edge server selection we propose a cooperative multi-agent system for addressing each sub-problem. MASITO’s design allows for faster training and more robust schedules using cooperative behavior where agents compensate for each other’s sub-optimal actions. Moreover, MASITO dynamically adapts to different network configurations which allows for high-mobility edge computing applications. Experiments on the ImageNet-mini dataset demonstrate the framework’s efficacy, outperforming genetic algorithms (GAs), simulated annealing (SA), and particle swarm optimization (PSO) in scheduling times by providing lower times ranging from 60% up to 90% while maintaining comparable average accuracy in worst-case scenarios and superior accuracy in best-case scenarios. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0834.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
