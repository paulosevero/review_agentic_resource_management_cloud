---
id: paper-1945
title: A Multi-Agent Deep Reinforcement Learning Framework for MEC Resource Allocation in 5G Networks
authors:
- Meghamala, Y.
- Pulipati, John Paul
- Kumar, M Aravind
venue: International Journal of Electrical and Electronics Research
venue_type: journal
year: 2025
doi: 10.37391/IJEER.130431
url: https://www.scopus.com/pages/publications/105028207047?origin=resultslist
publisher: Forex Publication
pages: 909--919
keywords:
- 5G
- DRL
- MEC
- Resource Allocation
- SAC Model
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

# paper-1945 — A Multi-Agent Deep Reinforcement Learning Framework for MEC Resource Allocation in 5G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper introduces a multi-agent Deep Reinforcement Learning (DRL)-based model of allocating resources in 5G MEC networks based on the Soft Actor-Critic (SAC) algorithm and the hierarchical MATD3/TD2PG-based actor-critic network. The model distributes sub-channels, power of transmission and MEC computing resources with taking into account user mobility and isolation of the slices. The Python simulation is provided with a Manhattan 5G environment comprising of four interconnected gNodeBs, 5 densities of users (327, 499, 596, 930 and 1088 users), and two MEC classes of service (security and entertainment) with predefined bandwidth, memory, and processing requirements. It is assessed against three baselines: Greedy, Best-fit and Worst-fit allocation strategies in three measures; number of services served, services blocked and services denied. Findings indicate that SAC-based allocation improves the number of services served by 8-14, blocked by 15-22 and denied services by 18-20, respectively, with respect to user density. The advantages of these results support that the suggested multi-agent model, which is SAC-based, offers a measurable performance increase in the given dynamic traffic and heterogeneous service conditions. © 2025 by Meghamala Y, Pulipati John Paul, and M Aravind Kumar.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1945.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
