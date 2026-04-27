---
id: "paper-1629"
title: "Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction"
authors: ["Harshith, P.", "Murthy, Anantha", "Harshitha, G.M.", "Prathwini", "Shetty, Keerthi", "Suvaris, Roshan D"]
year: 2025
venue: "2025 9th International Conference on Computational System and Information Technology for Sustainable Solutions, CSITSS 2025"
venue_type: "conference"
doi: "10.1109/CSITSS67709.2025.11294975"
url: "https://www.scopus.com/pages/publications/105031361980?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["cost-efficient LLM inference", "LightGBM", "Prompt routing", "semantic difficulty", "Sentence-BERT"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1629 — Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction

## Metadata

- **Authors:** Harshith, P. and Murthy, Anantha and Harshitha, G.M. and Prathwini and Shetty, Keerthi and Suvaris, Roshan D
- **Year:** 2025
- **Venue:** 2025 9th International Conference on Computational System and Information Technology for Sustainable Solutions, CSITSS 2025
- **DOI:** 10.1109/CSITSS67709.2025.11294975
- **URL:** https://www.scopus.com/pages/publications/105031361980?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** cost-efficient LLM inference; LightGBM; Prompt routing; semantic difficulty; Sentence-BERT

### Abstract

Large language models (LLMs) like GPT-4, Claude 3.5, and Gemini 2.5 are now widely used in natural language processing tasks. But their high inference cost and computing requirements make it hard to scale them, especially in areas with limited resources such as education, customer support, and interactive AI tools. This work proposes a cost-efficient inference setup that uses semantic embeddings from a BERT-based model, a LightGBM classifier to estimate prompt difficulty, and dynamic routing logic to pick the most appropriate LLM based on a balance between cost and accuracy. The system was tested on 990 prompts taken from OpenBookQA (Easy), GSM8K (Medium), and MMLU (Hard). It achieved a weighted F1 score of 0.89, while cutting average inference cost by over 95% from $12.08 to $0.34 per 1,000 prompts compared to always using high-end models. Both semantic embedding and routing logic were crucial in maint aining good performance at cheap cost, according to ablation stu dies, demonstrating that promptaware routing can be applied to real-world LLM inference systems and scale well. This research also evaluate routing framework end-to-end on a mixed workload of conversational, summarisation and code-generation tasks to measure its impact on latency and throughput. Across 1,200 real-world prompts, the system achieves a 40% reduction in average inference time and routes over 70% of queries to lower-capacity models without dropping overall response quality-maintaining an average human-judged acceptability score within 2% of always using the top-tier model. Finally, we release our implementation as a set of Dockerised microservices, complete with pre-trained difficulty predictors and REST endpoints, to simplify integration into existing LLM pipelines.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
