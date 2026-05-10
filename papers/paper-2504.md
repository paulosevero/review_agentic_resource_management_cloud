---
id: paper-2504
title: Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence
authors:
- Algawiaz, Danah
venue: Scientific Reports
venue_type: journal
year: 2026
doi: 10.1038/s41598-026-42981-3
url: https://www.scopus.com/pages/publications/105035879811?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- Attention mechanism
- Edge computing
- Hallucination detection
- Knowledge distillation
- Latency reduction
- Real-time inference
- Transformer optimisation
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
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
    my_justification: LLM as workload
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

# paper-2504 — Hallucination-aware learning and latency optimization transformer (HALL-OPT) for real-time edge intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Transformer architectures and large language models remain competitive across a broad range of AI tasks, making them challenging to deploy in resource-constrained edge computing environments due to high resource demands and the generation of erroneous or fake outputs (hallucinations). In this paper, a single scheme, HALL-OPT, is proposed to address both latency detection and reduction in hallucination for real-time edge intelligence. The paper presents three main elements of the framework, namely, (1) a dual-stream hallucination detector that analyses internal attention behaviour, (2) an adaptive token-pruning system, which decodes and extracts the necessary context at minimal computation, and (3) a lightweight edge-optimized transformer obtained by knowledge distillation. On SQuAD 2.0 and CNN/DailyMail, HALL-OPT detects hallucinations accurately at 94.3% and achieves a 67.8% reduction in inference latency with only a 2.1% decrease in accuracy compared to the BERT-base model. The system (when deployed on edge hardware) provides sub-50 ms response times while consuming 43% less energy. It is appropriate for real-time applications in industrial IoT, autonomous systems, healthcare monitoring, and other applications where low latency is critical. Existing transformer optimisation and hallucination mitigation approaches treat reliability and Efficiency as separate objectives, limiting their applicability in real-time edge environments. HALL-OPT uniquely integrates hallucination-aware attention, adaptive pruning, and edge-oriented optimisation into a single unified framework, enabling simultaneous reductions in hallucination, latency, and energy consumption. This integrated design distinguishes HALL-OPT from prior work that optimises accuracy or Efficiency in isolation. © The Author(s) 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "transformer" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Transformer" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "transformer" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "BERT" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2504.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
