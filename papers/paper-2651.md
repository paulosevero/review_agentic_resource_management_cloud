---
id: paper-2651
title: 'DT-MASAC: A Digital Twin-Augmented Multi-Agent Framework for AoI-Oriented Resource Allocation in Vehicular Networks'
authors:
- Lan, Jun
- Jia, Xiangdong
- Chen, Kuan
- Qu, Jingtao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3665539
url: https://www.scopus.com/pages/publications/105030713545?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Age of Information
- Digital Twin
- Multi-Agent Reinforcement Learning
- Resource Allocation
- Vehicular Edge Computing
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

# paper-2651 — DT-MASAC: A Digital Twin-Augmented Multi-Agent Framework for AoI-Oriented Resource Allocation in Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) networks supporting delay-sensitive services face fundamental challenges in maintaining information freshness under high mobility, bursty task arrivals, and limited communication and computation resources. This paper investigates an Age of Information (AoI)-oriented resource allocation problem in digital twin (DT)-empowered VEC systems, where task offloading, wireless transmission, and computation scheduling are tightly coupled across time. To address the limitations of reactive and myopic optimization, we propose a DT-augmented multi-agent soft actor-critic (DT-MASAC) framework that explicitly embeds AoI dynamics and DT-based predictive features into cooperative multi-agent learning. The DT layer provides short-term foresight of channel conditions and edge resource availability, enabling agents to make proactive and uncertainty-aware decisions. A joint AoI-energy minimization problem is formulated under realistic communication, computation, and deadline constraints, and solved via centralized training with decentralized execution. Extensive simulations demonstrate that the proposed DT-MASAC framework achieves superior AoI stability and energy efficiency compared with state-of-the-art baselines, particularly in highly dynamic vehicular environments.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2651.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
