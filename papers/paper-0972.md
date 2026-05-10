---
id: paper-0972
title: 'SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference'
authors:
- Jiang, Peiwen
- Wang, Haoxin
- Cai, Zinuo
- Gao, Lintao
- Zhang, Weishan
- Ma, Ruhui
- Zhou, Xiaokang
venue: IEEE Transactions on Computational Social Systems
venue_type: journal
year: 2024
doi: 10.1109/TCSS.2024.3423749
url: https://www.scopus.com/pages/publications/85206387767?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7941--7951
keywords:
- Heterogeneous GPU clusters
- inference service
- large language models
- parallel algorithms
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
    my_justification: LLM as workload
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

# paper-0972 — SLoB: Suboptimal Load Balancing Scheduling in Local Heterogeneous GPU Clusters for Large Language Model Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) are becoming powerful engines for social productivity in the manufacturing lifecycle. Existing application-level LLMs inference services focus on large datacenter and small edge intelligence (EI) scenarios, adopting iteration-level batch schedulers to solve resource utilization and inference speed problems. However, these services are incompatible with the scene of medium-sized local heterogeneous graphics processing unit (GPU) clusters with specific patterns, whose scale is between the two aforementioned scenarios. This type of scene proposes tradeoff problems for inference resource and speed, as well as user satisfaction problems for the semisparse frequency of queries with streaming responses. We propose suboptimal load balancing (SLoB), a distributed LLMs inference service scheduler in medium-sized local heterogeneous GPU clusters. SLoB leverages a multilevel adapter to accommodate LLMs usage patterns of scenes and balance resource utilization with inference efficiency. For semisparse problems, it adopts a mixed-priority pipeline scheduler with the least-padding principle to improve users' satisfaction, a metric considering the weights of different tokens in streaming responses. Based on the system prototype, our experiments under simulated workloads demonstrate that SLoB gains a maximum improvement of 29.4× under the satisfaction metric compared with the traditional run-to-completion scheduling solution while improving by up to 3.0× compared with the state-of-the-art (SOTA) solution Orca. © 2024 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0972.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
