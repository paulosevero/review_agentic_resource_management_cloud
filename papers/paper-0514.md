---
id: paper-0514
title: Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks
authors:
- Xia, Shichao
- Yao, Zhixiu
- Wu, Guangfu
- Li, Yun
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2022
doi: 10.1109/TITS.2022.3190280
url: https://www.scopus.com/pages/publications/85135225295?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16701--16714
keywords:
- Cooperative intelligent transportation system (C-ITS)
- multi-access edge computing (MEC)
- multi-agent deep deterministic policy gradient (MADDPG)
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

# paper-0514 — Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of the Internet of Vehicles and artificial intelligence (AI) technologies, the cooperative intelligent transportation system (C-ITS) has drawn great attention in recent years. To provide an ultra-reliable, low-latency computation experience of C-ITS, computation offloading is deemed indispensable by working with edge-cloud servers. In this paper, we first investigate a distributed dynamic computation offloading model for multi-access edge computing (MEC) enabled C-ITS under a heterogeneous road network, in which the multiple and heterogeneous computing power sources cooperatively provide computation offloading services for vehicles. Considering the autonomous offloading manner of the vehicles, we formulate the task offloading and computing power allocation as a distributed Stackelberg game, where the MEC servers as the leader to allocate computing resources and manage local energy, and the vehicles as the followers to offload local computation task. Since the observable states in the game is incomplete, the problem of resolving the optimal strategies for each game player is modeled as a partially observable Markov decision process (POMDP) to maximize the long-term cumulative reward. Then we develop a computation offloading algorithm using Stackelberg game-based multi-agent deep deterministic policy gradient (SG-MADDPG), which uses a centralized training and decentralized execution method to learn the optimal computing power allocation and computation offloading policies. Finally, extensive simulations are carried out and show the rationality and effectiveness of the proposed algorithm.  © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0514.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
