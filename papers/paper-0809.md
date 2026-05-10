---
id: paper-0809
title: Online Distributed Learning-Based Load-Aware Heterogeneous Vehicular Edge Computing
authors:
- Zhu, Lei
- Zhang, Zhizhong
- Liu, Lilan
- Feng, Linlin
- Lin, Peng
- Zhang, Yu
venue: IEEE Sensors Journal
venue_type: journal
year: 2023
doi: 10.1109/JSEN.2023.3283413
url: https://www.scopus.com/pages/publications/85162731160?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17350--17365
keywords:
- Load balancing
- multiagent reinforcement learning
- online distributed optimization
- vehicular edge computing (VEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0809 — Online Distributed Learning-Based Load-Aware Heterogeneous Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is an emerging enabler in strengthening driving efficiency and traffic safety. However, both performance bottlenecks and low-resource efficiency of heterogeneous edge servers arise concurrently because of the inhomogeneous load distribution among the servers. Further, the unsaturated infrastructure coverage situation can deteriorate the concurrent issues. Although transmitting raw task data with large sizes among heterogeneous edge servers can relieve the concurrent issues, it distinctly degrades the core network's efficiency, especially during rush hours. Meanwhile, it cannot settle the unsaturated coverage situation. To relieve the concurrent issues without degrading the core network's efficiency, we introduce an aerial relay station (ARS) that can flexibly relay vehicular tasks to nearby heterogeneous edge servers. The long-term task-scheduling problem without any prior environment knowledge for the considered vehicular edge system is crucial but still up in the air. We formulate the system latency minimization problem as a partially observable stochastic game (POSG). Then a model-free multiagent reinforcement learning algorithm is developed to search the real-time load-aware scheduling policy. Besides, we design a practical factor named offloading latency gain to assist the training process of the learning algorithm. Simulation experiments show that our proposed algorithm (PA) can better exploit idle computation resources of heterogeneous edge infrastructures and significantly reduce the average system latency up to 15%-20% over existing algorithms.  © 2001-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0809.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
