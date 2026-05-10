---
id: paper-1708
title: An AI-native application assemble platform for easy-integrating of AIGC based services
authors:
- Jin, Wei
- Chen, Hongzhi
- Wang, Xiaoyan
- Gong, Benru
- Lin, Xiufeng
venue: Proceedings of 2024 4th International Conference on Big Data, Artificial Intelligence and Risk Management, ICBAR 2024
venue_type: conference
year: 2025
doi: 10.1145/3718751.3718843
url: https://www.scopus.com/pages/publications/105007598788?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 578--583
keywords:
- Agent clusters
- AI-native platform
- AIGC
- Application assemble
- Autonomous agents
- Easy assemble
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Plataforma de montagem de aplicações AIGC — LLM/AIGC como workload servido, não como agente que toma decisões de RM.
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

# paper-1708 — An AI-native application assemble platform for easy-integrating of AIGC based services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The in-depth employing trend of platformization and ecological development in digital transformation over the enterprise has triggered even wider applications of cloud-native, product standardization, modular, and resilient production assemble techniques, onto the information reformation, thereby adapting the rapid iteration of software services. After introduction of field implementation of content generative AI, the AI-native services, that aims to plus the AI-native application services into the already-exist information system has been widely adopted. However, due to the use of loose coupling to assemble applications and embed enterprise business systems in vertical fields such as manufacturing, management, energy sales, etc., it is necessary to understand and abstract professional models such as business knowledge, models, processes, and mechanisms. At present, there are still challenges in automation and continuous iteration. The deal with such complicate issues, the manuscript proposes an AI native SaaS production and management platform (ANSAE) based on the integration of LLM, multi-agent system, and cloud native technology. With a distributed architecture designed, resilient AI-native SaaS assemble, autonomous plug/unplug, explainable implementation with business scenes, as well as continuous optimization have been stimulated. Through experiments in two real enterprise level application scenarios, ANSAE has been proven to achieve interpretable, low threshold, self supervised optimization of enterprise level AI native application assembly and continuous operation. © 2024 Copyright held by the owner/author(s).

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-native" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-native" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-native" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Plataforma de montagem de aplicações AIGC — LLM/AIGC como workload servido, não como agente que toma decisões de RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1708.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
