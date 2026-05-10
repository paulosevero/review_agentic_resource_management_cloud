---
id: paper-1982
title: Multiagent DRL-Based Consensus Mechanism for Blockchain-Based Collaborative Computing in UAV-Assisted 6G Networks
authors:
- Nahom Abishu, Hayla
- Sun, Guolin
- Habtamu Yacob, Yasin
- Owusu Boateng, Gordon
- Ayepah-Mensah, Daniel
- Liu, Guisong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3484005
url: https://www.scopus.com/pages/publications/85207392526?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4331--4348
keywords:
- Blockchain
- consensus mechanisms
- deep reinforcement learning (DRL)
- resource sharing
- sixth-generation (6G) networks
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

# paper-1982 — Multiagent DRL-Based Consensus Mechanism for Blockchain-Based Collaborative Computing in UAV-Assisted 6G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Sixth generation (6G) networks deploy unmanned aerial vehicles and mobile edge computing to provide collaborative computing and reliable connectivity for resource-limited mobile devices (MDs). However, due to the untrusted and broadcast nature of wireless transmission among communicating MDs and computing resource providers, ensuring the security of resource transactions will be challenging. Blockchain-based resource-sharing systems have been proposed to address security issues. However, these systems use existing consensus mechanisms like Proof-of-Work that consume massive amounts of system resources. In addressing this, some studies attempted to use single-agent deep reinforcement learning (DRL) in leader selection. Nevertheless, these solutions overlooked the intelligence and flexibility of blockchain configuration, and a single-point of failure can cause the system to fail. We propose a multiagent distributed deep deterministic policy gradient (MAD3PG)-assisted consensus mechanism for blockchain-based collaborative resource sharing to address these issues. First, we propose a stochastic game-based incentive-mechanism to encourage consensus nodes to participate in transaction validation. Then, we formulate the optimization problem of node selection and blockchain configuration as a Markov decision process and solve it with the MAD3PG algorithm. With MAD3PG, the agents select consensus nodes based on their experience and available resources and dynamically adjust blockchain settings. The simulation results show that MAD3PG outperforms the benchmarks in maximizing throughput and incentive while minimizing block production latency. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1982.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
