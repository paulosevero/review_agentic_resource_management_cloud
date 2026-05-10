---
id: paper-1671
title: Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence
authors:
- Huang, Hebin
- Liang, Junbin
- Min, Geyong
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3586793
url: https://www.scopus.com/pages/publications/105010316243?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12726--12741
keywords:
- DNN inference
- Edge intelligence
- mobile edge computing
- reinforcement learning
- service deployment
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1671 — Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge intelligence is an emerging paradigm in edge computing that deploys Deep Neural Network (DNN) models on edge servers with limited storage and computation capacities to provide inference services for high mobility and real-time applications, such as autonomous driving or smart surveillance, with varying accuracy and delay requirements. Adapting application configurations (e.g., image resolution or video frame rate) while selecting different DNN models and deployment locations can provide high-accuracy, low-delay inference services that meet user requirements. However, the configurations and DNN models of various inference services are highly heterogeneous. As balancing inference accuracy, resource cost, and delay is a multi-objective programming problem, it is a great challenge to obtain the optimal solution. To address this challenge, we propose a novel online framework to jointly optimize the configuration adaption, DNN model selection, and deployment for heterogeneous inference services. Specifically, we first formulate this joint optimization problem as an integer linear programming problem and prove it is NP-hard. Then, we further model the problem as a Partial Observable Markov Decision Process (POMDP) and solve it by developing a Heterogeneous-Agent Reinforcement Learning (HARL) based algorithm, named Heterogeneous Inference Service ProvidER (HISPER). It allows agents to have different action spaces corresponding to different types of configurations and DNN models. Finally, extensive experiments demonstrate that the proposed algorithm outperforms other state-of-the-art counterparts. © 2002-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1671.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
