---
id: paper-1559
title: MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning
authors:
- Fan, Wenhao
- Chen, Penghui
- Chun, Xiongfei
- Liu, Yuan'an
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3530482
url: https://www.scopus.com/pages/publications/85215382734?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5324--5341
keywords:
- Edge computing
- machine learning
- multi-agent reinforcement learning
- resource management
- split federated learning
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
    my_justification: RL
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

# paper-1559 — MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Split Federated Learning (SFL) has emerged as a promising paradigm to enhance FL by partitioning the Machine Learning (ML) model into parts and deploying them across clients and servers, effectively mitigating the workload on resource-constrained devices and preserving privacy. Compared to cloud-device-based and edge-device-based SFL, cloud-edge-device collaborative SFL offers both lower communication latency and wider network coverage. However, existing works adopt a uniform model partitioning strategy for different devices, ignoring the heterogeneous nature of device resources. This oversight leads to severe straggler problems, making the training process inefficient. Moreover, they do not consider joint optimization of model aggregation control and computing and communication resource allocation, and lack distributed algorithm design. To address these issues, we propose a joint resource management scheme for cloud-edge-device collaborative SFL to optimize the training latency and energy consumption of all devices. In our scheme, the partitioning strategy is optimized for each device based on resource heterogeneity. Meanwhile, we jointly optimize the aggregation frequency of ML models, computing resource allocation for all devices and edge servers, and transmit power allocation for all devices. We formulate a coordination game among all edge servers and then design a distributed optimization algorithm employing partially observable Multi-Agent Deep Reinforcement Learning (MADRL) with integrated numerical methods. Extensive experiments are conducted to validate the convergence of our algorithm and demonstrate the superiority of our scheme via evaluations under multiple scenarios and in comparison with four reference schemes. © 2002-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1559.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
