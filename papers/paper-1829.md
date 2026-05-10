---
id: paper-1829
title: 'Task Prioritization in Multiagent Environments: A Novel Approach Using Nash Q-Learning'
authors:
- Li, Kexin
- Hu, Yu
- Wang, Jielei
- Li, Lin
- Zhang, Shuyuan
- Luo, Guangchun
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2025
doi: 10.1109/TCE.2025.3542833
url: https://www.scopus.com/pages/publications/85218721275?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4206--4220
keywords:
- Edge computing
- multi-agent systems
- Nash Q-learning
- priority-based scheduling
- real-time decision-making
- resource optimization
- task allocation strategy
- task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1829 — Task Prioritization in Multiagent Environments: A Novel Approach Using Nash Q-Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid proliferation of smartphones and various terminal devices, edge computing has gained increasing importance in overcoming computational limitations and enhancing service quality through task offloading. However, most existing approaches handle tasks on a first-come, first-served basis, neglecting task prioritization, which is critical in real-world scenarios where tasks have different levels of urgency and resource requirements. This paper addresses the challenge of effective task prioritization in multi-agent task offloading by proposing a Nash Q-learning-based strategy. Our methodology involves optimizing task allocation decisions using Nash Q-learning to integrate Nash equilibrium principles, thereby enhancing adaptability and dynamic decision-making capabilities within a multi-agent environment. The proposed algorithm is evaluated through extensive simulations, comparing total delay, resource utilization, and task success rates across various task offloading strategies. The results demonstrate that our Nash Q-learning approach outperforms conventional techniques by dramatically lowering overall latency, optimizing resource allocation, and maintaining high task success rates. This work demonstrates the efficacy of Nash Q-learning for dynamically setting priorities for tasks in multi-agent edge computing environments, providing a robust framework for effective resource management and collaborative task completion. And also highlight the potential of Nash Q-learning in advancing intelligent task management in edge computing, suggesting its applicability in real-world, resource-constrained environments. © 1975-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1829.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
