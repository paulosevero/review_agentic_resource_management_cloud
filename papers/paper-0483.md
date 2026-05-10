---
id: paper-0483
title: Reinforcement learning for resource management in multi-Tenant serverless platforms
authors:
- Qiu, Haoran
- Mao, Weichao
- Patke, Archit
- Wang, Chen
- Franke, Hubertus
- Kalbarczyk, Zbigniew T.
- Başar, Tamer
- Iyer, Ravishankar K.
venue: EuroMLSys 2022 - Proceedings of the 2nd European Workshop on Machine Learning and Systems
venue_type: conference
year: 2022
doi: 10.1145/3517207.3526971
url: https://www.scopus.com/pages/publications/85128360409?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 20--28
keywords:
- function-As-A-service
- multi-Agent
- reinforcement learning
- resource allocation
- serverless computing
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

# paper-0483 — Reinforcement learning for resource management in multi-Tenant serverless platforms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless Function-As-A-Service (FaaS) is an emerging cloud computing paradigm that frees application developers from infrastructure management tasks such as resource provisioning and scaling. To reduce the tail latency of functions and improve resource utilization, recent research has been focused on applying online learning algorithms such as reinforcement learning (RL) to manage resources. Compared to existing heuristics-based resource management approaches, RL-based approaches eliminate humans in the loop and avoid the painstaking generation of heuristics. In this paper, we show that the state-of-The-Art single-Agent RL algorithm (S-RL) suffers up to 4.6x higher function tail latency degradation on multi-Tenant serverless FaaS platforms and is unable to converge during training. We then propose and implement a customized multi-Agent RL algorithm based on Proximal Policy Optimization, i.e., multi-Agent PPO (MA-PPO). We show that in multi-Tenant environments, MA-PPO enables each agent to be trained until convergence and provides online performance comparable to S-RL in single-Tenant cases with less than 10% degradation. Besides, MA-PPO provides a 4.4x improvement in S-RL performance (in terms of function tail latency) in multi-Tenant cases.  © 2022 ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0483.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
