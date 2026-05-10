---
id: paper-1191
title: Network analysis in a peer-to-peer energy trading model using blockchain and machine learning
authors:
- Shukla, Saurabh
- Hussain, Shahid
- Irshad, Reyazur Rashid
- Alattab, Ahmed Abdu
- Thakur, Subhasis
- Breslin, John G.
- Hassan, M Fadzil
- Abimannan, Satheesh
- Husain, Shahid
- Jameel, Syed Muslim
venue: Computer Standards and Interfaces
venue_type: journal
year: 2024
doi: 10.1016/j.csi.2023.103799
url: https://www.scopus.com/pages/publications/85175193267?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Blockchain
- Cloud computing
- Cyber security
- Energy
- Latency
- Machine learning
- Neural networks
- Peer-to-peer energy trade
- Q-learning
- Reinforcement learning
- Smart grids
- Smart meters
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1191 — Network analysis in a peer-to-peer energy trading model using blockchain and machine learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Existing technology like smart grid (SG) and smart meters play a significant role in meeting the everlasting demand of energy consumption, supply, and generation for peer-to-peer (P2P) energy trading between different distributed prosumers. Whereas blockchain when used with P2P energy trading plays a major role in cost and security by eliminating any involvement of outsiders and third parties. However, existing works related to the blockchain with P2P energy trading are engaged in increasing the cost related to resource allocation, latency, computational processing, and large network setup. The objective of this paper is to design and develop a three-tier architecture, an analytical model, and a hybrid algorithm for network analysis in a blockchain-based P2P energy trading system using reinforcement learning (RL) and feed forward neural network (FFNN) techniques. In this model, we will examine the various parameters and tradeoffs which affect the delay, throughput, and security in P2P energy trading. This will lead to profitable P2P energy trading between different distributed prosumers. By analyzing the simulation results of the proposed model and algorithm by benchmarking with the existing state-of-the-art techniques it's clear that the proposed algorithm shows marked improvement over network latency generated results. The simulation of the model is conducted using the iFogSim simulator, Ganache with Ethereum platform, Truffle, Python editor tool, and ATOM IDE with solidity. © 2023 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1191.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
