---
id: paper-1462
title: 'Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices'
authors:
- Chen, Yuhao
- Yan, Yuxuan
- Ge, Shuowei
- Qin, Yuyang
- Zheng, Yue
- Yang, Qianqian
- He, Shibo
- Shi, Zhiguo
- Chen, Jiming
- Shu, Yuanchao
venue: ACM MobiCom 2025 - Proceedings of the 2025 the 31st Annual International Conference on Mobile Computing and Networking
venue_type: conference
year: 2025
doi: 10.1145/3680207.3723487
url: https://www.scopus.com/pages/publications/105023823310?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 483--497
keywords:
- Edge Collaborative Training
- Large Language Models
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLMs é o workload não o tomador de decisões
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

# paper-1462 — Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) have emerged as a cornerstone for advancing AI technologies. It revolutionizes the way we interact with devices, websites, and information, and paves the way for the development of highly intuitive and capable virtual assistants. Training of today’s LLMs happens in cloud data centers due to the requirement of enormous data and a significant amount of computing power. Despite extensive research in mobile edge computing, fine-tuning pre-trained LLMs using resource-constrained devices like commodity smartphones remains highly under-explored. In this paper, we propose Confidant, a practical collaborative training framework that allows modern LLMs to be fine-tuned across multiple off-the-shelf mobile devices. To this end, Confidant partitions an LLM into several sub-models, allowing each of them to fit in the memory of a mobile device. Multiple mobile devices then collaborate to train the LLM by employing a novel pipeline parallel training approach. In specific, Confidant encompasses a memory-aware dynamic model partitioning and intra-device multi-processor scheduler to minimize the training time across heterogeneous platforms. To ensure resilient distributed training, a hybrid fault tolerance mechanism is devised to proactively manage potential device and network failures. We fully implemented Confidant in C++/Python, and built a cross-framework adapter, enabling collaborative training on a variety of mobile platforms. Experimental results show that Confidant excels in achieving computation-, memory-efficient, and robust customization of LLMs - it manages to train state-of-the-art billion-sized LLMs including BERT, GPT-2, Phi2, and LLaMA3, and fine-tunes Phi2-2.7B on Alpaca in just 40.1 hours using three consumer-grade mobile devices. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLMs é o workload não o tomador de decisões"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1462.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
