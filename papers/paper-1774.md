---
id: paper-1774
title: A multi-Agent Deep Reinforcement Learning -based Task Offloading Strategy for LEO-MEC-Assisted UAV Systems
authors:
- Li, Yuxuan
- Xiong, Ting
- Zhu, Shibing
- Sun, Bin
- Sun, Xiya
- Li, Yuwei
- Dai, Jianmei
venue: ICCIP 2024 - 2024 the 10th International Conference on Communication and Information Processing
venue_type: conference
year: 2025
doi: 10.1145/3708657.3708670
url: https://www.scopus.com/pages/publications/105010681574?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 87--92
keywords:
- computing offloading
- deep reinforcement learning
- LEO satellites
- Unmanned aerial vehicle
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

# paper-1774 — A multi-Agent Deep Reinforcement Learning -based Task Offloading Strategy for LEO-MEC-Assisted UAV Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) have already been promising components for providing enhanced coverage in wireless environments. However, UAVs suffer from constrained computing resources, hindering their ability to undertake delay-sensitive and computation-intensive tasks. In this paper, we propose a Low Earth Orbit (LEO)-Multi-access Edge Computing (MEC)-Assisted UAV system, which utilizes the MEC-enabled LEO satellites to assist UAVs in processing various tasks. Considering the limited power and energy of LEO satellites, we formulate a joint resource allocation and offloading decision-making problem to minimize the total delay of task execution, which is a Mixed-Integer NonLinear Programming (MINLP) problem. Due to the non-convexity, we convert the problem into a Markov Decision Process (MDP) and propose a Multi-Agent Proximal Policy Optimization (MAPPO)-based algorithm to derive efficient offloading strategies. Our simulation results demonstrate that the proposed algorithm effectively converges and achieves the minimum delay compared to other schemes. © 2024 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1774.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
