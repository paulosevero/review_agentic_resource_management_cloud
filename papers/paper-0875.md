---
id: paper-0875
title: Deep Reinforcement Learning for Smart Home Temperature Comfort in IoT-Edge Computing Systems
authors:
- Christopoulos, Marios
- Spantideas, Sotirios
- Giannopoulos, Anastasios
- Trakadas, Panagiotis
venue: 'MECC 2024 - Proceedings of the 1st International Workshop on MetaOS for the Cloud-Edge-IoT Continuum, Part of: EuroSys 2024'
venue_type: conference
year: 2024
doi: 10.1145/3642975.3678961
url: https://www.scopus.com/pages/publications/85201683868?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 1--7
keywords:
- Deep Reinforcement Learning (DRL)
- Energy Management
- Heating Ventilation and Air Conditioning (HVAC) systems
- IoT-Edge-Cloud Continuum (IEC)
- Smart Home
- Temperature Comfort
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0875 — Deep Reinforcement Learning for Smart Home Temperature Comfort in IoT-Edge Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, a novel IoT-Edge-Cloud (IEC) computing system designed for multiple Smart Homes is introduced, with a focus on supporting Home Energy Management Systems (HEMS) for temperature control within a defined comfort range. Leveraging model-free deep reinforcement learning, the proposed method, Smart Home Energy and Temperature Control (SHETEC), employs autonomous agents which are trained to manipulate the input power of Heating, Ventilation, and Air Conditioning (HVAC) systems and charging/discharging power of Energy Storage Systems (ESS) using Deep Deterministic Policy Gradients (DDPG). In addition, we present the Average Opinion (AO) method, a collaborative decision-making approach that combines the models of all Smart Homes in a distributed approach. Experimental results, conducted through simulation on three Smart Homes using real-world heterogeneous data, demonstrate the effectiveness of both SHETEC and Average Opinion in maintaining temperatures within the desired comfort bounds. © 2024 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0875.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
