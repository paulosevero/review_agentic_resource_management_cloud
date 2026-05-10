---
id: paper-2457
title: Stackelberg Game-Based Multi-Agent Algorithm for Resource Allocation and Task Offloading in MEC-Enabled C-ITS
authors:
- Zhang, Shubin
- Tong, Xun
- Chi, Kaikai
- Gao, Wei
- Chen, Xiaolong
- Shi, Zhiguo
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3553487
url: https://www.scopus.com/pages/publications/105002021842?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17940--17951
keywords:
- Collaborative intelligent transportation systems
- mobile edge computing
- Stackelberg game
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
    my_justification: Game theory
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

# paper-2457 — Stackelberg Game-Based Multi-Agent Algorithm for Resource Allocation and Task Offloading in MEC-Enabled C-ITS

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of sixth-generation (6G) networks and artificial intelligence technologies is leading to the emergence of collaborative intelligent transportation systems (C-ITS), which is regarded as an essential trend in the future of transportation. Integrating Internet of Things (IoT) with C-ITS is an efficient solution to provide real-time data collection and status monitoring for vehicles and infrastructures to improve the intelligence and reliability of C-ITS. In order to address the challenges of limited battery energy and low computing power of IoT nodes, integrating wireless power transfer (WPT) with mobile edge computing (MEC) is considered as a promising solution to improve their lifetime and computational capability for IoT nodes. In this paper, we investigate a distributed dynamic computing offloading model for an MEC-enabled C-ITS, where multiple roadside units (RSUs) collaborate to provide offloading services to wireless devices (WDs). We formulate the task offloading and bandwidth resource allocation as a distributed Stackelberg game. The WDs act as leaders, aiming to maximize their computing rate by offloading tasks to RSU or performing local computing. The RSUs act as followers, optimizing their bandwidth allocation based on the WDs’ offloading decisions, thereby improving the overall system computing rate. We prove the existence of a Stackelberg equilibrium (SE) and propose a multi-agent reinforcement learning algorithm to enable WDs to select offloading decisions and help RSUs optimize bandwidth allocation. Numerical simulation results demonstrate that the proposed scheme offers significant performance improvements over existing methods. © 2000-2011 IEEE.

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
- **my_justification:** "Game theory"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2457.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
