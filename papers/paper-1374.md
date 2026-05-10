---
id: paper-1374
title: Spot-Energy-Aware Check-pointing for Reliable and Cost-Efficient Cloud-Based LLM Fine-Tuning
authors:
- Akhtar, Alina
- Hasan, Muhammad Zulkifl
- Khan, Meheryar
- Tariq, Muhammad Umar
- Afzal, Samavia
venue: ICECE 2025 - 8th International Conference on Energy Conservation and Efficiency, Proceedings
venue_type: conference
year: 2025
doi: 10.1109/ICECE69114.2025.11272934
url: https://www.scopus.com/pages/publications/105030536978?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Adapter-Based Fine-Tuning
- Cloud AI Training
- Cost Optimization
- Energy
- Fault Tolerance
- Incremental State Saving
- Large Language Models (LLMs)
- Parameter-Efficient Learning
- Spot-Aware
- Spot-Energy-Aware Checkpointing
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

# paper-1374 — Spot-Energy-Aware Check-pointing for Reliable and Cost-Efficient Cloud-Based LLM Fine-Tuning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing has emerged as an important foundation for high-scale artificial intelligence (AI) computations, offer- ing the storage, scale, and GPU-accelerated resources requir- ed to train and fine-tune Large Language Models (LLMs). Yet, the use of spot instances while cost effective poses sub- stantial preemption risks, which can interrupt training and cause loss of computational progress. Legacy checkpointing methods that save the entire model are inefficient because of their high I/O overhead and slow recovery times, and storage at high costs. This paper introduces a Spot-Energy-Aware Adapter Layer Incremental Checkpointing Framework that selectively stores only adapter layer parameters and delta updates, with smaller, faster, and more efficient checkpoints. The framework coalesces predictive checkpoint scheduling and hybrid cloud deployment with both spot and on-demand instances to improve fault tolerance and cost savviness. Experimental results show that the proposed framework saves checkpoint storage, recovery time by 40%,and total training be less expensive compared to traditional full model checkpointing techniques. The findings validate the design’s capability to ensure high training continuity while optimizing performance and cost in preemptible cloud environments. ©2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1374.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
