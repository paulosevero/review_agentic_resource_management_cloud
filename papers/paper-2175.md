---
id: paper-2175
title: 'Aerial Reconfigurable Intelligent Surface-Aided MEC Networks with Ultra-Reliable Low-Latency Communications: A Digital Twin Approach'
authors:
- Su, Weirui
- Tan, Fangqing
- Li, Shichao
- Chen, Hongbin
venue: 2025 IEEE/CIC International Conference on Communications in China, ICCC Workshops 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCCWorkshops67136.2025.11148088
url: https://www.scopus.com/pages/publications/105017760376?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Digital twin
- mobile edge computing
- multi-agent deep deterministic policy gradient
- reconfigurable intelligent surface
- unmanned aerial vehicle
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

# paper-2175 — Aerial Reconfigurable Intelligent Surface-Aided MEC Networks with Ultra-Reliable Low-Latency Communications: A Digital Twin Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of digital twin (DT) and mobile edge computing (MEC) has emerged as a promising paradigm for enabling the rapid development of edge intelligence in 6G, which has been recognized as the key enabler for ultra-reliable low-latency communications (URLLC). However, the limited resources of MEC nodes and dynamic network environments pose significant challenges to conventional resource allocation schemes. This paper investigates a DT-driven aerial reconfigurable intelligent surface (RIS)-aided MEC network with ultra-reliable low-latency communications, where an unmanned aerial vehicle (UAV) is deployed to carry RIS for assisting computation offloading from user equipments (UEs) to edge servers. To minimize the system latency and energy consumption, we design a deep reinforcement learning framework based on multi-agent deep deterministic policy gradient (MADDPG) that enables edge nodes and UEs to automatically learn optimal strategies by exploiting DT-provided information, which effectively optimizes offloading decisions, computation resource, UEs' transmission power, RIS phase shifts, and the UAV's trajectory. Simulation results demonstrate that our approach significantly reduces system latency and energy consumption compared to benchmark methods. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2175.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
