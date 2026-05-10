---
id: paper-0939
title: 'RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering'
authors:
- Gui, Fei
- Wang, Songtao
- Li, Dan
- Chen, Li
- Gao, Kaihui
- Min, Congcong
- Wang, Yi
venue: ACM SIGCOMM 2024 - Proceedings of the 2024 ACM SIGCOMM 2024 Conference
venue_type: conference
year: 2024
doi: 10.1145/3651890.3672231
url: https://www.scopus.com/pages/publications/85202299053?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 71--85
keywords:
- machine learning
- network optimization
- traffic engineering
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0939 — RedTE: Mitigating Subsecond Traffic Bursts with Real-time and Distributed Traffic Engineering

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet traffic bursts usually happen within a second, thus conventional burst mitigation methods ignore the potential of Traffic Engineering (TE). However, our experiments indicate that a TE system, with a sub-second control loop latency, can effectively alleviate burst-induced congestion. TE-based methods can leverage network-wide tunnel-level information to make globally informed decisions (e.g., balancing traffic bursts among multiple paths). Our insight in reducing control loop latency is to let each router make local TE decisions, but this introduces the key challenge of minimizing performance loss compared to centralized TE systems.In this paper, we present RedTE, a novel distributed TE system with a control loop latency of < 100ms, while achieving performance comparable to centralized TE systems. RedTE's innovation is the modeling of TE as a distributed cooperative multi-agent problem, and we design a novel multi-agent deep reinforcement learning algorithm to solve it, which enables each agent to make globally informed decisions solely based on local information. We implement real RedTE routers and deploy them on a WAN spanning six city datacenters. Evaluation reveals notable improvements compared to existing solutions: < 100ms of control loop latency, a 37.4% reduction in maximum link utilization, and a 78.9% reduction in average queue length.  © 2024 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0939.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
