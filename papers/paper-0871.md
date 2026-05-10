---
id: paper-0871
title: 'MARS: Multi-Agent Deep Reinforcement Learning for Real-Time Workflow Scheduling in Hybrid Clouds with Privacy Protection'
authors:
- Cheng, Long
- He, Haoyang
- Gu, Yan
- Liu, Qingzhi
- Zhao, Zhiming
- Fang, Fang
venue: Proceedings of the International Conference on Parallel and Distributed Systems - ICPADS
venue_type: conference
year: 2024
doi: 10.1109/ICPADS63350.2024.00091
url: https://www.scopus.com/pages/publications/85212505274?origin=resultslist
publisher: IEEE Computer Society
pages: 657--666
keywords:
- Cloud computing
- deep reinforcement learning
- hybrid cloud
- multi-agent system
- workflow scheduling
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

# paper-0871 — MARS: Multi-Agent Deep Reinforcement Learning for Real-Time Workflow Scheduling in Hybrid Clouds with Privacy Protection

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Scheduling workflows in hybrid cloud environments presents significant challenges due to the inherent complexity of workflows and the dynamic nature of cloud resources. This complexity is further increased when attempting to balance workflow performance with privacy protection. Recent efforts have leveraged deep reinforcement learning (DRL) to address these challenges. However, most of these approaches rely on single-agent models, which can lead to security issues and scalability problems due to their centralized processing. Specifically, the properties of workflows are transferred to the single agent, which risks leaking privacy information. Our paper addresses these issues by introducing MARS, a real-time workflow scheduling method that prioritizes privacy protection in hybrid clouds. MARS leverages multi-agent deep reinforcement learning (MADRL) to optimize the workflow scheduling of cloud virtual machines (VMs). The benefit of our solution is that it relies on the collaborative learning of multi-agents on multiple VMs, which could assign user data to specific cloud servers for privacy protection while sharing training experiences between agents. In our implementation, MARS aims to reduce workflow completion time and operational costs while complying with strict privacy protection guidelines. The experimental results demonstrate that MARS can significantly surpass existing methods, reducing makespan by an average of 53.18% and costs by 61.98% compared to basic techniques, and achieving 20.26% and 25.71% improvements over the latest advanced methods, respectively. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0871.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
