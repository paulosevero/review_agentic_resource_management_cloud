---
id: paper-2693
title: DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization
authors:
- Lotfolahi, Amin
- Ferng, Huei-Wen
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3584786
url: https://www.scopus.com/pages/publications/105010023342?origin=resultslist
publisher: IEEE Computer Society
pages: 469--484
keywords:
- Industrial Internet of things (IIoT)
- mobile edge computing (MEC)
- multi-agent proximal policy optimization (MAPPO)
- non-orthogonal multiple access (NOMA)
- resource allocation
- Task offloading
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

# paper-2693 — DRL-Based Resource Allocation in NOMA-Aided Industrial IoT Towards Energy Productivity Maximization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper addresses the joint optimization problem of computing and communication resource allocation in a non-orthogonal multiple access (NOMA) supported industrial Internet of things (IoT) system. We introduce a decentralized deep reinforcement learning (DRL) based mechanism that collaboratively maximizes energy productivity (EP). Specifically, optimizing EP involves maximizing the amount of successfully processed bits while simultaneously minimizing task processing delay, energy consumption, and task drop ratio. With this goal, we design a comprehensive model that incorporates multiple factors, including NOMA-specific constraints, task queueing, partial processing, and multitasking, where each device can handle multiple concurrent tasks. Next, we propose a dual-decentralized multi-agent proximal policy optimization (MAPPO) based algorithm, where one MAPPO algorithm focuses explicitly on computing resource allocation for task processing at the edge servers, while the other MAPPO algorithm precisely manages communication resource allocation. Additionally, each MAPPO algorithm is equipped with a small residual network (ResNet) and a recurrent neural network (RNN) to effectively capture spatial features from complex channel conditions and the evolving task flow. Through extensive simulations, we validate the effectiveness of our resultant mechanism under various environmental conditions and demonstrate its superiority over the closely related mechanisms in the literature. © 2025 IEEE. All rights reserved.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2693.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
