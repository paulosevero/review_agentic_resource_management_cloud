---
id: paper-2858
title: A Joint Optimization Strategy of Computing Offloading and Service Migration Based on Multi-User With Mobility Consideration
authors:
- Xing, Shuo
- Feng, Xin
- Yue, Linze
- Zhang, Jing
- Li, Mingye
- Zheng, Tingting
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2026
doi: 10.1109/OJCOMS.2026.3657391
url: https://www.scopus.com/pages/publications/105028918990?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1137--1152
keywords:
- MAPPO
- MEC
- multi-agent
- service migration
- task-offloading decision
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2858 — A Joint Optimization Strategy of Computing Offloading and Service Migration Based on Multi-User With Mobility Consideration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) facilitates real-time task offloading in dynamic mobile environments. However, existing studies frequently overlook the impact of heterogeneous mobility patterns on execution costs caused by service migration delays. In this paper, a task offloading decision model is proposed to minimize average execution delay under diverse mobility patterns. Three distinct offloading strategies are designed: an offloading strategy based on unpredictable mobile location, an offloading strategy based on a short-term prediction algorithm for mobile location, and a multi-agent proximal policy optimization (MAPPO)-based strategy for coordinating multi-mobile users’ offloading decisions. The proposed strategies are benchmarked against a genetic algorithm-based joint optimization method and a local execution baseline under varying user densities and central processing unit speeds. Simulation results show that the proposed algorithms reduce average task delay by 6.72%, 12.27%, 36.49%, 27.63%, and 21.84% compared to the baseline algorithms, respectively. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2858.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
