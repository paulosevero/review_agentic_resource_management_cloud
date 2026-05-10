---
id: paper-0827
title: Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G
authors:
- Ayepah-Mensah, Daniel
- Sun, Guolin
- Boateng, Gordon Owusu
- Anokye, Stephen
- Liu, Guisong
venue: IEEE/ACM Transactions on Networking
venue_type: journal
year: 2024
doi: 10.1109/TNET.2023.3297390
url: https://www.scopus.com/pages/publications/85166743615?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 654--669
keywords:
- 5G
- Blockchain
- federated learning
- network slicing
- peer-to-peer resource trading
- privacy-preserving
- resource trading
- Stackelberg game
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

# paper-0827 — Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Radio Access Network (RAN) slicing enables resource sharing among multiple tenants and is an essential feature for next-generation mobile networks. Usually, a centralized controller aggregates available resource pools from multiple tenants to increase spectrum availability. In dynamic resource allocation, a tenant could behave strategically by adjusting its preferences based on perceived conditions to maximize its utility. Slice tenants may lie about the resources needed to gain greater utility. Such behavior could lead to poor resource utilization due to excess resources acquired by lying tenants and resource shortages because slice tenants choose not to purchase high-priced resources to save costs. Furthermore, in a scenario with many slice tenants, the centralized controller can become overwhelmed by the number of requests. This, in turn, can lead to slower response times and higher latency, resulting in poor resource utilization and QoS performance of slice tenants. Therefore, this paper proposes a peer-to-peer (P2P) approach to resource trading, where slice tenants communicate directly instead of relying on a centralized orchestrator. This design is motivated by the need for slice tenants to collaborate effectively. We model the interaction between tenants in a Stackelberg multi-leader and multi-follower game and solve the game with multi-agent deep reinforcement learning with an incentive-reward model to achieve the Stackelberg equilibrium. Furthermore, we propose a decentralized resource trading framework by integrating blockchain technology and federated deep reinforcement learning, enabling network tenants to perform inter-slice resource sharing securely. The simulation results show that the proposed mechanism has significant performance improvements over existing implementations.  © 1993-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0827.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
