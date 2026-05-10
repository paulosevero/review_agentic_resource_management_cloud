---
id: paper-0650
title: 'TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning'
authors:
- Li, Yihong
- Zeng, Tianyu
- Zhang, Xiaoxi
- Duan, Jingpu
- Wu, Chuan
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2023
doi: 10.1109/INFOCOM53939.2023.10229031
url: https://www.scopus.com/pages/publications/85148467042?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computation theory
- Fertilizers
- Multi agent systems
- Reinforcement learning
- Edge clouds
- Edge computing
- Edge resources
- Fine grained
- Learning tasks
- Machine-learning
- Multi-agent reinforcement learning
- Performance optimizations
- Resources allocation
- Task performance
- Resource allocation
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0650 — TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Machine learning (ML) tasks are one of the major workloads in today's edge computing networks. Existing edge-cloud schedulers allocate the requested amounts of resources to each task, falling short of best utilizing the limited edge resources flexibly for ML task performance optimization. This paper proposes TapFinger, a distributed scheduler that minimizes the total completion time of ML tasks in a multi-cluster edge network, through co-optimizing task placement and fine-grained multi-resource allocation. To learn the tasks' uncertain resource sensitivity and enable distributed online scheduling, we adopt multi-agent reinforcement learning (MARL), and propose several techniques to make it efficient for our ML-task resource allocation. First, TapFinger uses a heterogeneous graph attention network as the MARL backbone to abstract inter-related state features into more learnable environmental patterns. Second, the actor network is augmented through a tailored task selection phase, which decomposes the actions and encodes the optimization constraints. Third, to mitigate decision conflicts among agents, we novelly combine Bayes' theorem and masking schemes to facilitate our MARL model training. Extensive experiments using synthetic and test-bed ML task traces show that TapFinger can achieve up to 28.6% reduction in the average task completion time and improve resource efficiency as compared to state-of-the- art resource schedulers. © 2023 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0650.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
