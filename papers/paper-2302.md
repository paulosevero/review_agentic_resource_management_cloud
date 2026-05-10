---
id: paper-2302
title: Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks
authors:
- Wu, Mengru
- Wu, Haonan
- Lu, Weidang
- Guo, Lei
- Lee, Inkyu
- Jamalipour, Abbas
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3574061
url: https://www.scopus.com/pages/publications/105006830737?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11046--11060
keywords:
- cooperative jamming
- deep reinforcement learning
- Mobile edge computing
- service placement
- unmanned aerial vehicles
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

# paper-2302 — Security-Aware Designs of Multi-UAV Deployment, Task Offloading and Service Placement in Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has emerged as a promising solution to support wireless devices’ computation-intensive services in the absence of terrestrial infrastructures. Nevertheless, the heterogeneous nature of MEC services and the security vulnerability of wireless channels present significant challenges to achieving efficient and secure computation offloading. In this paper, we investigate a multi-UAV-assisted MEC network in which wireless devices need to process diverse computation tasks. The devices can perform local computing or offload their computation tasks to UAV servers that have pre-cached relevant service programs in the presence of eavesdroppers. To facilitate secure service provisioning, we propose a cooperative jamming-based scheme in which a UAV jammer transmits jamming signals to interfere with eavesdroppers during devices’ computation offloading processes. Taking into account UAV servers’ constrained caching spaces and secure offloading requirements, we minimize the total task completion delay of devices by jointly optimizing multi-UAV deployment, task offloading decisions, service placement, UAV jammer’s transmit power, and devices’ transmit power. To tackle the formulated mixed-integer nonlinear programming problem, we design an optimization-embedding multi-agent twin delayed deep deterministic policy gradient (OE-MATD3) algorithm. Specifically, the MATD3 approach is leveraged to deal with optimization variables concerning UAVs, while a closed-form solution for devices’ transmit power is derived and guides MATD3-based decision-making. Simulation results demonstrate that the proposed scheme outperforms baselines in terms of devices’ task completion delay. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2302.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
