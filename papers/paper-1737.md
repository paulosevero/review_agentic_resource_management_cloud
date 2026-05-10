---
id: paper-1737
title: Survey and Evaluation of Converging Architecture in LLMs Based on Footsteps of Operations
authors:
- Kim, Seongho
- Moon, Jihyun
- Oh, Juntaek
- Choi, Insu
- Yang, Joon-Sung
venue: IEEE Open Journal of the Computer Society
venue_type: journal
year: 2025
doi: 10.1109/OJCS.2025.3587005
url: https://www.scopus.com/pages/publications/105010893716?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1214--1226
keywords:
- Edge computing
- LLM
- NLP
- server deployment
- transformer architecture
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

# paper-1737 — Survey and Evaluation of Converging Architecture in LLMs Based on Footsteps of Operations

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs), which have emerged from advances in natural language processing (NLP), enable chatbots, virtual assistants, and numerous domain-specific applications. These models, often comprising billions of parameters, leverage the Transformer architecture and Attention mechanisms to process context effectively and address long-term dependencies more efficiently than earlier approaches, such as recurrent neural networks (RNNs). Notably, since the introduction of Llama, the architectural development of LLMs has significantly converged, predominantly settling on a Transformer-based decoder-only architecture. The evolution of LLMs has been driven by advances in high-bandwidth memory, specialized accelerators, and optimized architectures, enabling models to scale to billions of parameters. However, it also introduces new challenges: meeting compute and memory efficiency requirements across diverse deployment targets, ranging from data center servers to resource-constrained edge devices. To address these challenges, we survey the evolution of LLMs at two complementary levels: architectural trends and their underlying operational mechanisms. Furthermore, we quantify how hyperparameter settings influence inference latency by profiling kernel-level execution on a modern GPU architecture. Our findings reveal that identical models can exhibit varying performance based on hyperparameter configurations and deployment contexts, emphasizing the need for scalable and efficient solutions. The insights distilled from this analysis guide the optimization of performance and efficiency within these converged LLM architectures, thereby extending their applicability across a broader range of environments. © 2020 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1737.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
