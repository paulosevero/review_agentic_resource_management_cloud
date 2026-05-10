---
id: paper-0484
title: 'SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management'
authors:
- Qiu, Haoran
- Mao, Weichao
- Patke, Archit
- Wang, Chen
- Franke, Hubertus
- Kalbarczyk, Zbigniew T.
- Başar, Tamer
- Iyer, Ravishankar K.
venue: SoCC 2022 - Proceedings of the 13th Symposium on Cloud Computing
venue_type: conference
year: 2022
doi: 10.1145/3542929.3563475
url: https://www.scopus.com/pages/publications/85143252231?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 306--322
keywords:
- multi-agent
- reinforcement learning
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0484 — SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless Function-as-a-Service (FaaS) offers improved programmability for customers, yet it is not server-"less"and comes at the cost of more complex infrastructure management (e.g., resource provisioning and scheduling) for cloud providers. To maintain service-level objectives (SLOs) and improve resource utilization efficiency, recent research has been focused on applying online learning algorithms such as reinforcement learning (RL) to manage resources. Despite the initial success of applying RL, we first show in this paper that the state-of-the-art single-agent RL algorithm (S-RL) suffers up to 4.8x higher p99 function latency degradation on multi-tenant serverless FaaS platforms compared to isolated environments and is unable to converge during training. We then design and implement a scalable and incremental multi-agent RL framework based on Proximal Policy Optimization (SIMPPO). Our experiments demonstrate that in multi-tenant environments, SIMPPO enables each RL agent to efficiently converge during training and provides online function latency performance comparable to that of S-RL trained in isolation with minor degradation (<9.2%). In addition, SIMPPO reduces the p99 function latency by 4.5x compared to S-RL in multi-tenant cases.  © 2022 ACM.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0484.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
