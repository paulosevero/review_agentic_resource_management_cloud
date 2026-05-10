---
id: paper-1943
title: Proactive Edge Caching Through Multimodal Prediction of Movie Popularity
authors:
- Mashhadi, Siyavash Amirhajloo
- Kaedi, Marjan
venue: Proceedings of 2025 9th International Conference on Internet of Things and Applications, IoT 2025
venue_type: conference
year: 2025
doi: 10.1109/IoT69654.2025.11297680
url: https://www.scopus.com/pages/publications/105031361243?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge Computing
- Gemma-3N
- Internet of Things (IoT)
- Multimodal AI
- Popularity Prediction
- Proactive Caching
- Prompt Engineering
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1943 — Proactive Edge Caching Through Multimodal Prediction of Movie Popularity

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing demand for online movies, driven by a growing ecosystem of Internet of Things (IoT) devices such as smart TVs, connected vehicles, and mobile platforms, has placed unprecedented strain on core network infrastructure, consuming significant traffic and leading to increased latency and a degraded Quality of Experience (QoE). While edge caching is a key solution, its limited storage capacity necessitates intelligent content placement strategies. This paper introduces a novel, proactive framework that significantly advances caching by using a multimodal AI model to predict movie popularity. In contrast to traditional reactive methods that are ineffective for newly released movies and ignore regional trends, our approach forecasts demand before it peaks. We constructed a comprehensive, large scale dataset by integrating movie metadata, user ratings, and poster images, simulating both temporal and geographical user access patterns to model these dynamic trends. Our method utilizes the Gemma-3 N vision-language model, which was fine tuned to act as a zero-shot analyst. The process began with designing a sophisticated, rubric-based system prompt. The model was then trained to follow this instructional format, with final prompt engineering applied to optimize its analytical capabilities for jointly reasoning over textual (e.g., genre, cast) and visual (e.g., poster) signals. By employing Parameter-Efficient Fine-Tuning (PEFT) with LoRA, we achieved highly efficient training on a single GPU. Evaluation on a held-out test set demonstrates the framework's state-of-the-art, tunable performance. In its High Recall Mode, it achieves a perfect 100% recall rate, ensuring no popular movie is missed. By applying a post-inference refinement step, a High-Precision Mode is created that increases precision to 90.4% while maintaining an excellent recall of 94.9%, making it ideal for storage-constrained environments. This adaptability showcases a significant improvement over traditional methods and represents a key step towards truly intelligent content delivery networks.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1943.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
