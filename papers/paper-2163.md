---
id: paper-2163
title: 'MedQuery: A Comprehensive AI-Powered Healthcare Platform with Multi-Model Medical Consultation and Integrated Patient Management'
authors:
- Sophia, Ms. Sheeba Jeya
- Hazeesh, Shaik
- Kalyaani, M.
- Likhitha, Gajulapalli
venue: Proceedings of 5th International Conference on Evolutionary Computing and Mobile Sustainable Networks, ICECMSN 2025
venue_type: conference
year: 2025
doi: 10.1109/ICECMSN68058.2025.11382615
url: https://www.scopus.com/pages/publications/105035552915?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1693--1701
keywords:
- Artificial Intelligence
- Ensemble Learning
- Healthcare Technology
- Medical Consultation
- Medical Informatics
- Model Context Protocol (MCP)
- Multimodal Processing
- Open-Source Models
- Real-Time Systems
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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
    my_justification: Out of scope
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

# paper-2163 — MedQuery: A Comprehensive AI-Powered Healthcare Platform with Multi-Model Medical Consultation and Integrated Patient Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The paper discusses MedQuery, a health AI assistant which employs five open AI models MCP-managed orchestration. It has real-time text, audio, video processing capabilities and operates in a distributed micro-service configuration. The majority of AI health systems can work based on only a single model, thus making them not that transparent and their diagnosis can have extremely low hit rates. MedQuery manages to overcome that by coordinating the large number of models and cleaning things up with expert synthesis.MedQuery integrates five large open-source language models - GPT-OSS 120B, Qwen 3 32B, GPT-OSS 20B, DeepSeek R1, and Distill Llama 70B - operating concurrently for enhanced reasoning and reliability. Each of the models will give its own response and confidence rating. Then the Kimi K2 component takes all those responses, fact-checks against web searches, PubMed, the FDA database and drug-interaction APIs and puts them together in a single trustworthy answer. It can display a dropdown showing the answer and the confidence level of each model when used; however, you only see the final answer of Kimi. It also has a Compare Models option that allows you to view the differences between various models and this makes the entire process more transparent and makes it easier to make better decisions.Feeding the system with voice, video or text is possible through WebRTC and WebSocket and the system responds in less than half a second. Mediated by Next.js 15 site and deploying on Vercel microservices, MedQuery has a 96% score on diagnostic accuracy, 95% confidence, and 93% user satisfaction. It is a new benchmark of reliable, explainable and immediate AI health assistance. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Powered" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2163.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
