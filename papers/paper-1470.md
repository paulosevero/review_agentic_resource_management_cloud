---
id: paper-1470
title: Joint Optimization for Cooperative Service-Caching, Computation-Offloading, and Resource-Allocations Over EH/MEC 6G Ultra-Dense Mobile Networks
authors:
- Chen, Zhian
- Wang, Fei
- Zhang, Xi
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2025
doi: 10.1109/TWC.2025.3549415
url: https://www.scopus.com/pages/publications/105000071624?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5780--5795
keywords:
- computation-offloading
- cooperative service-caching
- EH/MEC-based 6G UDNs
- HMDRL
- resource-allocations
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

# paper-1470 — Joint Optimization for Cooperative Service-Caching, Computation-Offloading, and Resource-Allocations Over EH/MEC 6G Ultra-Dense Mobile Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Service-caching, computation-offloading, and mobile edge-computing (MEC) have been widely recognized as three key 6G mobile wireless neworking techniques which can efficiently support implementing the ultra-dense networks (UDNs) with massive small-cell base stations (SBSs). But, these impose the new challenges for the UDNs to solely rely on grid power for energy supplying and to jointly optimize service-caching, computation-offloading, and resource-allocations. To overcome the above described difficulties, integrating energy-harvesting (EH) techniques with MEC-enabled 6G UDNs, we propose to develop the joint optimization schemes for cooperative service-caching, computation-offloading, and resource-allocations. In our considered UDNs, there exist a large number of EH-based stationary users (SUs) or mobile users (MUs), and a mixture of on-grid SBSs powered by electric grid and off-grid SBSs power-supplied by solar, radio frequency (RF) energy, etc. Specifically, first we formulate an energy minimization problem under a non-linear RF-energy EH model to minimize the sum of weighted energy consumption of users and off-grid SBSs. Second, for scenarios with SUs, we develop a two-timescale based joint cooperative service-caching, computation-offloading, and resource-allocations scheme using the hierarchical multi-agent deep reinforcement learning. We derive cooperative service-caching in each time frame, and then derive computation-offloading and resource-allocations in each time slot. Third, we extend our work to scenarios with MUs, where MUs can move with certain trajectories at low speeds. Finally, we validate and evaluate the performances of our proposed schemes through the extensive simulations. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1470.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
