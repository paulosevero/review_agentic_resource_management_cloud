---
id: paper-1596
title: 'SigMorph: A Transfer-Oriented Toolkit for Fingerprint Injection in Fine-Tuned Models'
authors:
- Gong, Huiqi
- Fang, Chao
- Yan, Zhaokun
- Zhang, Yi
venue: 2025 7th International Conference on Internet of Things, Automation and Artificial Intelligence, IoTAAI 2025
venue_type: conference
year: 2025
doi: 10.1109/IoTAAI66837.2025.11213041
url: https://www.scopus.com/pages/publications/105022268919?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 68--74
keywords:
- Adapter-based injection
- Model fingerprinting
- Parameter-efficient tuning
- Plug-And-play toolkit
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Fine-tuned models? Pode ser LLM e/ou SLM.
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
    - ovr_cls_llm_present
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

# paper-1596 — SigMorph: A Transfer-Oriented Toolkit for Fingerprint Injection in Fine-Tuned Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We present SigMorph, a transfer-oriented toolkit for injecting and migrating identity fingerprints in fine-Tuned language models. Designed with practicality in mind, SigMorph leverages lightweight adaptation modules to embed ownership signals into compact components that can be seamlessly integrated into downstream models. Unlike traditional methods that require full model retraining, SigMorph enables plug-And-play fingerprint injection with minimal computational cost and no disruption to the task-specific learning process. The toolkit is built to support common fine-Tuning pipelines and ensures that the injected fingerprints remain functional under model transfer, incremental updates, or fusion with other models. This makes SigMorph well-suited for real-world scenarios such as large-scale model distribution, version control, and intellectual property protection. In particular, SigMorph offers strong relevance to information and communication engineering applications, including secure model deployment in edge computing environments, provenance tracking in intelligent network systems, and traceability enforcement in AI-driven communication services. By decoupling fingerprint logic from core model parameters, SigMorph provides a flexible and scalable approach to maintaining trust and accountability across evolving model ecosystems, especially in distributed or safety-critical communication infrastructure.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Fine-tuned models? Pode ser LLM e/ou SLM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-driven" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "language models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "AI-driven" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_lang_model, matched_substring: "language models" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1596.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
