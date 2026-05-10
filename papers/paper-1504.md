---
id: paper-1504
title: A review of state-of-the-art techniques for large language model compression
authors:
- Dantas, Pierre V.
- Cordeiro, Lucas C.
- Junior, Waldir S. S.
venue: Complex and Intelligent Systems
venue_type: journal
year: 2025
doi: 10.1007/s40747-025-02019-z
url: https://www.scopus.com/pages/publications/105012377469?origin=resultslist
publisher: Springer International Publishing
pages: ''
keywords:
- Adaptive compression
- Edge computing
- Fairness in AI models
- Knowledge distillation
- Large language model compression
- Multi-objective optimization
- Neural architecture search
- Pruning techniques
- Quantization
- Resource-constrained environments
- Robustness against adversarial attacks
- Scalable AI systems
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
    my_justification: Review
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

# paper-1504 — A review of state-of-the-art techniques for large language model compression

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of large language models (LLMs) has driven significant progress in natural language processing (NLP) and related domains. However, their deployment remains constrained by challenges related to computation, memory, and energy efficiency—particularly in real-world applications. This work presents a comprehensive review of state-of-the-art compression techniques, including pruning, quantization, knowledge distillation, and neural architecture search (NAS), which collectively aim to reduce model size, enhance inference speed, and lower energy consumption while maintaining performance. A robust evaluation framework is introduced, incorporating traditional metrics, such as accuracy and perplexity (PPL), alongside advanced criteria including latency-accuracy trade-offs, parameter efficiency, multi-objective Pareto optimization, and fairness considerations. This study further highlights trends and challenges, such as fairness-aware compression, robustness against adversarial attacks, and hardware-specific optimizations. Additionally, NAS-driven strategies are explored as a means to design task-aware, hardware-adaptive architectures that enhance LLM compression efficiency. Hybrid and adaptive methods are also examined to dynamically optimize computational efficiency across diverse deployment scenarios. This work not only synthesizes recent advancements and identifies open problems but also proposes a structured research roadmap to guide the development of efficient, scalable, and equitable LLMs. By bridging the gap between compression research and real-world deployment, this study offers actionable insights for optimizing LLMs across a range of environments, including mobile devices and large-scale cloud infrastructures. © The Author(s) 2025.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1504.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
