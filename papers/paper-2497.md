---
id: paper-2497
title: 'From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection'
authors:
- Adjewa, Frédéric
- Esseghir, Moez
- Merghem-Boulahia, Leïla
venue: Sensors
venue_type: journal
year: 2026
doi: 10.3390/s26020356
url: https://www.scopus.com/pages/publications/105028792177?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- artificial intelligence of things
- BERT
- computation offloading
- edge computing
- efficient intrusion detection
- semantic embeddings
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_justification: Offloaded embeddings de Edge Transformer para decisões IoT — inferência ML como workload, não loop agentic de RM.
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

# paper-2497 — From Edge Transformer to IoT Decisions: Offloaded Embeddings for Lightweight Intrusion Detection

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The convergence of Artificial Intelligence (AI) and the Internet of Things (IoT) is enabling a new class of intelligent applications. Specifically, Large Language Models (LLMs) are emerging as powerful tools not only for natural language understanding but also for enhancing IoT security. However, the integration of these computationally intensive models into resource-constrained IoT environments presents significant challenges. This paper provides an in-depth examination of how LLMs can be adapted to secure IoT ecosystems. We identify key application areas, discuss major challenges, and propose optimization strategies for resource-limited settings. Our primary contribution is a novel collaborative embeddings offloading mechanism for IoT intrusion detection named SEED (Semantic Embeddings for Efficient Detection). This system leverages a lightweight, fine-tuned BERT model, chosen for its proven contextual and semantic understanding of sequences, to generate rich network embeddings at the edge. A compact neural network deployed on the end-device then queries these embeddings to assess network flow normality. This architecture alleviates the computational burden of running a full transformer on the device while capitalizing on its analytical performance. Our optimized BERT model is reduced by approximately 90% from its original size, now representing approximately 41 MB, suitable for the Edge. The resulting compact neural network is a mere 137 KB, appropriate for the IoT devices. This system achieves 99.9% detection accuracy with an average inference time of under 70 ms on a standard CPU. Finally, the paper discusses the ethical implications of LLM-IoT integration and evaluates the resilience of LLMs in dynamic and adversarial environments. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Transformer" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "BERT" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Offloaded embeddings de Edge Transformer para decisões IoT — inferência ML como workload, não loop agentic de RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2497.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
