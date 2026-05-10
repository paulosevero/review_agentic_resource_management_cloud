---
id: paper-0605
title: Distributed access and offloading scheme for multiple UAVs assisted MEC networks
authors:
- He, Saifei
- Cheng, Ming
- Pan, Yijin
- Lin, Min
- Zhu, Wei-Ping
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2023
doi: 10.1109/VTC2023-Fall60731.2023.10333819
url: https://www.scopus.com/pages/publications/85181173150?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Adversarial multi-armed bandit
- distributed scheme
- long-term cost
- mobile edge computing
- unmanned aerial vehicle
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

# paper-0605 — Distributed access and offloading scheme for multiple UAVs assisted MEC networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) have improved the capacity and coverage of wireless networks. Mobile edge computing (MEC) has provided substantial computation capability to user equipment (UEs). The integration of UAV and MEC can take advantages of both to provide flexible computation service. In UAV assisted MEC networks, delay and energy consumption are two main concerns, which are conflicting to a certain extent. This paper investigates delay and energy consumption jointly in a multiple UAVs assisted MEC network. A cost function is defined to balance the delay and the energy consumption. The user access, task offloading, and computational resource allocation are jointly considered to minimize the long-term cost. To tackle this difficult problem, we formulate the long-term problem into sequential decision problem and treat all UEs as intelligent agents. Each UE decides its access UAV, task offloading proportion, and required edge computation resource to minimize the its own cost. Moreover, the optimal task offloading proportion and required computation resource can be obtained in closed-form given user access so that the action space can be significantly reduced. Then, an adversarial multi-armed bandit based algorithm is employed at each UE and a distributed scheme is proposed to solve the joint optimization problem. Simulation results validate the effectiveness and robustness of the distributed scheme and show its superiority to benchmarks. © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0605.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
