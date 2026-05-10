---
id: paper-0380
title: Multi-Agent Reinforcement Learning for Network Selection and Resource Allocation in Heterogeneous Multi-RAT Networks
authors:
- Allahham, Mhd Saria
- Abdellatif, Alaa Awad
- Mhaisen, Naram
- Mohamed, Amr
- Erbad, Aiman
- Guizani, Mohsen
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2022
doi: 10.1109/TCCN.2022.3155727
url: https://www.scopus.com/pages/publications/85125734785?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1287--1300
keywords:
- deep reinforcement learning
- edge computing
- Heterogeneous networks
- multi-RAT architecture
- wireless healthcare systems
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

# paper-0380 — Multi-Agent Reinforcement Learning for Network Selection and Resource Allocation in Heterogeneous Multi-RAT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid production of mobile devices along with the wireless applications boom is continuing to evolve daily. This motivates the exploitation of wireless spectrum using multiple Radio Access Technologies (multi-RAT) and developing innovative network selection techniques to cope with such intensive demand while improving Quality of Service (QoS). Thus, we propose a distributed framework for dynamic network selection at the edge level, and resource allocation at the Radio Access Network (RAN) level, while taking into consideration diverse applications' characteristics. In particular, our framework employs a deep Multi-Agent Reinforcement Learning (DMARL) algorithm, that aims to maximize the edge nodes' quality of experience while extending the battery lifetime of the nodes and leveraging adaptive compression schemes. Indeed, our framework enables data transfer from the network's edge nodes, with multi-RAT capabilities, to the cloud in a cost and energy-efficient manner, while maintaining QoS requirements of different supported applications. Our results depict that our solution outperforms state-of-the-art techniques of network selection in terms of energy consumption, latency, and cost.  © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0380.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
