---
id: paper-1620
title: A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing
authors:
- Han, Chengzhuo
- Yang, Tingting
- Cui, Zhengqi
- Sun, Xin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3583764
url: https://www.scopus.com/pages/publications/105009419811?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 51877--51891
keywords:
- Federated learning
- Internet of Things (IoT) security
- large language models (LLMs) deployment
- privacy preservation
- trustworthy inference
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

# paper-1620 — A Privacy-Preserving and Trustworthy Inference Framework for LLM-IoT Integration via Hierarchical Federated Collaborative Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article addresses the challenges of privacy protection, device constraints, resource heterogeneity, and trusted inference in the integration of large language models (LLMs) with Internet of Things (IoT) devices, proposing a hierarchical federated collaborative computing (HFCC) framework. Unlike traditional federated learning, HFCC employs horizontal splitting + chunking to reduce LLMs computation overhead. The framework dynamically splits LLMs into: 1) global shared layers optimized by edge servers and 2) device-local layers trained on private data, ensuring raw data remains on-device. During inference, chunking of shared layers and dynamic task allocation adjust computational loads based on real-time device states, mitigating high-load security risks. Furthermore, leveraging the hierarchical federated learning architecture, the system employs an anonymized parameter aggregation mechanism during training to achieve multilevel privacy protection. Simultaneously, a cross-device consensus verification mechanism performs trusted validation of distributed intermediate results, effectively identifying malicious node behavior. Experiments show 58% faster inference in resource-constrained environments, significantly reduced data exposure risks, and 94% malicious node detection accuracy versus traditional federated learning. This lays a solid foundation for building an intelligent, efficient, and secure IoT ecosystem. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1620.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
