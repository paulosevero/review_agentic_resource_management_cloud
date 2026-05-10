---
id: paper-0548
title: Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT
authors:
- Al-Maslamani, Noora Mohammed
- Abdallah, Mohamed
- Ciftler, Bekir Sait
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2023
doi: 10.1109/OJCOMS.2023.3280359
url: https://www.scopus.com/pages/publications/85161555519?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1274--1284
keywords:
- Deep reinforcement learning
- hierarchical federated learning
- neural networks
- poisoning attack
- reputation management
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0548 — Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Aiming at protecting device data privacy, Federated Learning (FL) is a framework of distributed machine learning in which devices' local model parameters are exchanged with a centralized server without revealing the actual data. Hierarchical Federated Learning (HFL) framework was introduced to improve FL communication efficiency where devices are clustered and seek model consensus with the support of edge servers (e.g., base stations). Devices in a cluster submit their local model updates to their assigned local edge server for aggregation at each iteration. The edge servers transmit the aggregated models to a centralized server and establish a global consensus. However, similar to FL, adversaries may threaten the security and privacy of HFL. The client devices within a cluster may deliberately provide unreliable local model updates through poisoning attacks or poor-quality model updates due to inconsistent communication channels, increased device mobility, or inadequate device resources. To address the above challenges, this paper investigates the client selection problem in the HFL framework to eliminate the impact of unreliable clients while maximizing the global model accuracy of HFL. Each FL edge server is equipped with a Deep Reinforcement Learning (DRL)-based reputation model to optimally measure the reliability and trustworthiness of FL workers within its cluster. A Multi-Agent Deep Deterministic Policy Gradient (MADDPG) is utilized to enhance the accuracy and stability of the HFL global model, given the workers' dynamic behaviors in the HFL environment. The experimental results indicate that our proposed MADDPG improves the accuracy and stability of HFL compared with the conventional reputation model and single-agent DDPG-based reputation model.  © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0548.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
