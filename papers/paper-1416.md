---
id: paper-1416
title: 'Sustainable Task Offloading in Secure UAV-Assisted Smart Farm Networks: A Multi-Agent DRL With Action Mask Approach'
authors:
- Bao, Tingnan
- Syed, Aisha
- Sean Kennedy, William
- Erol-Kantarci, Melike
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2025
doi: 10.1109/TNSM.2024.3486288
url: https://www.scopus.com/pages/publications/85208272677?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3191--3200
keywords:
- deep reinforcement learning (DRL)
- energy consumption
- physical layer security
- Task offloading
- unmanned aerial vehicles (UAVs)
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

# paper-1416 — Sustainable Task Offloading in Secure UAV-Assisted Smart Farm Networks: A Multi-Agent DRL With Action Mask Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of unmanned aerial vehicles (UAVs) with mobile edge computing (MEC) and Internet of Things (IoT) technology is crucial for efficient resource management and sustainable agricultural productivity in smart frames. This paper addresses the critical need for optimizing task offloading in secure UAV-assisted smart farm networks, aiming to reduce total delay and energy consumption while maintaining robust security in data communications. We propose a multi-agent deep reinforcement learning (DRL)-based approach using a deep double Q-network (DDQN) with an action mask (AM), designed to manage task offloading dynamically and efficiently. Simulation results demonstrate the superior performance of our method in managing task offloading, highlighting significant improvements in operational efficiency, such as reduced delay and energy consumption. This aligns with the goal of developing sustainable and energy-efficient solutions for next-generation network infrastructures, making our approach an advanced solution for performance and sustainability in smart farming applications. © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1416.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
