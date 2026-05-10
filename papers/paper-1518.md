---
id: paper-1518
title: Dynamic Resource Allocation Using Reinforcement Learning in Edge-Cloud Environments
authors:
- Dhara, S.
- Safrin Salma, U.
- Shalini, S.
- Shobana, S.
- Yuvashree, B.
- Pradeepa, M.
venue: 3rd IEEE International Conference on Data Science and Network Security, ICDSNS 2025
venue_type: conference
year: 2025
doi: 10.1109/ICDSNS65743.2025.11168688
url: https://www.scopus.com/pages/publications/105019047713?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- DQN
- dynamic scaling
- edge-cloud computing
- MARL
- PPO
- reinforcement learning
- resource allocation
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

# paper-1518 — Dynamic Resource Allocation Using Reinforcement Learning in Edge-Cloud Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge-cloud computing has emerged as a powerful pattern to support delay-sensitive and resource-intensive applications in modern distributed systems. However, dynamic and unexpected workloads in this environment face significant challenges for efficient resource allocation. This paper proposed a Multi-Agent Reinforcement Learning (MARL) approach to optimize resource management in edge-cloud architectures. Specifically, three methodologies are introduced to address diverse real-world scenarios. Deep Q-Network (DQN) is used to learn resource selection. Proximal Policy Optimization (PPO) supports continuous control for adaptive scaling and ensuring consistent performance under fluctuating workloads. Finally, they introduced a MARL method for decentralized agents operating collaboratively, each optimizing local efficiency, minimizing network delay, and reducing forwarding costs. The MARL models adapt more effectively to dynamic conditions than traditional static and heuristic-based approaches. Experimental results show an average of 20 % improvement in task completion efficiency and a 15 % reduction in resource wastage, confirming the effectiveness of MARL in edge-cloud resource orchestration. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1518.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
