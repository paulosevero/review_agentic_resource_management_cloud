---
id: paper-2546
title: Cooperative Task Offloading Strategy for Vehicular Edge Computing Based on Multi-Agent Deep Reinforcement Learning
authors:
- Cui, Yuya
- Zhang, Degan
- Li, Honghu
- Qiang, Hao
- Zhao, Haitao
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2025.107950
url: https://www.scopus.com/pages/publications/105007813096?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Multi -agent reinforcement learning
- Vehicular Edge Computing (VEC)
- Vehivle to Vehicle (V2V)
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

# paper-2546 — Cooperative Task Offloading Strategy for Vehicular Edge Computing Based on Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular Edge Computing (VEC) and Vehicle- to-Vehicle (V2V) offloading can significantly reduce in-vehicle task latency. This paper investigates a cooperative task offloading strategy in VEC, where latency-sensitive and computation -intensive tasks can be offloaded to Road Side Units (RSUs) using 5 G connectivity. Additionally, these tasks can be shared among nearby vehicles through V2V links. Joint VEC and V2V cooperative offloading can not only minimizes task execution delays but also prevents network congestion. When vehicles are in motion, dynamic migration of computation tasks is necessary to maintain service continuity. We propose a two-phase distributed task offloading and migration strategy for multiple vehicles. In the first phase, vehicles select the optimal service vehicle based on inter-vehicle link quality and offloading willingness. In the second phase, to minimize system cost, we introduce a multi-agent reinforcement learning (MARL) based distributed task offloading and migration strategy. This strategy allows vehicles to choose the optimal edge node in a dynamic environment without fully offloading information. Moreover, we implement a counterfactual multi- agent (COMA) reinforcement learning approach to address the inefficiency caused by the credit allocation problem in multi-agent systems. Extensive evaluations demonstrate that the algorithm proposed in this paper perform better in terms of average system latency and overall task completion rate. Compared with related scheme, the proposed method can reduce latency by up to 54 % and improve task completion rate by up to 15 % in different scenarios. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2546.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
