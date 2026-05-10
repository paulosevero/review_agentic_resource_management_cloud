---
id: paper-2332
title: Digital-Twin-Assisted Intelligent Secure Task Offloading and Caching in Blockchain-Based Vehicular Edge Computing Networks
authors:
- Xu, Chi
- Zhang, Peifeng
- Xia, Xiaofang
- Kong, Linghe
- Zeng, Peng
- Yu, Haibin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3482870
url: https://www.scopus.com/pages/publications/85207704101?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4128--4143
keywords:
- Content caching
- deep reinforcement learning (DRL)
- digital twin (DT)
- resource allocation
- task offloading
- vehicular edge computing (VEC) networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2332 — Digital-Twin-Assisted Intelligent Secure Task Offloading and Caching in Blockchain-Based Vehicular Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Blockchain-based vehicular edge computing (VEC) is regarded as a promising computing paradigm that can enhance the computing capabilities of mobile vehicles while ensuring security during task offloading. However, the blockchain consensus for secure task offloading inevitably increases the communication and computation resource consumption. More importantly, the frequent handover among roadside units during the fast movement of vehicles also raises the communication cost for blockchain consensus. To address these issues, this article proposes intelligent secure task offloading and caching (ISTOC) scheme for VEC networks. Specifically, we first establish a digital twin-assisted VEC network that migrates the blockchain consensus process from the physical space to the cyber space, supporting the dynamic handover of vehicles. Correspondingly, we propose a lightweight blockchain scheme named diffused delegated Byzantine fault tolerance (d2BFT). Then, aiming at simultaneously reducing the task processing latency and improving the blockchain transaction throughput, we formulate the joint blockchain, communication, computation, and caching (B3C) optimization problem subject to task division, communication bandwidth, computing frequency, cache storage, task deadline, and blockchain stability. Due to the nonconvexity of B3C, we transform it into a Markov decision process, and propose a multiagent double actor-critic (MADAC) algorithm in light of the distributed characteristic of blockchain. Through offline training and online execution, we jointly optimize the task division, communication bandwidth, computing frequency and cache storage allocation, block size, and block generation interval for ISTOC. Experimental results show that the proposed MADAC-based ISTOC scheme can stably converge with a much higher reward than the benchmark schemes based on MADDPG, soft actor-critic, deep deterministic policy gradient, and TD3. The improvement of MADAC-ISTOC over SAC-ISTOC is more than 25.93%. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2332.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
