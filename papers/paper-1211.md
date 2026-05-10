---
id: paper-1211
title: 'Intelligent Vehicle Computation Offloading in Vehicular Ad Hoc Networks: A Multi-Agent LSTM Approach with Deep Reinforcement Learning'
authors:
- Sun, Dingmi
- Chen, Yimin
- Li, Hao
venue: Mathematics
venue_type: journal
year: 2024
doi: 10.3390/math12030424
url: https://www.scopus.com/pages/publications/85184705380?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- computation offloading
- deep reinforcement learning
- edge computing
- resource allocation
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

# paper-1211 — Intelligent Vehicle Computation Offloading in Vehicular Ad Hoc Networks: A Multi-Agent LSTM Approach with Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As distributed computing evolves, edge computing has become increasingly important. It decentralizes resources like computation, storage, and bandwidth, making them more accessible to users, particularly in dynamic Telematics environments. However, these environments are marked by high levels of dynamic uncertainty due to frequent changes in vehicle location, network status, and edge server workload. This complexity poses substantial challenges in rapidly and accurately handling computation offloading, resource allocation, and delivering low-latency services in such a variable environment. To address these challenges, this paper introduces a “Cloud–Edge–End” collaborative model for Telematics edge computing. Building upon this model, we develop a novel distributed service offloading method, LSTM Muti-Agent Deep Reinforcement Learning (L-MADRL), which integrates deep learning with deep reinforcement learning. This method includes a predictive model capable of forecasting the future demands on intelligent vehicles and edge servers. Furthermore, we conceptualize the computational offloading problem as a Markov decision process and employ the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) approach for autonomous, distributed offloading decision-making. Our empirical results demonstrate that the L-MADRL algorithm substantially reduces service latency and energy consumption by 5–20%, compared to existing algorithms, while also maintaining a balanced load across edge servers in diverse Telematics edge computing scenarios. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1211.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
