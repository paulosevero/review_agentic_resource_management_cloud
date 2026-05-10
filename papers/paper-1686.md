---
id: paper-1686
title: 'Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications'
authors:
- Jain, Aditi M
- Jain, Ayush
venue: 2025 6th International Conference on Artificial Intelligence, Robotics, and Control, AIRC 2025
venue_type: conference
year: 2025
doi: 10.1109/AIRC64931.2025.11077484
url: https://www.scopus.com/pages/publications/105012182372?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8--16
keywords:
- Benchmarking
- Chatbot Systems
- Cost-Efficiency
- Distributed Inference
- Edge Computing
- Hybrid Architectures
- Large Language Models
- Microservices Architecture
- Performance Optimization
- Scalability Analysis
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1686 — Scaling LLM Inference Architectures: A Performance Analysis for Chatbot Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a systematic evaluation of architectural patterns for Large Language Model (LLM) inference in production chatbot applications, addressing the critical challenge of balancing performance, cost, and scalability. We analyze five distinct architectures-monolithic, microservices, edge computing, event-driven, and hybrid edge-microservices-using a novel experimental framework with 100 concurrent users as a baseline. Our methodology incorporates precise measurements of latency profiles, throughput, resource utilization, and cost metrics, employing GPT-3.5-turbo with vLLM optimization. Key findings reveal that hybrid edge-microservices architecture offers 46% lower P99 latency and 67% higher throughput compared to monolithic approaches, while edge computing demonstrates 37% lower CPU usage. We introduce a scaling factor analysis methodology for accurate performance predictions at larger scales, validated through controlled experiments. This research contributes: (1) a systematic evaluation methodology for LLM inference architectures, (2) empirical evidence for architectural decision-making, (3) novel scaling factors for performance prediction, and (4) a detailed cost-benefit analysis across architectural patterns. These insights advance the scientific understanding of LLM deployment strategies and provide crucial guidance for both researchers and practitioners in optimizing large-scale neural inference systems.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1686.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
