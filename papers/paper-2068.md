---
id: paper-2068
title: Hyper-Automated AIOps for Unified Operations Orchestration in Industry
authors:
- Rana, Milankumar
- Giri, Nandita
- Gadde, Sakhita Sree
venue: 'AI-SI 2025 - IEEE International Conference on Artificial Intelligence for Sustainable Innovation: Shaping the Future with Intelligent Solutions'
venue_type: conference
year: 2025
doi: 10.1109/AI-SI66213.2025.11340854
url: https://www.scopus.com/pages/publications/105033356227?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AIOps
- artificial intelligence for it operations
- automated remediation
- generative AI
- hybrid cloud
- hyperautomated aiops
- knowledge graphs
- mean time to repair
- omniorchestrate
- orchestration
- unified operations
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: AIOps hiper-automatizado genérico — sem evidência de loop agentic atuando sobre RM.
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

# paper-2068 — Hyper-Automated AIOps for Unified Operations Orchestration in Industry

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern IT operations face unprecedented complexity due to hybrid cloud architectures, IoT ecosystems, and microservices-based applications. Organizations have difficulties due to fragmented visibility, contextual inadequacies, and manual corrective processes in progressively remote systems. This paper introduces OmniOrchestrate, a pioneering hyper-automated AIOps solution that amalgamates operations orchestration using knowledge graphs, generative AI, and closed-loop automation. The framework systematically captures and makes operational knowledge available, increases operational data with contextual intelligence, addresses important challenges by means of extensive visibility across several environments, enables comprehensive automation from detection to remediation, and promotes continuous improvement via adaptive learning. Empirical evaluations of twelve shipping, e-commerce, supply chain, and retail sector companies show notable improvements in a 79.3% decrease in manual tickets, a 62.2% decrease in mean time to detect (MTTD), a 50.5% decrease in mean time to repair (MTTR), and a 66.7% increase in auto-remediation rates. OmniOrchestrate shows to be above conventional AIOps and human operations with a detection accuracy (F1 score) of 0.93, a root cause accuracy of 93%, and a corrective success rate of 89%. Case studies catered to every sector show how well the architecture performs in real-world scenarios, including a shipping container monitoring disturbance repaired in 17 minutes and an e-commerce platform maintaining performance throughout a 215% increase in traffic. Combining fully autonomous remedial capabilities with conventional monitoring systems, the framework provides a complete plan for next-generation IT operations that helps businesses to properly control complexity and improve operational resilience and efficiency in the fast-changing technological environment of today. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_aiops, matched_substring: "AIOps" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_aiops, matched_substring: "AIOps" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "AIOps hiper-automatizado genérico — sem evidência de loop agentic atuando sobre RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2068.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
