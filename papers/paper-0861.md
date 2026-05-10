---
id: paper-0861
title: Joint optimization for service-caching, computation-offloading, and UAVs flight trajectories over rechargeable UAV-aided MEC using hierarchical multi-agent deep reinforcement learning
authors:
- Chen, Zhian
- Wang, Fei
- Wang, Jiaojie
venue: Vehicular Communications
venue_type: journal
year: 2024
doi: 10.1016/j.vehcom.2024.100844
url: https://www.scopus.com/pages/publications/85203964138?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- Computation-offloading
- HMDRL
- Rechargeable UAV-aided MEC
- Service-caching
- UAVs flight trajectories
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

# paper-0861 — Joint optimization for service-caching, computation-offloading, and UAVs flight trajectories over rechargeable UAV-aided MEC using hierarchical multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the high mobility, high chance of line-of-sight (LoS) transmission, and flexible deployment, unmanned aerial vehicles (UAVs) have been used as mobile edge computing (MEC) servers to provide ubiquitous computation services to mobile users (MUs). However, the limited energy storage, caching capacity, and computation resources of UAVs bring new challenges for UAV-aided MEC, e.g., how to recharge UAVs and how to jointly optimize service-caching, computation-offloading, and UAVs flight trajectories. To overcome the above-mentioned difficulties, in this paper we study the joint optimization for service-caching, computation-offloading, and UAVs flight trajectories for UAV-aided MEC, where multiple rechargeable UAVs cooperatively provide MEC services to a number of MUs. First, we formulate an energy minimization problem to minimize all MUs' energy consumptions by taking into account the mobility of MUs and the energy replenishment of UAVs. Then, using the hierarchical multi-agent deep reinforcement learning (HMDRL), we develop a two-timescale based joint service-caching, computation-offloading, and UAVs flight trajectories scheme, called HMDRL-Based SCOFT. Using HMDRL-Based SCOFT, we derive UAVs' service-caching policies in each time frame, and then derive UAVs flight trajectories and MUs' computation-offloading in each time slot. Finally, we validate and evaluate the performances of our proposed HMDRL-Based SCOFT scheme through extensive simulations, which show that our developed scheme outperforms the other baseline schemes to converge faster and greatly reduce MUs' energy consumptions. © 2024 Elsevier Inc.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0861.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
