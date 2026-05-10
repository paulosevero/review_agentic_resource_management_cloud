---
id: paper-2427
title: Distributed Task Scheduling Algorithm Based on MADDPG in MEC Emergency Networks
authors:
- Zhang, Gaowei
- Song, Junping
- Hu, Yahui
- Fan, Pengfei
- Li, Chong
- Zhou, Xu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3581514
url: https://www.scopus.com/pages/publications/105008805333?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 44692--44704
keywords:
- Distributed task scheduling
- mobile edge computing (MEC) emergency networks
- multiagent deep reinforcement learning
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
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

# paper-2427 — Distributed Task Scheduling Algorithm Based on MADDPG in MEC Emergency Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In resource-constrained emergency networks, task scheduling algorithms play a crucial role in allocating computational tasks and managing data transmission. Currently, centralized scheduling algorithms face the risk of single-point failures and incur significant overhead in maintaining global computational node states and network topology. Distributed scheduling algorithms typically assume a fixed network topology, making them less adaptable to highly dynamic environments with constantly changing node capabilities and network conditions. To address these challenges, this article proposes a multiagent deep deterministic policy gradient (MADDPG)-based distributed task scheduling algorithm (MATS). The algorithm deploys an agent on each computational node, which only perceives real-time states of adjacent nodes and links, thereby reducing the overhead of maintaining network states. This article designs an asymmetric multiagent structure to accommodate computational nodes with varying performance, introduces a dual-buffer pool structure to accelerate model convergence, and develops an agent action mechanism independent of node scale to enhance adaptability to dynamic network topology changes. Experimental results demonstrate that MATS significantly outperforms existing centralized and distributed approaches in handling node dynamics while achieving task average processing latency comparable to optimal centralized algorithms. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2427.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
