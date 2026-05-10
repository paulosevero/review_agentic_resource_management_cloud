---
id: paper-1868
title: Adaptive UAV Deployment for Remote Iot Computation Offloading in Integrated Space-Air-Ground Networks
authors:
- Liu, Xiaomin
- Peng, Yujie
- Song, Tiecheng
- Song, Xiaoqin
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2025
doi: 10.1109/VTC2025-Spring65109.2025.11174651
url: https://www.scopus.com/pages/publications/105019039352?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- computation offloading
- multi-agent deep reinforcement learning (MADRL)
- SAGIN
- UAV deployment
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1868 — Adaptive UAV Deployment for Remote Iot Computation Offloading in Integrated Space-Air-Ground Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the realm of the Internet of Things (IoT), computation offloading confronts challenges in remote areas due to scarce general-purpose edge/cloud infrastructure and insufficient terrestrial network coverage. To address this, we introduce a novel space-air-ground integrated network (SAGIN) computing architecture, designed for the efficient offloading of computationintensive applications. Within this architecture, unmanned aerial vehicles (UAVs) conduct edge computing near users, while satellites act as a bridge to cloud computing resources. Given the limitations of UAVs in terms of battery capacity and dynamic network topology, their deployment strategy is crucial for maintaining service quality. Due to the impracticality of collecting global user information for centralized control of UAVs, we have conducted research on the adaptive deployment of UAVs under the condition that they rely solely on local observations. We propose a multi-agent softmax deep double deterministic policy gradient (MASD3) algorithm and comprehensively consider maximizing the uplink transmission rate of terrestrial IoT devices and reducing the energy consumption of UAVs during flight and communication in the optimization objective. Simulation results demonstrate that our proposed solution outperforms existing state-of-the-art baselines. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1868.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
