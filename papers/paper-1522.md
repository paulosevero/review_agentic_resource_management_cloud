---
id: paper-1522
title: 'LLM Compression for Enhanced Performance: A Comparative Study of Structured and Unstructured Pruning Techniques'
authors:
- Dichitha, Balakrishna
- Brunda, L.
- Upadhyaya, Sujatha R
venue: 2025 IEEE 2nd International Conference on Advances in Modern Age Technologies for Health and Engineering Science, AMATHE 2025 - Proceedings
venue_type: conference
year: 2025
doi: 10.1109/AMATHE65477.2025.11080874
url: https://www.scopus.com/pages/publications/105012713276?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- BERT
- GLUE Benchmark
- Large Lan- guage Models (LLMs)
- Model Compression
- Natural Language Processing (NLP)
- Structured Pruning
- Trans- former Models
- Unstructured Pruning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1522 — LLM Compression for Enhanced Performance: A Comparative Study of Structured and Unstructured Pruning Techniques

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The usage of transformer models has increased significantly in NLP tasks. However, deploying them in resource-constrained situations, including mobile devices and edge computing systems, is extremely difficult due to their high parameter count. Pruning is one of the prominent model compression strategies that offers an effective solution by reducing the model size and computational requirements without compromising its functionality. These methods are also perfect for real-time applications as they enable faster inference and consume less energy. This study investigates the comparative effectiveness of both structured and unstructured pruning methods towards compressing LLMs. Using the GLUE benchmark, performance is evaluated across tasks using accuracy, F1 score, Matthews correlation coefficient (MCC), and model size. The results demonstrate significant differences between structured and unstructured pruning methods, which provides valuable insights for optimizing transformer models in real-life applications. Structured pruning, in particular, shows stronger resilience to parameter reduction and consistently delivers better results at higher pruning ratios, making it advantageous for latency-sensitive, real-time applications. Furthermore, a pruning ratio of 0.4 was found to preserve most of the model's original accuracy, while 0.6 offers a balanced compromise between compression efficiency and performance retention. © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1522.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
