---
id: paper-0314
title: Deep Federated Q-Learning-Based Network Slicing for Industrial IoT
authors:
- Messaoud, Seifeddine
- Bradai, Abbas
- Ahmed, Olfa Ben
- Quang, Pham Tran Anh
- Atri, Mohamed
- Hossain, M. Shamim
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2021
doi: 10.1109/TII.2020.3032165
url: https://www.scopus.com/pages/publications/85105577822?origin=resultslist
publisher: IEEE Computer Society
pages: 5572--5582
keywords:
- Federated learning (FL)
- industrial Internet of Things (IIoT)
- network slicing (NS)
- quality-of-service (QoS)
- reinforcement learning (RL)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0314 — Deep Federated Q-Learning-Based Network Slicing for Industrial IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fifth generation and beyond networks are envisioned to support multi industrial Internet of Things (IIoT) applications with a diverse quality-of-service (QoS) requirements. Network slicing is recognized as a flagship technology that enables IIoT networks with multiservices and resource requirements by allowing the network-as-infrastructure transition to the network-as-service. Motivated by the increasing IIoT computational capacity, and taking into consideration the QoS satisfaction and private data sharing challenges, federated reinforcement learning (RL) has become a promising approach that distributes data acquisition and computation tasks over distributed network agents, exploiting local computation capacities and agent's self-learning experiences. This article proposes a novel deep RL scheme to provide a federated and dynamic network management and resource allocation for differentiated QoS services in future IIoT networks. This involves IIoT slices resource allocation in terms of transmission power (TP) and spreading factor (SF) according to the slices QoS requirements. Toward this goal, the proposed deep federated Q-learning (DFQL) is reached into two main steps. First, we propose a multiagent deep Q-learning-based dynamic slices TP and SF adjustment process that aims at maximizing self-QoS requirements in term of throughput and delay. Second, the deep federated learning is proposed to learn multiagent self-model and enable them to find an optimal action decision on the TP and the SF that satisfy IIoT virtual network slice QoS reward, exploiting the shared experiences between agents. Simulation results show that the proposed DFQL framework achieves efficient performance compared to the traditional approaches.  © 2005-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0314.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
