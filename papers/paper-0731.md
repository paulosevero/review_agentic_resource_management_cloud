---
id: paper-0731
title: Communication-Assisted Multi-Agent Reinforcement Learning Improves Task-Offloading in UAV-Aided Edge-Computing Networks
authors:
- Tan, Siyang
- Chen, Binqiang
- Liu, Dong
- Zhang, Jianglong
- Hanzo, Lajos
venue: IEEE Wireless Communications Letters
venue_type: journal
year: 2023
doi: 10.1109/LWC.2023.3316794
url: https://www.scopus.com/pages/publications/85173006271?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2233--2237
keywords:
- Multi-agent reinforcement learning
- trajectory planning
- UAV
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

# paper-0731 — Communication-Assisted Multi-Agent Reinforcement Learning Improves Task-Offloading in UAV-Aided Edge-Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Equipping unmanned aerial vehicles (UAVs) with computing servers allows the ground-users to offload complex tasks to the UAVs, but the trajectory optimization of UAVs is critical for fully exploiting their maneuverability. Existing studies either employ a centralized controller having prohibitive communication overhead, or fail to glean the benefits of interaction and coordination among agents. To circumvent this impediment, we propose to intelligently exchange critical information among agents for assisting their decision-making. We first formulate a problem for maximizing the number of offloaded tasks and the offloading fairness by optimizing the trajectory of UAVs. We then conceive a multi-agent deep reinforcement learning (DRL) framework by harnessing communication among agents, and design a communication-assisted decentralized trajectory control algorithm based on value-decomposition networks (VDN) for fully exploiting the benefits of messages exchange among agents. Simulation results demonstrate the superiority of the proposed algorithm over the state-of-the-art DRL-based algorithms.  © 2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0731.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
