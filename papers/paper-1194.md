---
id: paper-1194
title: 'DeepLRA: An Efficient Long Running Application Scheduling Framework with Deep Reinforcement Learning in the Cloud'
authors:
- Si, Qi
- Lu, Xuesong
- Li, Weiyi
- Pu, Peng
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2024
doi: 10.1007/978-981-99-7019-3_16
url: https://www.scopus.com/pages/publications/85177164759?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 157--163
keywords:
- Cloud Computing
- Deep Reinforcement Learning
- Long Running Applications
- Scheduling
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

# paper-1194 — DeepLRA: An Efficient Long Running Application Scheduling Framework with Deep Reinforcement Learning in the Cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the growth of cloud computing, an increasing number of long-running applications (LRAs) are running in the cloud, providing scalability, cost-effectiveness, and flexibility. Considering LRA interactions and resource interferences, scheduling LRAs in the cloud poses significant challenges regarding runtime performance maximization and efficient resource utilization. However, existing schedulers are usually constraint-based methods requiring priori knowledge and hard to balance LRA performance and efficient resource utilization. To address this problem, we propose DeepLRA, a novel and efficient LRA scheduling framework in the cloud. Specifically, we introduce Deep Reinforcement Learning (DRL) in LRA scheduling, where the agent learn the scheduling policy without human intervention. Furthermore, a multi-objective LRA scheduling is designed with multi-agent training. Extensive simulation experiments conducted with real-world workloads indicate that DeepLRA outperforms the state-of-the-art in the multi-objective LRA scheduling. DeepLRA shows 26.1 % and 36.9 % average improvement in throughput and efficient resource utilization over Kubernetes, respectively. © 2024, The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1194.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
