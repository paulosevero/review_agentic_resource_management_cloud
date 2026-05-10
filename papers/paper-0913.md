---
id: paper-0913
title: 'TacNet: A Tactic-Interactive Resource Allocation Method for Vehicular Networks'
authors:
- Fu, Xiaoyuan
- Yuan, Quan
- Zhuang, Zirui
- Li, Yang
- Liao, Jianxin
- Zhao, Dongmei
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3345853
url: https://www.scopus.com/pages/publications/85181565841?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 14370--14382
keywords:
- Digital twin (DT)
- multiagent deep reinforcement learning (MADRL)
- resource allocation
- vehicular networks
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

# paper-0913 — TacNet: A Tactic-Interactive Resource Allocation Method for Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To support safety driving and various on-board services, efficient resource allocation is crucial for the promising implement of vehicle platooning in intelligent transportation systems (ITSs). The resource allocation of vehicle-to-everything (V2X) communications for vehicular platoons is studied in this article. First, a multiobjective function is formulated to jointly optimize sub-band and power allocation to satisfy Quality-of- Service (QoS) in vehicular networks. With the advantage of dealing with complex decision-making problems in multiagent systems, distributed multiagent deep reinforcement learning (MADRL) stands out for resource allocation of vehicular networks. However, it faces the challenge of cooperation aging when every agent is only learning from information of others to form a cooperation model in the training process. Considering the random and dynamic combination of vehicles in vehicle platooning, a tactic-interactive MADRL method named as TacNet is then proposed to improve the cooperation efficiency of multiple agents. In TacNet, the tactics of other agents will be encoded and transmitted through interactive communications among agents. In addition, with the development of vehicular edge computing (VEC), digital twin (DT) networks are constructed to assist offloading computation-intensive resource allocation tasks in vehicles to the edge. The superiority of the proposed method is verified through extensive simulation results, which refers to convergence and performance of satisfying diversified QoS requirements compared with state-of-the-art MADRL methods.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0913.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
