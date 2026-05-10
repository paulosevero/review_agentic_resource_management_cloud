---
id: paper-1617
title: 'Nutriguard: LLM-Driven Nutritional Assessment for Chronic Disease Prevention'
authors:
- Hakim, Md Azizul
- Ifty, Rashedul Arefin
- Delowar, Khaled Eabne
- Chowdhury, Sazzad Hossen
- Rashid, Imdadur
- Shakib, Md.
venue: 2025 IEEE International Conference on Quantum Photonics, Artificial Intelligence, and Networking, QPAIN 2025
venue_type: conference
year: 2025
doi: 10.1109/QPAIN66474.2025.11171750
url: https://www.scopus.com/pages/publications/105019052830?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- chronic disease prevention
- clinical decision support
- CNN Inference
- Deep learning
- edge computing
- food label recognition
- LLM
- multimodal AI
- Personalized nutrition
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

# paper-1617 — Nutriguard: LLM-Driven Nutritional Assessment for Chronic Disease Prevention

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Chronic diseases linked to poor dietary choices necessitate innovative tools for personalized nutrition management. This paper presents NutriGuard, a multimodal AI framework that integrates optical character recognition (OCR), deep learning, and fine-tuned large language models (LLMs) to deliver realtime, context-aware dietary recommendations tailored to users' health profiles. The system begins by extracting nutritional information from food labels via a hybrid OCR pipeline, combining PaddleOCR for English and Surya for Bengali text. For lowquality images, a convolutional neural network (CNN) trained on a dataset of food labels detects product categories, crossreferencing a nutritional database to fill information gaps. A Llama-3.2 model, fine-tuned on clinical guidelines and medical literature, analyzes extracted data against user-specific health conditions (e.g., diabetes, hypertension) to generate risk assessments, substitution suggestions, and personalized meal plans. This work advances AI-driven preventive healthcare by establishing a multilingual, clinically validated framework for dietary risk mitigation. The system's modular design permits rapid adaptation to regional food cultures and emerging nutritional research, addressing critical gaps in scalable personalized nutrition management. Future integration with continuous glucose monitors and gut microbiome data promises to enable dynamic, biomarker-informed dietary optimization. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1617.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
