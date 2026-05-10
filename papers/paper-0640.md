---
id: paper-0640
title: Adaptive Digital Twin for UAV-Assisted Integrated Sensing, Communication, and Computation Networks
authors:
- Li, Bin
- Liu, Wenshuai
- Xie, Wancheng
- Zhang, Ning
- Zhang, Yan
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2023
doi: 10.1109/TGCN.2023.3298039
url: https://www.scopus.com/pages/publications/85165896241?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1996--2009
keywords:
- Digital twin
- dual function radar and communication
- mobile edge computing
- proximal policy optimization
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

# paper-0640 — Adaptive Digital Twin for UAV-Assisted Integrated Sensing, Communication, and Computation Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we study a digital twin (DT)-empowered integrated sensing, communication, and computation network. Specifically, the users perform radar sensing and computation offloading on the same spectrum, while unmanned aerial vehicles (UAVs) are deployed to provide edge computing service. We first formulate a multi-objective optimization problem to minimize the beampattern performance of multi-input multi-output (MIMO) radars and the computation offloading energy consumption simultaneously. Then, we explore the prediction capability of DT to provide intelligent offloading decision, where the DT estimation deviation is considered. To track this challenge, we reformulate the original problem as a multi-agent Markov decision process and design a multi-agent proximal policy optimization (MAPPO) framework to achieve a flexible learning policy. Furthermore, the Beta-policy and attention mechanism are used to improve the training performance. Numerical results show that the proposed method is able to balance the performance tradeoff between sensing and computation functions, while reducing the energy consumption compared with the existing studies.  © 2017 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0640.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
