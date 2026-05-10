---
id: paper-0894
title: 'Optimizing Generative AI Workloads for Sustainability: Balancing Performance and Environmental Impact in Generative AI'
authors:
- Dua, Ishneet Kaur
- Patel, Parth Girish
venue: 'Optimizing Generative AI Workloads for Sustainability: Balancing Performance and Environmental Impact in Generative AI'
venue_type: book
year: 2024
doi: 10.1007/979-8-8688-0917-0
url: https://www.scopus.com/pages/publications/105004123367?origin=resultslist
publisher: Springer Science+Business Media
pages: 1--335
keywords:
- AI Efficiency and Optimization
- Artificial Intelligence
- Ethical generative models
- Generative AI
- Machine Learning
- Responsible Generative AI
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Review
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-0894 — Optimizing Generative AI Workloads for Sustainability: Balancing Performance and Environmental Impact in Generative AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This comprehensive guide provides practical strategies for optimizing Generative AI systems to be more sustainable and responsible. As advances in Generative AI such as large language models accelerate, optimizing these resource-intensive workloads for efficiency and alignment with human values grows increasingly urgent. The book starts with the concept of Generative AI and its wide-ranging applications, while also delving into the environmental impact of AI workloads and the growing importance of adopting sustainable AI practices. It then delves into the fundamentals of efficient AI workload management, providing insights into understanding AI workload characteristics, measuring performance, and identifying bottlenecks and inefficiencies. Hardware optimization strategies are explored in detail, covering the selection of energy-efficient hardware, leveraging specialized AI accelerators, and optimizing hardware utilization and scheduling for sustainable operations. You are also guided through software optimization techniques tailored for Generative AI, including efficient model architecture, compression, and quantization methods, and optimization of software libraries and frameworks. Data management and preprocessing strategies are also addressed, emphasizing efficient data storage, cleaning, preprocessing, and augmentation techniques to enhance sustainability throughout the data life cycle. The book further explores model training and inference optimization, cloud and edge computing strategies for Generative AI, energy-efficient deployment and scaling techniques, and sustainable AI life cycle management practices, and concludes with real-world case studies and best practices By the end of this book, you will take away a toolkit of impactful steps you can implement to minimize the environmental harms and ethical risks of Generative AI. For organizations deploying any type of generative model at scale, this essential guide provides a blueprint for developing responsible AI systems that benefit society. What You Will Learn: • Understand how Generative AI can be more energy-efficient through improvements such as model compression, efficient architecture, hardware optimization, and carbon footprint tracking • Know the techniques to minimize data usage, including evaluation, filtering, synthesis, few-shot learning, and monitoring data demands over time • Understand spanning efficiency, data minimization, and alignment for comprehensive responsibility • Know the methods for detecting, understanding, and mitigating algorithmic biases, ensuring diversity in data collection, and monitoring model fairness Who This book Is: For Professionals seeking to adopt responsible and sustainable practices in their Generative AI work; leaders and practitioners who need actionable strategies and recommendations that can be implemented directly in real-world systems and organizational workflows; ML engineers and data scientists building and deploying Generative AI systems in industry settings; and researchers developing new generative AI techniques, such as at technology companies or universities. © 2024 by Ishneet Kaur Dua and Parth Girish Patel.

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
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0894.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
