---
id: paper-1736
title: 'Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster'
authors:
- Kim, Seoyoung
- Ha, Jiwon
- Kim, Yoonhee
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-025-05216-0
url: https://www.scopus.com/pages/publications/105014810871?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Affinity-aware
- Deep Learning Inference
- Heterogeneous GPU Cluster
- Machine Learning
- Online-learning
- Resource Scheduling
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

# paper-1736 — Oltunes: Online learning-based auto-tuning system for DL inference in heterogeneous GPU cluster

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With rapid advancements in AI, GPU accelerator technology is evolving, leading to an increase in heterogeneous computing nodes within data centers. This necessitates schedulers that can identify and efficiently manage diverse resources to dynamically meet application demands. For latency-sensitive tasks such as deep learning inference, imprecise GPU scheduling can cause resource interference, degrading both application performance and overall GPU utilization. The rise of NLP and large language models (LLMs) has heightened the focus on balancing throughput and latency. However, dynamic loads on specific resources can lead to performance degradation due to head-of-line blocking. Consequently, proactive resource management is essential to reduce costs while ensuring quality of service (QoS) and maintaining energy efficiency. This paper introduces OLTunes, a cluster-level scheduling system for deep learning inference models that integrates streaming and batch methods to efficiently manage both online and offline models. By leveraging FM-FTML, an online learning technique, OLTunes optimizes runtime environments and resource allocation to meet user SLAs through prediction and optimization. It groups tasks based on their characteristics and model variants to minimize interference, ensuring complementary affinities. It also automatically adjusts resources and configurations to improve performance and reduce resource fragmentation. Performance experiments on a heterogeneous GPU cluster demonstrated a 58% average improvement in GPU utilization, up to 49% reduction in p99 tail latency, and a 61% increase in throughput. It also achieved approximately 84.6% energy savings with a maximum accuracy loss of 4% and reduced latency-sensitive SLO violations by up to 92% compared to other baselines, ensuring end-to-end QoS. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1736.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
