---
id: paper-1051
title: 'SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments'
authors:
- Lin, Liduo
- Pan, Li
- Liu, Shijun
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2024
doi: 10.1109/TSC.2024.3422828
url: https://www.scopus.com/pages/publications/85197553447?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2904--2917
keywords:
- Heterogeneous cloud environments
- IaaS
- on-demand instance
- spot instance
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

# paper-1051 — SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As increasingly complex functions are implemented in applications, directed acyclic graphs (DAGs) are widely used to model the inter-dependencies between individual functions. Cloud-based data processing platforms need to consider the complex topology of DAGs and arbitrary deadlines given by users for job scheduling, leading to an NP-hard decision-making problem. Leveraging spot instances in data processing platforms can achieve significant cost savings, but the unpredictable interruption of spot instances makes the problem of VM scaling and job scheduling more difficult. In this paper, a Reinforcement Learning (RL) based approach called SpotDAG is proposed to solve the auto-scaling problem for jobs modeled as DAGs on a data processing platform where spot instances are introduced. SpotDAG makes cluster scaling and job scheduling decisions at the same time by mapping its output to several meta-policies. This paper introduces the self-attention mechanism for feature extraction to help the intelligent agent learn faster. A mask layer after the output of the proposed RL-based algorithm circumvents illegal actions to ensure that a job is completed by its deadline. Extensive experimental results show that the proposed approach can significantly reduce the cost of instances for data processing platforms while ensuring that jobs are completed in time.  © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1051.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
