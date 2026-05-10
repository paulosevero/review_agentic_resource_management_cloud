---
id: paper-2173
title: Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference
authors:
- Stoyanov, Radostin
- Spišaková, Viktória
- Reber, Adrian
- Armour, Wesley
- Copik, Marcin
- Bruno, Rodrigo
venue: Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops
venue_type: conference
year: 2025
doi: 10.1145/3731599.3767354
url: https://www.scopus.com/pages/publications/105023407201?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 114--125
keywords:
- Cloud Computing
- Containers
- GPU Checkpointing
- LLM Inference
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

# paper-2173 — Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The widespread adoption of Large Language Models (LLMs) has led to an increased demand for large-scale inference services, presenting a unique set of challenges for the HPC community. These services are characterized by moderate-scale models that require dedicating expensive GPUs to handle bursty inference requests, leading to high costs and resource underutilization. In this paper, we propose SwapServeLLM - a novel engine-agnostic hot-swapping method for cost-effective inference. This model hot-swapping approach is enabled by recent driver capabilities for transparent GPU checkpointing. SwapServeLLM optimizes resource utilization by dynamically allocating GPU resources with two key mechanisms: (1) a demand-aware preemption leveraging information about concurrent requests, and (2) efficient request routing with memory reservation minimizing inference latency. Our evaluation demonstrates that SwapServeLLM optimizes model loading for state-ofthe-art inference engines by 31× compared to vLLM and up to 29% compared to Ollama, enabling cost-effective inference. © 2025 Copyright held by the owner/author(s).

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2173.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
