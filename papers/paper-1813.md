---
id: paper-1813
title: Multiagent Reinforcement-Learning-Based AAV Path and Resource Allocation for Ground-to-Air Communication Network
authors:
- Li, Kuixian
- Fan, Haodong
- Yang, Yandie
- Wang, Chen
- Gao, Qiling
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3602122
url: https://www.scopus.com/pages/publications/105015341287?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 44243--44254
keywords:
- Energy optimization
- mobile edge computing (MEC)
- multiagent systems
- reinforcement learning (RL)
- resource scheduling
- trajectory optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1813 — Multiagent Reinforcement-Learning-Based AAV Path and Resource Allocation for Ground-to-Air Communication Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid expansion of the Internet of Things (IoT) and the increasing unmanned devices, data transmission and sharing between unmanned agents in the Internet of Unmanned Agents (IUA) face significant challenges. mobile edge computing (MEC), which extends computing power from the cloud to the network edge, has become a key technology for enabling efficient, low-latency communication services. However, with the surge in the number of terminal devices and the diversification of service requirements, traditional MEC deployment methods face challenges, such as inflexible resource allocation and limited service coverage. This article mainly researches an autonomous aerial vehicle (AAV)-assisted ground-to-air communication and computing system, constructs a multi-AAV network communication model and a computing model, and proposes a joint optimization problem of system task processing delay and energy consumption based on the total system delay and the energy consumption of the AAV. For the path planning and resource allocation problems of the multi-AAV network, an improved double-delay deep deterministic policy gradient algorithm is proposed to jointly optimize the trajectory planning, user association and task offloading strategies of the multiagent AAV. Finally, the performance of the proposed algorithm is verified and analyzed through simulation experiments. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1813.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
