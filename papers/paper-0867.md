---
id: paper-0867
title: 'SpaceEdge: Optimizing Service Latency and Sustainability for Space-Centric Task Offloading in LEO Satellite Networks'
authors:
- Chen, Jia-Hong
- Kuo, Wei-Che
- Liao, Wanjiun
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2024.3429510
url: https://www.scopus.com/pages/publications/85200816034?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15435--15446
keywords:
- deep reinforcement learning
- LEO satellite
- power allocation
- service migration
- SpaceEdge
- task offloading
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

# paper-0867 — SpaceEdge: Optimizing Service Latency and Sustainability for Space-Centric Task Offloading in LEO Satellite Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low Earth Orbit (LEO) satellite networks are expected to enable global connectivity for next-generation communications. To provide space-centric solutions, the limited coverage time and limited resources of LEO satellites pose challenges to maintaining service continuity and ensuring low latency for users. Furthermore, LEO satellites rely on solar panels to obtain energy, so a balance needs to be struck between energy consumption and service provision for satellite mobile edge computing. In this paper, we aim to achieve space-centric computational task offloading in LEO satellite networks. The goal is to minimize end-to-end task offloading latency while considering the constraints posed by the limited onboard computing, storage, and energy resources in constantly moving LEO satellites. To achieve this, we formulate a joint problem of service migration and power control in energy-harvesting LEO satellite networks. The problem is then converted into a Markov decision process (MDP) and solved with SpaceEdge, a novel algorithm based on Deep Reinforcement Learning (DRL). SpaceEdge offers supports for both centralized learning and multi-agent learning. Simulation results show that SpaceEdge, particularly the multi-agent model, outperforms existing solutions, demonstrating its effectiveness in deploying space-centric task offloading services in LEO satellite networks. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0867.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
