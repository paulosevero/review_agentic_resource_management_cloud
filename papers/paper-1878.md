---
id: paper-1878
title: Distributed Resource Management and Task Scheduling in MEC Networks Against Intelligent Eavesdropping Jammer
authors:
- Liu, Songyi
- Xu, Yuhua
- Wang, Ximing
- Li, Wen
- Li, Guoxin
- Li, Yangyang
- Gong, Yuping
- Zhang, Xiaokai
venue: IEEE Transactions on Communications
venue_type: journal
year: 2025
doi: 10.1109/TCOMM.2024.3487525
url: https://www.scopus.com/pages/publications/85208242798?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3364--3379
keywords:
- Mobile edge computing
- multi-agent reinforcement learning
- physical layer security
- resource allocation
- task scheduling
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

# paper-1878 — Distributed Resource Management and Task Scheduling in MEC Networks Against Intelligent Eavesdropping Jammer

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper focuses on distributed resource management and task scheduling for multi-access MEC networks against the intelligent eavesdropping jammer (IEJ). Due to the lack of a central controller, the problem of joint task scheduling and network resource allocation is formulated as a distributed multi-user hybrid-integer non-convex model. The optimization objective is to maximize users' satisfaction while meeting the Quality of Service (QoS) requirements of tasks and ensuring the high-reliable demands of data offloading. To overcome the challenge of partial observability for users, the channel observation matrix and Gramian Angular Field (GAF) are utilized to preprocess the limited channel state information and to mine the potential time-frequency characteristics of the external environment. Moreover, the hierarchical architecture and parallel networks are introduced for a parameterized redesign of the Multi-Agent Twin Delayed Deep Deterministic Policy Gradient (MATD3) method to improve the decision accuracy. Finally, simulation results demonstrate the superiority of the proposed algorithm over existing methods in terms of delay, energy consumption, and security. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1878.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
