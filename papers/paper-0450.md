---
id: paper-0450
title: Revenue-Model Learning for a Slice Broker in the Presence of Adversaries
authors:
- Khan, Muhidul Islam
- Nencioni, Gianfranco
venue: International Symposium on Advanced Networks and Telecommunication Systems, ANTS
venue_type: conference
year: 2022
doi: 10.1109/ANTS56424.2022.10227783
url: https://www.scopus.com/pages/publications/85171778364?origin=resultslist
publisher: IEEE Computer Society
pages: 387--392
keywords:
- Network slicing
- Reinforcement learning
- Revenue model
- Slice broker
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0450 — Revenue-Model Learning for a Slice Broker in the Presence of Adversaries

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-Access Edge Computing (MEC) and network slicing two of the key enabling technologies of the Fifth Generation (5G) of cellular network. MEC helps to reduce latency, offload the cloud, and allow context-awareness. Network slicing allows to create heterogeneous services on top of shared infrastructures. Slice brokers are emerging intermediate entities that take the resources from the infrastructure providers and make slices for the tenants. In this scenario, a slice broker needs to manage the resource and create the slices in order to maximize its revenue to cover the cost and increase the profit. In this work, we consider that the demand of the slice tenant is depending on the price of the slices. Therefore, we formulate a slice allocation problem that consider this demand-price dynamic. Moreover, we consider the presence of adversary that want to compromise the decision process. In order to solve the problem, we propose a multi-agent environment, where some agents cooperate to learn the revenue model and maximize the revenue. Finally, we evaluate the effectiveness of the proposed solution by comparing it with reference solutions. The results highlight that a notable increment of the revenue can be obtained by using our solution. © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0450.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
