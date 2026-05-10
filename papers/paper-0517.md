---
id: paper-0517
title: Joint Optimization of Trajectory and Frequency in Energy Constrained Multi-UAV Assisted MEC System
authors:
- Xu, Zhuohan
- Yang, YanPing
- Shi, Bing
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2022
doi: 10.1007/978-3-031-20984-0_30
url: https://www.scopus.com/pages/publications/85145006146?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 422--429
keywords:
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Unmanned aerial vehicle
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0517 — Joint Optimization of Trajectory and Frequency in Energy Constrained Multi-UAV Assisted MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is a promising technology to enhance the computation capability of smart devices (SDs) in the Internet-of-Things (IoT). However, the performance of MEC server is limited due to the fixed location and constrained coverage. In order to address this issue, a multiple unmanned aerial vehicles (UAVs) assisted MEC system is studied in this paper. We consider an energy constrained multi-UAV assisted MEC system where multiple UAVs collaborate with each other to provide computing services, and UAVs can dynamically change the frequency according to the computing task size. We aim to maximize the computation bits, SDs’ fairness and UAVs’ load balancing in multi-UAV MEC system by jointly optimizing the trajectory and frequency. To address this problem, we model it as a Partially Observable Markov Decision Process, and propose a joint optimization strategy based on multi-agent deep reinforcement learning. Finally, we evaluate our strategy against some typical benchmark strategies on the realistic dataset. The experiment results show that our strategy can outperform other strategies. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0517.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
