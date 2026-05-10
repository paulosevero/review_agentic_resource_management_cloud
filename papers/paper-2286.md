---
id: paper-2286
title: Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks
authors:
- Wei, Yuting
- Ji, Zhe
- Wu, Sheng
- Jia, Haoge
- Xiao, Ailing
- Kuang, Linling
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3605153
url: https://www.scopus.com/pages/publications/105015582022?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- hierarchical reinforcement learning
- MATD3 algorithm for UAVs
- Space-air integrated edge computing
- task scheduling
- TD3-based controller for satellite-level coordination
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

# paper-2286 — Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In space–air–ground integrated networks (SAGINs), efficient task scheduling is critical to ensuring low latency and energy efficiency for computation-intensive applications. This paper proposes a hierarchical reinforcement learning (HRL)–based task scheduling framework for space–air integrated edge computing systems, consisting of low Earth orbit (LEO) satellites and unmanned aerial vehicles (UAVs). The architecture is structured into two layers: UAVs handle task reception and local execution, while satellites assist in offloaded task processing. To enable intelligent and decentralized decision-making, we employ a multi-agent twin delayed deep deterministic policy gradient (MATD3) algorithm for UAVs and a TD3-based controller for satellite-level coordination. A shared reward mechanism is introduced to promote cross-layer optimization. Simulation results demonstrate that the proposed framework significantly reduces task execution delay and energy consumption compared to baseline schemes, achieving faster convergence. These results verify the effectiveness and practicality of the proposed method in dynamic and resource-constrained space–air environments. The proposed method reduces average total cost (ATC) by at least 13% compared to existing methods. © 2014 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2286.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
