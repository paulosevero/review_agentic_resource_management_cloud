---
id: paper-0243
title: Intelligent Resource Allocation in UAV-Enabled Mobile Edge Computing Networks
authors:
- Wang, Meng
- Shi, Shuo
- Gu, Shushi
- Zhang, Ning
- Gu, Xuemai
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2020
doi: 10.1109/VTC2020-Fall49728.2020.9348573
url: https://www.scopus.com/pages/publications/85101404929?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- intelligent resource allocation
- mobile edge computing
- reinforcement learning
- UAV communications
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0243 — Intelligent Resource Allocation in UAV-Enabled Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) have been considered as effective flying base stations (FBSs) to provide on- demand wireless communications. Equipped with computation resource, UAVs are also capable of offering computation offloading opportunities for the mobile users (MUs) in mobile edge computing (MEC) networks. However, due to the small hardware and load capacity, UAVs can only supply limited computation and energy resource. It is thus challenging for UAVs to guarantee the quality of service (QoS) of MUs, while minimizing their total resource consumptions. Toward this end, instead of using all resource for every single task, we propose an intelligent resource allocation algorithm based on reinforcement learning, which enables UAVs to make energy-efficent and computation-efficent allocation decisions intelligently. Then, we take UAVs as learning agents by forming resource allocation decisions as actions and designing a reward function with the aim of minimizing the weighted resource consumptions. Each UAV performs the algorithm only based on its local observations without information exchange among different UAVs. Simulation results show that the proposed reinforcement learning based approach outperforms the benchmark algorithms in terms of weighted consumptions in a whole time period. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0243.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
