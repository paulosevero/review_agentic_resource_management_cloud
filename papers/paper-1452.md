---
id: paper-1452
title: MAPPO for Edge Server Monitoring
authors:
- Chamoun, Samuel
- McDowell, Christian
- Buchanan, Robin
- Chan, Kevin
- Graves, Eric
- Sun, Yin
venue: Proceedings - IEEE Military Communications Conference MILCOM
venue_type: conference
year: 2025
doi: 10.1109/MILCOM64451.2025.11310582
url: https://www.scopus.com/pages/publications/105031776050?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cooperative communication
- Costs
- Decision making
- Edge computing
- Electric load dispatching
- Observability
- Optimization
- Problem solving
- Query processing
- Throughput
- Centralised
- Communication problems
- Edge server
- Finite queue
- Finite-time
- Goal-oriented communication
- Multi agent
- Policy optimization
- Server monitoring
- Time-varying availability
- Multi agent systems
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1452 — MAPPO for Edge Server Monitoring

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we consider a goal-oriented communication problem for edge server monitoring, where jobs arrive intermittently at multiple dispatchers and must be assigned to shared edge servers with finite queues and time-varying availability. Accurate knowledge of server status is critical for sustaining high throughput, yet remains challenging under dynamic workloads and partial observability. To address this challenge, each dispatcher maintains server knowledge through two complementary mechanisms: (i) active status queries that provide instantaneous updates at a communication cost, and (ii) job execution feedback that reveals server conditions upon successful or failed job completion. We formulate a cooperative multi-agent distributed decision-making problem in which dispatchers jointly optimize query scheduling to balance throughput against communication overhead. To solve this problem, we propose a Multi-Agent Proximal Policy Optimization (MAPPO)-based algorithm that leverages centralized training with de-centralized execution (CTDE) to learn distributed query-and-dispatch policies under partial and stale observations. Experiments show that MAPPO achieves superior throughput-cost tradeoffs and significantly outperforms baseline strategies across varying query costs, job arrival rates, and dispatchers.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1452.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
