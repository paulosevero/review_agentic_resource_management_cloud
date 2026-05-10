---
id: paper-2327
title: A DRL Method Based on Hybrid Action Representation for Task Offloading and Resource Allocation for Mobile Edge Computing
authors:
- Xu, Sai
- Liu, Jun
- Ren, Zixuan
- Li, Zhi
venue: Proceedings - 2025 IEEE International Symposium on Parallel and Distributed Processing with Applications, ISPA 2025
venue_type: conference
year: 2025
doi: 10.1109/ISPA67752.2025.00154
url: https://www.scopus.com/pages/publications/105030172392?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1121--1128
keywords:
- Deep Reinforcement Learning
- Hybrid Action Representation
- Mobile Edge Computing
- Resource Allocation
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2327 — A DRL Method Based on Hybrid Action Representation for Task Offloading and Resource Allocation for Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In multi-task mobile edge computing (MEC) environments, optimizing task offloading and resource allocation is particularly challenging due to the coexistence of discrete and continuous decision variables under limited computational resources. To address these challenges, this paper proposes a joint optimization algorithm based on deep reinforcement learning (DRL) with a hybrid action representation mechanism. Specifically, a comprehensive MEC framework with multiple terminal devices and base stations is established, and the joint optimization of discrete task offloading and continuous resource allocation is formulated as a mixed-integer nonlinear programming (MINLP) problem. To effectively handle the hybrid action space, an innovative representation mechanism is designed to capture the dependencies between discrete and continuous actions. Furthermore, an enhanced multi-agent Deep Deterministic Policy Gradient (DDPG) algorithm is developed to optimize offloading decisions and resource allocation simultaneously. The objective is to minimize task processing latency and device energy consumption. Simulation results demonstrate that the proposed approach outperforms state-of-the-art methods, achieving lower latency and reduced energy consumption in MEC scenarios.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2327.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
