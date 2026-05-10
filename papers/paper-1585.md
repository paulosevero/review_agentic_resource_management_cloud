---
id: paper-1585
title: Multi-Agent Reinforcement Learning-Based Routing and Scheduling Models in Time-Sensitive Networking for Internet of Vehicles Communications Between Transportation Field Cabinets
authors:
- Garcia-Cantón, Sergi
- Ruiz de Mendoza, Carlos
- Cervelló-Pastor, Cristina
- Sallent, Sebastià
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/app15031122
url: https://www.scopus.com/pages/publications/85217826256?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- DRL
- I2I
- IoV
- MARL
- routing and scheduling optimization
- RSU
- SDN
- smart road side infrastructure
- TMC
- TMS
- TSN
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1585 — Multi-Agent Reinforcement Learning-Based Routing and Scheduling Models in Time-Sensitive Networking for Internet of Vehicles Communications Between Transportation Field Cabinets

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Future autonomous vehicles will interact with traffic infrastructure through roadside units (RSUs) directly connected to transportation field cabinets (TFCs). These TFCs must be interconnected to share traffic information, enabling infrastructure-to-infrastructure (I2I) communications that are reliable, synchronous and capable of transmitting vehicle data to the Internet. However, I2I communications present a complex optimization challenge. This study addresses this by proposing the design, implementation, and evaluation of an automated management model for I2I service channels based on multi-agent reinforcement learning (MARL) integrated with deep reinforcement learning (DRL). The proposed models efficiently manage the routing and scheduling of data frames between internet of vehicles (IoV) infrastructure devices through time-sensitive networking (TSN) to ensure real-time synchronous I2I communications. The solution incorporates both a routing model and a scheduling model, evaluated in a simulated shared environment where agents operate within the TSN control plane. Both models are tested for different topologies and background traffic levels. The results demonstrate that the models establish the majority of paths in the scenario, adhering to near-optimal routing and scheduling policies. Recursively, for each individual request to create a service channel, the system establishes online an optimal synchronous path between entities with a limited time budget. In total, 71% of optimal routing paths are established and 97% of optimal schedules are achieved. The approach takes into account the periodic nature of the transmitted data and its robustness through TSN networks, obtaining 99 percent of compliant service requests with flow jitter levels below 100 microseconds for different topologies and different network utility percentages. The proposed solution achieves lower execution delays compared to the iterative ILP approach. Additionally, the solution facilitates the integration of 5G networks for vehicle-to-infrastructure (V2I) communications, which is identified as an area for future exploration. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1585.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
