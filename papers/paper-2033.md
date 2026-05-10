---
id: paper-2033
title: Cooperative Task Offloading Strategy for Utility Optimization in Blockchain-Enabled IoT Networks
authors:
- Peng, Cheng
- Li, Jiangfeng
- Zhu, Yuning
venue: Proceedings of the International Conference on Computer Supported Cooperative Work in Design, CSCWD
venue_type: conference
year: 2025
doi: 10.1109/CSCWD64889.2025.11033324
url: https://www.scopus.com/pages/publications/105011494971?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 32--37
keywords:
- blockchain
- deep reinforcement learning
- edge computing
- mining utility
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2033 — Cooperative Task Offloading Strategy for Utility Optimization in Blockchain-Enabled IoT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the convergence of the Internet of Things (IoT) and blockchain, edge computing enables resource-constrained end devices to offload compute-intensive mining tasks to edge servers to enhance their performance or profits. This calls for a task offloading strategy that accounts for the inherent complexity and variability of the environment, while effectively solving a typically NP-hard offloading problem. Traditional one-shot opti-mization methods often struggle to adapt to dynamic conditions. Meanwhile, existing learning-based approaches usually rely on centralized frameworks or independent agents, which are inad-equate for distributed IoT networks. To this end, a cooperative task offloading strategy is proposed for a blockchain-enabled IoT network with multiple edge service providers. Specifically, the offloading problem is first incorporated into a Markov decision process that considers time-varying channel conditions. A multi-agent deep reinforcement learning algorithm with a gradient estimator is then utilized to optimize the long-term mining utility. Following a centralized training and decentralized execution paradigm, this algorithm allows IoT devices to learn collaborative policies during training while making autonomous decisions based on local observations during execution. Experimental results show that the proposed strategy outperforms existing benchmarks in mining utility under varying conditions.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2033.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
