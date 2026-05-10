---
id: paper-2847
title: Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters
authors:
- Wu, Qingfu
- Chen, Pengfei
- Wang, Yilun
venue: SoCC 2025 - Proceedings of the 2025 ACM Symposium on Cloud Computing
venue_type: conference
year: 2026
doi: 10.1145/3772052.3772242
url: https://www.scopus.com/pages/publications/105028583037?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 402--415
keywords:
- Deep Reinforcement Learning
- Fragmentation
- GPU Sharing
- Large Language Model
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

# paper-2847 — Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern GPU clusters in computing centers face significant challenges in resource utilization due to fragmentation caused by GPU-sharing mechanisms, job diversity and asynchronous job lifecycles. Existing methods fail to address GPU fragmentation in dynamic scheduling scenarios under GPU sharing. To tackle this issue, this paper proposes DRR, a defragmentation scheduler with deep reinforcement learning (DRL) and rescheduling to mitigate GPU fragmentation. DRR employs a DRL agent trained via imitation learning from heuristic algorithms to overcome cold-start issues, and further enhanced by multi-scale policy optimization for balanced exploration and exploitation to reduce GPU fragmentation. Additionally, the rescheduling strategy in DRR further optimizes GPU utilization by relocating the running jobs. Evaluations conducted on the physical Kubernetes-based testbed and large-scale simulated clusters demonstrate that DRR reduces the average GPU fragmentation rate by 50% compared to state-of-the-art methods, while maintaining Quality of Service (QoS) and ensuring fairness for users.  © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2847.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
