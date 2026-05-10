---
id: paper-0338
title: Supporting Sustainable Virtual Network Mutations with Mystique
authors:
- Sacco, Alessio
- Flocco, Matteo
- Esposito, Flavio
- Marchetto, Guido
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2021
doi: 10.1109/TNSM.2021.3059647
url: https://www.scopus.com/pages/publications/85101242342?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2714--2727
keywords:
- auto-scaling
- network management
- reinforcement learning
- SDN
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0338 — Supporting Sustainable Virtual Network Mutations with Mystique

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The abiding attempt of automation has also permeated the networks, with the ability to measure, analyze, and control themselves in an automated manner, by reacting to changes in the environment (e.g., demand). When provided with these features, networks are often labeled as 'self-driving' or 'autonomous'. In this regard, the provision and orchestration of physical or virtual resources are crucial for both Quality of Service (QoS) guarantees and cost management in the edge/cloud computing environment. To effectively manage the lifecycle of these resources, an auto-scaling mechanism is essential. However, traditional threshold-based and recent Machine Learning (ML)-based policies are often unable to address the soaring complexity of networks due to their centralized approach. By relying on multi-agent reinforcement learning, we propose Mystique, a solution that learns from the load on links to establish the minimal set of active network resources. As traffic demands ebb and flow, our adaptive and self-driving solution can scale up and down and also react to failures in a fully automated, flexible, and efficient manner. Our results demonstrate that the presented solution can reduce network energy consumption while providing an adequate service level, outperforming other benchmark auto-scaling approaches. © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0338.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
