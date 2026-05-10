---
id: paper-2609
title: Joint Resource Allocation and Task Offloading for Heterogeneous Cloud-Edge-End Networks Assisted by NOMA
authors:
- Hu, Xiaoxuan
- Shan, Liang
- Hua, Jialin
- Qi, Jin
- Dong, Zhenjiang
- Xu, Bin
- Sun, Yanfei
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TGCN.2026.3653056
url: https://www.scopus.com/pages/publications/105027979655?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1765--1778
keywords:
- Cloud-edge-end
- digital twin
- MADDPG
- NOMA
- resource allocation
- task offloading
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

# paper-2609 — Joint Resource Allocation and Task Offloading for Heterogeneous Cloud-Edge-End Networks Assisted by NOMA

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of computational task offloading for resource-constrained, heterogeneous terminals in the 6G Industrial Internet of Things (IIoT), which generate computation-intensive and resource-efficient tasks in real time, we propose a Digital Twin(DT)-driven cloud-edge-end collaborative resource allocation and task offloading (RATO) model that accounts for both latency and energy consumption. First, we establish a cloud-edge-end collaborative communication and computation framework by integrating cloud computing with edge computing, accommodating terminal and edge server heterogeneity, and employing Non-Orthogonal Multiple Access (NOMA) communication along with key authentication mechanisms to ensure secure communications. Next, Digital Twin technology is utilized for real-time monitoring of the physical environment, considering simulation bias to construct accurate DT entities. Finally, we employ a DT-driven multi-agent deep deterministic policy gradient (DT-MADDPG) algorithm to derive the optimal task scheduling strategy. Simulation results demonstrate that the proposed model significantly outperforms existing schemes in terms of delay, energy cost, load balancing of edge servers, and Quality of Service (QoS) for terminals. © 2017 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2609.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
