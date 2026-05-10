---
id: paper-2657
title: Collaborative Optimization Scheduling Strategy of Electric Vehicle Load Cluster and Data Center for Multi-Station Integration
authors:
- Li, Siwei
- Yuan, Shuai
- Guo, Shulin
- Yu, Jiancheng
- Pei, Xiaolu
- Zhang, Zhida
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3668920
url: https://www.scopus.com/pages/publications/105031629372?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 36414--36429
keywords:
- electric vehicles
- Multi-station convergence
- reinforcement learning
- smart energy stations
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

# paper-2657 — Collaborative Optimization Scheduling Strategy of Electric Vehicle Load Cluster and Data Center for Multi-Station Integration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To harness the collaborative advantages of integrated multi-station smart energy hubs and mitigate their carbon footprint, this study investigates dense urban travel patterns and addresses privacy concerns inherent in traditional centralized grid dispatch systems. We propose a distributed dispatch optimization framework for smart energy stations leveraging multi-agent deep reinforcement learning. For the first time, an optimal carbon emissions decision model is introduced, synthesizing human social behavior at edge data centers, electric vehicle charging dynamics, and active distribution network operations. The multi-station carbon optimization challenge is reformulated as a Decentralized Partially Observable Markov Decision Process (DEC-POMDP), resolved through an Actor-Critic-based decentralized execution framework. This approach enables real-time scheduling where stations autonomously make decisions while collaboratively processing raw user data locally to ensure privacy preservation. Furthermore, spatial migration of data center computing tasks and coordinated vehicle charging-discharging strategies effectively address the dual volatility arising from stochastic renewable energy generation and electric vehicle load fluctuations. Experimental results demonstrate that our method fully exploits the synergistic potential between electric vehicles and data centers, significantly enhancing clean energy utilization and reducing carbon emissions across smart energy stations. © 2013 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2657.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
