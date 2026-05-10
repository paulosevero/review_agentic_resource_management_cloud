---
id: paper-1586
title: Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]
authors:
- Ge, Xuran
- Ou, Yang
- Wang, Bo
- Zhao, Yu
- Wu, Lizhou
- Wang, Zicong
- Chen, Zhiguang
- Xiao, Nong
venue: Jisuanji Yanjiu yu Fazhan/Computer Research and Development
venue_type: journal
year: 2025
doi: 10.7544/issn1000-1239.202440628
url: https://www.scopus.com/pages/publications/105001257497?origin=resultslist
publisher: Science Press
pages: 545--562
keywords:
- distributed storage
- fault recovery
- heterogeneous storage
- LLM inference system
- memory management
- serverless LLM inference
language: Chinese
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1586 — Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, LLM (large language model) has exhibited remarkable performance, profoundly transforming various aspects of human life. As these models grow in size and user demand for long-context inference increases, LLM inference systems face significant storage challenges. These challenges stem primarily from the vast number of model parameters and the key value cache required for efficient inference, both of which strain GPU memory resources. Additionally, inefficiencies in storage usage in distributed systems often result in over-provisioning and fault tolerance issues, further complicating resource management. Researchers explore memory optimization, heterogeneous storage, and distributed storage, synthesizing various research efforts to address GPU memory constraints and enhance resource utilization. Memory-optimized LLM inference systems improve GPU memory efficiency and reduce memory footprint through techniques like efficient key value cache management, compression, and attention operator optimization. Heterogeneous storage based LLM inference systems expand storage capacity by integrating various storage resources, thereby minimizing I/O overhead via tensor placement strategies, asynchronous data transfer, and intelligent memory allocation and prefetching methods. Distributed LLM systems enhance the utilization of multi-machine resources, boosting execution efficiency and fault tolerance in LLM inference tasks through batching, multi-level scheduling, and redundant replication. Finally, we review existing research and outline future research directions to further optimize storage solutions for LLM inference systems. © 2025 Science Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1586.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
