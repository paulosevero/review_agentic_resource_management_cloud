---
id: paper-2032
title: Cooperative Multiagent Deep Reinforcement Learning for Computation Offloading in Digital Twin Cyber-Physical-Social System
authors:
- Peng, Ziyu
- Xu, Yang
- Kang, Runyu
- Liu, Yaqin
- Zhang, Yaoxue
venue: IEEE Transactions on Computational Social Systems
venue_type: journal
year: 2025
doi: 10.1109/TCSS.2025.3548476
url: https://www.scopus.com/pages/publications/105000323217?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cooperative computation offloading
- digital twin (DT)
- multiagent deep reinforcement learning (MADRL)
- reputation model
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2032 — Cooperative Multiagent Deep Reinforcement Learning for Computation Offloading in Digital Twin Cyber-Physical-Social System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The widespread deployment of edge computing infrastructures has greatly advanced cyber-physical-social systems (CPSSs) by enabling computation offloading for various applications. However, the heterogeneous nature of edge servers (ESs) and the single-destination offloading strategy may limit the overall network performance. In this case, tasks are exclusively handled by the administrative ES, resulting in only marginal improvements in service quality, such as energy consumption and task delay. To fully exploit the advantages of edge computing, this article investigates the cooperation among ESs within CPSS and proposes a cooperative algorithm, named MATORA, to exploit a further performance gain by calculating the task offloading and resource allocation decisions. First, we formulate the joint optimization problem as a time-varying mixed integer nonlinear programming problem; then, we utilize the multiagent deep reinforcement learning (MADRL) to learn the action policy. Second, the MATORA novelly builds reputation model for each ES to obtain insightful knowledge based on service quality, enhancing the training efficiency of MADRL. Thirdly, we simulate a digital twin-based virtual system to monitor the physical network, in which a risk-free, centralized training environment is provided for the multiagent algorithm. Finally, the simulation results and analysis directly validate the effectiveness of our algorithm. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2032.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
