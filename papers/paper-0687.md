---
id: paper-0687
title: Cooperative Task Offloading and Block Mining in Blockchain-Based Edge Computing With Multi-Agent Deep Reinforcement Learning
authors:
- Nguyen, Dinh C.
- Ding, Ming
- Pathirana, Pubudu N.
- Seneviratne, Aruna
- Li, Jun
- Poor, H. Vincent
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2023
doi: 10.1109/TMC.2021.3120050
url: https://www.scopus.com/pages/publications/85117750721?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2021--2037
keywords:
- block mining
- Blockchain
- deep reinforcement learning
- mobile edge computing
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0687 — Cooperative Task Offloading and Block Mining in Blockchain-Based Edge Computing With Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The convergence of mobile edge computing (MEC) and blockchain is transforming the current computing services in mobile networks, by offering task offloading solutions with security enhancement empowered by blockchain mining. Nevertheless, these important enabling technologies have been studied separately in most existing works. This article proposes a novel cooperative task offloading and block mining (TOBM) scheme for a blockchain-based MEC system where each edge device not only handles data tasks but also deals with block mining for improving the system utility. To address the latency issues caused by the blockchain operation in MEC, we develop a new Proof-of-Reputation consensus mechanism based on a lightweight block verification strategy. A multi-objective function is then formulated to maximize the system utility of the blockchain-based MEC system, by jointly optimizing offloading decision, channel selection, transmit power allocation, and computational resource allocation. We propose a novel distributed deep reinforcement learning-based approach by using a multi-agent deep deterministic policy gradient algorithm. We then develop a game-theoretic solution to model the offloading and mining competition among edge devices as a potential game, and prove the existence of a pure Nash equilibrium. Simulation results demonstrate the significant system utility improvements of our proposed scheme over baseline approaches.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0687.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
