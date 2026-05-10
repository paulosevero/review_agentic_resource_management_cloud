---
id: paper-0663
title: Energy-Efficient Task Transfer in Wireless Computing Power Networks
authors:
- Lu, Yunlong
- Ai, Bo
- Zhong, Zhangdui
- Zhang, Yan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2022.3223690
url: https://www.scopus.com/pages/publications/85144080521?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9353--9365
keywords:
- Digital twin
- energy efficiency
- multiagent deep reinforcement learning (DRL)
- wireless computing power networks (WCPNs)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0663 — Energy-Efficient Task Transfer in Wireless Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The sixth generation (6G) wireless communication aims to enable ubiquitous intelligent connectivity in future space-air-ground-ocean-integrated networks, with extremely low latency and enhanced global coverage. However, the explosive growth in Internet of Things devices poses new challenges for smart devices to process the generated tremendous data with limited resources. In 6G networks, conventional mobile edge computing (MEC) systems encounter serious problems to satisfy the requirements of ubiquitous computing and intelligence, with extremely high mobility, resource limitation, and time variability. In this article, we propose the model of wireless computing power networks (WCPNs), by jointly unifying the computing resources from both end devices and MEC servers. Furthermore, we formulate the new problem of task transfer, to optimize the allocation of computation and communication resources in WCPN. The main objective of task transfer is to minimize the execution latency and energy consumption with respect to resource limitations and task requirements. To solve the formulated problem, we propose a multiagent deep reinforcement learning (DRL) algorithm to find the optimal task transfer and resource allocation strategies. The DRL agents collaborate with others to train a global strategy model through the proposed asynchronous federated aggregation scheme. Numerical results show that the proposed scheme can improve computation efficiency, speed up convergence rate, and enhance utility performance.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0663.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
