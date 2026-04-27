---
id: "paper-2643"
title: "Building Domain-Specific Small Language Models via Guided Data Generation"
authors: ["Kumar, Aman", "Amin, Ekant Muljibhai", "Lee, Xian Yeow", "Vidyaratne, Lasitha", "Farahat, Ahmed K.", "Ghosh, Dipanjan D.", "Koreeda, Yuta", "Gupta, Chetan"]
year: 2026
venue: "Proceedings of the AAAI Conference on Artificial Intelligence"
venue_type: "conference"
doi: "10.1609/aaai.v40i47.41467"
url: "https://www.scopus.com/pages/publications/105034267635?origin=resultslist"
publisher: "Association for the Advancement of Artificial Intelligence"
pages: "40287--40294"
keywords: ["Benchmarking", "Computational linguistics", "Data accuracy", "Data privacy", "Domain Knowledge", "Knowledge management", "Natural language processing systems", "Open systems", "Computational resources", "Data generation", "Domain specific", "Effective domains", "Knowledge intensive tasks", "Language model", "Open-source model", "Privacy concerns", "Saas solutions", "Subject matter experts", "Pipelines"]
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

# paper-2643 — Building Domain-Specific Small Language Models via Guided Data Generation

## Metadata

- **Authors:** Kumar, Aman and Amin, Ekant Muljibhai and Lee, Xian Yeow and Vidyaratne, Lasitha and Farahat, Ahmed K. and Ghosh, Dipanjan D. and Koreeda, Yuta and Gupta, Chetan
- **Year:** 2026
- **Venue:** Proceedings of the AAAI Conference on Artificial Intelligence
- **DOI:** 10.1609/aaai.v40i47.41467
- **URL:** https://www.scopus.com/pages/publications/105034267635?origin=resultslist
- **Publisher:** Association for the Advancement of Artificial Intelligence
- **Pages:** 40287--40294
- **Language:** English
- **Keywords:** Benchmarking; Computational linguistics; Data accuracy; Data privacy; Domain Knowledge; Knowledge management; Natural language processing systems; Open systems; Computational resources; Data generation; Domain specific; Effective domains; Knowledge intensive tasks; Language model; Open-source model; Privacy concerns; Saas solutions; Subject matter experts; Pipelines

### Abstract

Large Language Models (LLMs) have shown remarkable success in supporting a wide range of knowledge-intensive tasks. In specialized domains, there is growing interest in leveraging LLMs to assist subject matter experts with domain-specific challenges. However, deploying LLMs as SaaS solutions raises data privacy concerns, while many open-source models demand significant computational resources for effective domain adaptation and deployment. A promising alternative is to develop smaller, domain-specialized LLMs, though this approach is often constrained by the lack of high-quality domain-specific training data. In this work, we address these limitations by presenting a cost-efficient and scalable training pipeline that combines guided synthetic data generation from a small seed corpus with bottom-up domain data curation. Our pipeline integrates Domain-Adaptive Pre-training (DAPT), Domain-specific Supervised Fine-tuning (DSFT), and Direct Preference Optimization (DPO) to train effective small-scale models for specialized use cases. We demonstrate this approach through DiagnosticSLM, a 3B-parameter domain-specific model tailored for fault diagnosis, root cause analysis, and repair recommendation in industrial settings. To evaluate model performance, we introduce four domain-specific benchmarks: multiple-choice questions (DiagnosticMCQ), question answering (DiagnosticQA), sentence completion (DiagnosticComp), and summarization (Di-agnosticSum). DiagnosticSLM achieves up to 25% accuracy improvement over open-source models of comparable or larger size (2B-9B) on the MCQ task, while also outperforming or matching them in other tasks, demonstrating effective domain-specific reasoning and generalization capabilities. © 2026, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

## 04 — Title Screening

**Title:** Building Domain-Specific Small Language Models via Guided Data Generation

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Building Domain-Specific Small Language Models via Guided Data Generation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Building Domain-Specific Small Language Models via Guided Data Generation
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
