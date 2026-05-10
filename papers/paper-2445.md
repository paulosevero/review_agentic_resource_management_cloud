---
id: paper-2445
title: Multi-Agent Deep Reinforcement Learning Based Offloading Strategies and Collaborative Optimization for Computing Power Networks
authors:
- Zhang, Ruiqi
- Shao, Caixing
- Li, Ran
- Zhang, Qilin
- He, Jianhua
venue: Proceedings - 2025 IEEE International Conference on Smart Internet of Things, SmartIoT 2025
venue_type: conference
year: 2025
doi: 10.1109/SmartIoT66867.2025.00023
url: https://www.scopus.com/pages/publications/105032176211?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 103--108
keywords:
- Computing Power Network
- Federated Learning
- Mobile Edge Computing
- Multi-agent deep reinforcement learning
- Task Offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2445 — Multi-Agent Deep Reinforcement Learning Based Offloading Strategies and Collaborative Optimization for Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid expansion of the Internet of Things (IoT) ecosystem, increasing device density and resource heterogeneity have made timely multi-terminal collaboration very challenging for edge computing strategies. This paper proposes MACPN (Multi-Agent Computing-aware and Adaptive Policy Network), an offloading algorithm that incorporates the Computing Power Network (CPN) for dynamic interconnection and unified scheduling of heterogeneous IoT resources. Built on the CPN-based task offloading framework, MACPN utilizes a Collaborative Multi-Agent Optimization Architecture (CMOA) with adaptive and collaborative features. It integrates Centralized Training with Decentralized Execution (CTDE), federated policy aggregation, and centralized value evaluation. The framework models the task offloading of IoT terminals as a Markov Decision Process (MDP), achieving optimal scheduling under constraints of energy consumption, resource availability, and task deadlines. Experimental results demonstrate that MACPN significantly reduces latency, lowers energy overhead, and achieves robust training convergence. MACPN can be a promising solution for complex and dynamic edge offloading scenarios, offering a novel paradigm for adaptive task scheduling in highly dynamic edge computing environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2445.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
