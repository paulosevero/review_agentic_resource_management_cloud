---
id: paper-1363
title: AI-Driven Optimization of Chiplet Architectures Using Reinforcement Learning
authors:
- Abdelraouf, Hussien
- Ibrahem, Mohamed I.
venue: 2025 International Conference on Information and Communication Technology, ICoICT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICoICT66265.2025.11193060
url: https://www.scopus.com/pages/publications/105020980705?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- and AI-driven systems
- Chiplet-based architecture
- Markov Decision Process (MDP)
- Reinforcement learning (RL)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1363 — AI-Driven Optimization of Chiplet Architectures Using Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing demand for scalable and energy-efficient processing in domains such as artificial intelligence (AI), cloud computing, and edge analytics has driven the exploration of chiplet-based architectures. These architectures enhance performance, modularity, and manufacturing yield by integrating multiple smaller dies, referred to as chiplets, within a single package, enabling heterogeneous integration and improved scalability compared to traditional monolithic systems. However, this shift introduces new challenges, including inter-chiplet communication latency, uneven thermal distribution, and inefficient workload scheduling under dynamic conditions. To address these limitations, this paper proposes a reinforcement learning (RL)-based methodology that leverages intelligent, adaptive decision-making to optimize system performance. By modeling the chiplet-based platform as a Markov Decision Process (MDP), the proposed framework allows RL agents to dynamically manage interconnect configurations, workload allocation, power consumption, and thermal balancing in real-time. Simulation results demonstrate that the RL-driven approach achieves significant improvements across multiple performance metrics, including a 52% increase in throughput, a 36% reduction in latency, a 29.2% reduction in power consumption, and a 16.3% improvement in thermal balance. These results highlight the potential of RL to enable highly efficient, scalable, and self-optimizing chiplet-based systems for next-generation high-performance computing applications. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1363.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
