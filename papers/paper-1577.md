---
id: paper-1577
title: Cooperative DNN Partitioning in Energy-Harvesting and MEC-Enabled AAV Networks
authors:
- Gao, Ke
- Du, Jun
- Jiang, Chunxiao
- Simonjan, Jennifer
- Mishra, Debashisha
- Zhang, Chao
- Debbah, Merouane
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3558162
url: https://www.scopus.com/pages/publications/105002256299?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 24329--24344
keywords:
- DNN partitioning
- edge offloading
- energy harvesting
- predictive Markov decision process (P-MDP)
- transformer-enhanced MHAPPO (TE-MHAPPO)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1577 — Cooperative DNN Partitioning in Energy-Harvesting and MEC-Enabled AAV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Autonomous aerial vehicles (AAVs) are critical in modern emergency response due to their high mobility. However, limited computing resources and energy supplies necessitate the use of AAV networks for collaborative inference. AAV intelligent tasks are often deep neural networks (DNN)-based, with DNN partitioning enabling collaborative inference. However, executing DNN partitioning in a highly dynamic AAV network faces two challenges that have not been addressed in existing research: the time gap between the state sampling and the execution of the corresponding action based on that state, and the unknown trajectories in advance. The time gap requires predictive action decision-making. To address this, we model DNN partitioning and edge offloading with hybrid action decisions in dynamic, energy-harvesting AAV networks as a predictive Markov decision process (P-MDP). The rapidly changing and previously unknown network topology significantly impacts channel and data transmission energy consumption, affecting DNN partitioning decisions. To better solve the action prediction problem, we use the Transformer module to extract motion features from recent time slots in the proposed Transformer-enhanced multiagent hybrid action proximal policy optimization (TE-MHAPPO) framework. Simulation results show that TE-MHAPPO reduces the reward which comprehensively considers task delay and energy consumption, by at least 12.1% compared to the state-of-the-art MHAPPO. Additionally, its reward performance degradation with the increase in prediction time is at most 55.2% of that observed in the baseline. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1577.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
