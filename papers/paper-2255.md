---
id: paper-2255
title: Delay- and Energy-Efficient Task Offloading in Cell Free Massive MIMO-Enabled Vehicular Fog Computing
authors:
- Wang, Shujuan
- Yang, Mulin
- Jiang, Yanxiang
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2025
doi: 10.1109/TWC.2025.3536486
url: https://www.scopus.com/pages/publications/85217695159?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3715--3730
keywords:
- CF-mMIMO
- LSTM
- MADDPG
- Task offloading
- VFC
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

# paper-2255 — Delay- and Energy-Efficient Task Offloading in Cell Free Massive MIMO-Enabled Vehicular Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task offloading is a promising approach to efficiently realize delay-sensitive, computation-intensive applications in Internet of Vehicles (IoVs). However, task allocation and scheduling pose great challenges in Vehicular Fog Computing (VFC) environment due to resource heterogeneity, workload unpredictability, fixed Fog Access Points (F-APs), and the dynamic nature of fog environment. This paper investigates the delay- and energy-efficient task offloading strategy in Cell Free massive MIMO (CF-mMIMO)-enabled VFC network. CF-mMIMO system is integrated into the VFC network so that task transfer among F-APs is enabled. A Long Short Term Memory (LSTM)-based algorithm is designed to predict the workload of F-APs. Based on the result, the delay and energy consumption of a task if it is offloaded on a F-AP can be calculated. After that, a Multi-Agent Deep Deterministic Policy Gradient (MADDPG)-based algorithm is developed to explore the best combination of task offloading and resource allocation strategies to reduce the overhead of each vehicle, and to minimize the long-term system cost, eventually. Simulation results show that the proposed strategy not only exhibits good convergence performance in scenario which involves a mixture of continuous-discrete action spaces, but also achieves satisfying performance in terms of average cost under varied circumstances. © 2002-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2255.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
