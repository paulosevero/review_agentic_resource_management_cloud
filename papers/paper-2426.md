---
id: paper-2426
title: Distributed Multiagent Reinforcement Learning Approach for Multiserver Multiuser Task Offloading
authors:
- Zhang, He
- Tian, Zijian
- Zeng, Lanting
- Lu, Limin
- Qiao, Simengxu
- Chen, Shifan
- Liu, Xinggao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3585025
url: https://www.scopus.com/pages/publications/105010196759?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 37836--37852
keywords:
- Computation offloading
- decentralized partially observable stochastic game (Dec-POSG)
- mobile-edge computing (MEC)
- multiagent deep reinforcement learning (MADRL)
- resource allocation
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

# paper-2426 — Distributed Multiagent Reinforcement Learning Approach for Multiserver Multiuser Task Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The industrial manufacturing industry requires user devices (UDs) to process massive data, leading to latency and energy consumption. To achieve low-latency and low-power task execution, we propose an industrial intelligent manufacturing system utilizing mobile-edge computing. A dynamic computation offloading and resource allocation problem is formulated in multiserver multiuser scenarios to balance latency and energy cost. To solve this optimization problem, multiagent deep reinforcement learning (MADRL) offers a theoretical framework. However, the widely used centralized training and decentralized execution (CTDE) scheme has two major drawbacks. First, it is unsuitable for scenarios without a central controller for global information collection. Second, it incurs significant communication overhead. Consequently, the decentralized training and execution (DTDE) scheme becomes necessary. However, DTDE introduces nonstationarity by treating other UDs as part of the environment, which leads to nonconvergence. To address these issues, we design a distributed partial communication-based computation offloading and resource allocation algorithm (DPC-CORAA). This algorithm establishes a partial communication model based on the decentralized partially observable stochastic game (Dec-POSG) framework. It also incorporates the multiagent deep deterministic policy gradient method under the DTDE scheme. The proposed method enables UDs to exchange information with neighbors to estimate the global decision, reducing communication cost. It also ensures theoretical convergence of this estimation to the real decision, serving as a local observation for independent strategy learning. Simulation results demonstrate that DPC-CORAA achieves stable convergence, whereas the general DTDE scheme fails to converge. When contrasted with MADRL using centralized training with decentralized execution (CTDE), DPC-CORAA delivers superior performance in reducing latency and energy consumption, particularly in large-scale scenarios. © 2014 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2426.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
