---
id: paper-0590
title: Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing
authors:
- Gao, Zhen
- Yang, Lei
- Dai, Yu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2022.3228246
url: https://www.scopus.com/pages/publications/85144761162?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6818--6835
keywords:
- Mobile-edge computing (MEC)
- multiagent reinforcement learning (MARL)
- task offloading
- vehicular fog computing (VFC)
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

# paper-0590 — Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In vehicular fog computing, task offloading enables mobile vehicles (MVs) to offer ultralow latency services for computation-intensive tasks. Nevertheless, the edge server (ES) may have a high load when a large number of MVs offload their tasks to it, causing many tasks either experience long processing times or being dropped, particularly for latency-sensitive tasks. Moreover, most existing methods are largely limited to training a model from scratch for new environments. This is because they focus more on model structures with fixed input and output sizes, impeding the transfer of trained models across different environments. To solve these problems, we propose a decentralized task offloading method based on transformer and policy decoupling-based multiagent actor-critic (TPDMAAC). We first introduce a transformer-based long sequence forecasting network (TLSFN) for predicting the current and future queuing delay of ESs to solve uncertain load. Second, we redesign the actor-network using transformer-based temporal feature extraction network (TTFEN) and policy decoupling network (PDN). TTFEN can adapt to various input sizes through a transformer that accepts different tokens we build from the raw input. PDN provides a mapping between the transformer-based embedding features and offloading policies utilizing self-attention mechanism to address various output dimensions. Finally, the experiments on two real-world data sets show that TPDMAAC can quickly adapt to a new environment. And compared to existing algorithms, TPDMAAC reduces the system cost by 11.01%-12.03% as well as improves task completion rates by 10.45%-13.56%.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0590.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
