---
id: "paper-1943"
title: "Proactive Edge Caching Through Multimodal Prediction of Movie Popularity"
authors: ["Mashhadi, Siyavash Amirhajloo", "Kaedi, Marjan"]
year: 2025
venue: "Proceedings of 2025 9th International Conference on Internet of Things and Applications, IoT 2025"
venue_type: "conference"
doi: "10.1109/IoT69654.2025.11297680"
url: "https://www.scopus.com/pages/publications/105031361243?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge Computing", "Gemma-3N", "Internet of Things (IoT)", "Multimodal AI", "Popularity Prediction", "Proactive Caching", "Prompt Engineering"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1943 — Proactive Edge Caching Through Multimodal Prediction of Movie Popularity

## Metadata

- **Authors:** Mashhadi, Siyavash Amirhajloo and Kaedi, Marjan
- **Year:** 2025
- **Venue:** Proceedings of 2025 9th International Conference on Internet of Things and Applications, IoT 2025
- **DOI:** 10.1109/IoT69654.2025.11297680
- **URL:** https://www.scopus.com/pages/publications/105031361243?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge Computing; Gemma-3N; Internet of Things (IoT); Multimodal AI; Popularity Prediction; Proactive Caching; Prompt Engineering

### Abstract

The increasing demand for online movies, driven by a growing ecosystem of Internet of Things (IoT) devices such as smart TVs, connected vehicles, and mobile platforms, has placed unprecedented strain on core network infrastructure, consuming significant traffic and leading to increased latency and a degraded Quality of Experience (QoE). While edge caching is a key solution, its limited storage capacity necessitates intelligent content placement strategies. This paper introduces a novel, proactive framework that significantly advances caching by using a multimodal AI model to predict movie popularity. In contrast to traditional reactive methods that are ineffective for newly released movies and ignore regional trends, our approach forecasts demand before it peaks. We constructed a comprehensive, large scale dataset by integrating movie metadata, user ratings, and poster images, simulating both temporal and geographical user access patterns to model these dynamic trends. Our method utilizes the Gemma-3 N vision-language model, which was fine tuned to act as a zero-shot analyst. The process began with designing a sophisticated, rubric-based system prompt. The model was then trained to follow this instructional format, with final prompt engineering applied to optimize its analytical capabilities for jointly reasoning over textual (e.g., genre, cast) and visual (e.g., poster) signals. By employing Parameter-Efficient Fine-Tuning (PEFT) with LoRA, we achieved highly efficient training on a single GPU. Evaluation on a held-out test set demonstrates the framework's state-of-the-art, tunable performance. In its High Recall Mode, it achieves a perfect 100% recall rate, ensuring no popular movie is missed. By applying a post-inference refinement step, a High-Precision Mode is created that increases precision to 90.4% while maintaining an excellent recall of 94.9%, making it ideal for storage-constrained environments. This adaptability showcases a significant improvement over traditional methods and represents a key step towards truly intelligent content delivery networks.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Proactive Edge Caching Through Multimodal Prediction of Movie Popularity

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Proactive Edge Caching Through Multimodal Prediction of Movie Popularity
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Proactive Edge Caching Through Multimodal Prediction of Movie Popularity
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
