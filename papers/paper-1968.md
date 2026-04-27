---
id: "paper-1968"
title: "“Small Device, Big Decision:” Comparing Lightweight LLMs’ Computational Performance and Output Quality for AIED Unplugged"
authors: ["Monteiro, Mateus", "Barros, Aristoteles", "Rodrigues, Luiz", "Dermeval, Diego", "Bittencourt, Ig Ibert", "Isotani, Seiji", "Macario, Valmir"]
year: 2025
venue: "Communications in Computer and Information Science"
venue_type: "conference"
doi: "10.1007/978-3-031-99267-4_20"
url: "https://www.scopus.com/pages/publications/105013026063?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "160--167"
keywords: ["AIED Unplugged", "Benchmark", "Large Language Models", "Performance", "Quality"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1968 — “Small Device, Big Decision:” Comparing Lightweight LLMs’ Computational Performance and Output Quality for AIED Unplugged

## Metadata

- **Authors:** Monteiro, Mateus and Barros, Aristoteles and Rodrigues, Luiz and Dermeval, Diego and Bittencourt, Ig Ibert and Isotani, Seiji and Macario, Valmir
- **Year:** 2025
- **Venue:** Communications in Computer and Information Science
- **DOI:** 10.1007/978-3-031-99267-4_20
- **URL:** https://www.scopus.com/pages/publications/105013026063?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 160--167
- **Language:** English
- **Keywords:** AIED Unplugged; Benchmark; Large Language Models; Performance; Quality

### Abstract

Deploying Large Language Models (LLMs) in offline educational contexts, particularly on edge devices like smartphones, presents significant computational challenges due to their high resource demands. Addressing this issue, AIED Unplugged proposes using lightweight LLMs optimized for mobile platforms, yet understanding the practical performance-quality trade-offs remains limited. This study investigates these trade-offs through benchmarking six compact LLMs embedded via the Llama.cpp framework into an Android application on a low-resource smartphone. Performance metrics (response time, memory usage, and storage size) were tracked using Sentry, while DeepEval assessed response quality based on relevance, clarity, accuracy, and completeness. The evaluation demonstrated notable trade-offs: lighter models, such as MobileVLM and TinyLlama, exhibited fast inference speeds but lower quality in completeness and accuracy, whereas slightly larger models like Qwen2 and DeepSeek provided enhanced accuracy and completeness but suffered from slower responses and increased memory requirements. These insights underscore the necessity of targeted optimization strategies, including model quantization and hybrid deployments, to effectively balance resource efficiency and educational quality. Ultimately, this research supports equitable access to learning materials for marginalized people by providing insights for AI-powered education in offline situations. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

## 04 — Title Screening

**Title:** “Small Device, Big Decision:” Comparing Lightweight LLMs’ Computational Performance and Output Quality for AIED Unplugged

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** “Small Device, Big Decision:” Comparing Lightweight LLMs’ Computational Performance and Output Quality for AIED Unplugged
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** “Small Device, Big Decision:” Comparing Lightweight LLMs’ Computational Performance and Output Quality for AIED Unplugged
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
