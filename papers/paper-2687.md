---
id: paper-2687
title: Multi-Agent Reinforcement Learning-Based Task Offloading with Evolutionary Game Theory for User Association in Edge Computing
authors:
- Liu, Haoran
- Li, Deqiang
venue: 2026 6th International Conference on Consumer Electronics and Computer Engineering, ICCECE 2026
venue_type: conference
year: 2026
doi: 10.1109/ICCECE69169.2026.11399759
url: https://www.scopus.com/pages/publications/105035989541?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 454--460
keywords:
- Edge Computing
- Evolutionary Game Theory
- Heterogeneous Networks
- Multi-Agent Reinforcement Learning
- Task Offloading
- User Association
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2687 — Multi-Agent Reinforcement Learning-Based Task Offloading with Evolutionary Game Theory for User Association in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Heterogeneous networks, which integrate diverse access nodes such as base stations, WiFi access points, and unmanned aerial vehicles (UAVs), provide an effective solution to address the computational bottlenecks of mobile devices in edge computing. The differences in coverage, bandwidth, and channel characteristics among network nodes enable flexible resource allocation and expanded service coverage. This paper proposes a novel two-stage optimization framework that integrates evolutionary game theory with Multi-Agent Soft ActorCritic (MASAC) for user association and task offloading in heterogeneous edge computing environments comprising base stations, WiFi APs, and UAVs. In the first stage, we model user association as an evolutionary game to achieve Nash equilibrium among users, enabling stable and efficient allocation of users to access nodes. In the second stage, we formulate the task offloading problem as a multi-Agent reinforcement learning (MARL) problem and employ MASAC to optimize offloading decisions based on the user association results. Experimental results demonstrate that our proposed approach outperforms existing methods (MATD3, MADDPG) with 38.5% improvement in reward, 33.6% reduction in latency, and 24.7% decrease in energy consumption compared to MATD3, and 75.1%, 58.1%, and 48.4% improvements compared to MADDPG, respectively. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2687.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
