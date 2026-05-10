---
id: paper-1821
title: SAC-Based Latency Optimization for Collaborative Inference of Distributed Large Language Models in Industrial IoT
authors:
- Li, Yang
- Jing, Tao
- Li, Xuehan
- Zhang, Boyang
- Gao, Bo
- Zhu, Minghao
venue: Proceeding of 2025 IEEE 4th International Conference on Computing, Communication, Perception and Quantum Technology, CCPQT 2025
venue_type: conference
year: 2025
doi: 10.1109/CCPQT66408.2025.11382826
url: https://www.scopus.com/pages/publications/105034881034?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Industrial Internet of Things (IIoT)
- Large Language Models (LLMs)
- reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1821 — SAC-Based Latency Optimization for Collaborative Inference of Distributed Large Language Models in Industrial IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) enable advanced natural language processing, enhancing human-machine interaction and supporting intelligent manufacturing in Industry 5.0. However, the cloud-based architecture commonly used for LLMs in Industrial Internet of Things (IIoT) environments faces significant latency issues due to limited computational power of edge infrastructure. To address this, collaborative edge computing partitions LLMs into distributed shards across heterogeneous industrial edge servers (IESs), reducing latency by bringing computation closer to industrial devices (IDs). Existing works primarily focus on single inference task and fail to handle concurrent multi-demand scenarios or the computational heterogeneity of IESs. This paper proposes a heterogeneity-aware scheduling framework for LLM inference in concurrent environments. The Distributed LLM Inference Task Scheduling Algorithm (DLITS) uses Soft Actor-Critic (SAC) for adaptive resource allocation, minimizing latency through intelligent workload distribution. Empirical results from simulations conducted using real smart factory configurations show that DLITS reduces latency by 10% to 94% compared to baseline methods across various scenarios, effectively optimizing offloading in heterogeneous edge-cloud architectures. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1821.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
