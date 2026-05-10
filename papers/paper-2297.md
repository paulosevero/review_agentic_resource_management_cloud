---
id: paper-2297
title: Multi-agent deep reinforcement learning for computation offloading in cooperative edge network
authors:
- Wu, Pengju
- Guan, Yepeng
venue: Journal of Intelligent Information Systems
venue_type: journal
year: 2025
doi: 10.1007/s10844-024-00907-3
url: https://www.scopus.com/pages/publications/105001952146?origin=resultslist
publisher: Springer
pages: 567--591
keywords:
- Computation offloading
- Mobile edge computing
- Multi-agent deep reinforcement learning
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

# paper-2297 — Multi-agent deep reinforcement learning for computation offloading in cooperative edge network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) has emerged as an effective paradigm for reducing latency and enhancing computational efficiency. However, the rapid proliferation of edge servers and user devices has significantly increased the complexity of task processing and resource management. Traditional task offloading approaches often rely on centralized decision-making, resulting in high computational complexity and time costs. To address these challenges, this paper introduces a dynamic collaborative framework involving multiple users and edge servers. We formulate the problem of resource allocation and task offloading as a multi-objective Markov Decision Process (MDP) with a mixed action space. To solve this, we propose a novel algorithm called Multi-Agent Mobile Edge Computing (MA-MEC), which leverages multi-agent reinforcement learning. In MA-MEC, each mobile edge server (MES) operates as an independent learning agent. Through centralized training and decentralized execution, these agents collaborate to develop efficient task offloading strategies in complex and dynamic edge environments. Simulation results demonstrate the effectiveness of our approach. MES agents learn to execute tasks more efficiently, increasing the number of processed tasks by 12.5%, while task offloading rates rise by 17%, and time costs are reduced by 53% compared to baseline methods. The proposed method shows significant advantages, especially in resource-constrained scenarios. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2297.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
