---
id: paper-2670
title: A Comprehensive Survey on Large Language Model Compression for Artificial Intelligence Applications in Edge Systems
authors:
- Liang, Yuzhu
- Xu, Changfu
- Mei, Yaxin
- Zou, Haodong
- Guo, Jianxiong
- Fan, Xinggang
- Wang, Tian
- Huang, Haiyang
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3675866
url: https://www.scopus.com/pages/publications/105034510858?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Artificial intelligence
- Edge deployment optimization
- Edge-based LLMs
- Hybrid compression
- Model compression
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2670 — A Comprehensive Survey on Large Language Model Compression for Artificial Intelligence Applications in Edge Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) have achieved remarkable performance across various artificial intelligence applications. However, current LLMs cannot be deployed directly on edge nodes due to their large number of parameters. Fortunately, model compression technology has been proposed to reduce the computational workload and memory usage of LLMs, enabling further edge-based LLM services. However, existing research typically concentrates on isolated compression algorithms and lacks a comprehensive perspective on how to leverage these techniques for practical, end-to-end LLM deployment in edge environments. In this survey, we review edge-oriented LLM compression techniques and software–hardware co-design strategies to enable efficient LLM deployment on resource-constrained edge systems and guide future research in this area. First, we analyze techniques for LLM compression from the perspective of cloud–edge collaborative intelligence, including model quantization, parameter pruning, and knowledge distillation. Second, we present several hybrid model frameworks tailored to dynamic, heterogeneous edge environments, based on model architecture, application scenarios, and combination selection. Third, we further refine a four-layer software–hardware codesign and an overhead-aware LLM deployment optimization. Finally, we discuss the challenges of current model compression approaches and offer insights into future research directions, with a focus on edge-based LLM services. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2670.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
