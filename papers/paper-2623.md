---
id: paper-2623
title: 'Quality of experience aware task execution in digital twinning vehicular edge computing: A framework and A3C algorithm'
authors:
- Jihad, Mostakim
- Al Fahad, Abdullah
- Roy, Palash
- Razzaque, Md Abdur
- Alelaiwi, Abdulhameed
- Hassan, Md Rafiul
- Hassan, Mohammad Mehedi
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2025.108144
url: https://www.scopus.com/pages/publications/105017964081?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Asynchronous advantage actor-critic (A3C)
- Digital twin
- Quality-of-experience
- Reputation
- Vehicular edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2623 — Quality of experience aware task execution in digital twinning vehicular edge computing: A framework and A3C algorithm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Real-time computationally intensive task scheduling for intelligent transportation system (ITS) applications like road safety and traffic forecasting within the deadline while ensuring user quality of experience (QoE) is a complex engineering problem. Meanwhile, adopting Digital Twin (DT) as an emerging technology in vehicular edge computing (VEC) enables efficient capture of real-time state information, thereby addressing the resource scheduling problem in an unpredictable vehicular topology setting. However, exploring strategies to enhance user QoE in timeliness and reliability domains could be a compelling and underexplored research challenge, particularly within the dynamic and trust-sensitive context of vehicular edge computing. In this paper, we have developed an optimization framework using Mixed Integer Linear Programming (MILP), which maximizes user QoE by allocating task execution responsibility to highly reliable and reputed vehicles in a DT-enabled VEC environment. The framework leverages the demand-supply theory of economics to cluster vehicles based on computational resources and applies multi-weighted subjective logic to ensure accurate reputation updates. The NP-hard nature of the formulated optimization problem has driven us to develop an Asynchronous Advantage Actor-Critic (A3C)-based deep reinforcement learning algorithm, namely DARQoE, for offloading tasks in the Internet of Vehicles (IoV). The developed DARQoE framework utilizes effective parallelization across multiple agents with separate environments, accelerating the learning process for IoV task offloading. The experimental results of the developed DARQoE framework demonstrate significant performance improvements in terms of QoE in the timeliness and reliability domains of task execution by up to 15 % and 25 %, respectively, compared to state-of-the-art works. © 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2623.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
