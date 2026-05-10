---
id: paper-0505
title: 'HiveMind: Towards Cellular Native Machine Learning Model Splitting'
authors:
- Wang, Song
- Zhang, Xinyu
- Uchiyama, Hiromasa
- Matsuda, Hiroki
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2022
doi: 10.1109/JSAC.2021.3118403
url: https://www.scopus.com/pages/publications/85119627212?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 626--640
keywords:
- 5G mobile communication
- Edge computing
- machine learning (ML)
- neural networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0505 — HiveMind: Towards Cellular Native Machine Learning Model Splitting

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing processing load of today's mobile machine learning (ML) application challenges the stringent computation budget of mobile user equipment (UE). With the wide deployment of 5G edge-cloud, a new ML offloading scheme called split ML is provisioned to enable computation-intensive mobile ML applications by splitting an ML model across mobile UE, edge, and cloud. However, the complex split assignment problems pose new challenges for split ML system design. In this paper, we introduce HiveMind, the first practical multi-split ML system tailored for 5G cellular networks. HiveMind reformulates the complicated multi-split problem to a min-cost graph search and optimizes the distributed algorithm to drastically reduce the signaling overhead. Benefit from its low overhead property, HiveMind makes the optimal split decision on multiple computing nodes in real-time and adapts the split decisions to the instantaneous network dynamics. HiveMind also incorporates a multi-objective mechanism that accommodates heterogeneous objectives for a single ML task. HiveMind adapts to a wide range of ML frameworks, including non-linear models like Recurrent Neural Network (RNN), Federated Learning (FL), and Multi-agent Reinforcement Learning (MARL). We evaluate HiveMind on 5G MEC network simulators with realistic traffic patterns and real-life MEC computation/communication profiles. Our experiments demonstrate that HiveMind achieves the optimal efficiency comparing to state-of-art split ML designs.  © 1983-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0505.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
