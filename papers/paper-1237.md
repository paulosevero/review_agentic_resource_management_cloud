---
id: paper-1237
title: 'Ratio-Based Offloading Optimization for Edge and Vehicular-Fog Federated Systems: A Multi-Agent TD3 Approach'
authors:
- Wakgra, Frezer Guteta
- Yahya, Widhi
- Kar, Binayak
- Lai, Yuan-Cheng
- Lin, Ying-Dar
- Tadele, Seifu Birhanu
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2024.3431549
url: https://www.scopus.com/pages/publications/85199324382?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17684--17696
keywords:
- Edge
- offloading
- optimization
- RL
- TD3
- vehicular-fog
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

# paper-1237 — Ratio-Based Offloading Optimization for Edge and Vehicular-Fog Federated Systems: A Multi-Agent TD3 Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge and vehicular-fog architectures enable a two-tier Multi-access Edge Computing (MEC) system, where computing resources are positioned behind base stations and vehicular-fog nodes are placed closer to user equipment (UE), resulting in lower latency compared to cloud alternatives. Vehicular-fog is a computing resource formed by a group of either stationary or mobile vehicles. In densely populated areas like congested intersections or festivals, UEs can generate concentrated hotspot traffic towards nearby MEC servers, potentially straining the access network MEC (AN-MEC) site behind the base station. To address this, a portion of the traffic can be offloaded, either vertically to nearby vehicular-fog nodes or horizontally to neighboring AN-MEC sites. The control plane rapidly determines traffic offloading locations and ratios within seconds, with the goal of minimizing average system latency. Our work proposes a reinforcement learning (RL)-based multi-agent TD3, which is built on top of the Twin-Delayed Deep Deterministic Policy Gradient (TD3) algorithm to determine optimal offloading ratios. Evaluation results underscore the remarkable decision-making speed of the multi-agent TD3-based approach, which surpasses the single-agent TD3 and simulated annealing (SA) methods by one and five orders of magnitude, respectively. Notably, the average latency of the multi-agent TD3 is better than that of the single-agent TD3, with only a marginal increase of 2 to 6 ms when compared to SA.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1237.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
