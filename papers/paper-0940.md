---
id: paper-0940
title: 'MADRLOM: A Computation offloading mechanism for software-defined cloud-edge computing power network'
authors:
- Guo, Yinzhi
- Xu, Xiaolong
- Xiao, Fu
venue: Computer Networks
venue_type: journal
year: 2024
doi: 10.1016/j.comnet.2024.110352
url: https://www.scopus.com/pages/publications/85189521391?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Computing power network
- Deep reinforcement learning
- Software-defined networking
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

# paper-0940 — MADRLOM: A Computation offloading mechanism for software-defined cloud-edge computing power network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-edge computing power network often exhibits complex and heterogeneous structures, posing several challenges to computation offloading that significantly impact network performance and the efficient utilization of computation resources. In this paper, we propose a cloud-edge computing power network architecture that efficiently integrates cloud and edge computing resources into a single network system using software-defined networking technology to support upper-layer business applications. In this context, existing computation offloading methods struggle with issues like users' personalized requirements for latency and energy consumption, as well as the inability to adapt to dynamically complex environments. To overcome these challenges, we introduce a computation offloading mechanism, MADRLOM, focusing on the network's heterogeneity and modeling the computation offloading problem at the cloud-edge end. We formalize the offloading problem as a Markov process and employ a multi-agent deep reinforcement learning algorithm based on priority experience replay sampling to address the planning problem of computation offloading, allowing user equipment to continuously optimize offloading strategies in response to environmental changes and achieve rational resource allocation. Through dynamic offloading strategies, computation tasks can be intelligently allocated to appropriate computing nodes, thereby achieving optimal resource utilization. We utilized the Mininet simulation platform to construct the experimental environment for the software-defined cloud-edge computing power network and compared it with several representative computation offloading strategies. The experimental results demonstrate that the MADRLOM significantly reduces the total system overhead in the software-defined cloud-edge computing network and shows excellent adaptability to environmental changes. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0940.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
