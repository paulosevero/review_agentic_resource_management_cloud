---
id: paper-1070
title: Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing
authors:
- Long, Wanqing
- Lu, Hancheng
- Chong, Baolin
- Cheng, Guo
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901737
url: https://www.scopus.com/pages/publications/105000820483?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4624--4629
keywords:
- Blockchain
- deep reinforcement learning
- resource al-location
- serverless computing
- task scheduling
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1070 — Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing is gaining popularity due to its "pay-per-use"model and simplified management. Benefiting from the common features of Internet of Things (IoT), the adaptation of serverless in edge computing is extensively researched. To protect nodes in serverless edge computing from potential attacks, blockchain technology plays a crucial role. Considering that the computing time of a single serverless function can be less than the time for a blockchain to generate a block, the blockchain component requires significant computing and bandwidth resources to ensure the generation efficiency of blocks matches the execution efficiency of serverless functions. However, existing studies on minimizing the completion time (a.k.a. makespan) of application workflows in serverless edge computing have never considered the impact brought by blockchain, leading to an imbalance in the resource allocation between the computing and blockchain components. To address this, we propose a Heterogeneous Event-driven Scheduling (HEDS) mechanism, which employs a fine-grained CPU al-location scheme and an event-driven approach, to make the adjustment of resource allocation between the computing and blockchain components more flexible and expeditious, leading to improving the utilization of both computing and bandwidth resources. Meanwhile, a Multi-agent Double Deep Q-network (MADDQN) algorithm is proposed to help agents minimize the makespan while balancing the resource consumption in the computing and blockchain components. Simulation results demonstrate that HEDS with MADDQN outperforms existing algorithms in terms of average makespan over different numbers of functions and nodes while satisfying the latency requirements of block generation. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1070.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
