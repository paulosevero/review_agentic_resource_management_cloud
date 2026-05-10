---
id: paper-2024
title: A Multi-Agent Federated DRL Model for Vehicular Task Offloading in WPT-Aided eROAD Environment
authors:
- Paul, Anal
- Singh, Keshav
- Li, Chih-Peng
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3537983
url: https://www.scopus.com/pages/publications/85217898587?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17723--17739
keywords:
- deep reinforcement learning
- distributed edge computing
- electrified roads
- federated learning
- Intelligent transport systems
- privacy-preserving
- terrestrial and non-terrestrial networks
- vehicular task offloading
- wireless power transfer
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

# paper-2024 — A Multi-Agent Federated DRL Model for Vehicular Task Offloading in WPT-Aided eROAD Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper introduces a novel multi-agent federated deep reinforcement learning (MA-FDRL) framework designed to minimize vehicular task offloading latency in electrified road (eROAD) environments. The solution integrates inductive coil-based wireless power transfer (WPT) systems with full duplex multiple input and multiple output (MIMO) vehicular networks, enabling continuous charging and reducing computational delays for electric vehicles (EVs) on eROADs. The MA-FDRL framework optimizes the offloading of vehicular tasks, with support from base stations (BS), unmanned aerial vehicles (UAVs), and satellites, while ensuring data privacy through differential privacy techniques. By intelligently distributing resources across these supporting entities, the framework enhances the efficiency of task processing. Key challenges such as dynamic wireless charging, intermittent BS coverage, and privacy-preserving task offloading are addressed using a comprehensive WPT framework, a mobility model, and a differential privacy-enhanced MA-FDRL algorithm. The proposed MA-FDRL solution effectively reduces the latency of vehicle task offloading by 17.05% over proximal policy optimization (PPO) algorithm, ensures balanced task distribution between edge servers, and offers a scalable and privacy-preserving approach for future autonomous electric vehicles and connected wireless environments. © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2024.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
