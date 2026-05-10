---
id: paper-1032
title: Multiagent Reinforcement Learning-Based Multimodel Running Latency Optimization in Vehicular Edge Computing Paradigm
authors:
- Li, Peisong
- Xiao, Ziren
- Wang, Xinheng
- Iqbal, Muddesar
- Casaseca-De-La-Higuera, Pablo
venue: IEEE Systems Journal
venue_type: journal
year: 2024
doi: 10.1109/JSYST.2024.3407213
url: https://www.scopus.com/pages/publications/85211500835?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1860--1870
keywords:
- Autonomous driving
- deep reinforcement learning (DRL)
- edge computing
- latency optimization
- multimodel inferences
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1032 — Multiagent Reinforcement Learning-Based Multimodel Running Latency Optimization in Vehicular Edge Computing Paradigm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advancement of edge computing, more and more intelligent applications are being deployed at the edge in proximity to end devices to provide in-vehicle services. However, the implementation of some complex services requires the collaboration of multiple AI models to handle and analyze various types of sensory data. In this context, the simultaneous scheduling and execution of multiple model inference tasks is an emerging scenario and faces many challenges. One of the major challenges is to reduce the completion time of time-sensitive services. In order to solve this problem, a multiagent reinforcement learning-based multimodel inference task scheduling method was proposed in this article, with a newly designed reward function to jointly optimize the overall running time and load imbalance. First, the multiagent proximal policy optimization algorithm is utilized for designing the task scheduling method. Second, the designed method can generate near-optimal task scheduling decisions and then dynamically allocate inference tasks to different edge applications based on their status and task characteristics. Third, one assessment index, quality of method, is defined and the proposed method is compared with the other five benchmark methods. Experimental results reveal that the proposed method can reduce the running time of multimodel inference by at least 25% or more, closing to the optimal solution. © 2007-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1032.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
