---
id: paper-2614
title: 'KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems'
authors:
- Huang, Congyue
- Tan, Wei
- Ou, Miaohua
- Yang, Erfu
- Li, Yun
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3658608
url: https://www.scopus.com/pages/publications/105028891283?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge computing
- Kubernetes
- multi-agent proximal policy optimization
- reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2614 — KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Kubernetes (K8s) provides the foundation for integrating distributed edge-cloud resources. However, existing frameworks struggle to address the challenges of cross-cluster coordination and dynamic resource changes, limiting throughput. We propose KMPS, a deep reinforcement learning-based scheduling framework to enhance long-term throughput. KMPS integrates a multi-agent proximal policy optimization algorithm for autonomous edge access point scheduling, combined with gRPC cross-cluster scheduling and invalid target filtering; utilizes graph neural networks to embed system state information, decomposing high-dimensional service orchestration actions through multiple separate policy networks; and constructs a three-time-scale coordination mechanism (0.25s, 2s, 25s) to coordinate scheduling and orchestration, with K8s compatibility. Experiments on real workloads verify that KMPS operates stably under dynamic loads, sudden emergency tasks, and multi-cluster scenarios. Compared to baselines, the proposed framework achieves an over 5.3% increase in long-term throughput and a 60% reduction in cross-cluster scheduling latency. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2614.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
