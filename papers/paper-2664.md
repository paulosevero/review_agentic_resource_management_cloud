---
id: paper-2664
title: 'Joint energy and computing scheduling for multi-energy microgrid: A hierarchical federated multiagent dueling deep Q-network approach'
authors:
- Li, Haitao
- Xie, Dongxue
- Yang, Yanhong
venue: Sustainable Energy, Grids and Networks
venue_type: journal
year: 2026
doi: 10.1016/j.segan.2026.102149
url: https://www.scopus.com/pages/publications/105030934126?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Dueling deep Q-network
- Energy management
- Hierarchical federated learning
- Joint energy and computing scheduling
- Multi-energy microgrid
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

# paper-2664 — Joint energy and computing scheduling for multi-energy microgrid: A hierarchical federated multiagent dueling deep Q-network approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-energy microgrid (MEMG), which consists of solar photovoltaic, wind power generation, battery energy storage and hydrogen energy storage, is considered as a critical technology to promote carbon neutrality and achieve sustainable development of modern power system, but it faces challenges in dispatching multiple resources to minimize the operating cost of the edge computing enabled MEMG with source-grid-load-storage-computing coordination. In this article, a joint energy and computing scheduling strategy is investigated for the MEMG system. Firstly, a MEMG model with energy-computing-carbon trading is introduced, and the corresponding Markov decision process (MDP) problem to facilitate joint scheduling is built. Subsequently, an improved dueling deep Q-network (iDDQN) algorithm is incorporated into the federated learning framework to propose a hierarchical federated multiagent iDDQN with model compression (HFc-MAiDDQN). Then joint energy and computing scheduling strategy based on the HFc-MAiDDQN algorithm is developed to resolve the MDP problem. Finally, simulation results demonstrate that the proposed joint resource scheduling strategy can greatly reduce the long-term operating cost of the MEMG by approximately 10 %, while promoting lower carbon emission and protecting data privacy. © 2026 Elsevier Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2664.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
