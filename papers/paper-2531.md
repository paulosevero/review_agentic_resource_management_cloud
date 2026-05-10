---
id: paper-2531
title: DRL-based privacy-preserving video streaming task offloading under energy constraints in MEC
authors:
- Chen, Hongyi
- Peng, Yun
- Wei, Chen
- Meng, Tao
- Ai, Wei
- He, Zhixiong
- Li, Keqin
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112164
url: https://www.scopus.com/pages/publications/105031749872?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- DRL
- MEC
- Task offloading
- Video processing tasks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2531 — DRL-based privacy-preserving video streaming task offloading under energy constraints in MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid proliferation of video surveillance, autonomous driving, and smart home applications, video task offloading in Mobile Edge Computing (MEC) has attracted growing research interest. Compared with traditional cloud computing, MEC reduces latency and energy consumption by deploying computational resources closer to end devices. However, it also introduces two fundamental challenges: privacy leakage from untrusted edge servers and resource constraints that cause dynamic fluctuations in latency, energy consumption, and Quality of Service (QoS). Existing optimization and learning-based methods often fail to ensure privacy within energy limits or to balance multiple conflicting objectives under dynamic MEC conditions. To overcome these challenges, this paper addresses the core difficulty of jointly modeling and optimizing multi-objective (accuracy, latency, energy) and multi-constraint (privacy, energy cap) problems in MEC-based video task offloading, where privacy protection and resource limitations coexist. We formulate this as a Constrained Markov Game (CMG) and propose a novel Constrained Policy Optimization Multi-Agent Deep Deterministic Policy Gradient (CPO-MADDPG) algorithm. Extensive simulations demonstrate that CPO-MADDPG effectively mitigates privacy leakage, maintains energy constraints, and minimizes latency while maximizing video analysis accuracy. The proposed framework provides a unified and scalable solution to the long-standing trade-off between privacy protection and resource efficiency in dynamic MEC environments. © 2026

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2531.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
