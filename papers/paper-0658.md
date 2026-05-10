---
id: paper-0658
title: Mobility-Aware Dynamic Service Migration in Communication and Computing Integrated VNETs
authors:
- Liu, Haoran
- Jiang, Ning
- Guo, Fengxian
- Yan, Shi
- Peng, Mugen
venue: 2023 IEEE Globecom Workshops, GC Wkshps 2023
venue_type: conference
year: 2023
doi: 10.1109/GCWkshps58843.2023.10465221
url: https://www.scopus.com/pages/publications/85190254421?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2061--2066
keywords:
- communication and computing integrated vehicular networks
- mobility-aware
- resource allocation
- Service migration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0658 — Mobility-Aware Dynamic Service Migration in Communication and Computing Integrated VNETs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Communication and computing integrated vehicular networks have emerged as a reliable platform for intelligent vehicular applications. These networks leverage mobile edge computing technology to enable computing capabilities at the network edge closer to vehicles. However, the mobility of vehicles could break service continuity and make it difficult to accomplish intelligent services within tolerant latency under communication and computing resource-constrained conditions. To overcome these challenges, this paper proposes a mobility-aware service migration approach to effectively reduce service latency under the expected migration cost constraint. The key aspect of this approach is leveraging the mobility information of vehicles to search for the best migration strategy. This paper utilizes the wireless sensing technology of the base stations to acquire real-time mobility information of vehicles. The mobility information and channel states are jointly considered to make decisions on service migration as well as resource allocation strategies via a decentralized multi-agent proximal policy optimization (MAPPO) algorithm. Simulation results demonstrate that the proposed mobility-aware service migration approach can effectively reduce the average service latency compared to other benchmark approaches.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0658.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
