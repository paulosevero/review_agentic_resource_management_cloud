---
id: paper-1767
title: 'Performance Evaluation of Modern GPU Accelerator-Based Edge Systems: A Holistic Approach'
authors:
- Lee, Hoyeong
- Kang, Pilsung
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3616166
url: https://www.scopus.com/pages/publications/105017664131?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Accelerators
- Edge Computing
- Graphics Processing Unit (GPU)
- High-Performance Computing
- Parallel Systems
- Performance Benchmarks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1767 — Performance Evaluation of Modern GPU Accelerator-Based Edge Systems: A Holistic Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Amid the growing demand for low-latency edge computing, this study presents a comprehensive performance evaluation of modern GPU (Graphics Processing Unit)-accelerated edge systems, using NVIDIA's leading Jetson series as representative platforms. We assess these devices across a broad spectrum of workloads - including scientific computing, memory-bound tasks, conventional AI inference, and modern generative AI via a Large Language Model (LLM) case study. Results reveal significant performance scaling across the Jetson family. The high-end Jetson Orin NX delivers an average speedup of 42.7× higher frame rate in traditional AI and a 5.3× speedup in High-Performance Computing (HPC) workloads over the entry-level Nano. Our LLM case study, which establishes a clear hardware threshold for generative AI, shows the Orin NX provides approximately 15% faster token generation. Conversely, the Orin Nano emerges as the leading device for overall efficiency, demonstrating superior cost-performance and power-performance ratios, and proving more energy-frugal in the LLM task for the same high-quality output. Our findings provide practical, evidence-based guidelines for selecting optimal edge devices by balancing absolute performance against critical cost and energy constraints.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1767.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
