---
id: paper-1812
title: Multiagent Reinforcement Learning-Based Cost-Efficient Edge Server Deployment in CPSS
authors:
- Li, Chuang
- Su, Yuntao
- Zhou, Zhou
- Zhao, Zhixue
- Wen, Yanhua
- Chen, Junjie
- Wei, Jianhao
venue: IEEE Transactions on Computational Social Systems
venue_type: journal
year: 2025
doi: 10.1109/TCSS.2025.3616223
url: https://www.scopus.com/pages/publications/105020959929?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Collaborative learning
- cyber-physical-social systems (CPSS)
- intelligent Internet-of-Things (IoT)
- multiagent reinforcement learning (MARL)
- multiobjective optimization
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

# paper-1812 — Multiagent Reinforcement Learning-Based Cost-Efficient Edge Server Deployment in CPSS

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent transportation systems (ITS), as a crucial application of cyber-physical-social systems (CPSS), leverage collaborative learning to optimize the deployment of edge servers and enhance security management efficiency in ITS. However, previous edge server deployment algorithms have primarily focused on optimizing specific performance metrics, such as energy consumption and load balancing, without adequately addressing the overall system performance under multiple constraints. Consequently, the quality of system services has been compromised. To address this issue, this article proposes a novel edge server deployment algorithm based on multiagent reinforcement learning (MARL) within the CPSS framework, denoted as simulated annealing (SA)-MARL. The algorithm employs SA to determine the initial edge server deployment, ensuring rapid convergence toward a near-optimal solution. Subsequently, MARL is utilized to further refine the initial solution, optimizing the final deployment of edge servers and achieving comprehensive optimization across multiple performance metrics. Extensive experimental results demonstrate that our SA-MARL algorithm effectively addresses complex multiobjective optimization problems. Compared to state-of-the-art methods, our method reduces system latency by 11%, decreases energy consumption by 15%, and improves load balancing by 24%. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1812.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
