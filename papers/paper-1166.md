---
id: paper-1166
title: 'LearnChain: Transparent and cooperative reinforcement learning on Blockchain'
authors:
- Sami, Hani
- Mizouni, Rabeb
- Otrok, Hadi
- Singh, Shakti
- Bentahar, Jamal
- Mourad, Azzam
venue: Future Generation Computer Systems
venue_type: journal
year: 2024
doi: 10.1016/j.future.2023.09.012
url: https://www.scopus.com/pages/publications/85171891314?origin=resultslist
publisher: Elsevier B.V.
pages: 255--271
keywords:
- Blockchain
- Cooperative artificial intelligence (AI)
- Ethereum
- Quorum
- Reinforcement learning
- Transparency
- Trust
- Vehicular edge computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1166 — LearnChain: Transparent and cooperative reinforcement learning on Blockchain

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We consider multi-agent reinforcement learning (MARL) with the popular paradigm of centralized training and decentralized execution (CTDE). CTDE empowers sharing knowledge from agents in different environments for updating a shared model. A wide range of applications is supported through CTDE in MARL, such as self-driving vehicle coordination, traffic lights synchronization, or cooperation in various aspects of the Internet of Things (IoT), including resource management. Despite the drawbacks of relying on a central authority for handling model updates, incorporating multiple sources of data raises concerns about the trustworthiness of the process. For instance, participating agents could provide data in the favor of their experiences to shift the model towards certain behaviors. Similarly, sending falsified data for updates could lead to adversarial attacks. To overcome these challenges, it is essential to integrate the Ethereum Blockchain technology to handle model updates in the CTDE paradigm by achieving decentralized storage and consensus mechanism for model updates. In the literature, there exist multiple efforts that propose using reinforcement learning (RL) on Blockchain; however, none of them have considered updating MARL of CTDE on-chain, allowing transparent and auditable record of the training process. Therefore, we propose LearnChain, a framework that offers an integration between the CTDE mechanism and a Consortium Blockchain built between authorized participants, thus avoiding gas costs. At the core of LearnChain, RL is integrated with Quorum, offering separate smart contracts for deployment, data handling with incentive mechanisms, training, target update, and inference. Based on a real use-case entailing management of Vehicular Edge Computing tasks through multi-agent synchronization, we implement LearnChain and evaluate its performance and cost in different settings. Our results show the ability to improve learning from shared experiences and to adapt to environment changes on the Quorum BlockChain. © 2023

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1166.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
