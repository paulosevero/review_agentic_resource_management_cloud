---
id: paper-1387
title: Optimizing disaster response with UAV-mounted RIS and HAP-enabled edge computing in 6G networks
authors:
- Alotaibi, Jamal
- Oubbati, Omar Sami
- Atiquzzaman, Mohammed
- Alromithy, Fares
- Altimania, Mohammad Rashed
venue: Journal of Network and Computer Applications
venue_type: journal
year: 2025
doi: 10.1016/j.jnca.2025.104213
url: https://www.scopus.com/pages/publications/105005586095?origin=resultslist
publisher: Academic Press
pages: ''
keywords:
- 6G
- Disaster response
- Edge computing
- Reconfigurable intelligent surfaces (RIS)
- UAV
- Wireless energy transfer (WET)
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

# paper-1387 — Optimizing disaster response with UAV-mounted RIS and HAP-enabled edge computing in 6G networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the context of disaster response and recovery within 6th Generation (6G) networks, achieving both low-latency and energy-efficient communication under compromised infrastructure remains a critical challenge. This paper introduces a novel framework that integrates a solar-powered High-Altitude Platform (HAP) with multiple Unmanned Aerial Vehicles (UAVs) equipped with Reconfigurable Intelligent Surfaces (RISs), significantly enhancing disaster response capabilities. A hybrid approach combining game theory and multi-agent reinforcement learning (MARL) is employed to optimize UAV energy management, RIS control, and the offloading data rates of ground devices (GDs). Specifically, game theory is used to determine optimal task offloading decisions, balancing energy consumption, latency, and computational efficiency, while MARL dynamically guides UAV trajectories and RIS configurations to maintain robust communication links. A key innovation is the RIS ON/OFF mechanism, which conserves energy by switching OFF RISs when not needed, allowing UAVs to recharge during inactive periods and extending operational lifetimes. The proposed framework also demonstrates superior performance in optimizing offloading data rates and minimizing task offloading costs, ensuring efficient resource utilization. Extensive simulations validate the effectiveness of this approach, showing significant improvements in energy efficiency, data processing performance, and overall network reliability compared to traditional methods. These advancements contribute to more reliable and energy-efficient disaster response operations within 6G networks. © 2025 Elsevier Ltd

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1387.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
