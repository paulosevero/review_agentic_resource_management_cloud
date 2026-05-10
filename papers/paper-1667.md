---
id: paper-1667
title: Development of an Automotive Electronics Internship Assistance System Using a Fine-Tuned Llama 3 Large Language Model
authors:
- Huang, Ying-Chia
- Tsai, Hsin-Jung
- Liang, Hui-Ting
- Chen, Bo-Siang
- Chu, Tzu-Hsin
- Ho, Wei-Sho
- Huang, Wei-Lun
- Tseng, Ying-Ju
venue: Systems
venue_type: journal
year: 2025
doi: 10.3390/systems13080668
url: https://www.scopus.com/pages/publications/105014424277?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- artificial intelligence (AI)
- automotive electronics
- internship learning
- Llama 3
- model fine-tuning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1667 — Development of an Automotive Electronics Internship Assistance System Using a Fine-Tuned Llama 3 Large Language Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study develops and validates an artificial intelligence (AI)-assisted internship learning platform for automotive electronics based on the Llama 3 large language model, aiming to enhance pedagogical effectiveness within vocational training contexts. Addressing critical issues such as the persistent theory–practice gap and limited innovation capability prevalent in existing curricula, we leverage the natural language processing (NLP) capabilities of Llama 3 through fine-tuning based on transfer learning to establish a specialized knowledge base encompassing fundamental circuit principles and fault diagnosis protocols. The implementation employs the Hugging Face Transformers library with optimized hyperparameters, including a learning rate of 5 × 10<sup>−5</sup> across five training epochs. Post-training evaluations revealed an accuracy of 89.7% on validation tasks (representing a 12.4% improvement over the baseline model), a semantic comprehension precision of 92.3% in technical question-and-answer assessments, a mathematical computation accuracy of 78.4% (highlighting this as a current limitation), and a latency of 6.3 s under peak operational workloads (indicating a system bottleneck). Although direct trials involving students were deliberately avoided, the platform’s technical feasibility was validated through multidimensional benchmarking against established models (BERT-base and GPT-2), confirming superior domain adaptability (F1 = 0.87) and enhanced error tolerance (σ<sup>2</sup> = 1.2). Notable limitations emerged in numerical reasoning tasks (Cohen’s d = 1.15 compared to human experts) and in real-time responsiveness deterioration when exceeding 50 concurrent users. The study concludes that Llama 3 demonstrates considerable promise for automotive electronics skills development. Proposed future enhancements include integrating symbolic AI modules to improve computational reliability, implementing Kubernetes-based load balancing to ensure latency below 2 s at scale, and conducting longitudinal pedagogical validation studies with trainees. This research provides a robust technical foundation for AI-driven vocational education, especially suited to mechatronics fields that require close integration between theoretical knowledge and practical troubleshooting skills. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1667.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
