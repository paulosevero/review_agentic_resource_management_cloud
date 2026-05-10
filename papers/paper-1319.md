---
id: paper-1319
title: Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics
authors:
- Yue, Xiaofei
- Yang, Song
- Zhu, Liehuang
- Trajanovski, Stojan
- Li, Fan
- Fu, Xiaoming
venue: IEEE/ACM Transactions on Networking
venue_type: journal
year: 2024
doi: 10.1109/TNET.2024.3486788
url: https://www.scopus.com/pages/publications/85208668133?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- data analytics
- function placement
- reinforcement learning
- resource allocation
- Serverless computing
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

# paper-1319 — Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the flourishing of global services, low-latency analytics on large-volume geo-distributed data has been a regular requirement for application decision-making. Serverless computing, with its rapid function start-up and lightweight deployment, provides a compelling way for geo-distributed analytics. However, existing research focuses on elastic resource scaling at the stage granularity, struggling to heterogeneous resource demands across component functions in wide-area settings. The neglect potentially results in the cost inefficiency and Service Level Objective (SLO) violations. In this paper, we advocate for fine-grained function orchestration to exploit wide-area resource elasticity. We thereby present Demeter, a fine-grained function orchestrator that saves job execution costs for geo-distributed serverless analytics while ensuring SLO compliance. By learning from volatile and bursty environments, Demeter jointly makes per-function placement and resource allocation decisions using a well-optimized multi-agent reinforcement learning algorithm with a pruning mechanism. It prevent the irreparable performance loss by function congestion control. Ultimately, we implement Demeter and evaluate it with the realistic workloads. Experimental results reveal that Demeter outperforms the baselines by up to 46.6% on cost, while reducing SLO violation by over 23.7% and bringing it to below 15%.  © 1993-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1319.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
