---
id: paper-0189
title: Adaptive Data Sharing and Computation Offloading in Cloud-Edge Computing with Resource Constraints
authors:
- Chu, Wenjie
- Zhao, Haiyan
- Jin, Zhi
- Hu, Zhenjiang
venue: Conference Proceedings - IEEE International Conference on Systems, Man and Cybernetics
venue_type: conference
year: 2020
doi: 10.1109/SMC42975.2020.9283207
url: https://www.scopus.com/pages/publications/85098872719?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2842--2849
keywords:
- Adaptive Data Sharing
- Cloud-Edge Computing
- Collaborative Planning
- Computation Offloading
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0189 — Adaptive Data Sharing and Computation Offloading in Cloud-Edge Computing with Resource Constraints

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Collaborative tasks require the participation of multiple agents. Each agent in collaboration needs sufficient data to make optimal decisions. However, in general, each agent can only collect and process a limited amount of data due to resource constraints. Peer-to-peer data sharing can enrich local observations, but a particular agent may not have enough resources to adequately store and process data, thus compromising group decision making. Cloud-Edge Computing (CEC) can relieve agents of these limitations by providing them with further storage and computing resources through connected cloud-like infrastructures. However, CEC-based collaborations currently face two key challenges: 1) lack of adaptability to resource restrictions in data sharing; 2) no support of offloading non-trivial tasks with complex data dependencies. This paper proposes an approach to realize adaptive data sharing and support computation offloading. Roughly speaking, the paired parameterized-structure is designed based on data flow analysis and bidirectional transformations to benefit adaptive data synchronization and offloading. And a hybrid offloading mechanism is offered for allocating computations among agents and the cloud, regarding data dependencies and restrictions. We demonstrate the feasibility and flexibility through a collaborative victim search and rescue case. Experiments show that our approach outperforms state-of-the-art methods. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0189.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
