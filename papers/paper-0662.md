---
id: paper-0662
title: Human-Centric Resource Allocation for the Metaverse With Multiaccess Edge Computing
authors:
- Long, Zijian
- Dong, Haiwei
- Saddik, Abdulmotaleb El
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3283335
url: https://www.scopus.com/pages/publications/85161559304?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19993--20005
keywords:
- Attention mechanism
- extended reality (XR)
- graph convolutional network
- multiagent reinforcement learning
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

# paper-0662 — Human-Centric Resource Allocation for the Metaverse With Multiaccess Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multiaccess edge computing (MEC) is a promising solution to the computation-intensive, low-latency rendering tasks of the metaverse. However, how to optimally allocate limited communication and computation resources at the edge to a large number of users in the metaverse is quite challenging. In this article, we propose an adaptive edge resource allocation method based on multiagent soft actor-critic with graph convolutional networks (SAC-GCN). Specifically, SAC-GCN models the multiuser metaverse environment as a graph where each agent is denoted by a node. Each agent learns the interplay between agents by graph convolutional networks with a self-attention mechanism to further determine the resource usage for one user in the metaverse. The effectiveness of SAC-GCN is demonstrated through the analysis of user experience, balance of resource allocation, and resource utilization rate by taking a virtual city park metaverse as an example. Experimental results indicate that SAC-GCN outperforms other resource allocation methods in improving overall user experience, balancing resource allocation, and increasing resource utilization rate by at least 27%, 11%, and 8%, respectively.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0662.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
