---
id: paper-1114
title: Simplifying Network Orchestration using Conversational AI
authors:
- Panchal, Deven
- Verma, Prafulla
- Baran, Isilay
- Musgrove, Dan
- Lu, David
venue: International Conference on Information Networking
venue_type: conference
year: 2024
doi: 10.1109/ICOIN59985.2024.10572160
url: https://www.scopus.com/pages/publications/85198366981?origin=resultslist
publisher: IEEE Computer Society
pages: 84--89
keywords:
- 5G
- 6G
- Intent Driven Networking
- Intent-Based Networking
- Large Language Models (LLMs)
- Machine Learning
- Natural Language Processing
- Network Function Virtualization
- Network Orchestration
- Next Generation Networks
- Open Network Automation Platform (ONAP)
- Open Source
- Operations support systems (OSS)
- Software Defined Net-working
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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
    my_justification: Gerenciamento de recursos é dito ser deixado para o futuro. O que é feito é usar LLM como interface para a API do ONAP.
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

# paper-1114 — Simplifying Network Orchestration using Conversational AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> ONAP is a comprehensive platform for orchestration, management and automation of network and edge computing services for 5G, 6G and Next Generation Networks. Unlike traditional OSSs, it is an open-source project where companies all over the world are collaborating to build different functionalities of an end-to-end Network operating system. For this reason, the ONAP platform has several different sub projects and APIs each performing a specific function to achieve Network Management. There is some complexity associated with using these APIs and knowing and understanding the many parameters associated with them, which impedes adoption. This not only prevents an end- to-end cloud service orchestration like experience for network services, but also increases the time and money spent on network orchestration. This paper proposes and discusses the design of a conversational AI solution that can interface with some significant APIs in ONAP to solve these problems. The conversational AI solution has the potential to significantly simplify network orchestration tasks. This work is being further extended to using Large Language Models (LLMs) to achieve simplified Intent-Based management and orchestration paradigms within ONAP.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "conversational AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Gerenciamento de recursos é dito ser deixado para o futuro. O que é feito é usar LLM como interface para a API do ONAP."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1114.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
