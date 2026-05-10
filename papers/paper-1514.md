---
id: paper-1514
title: Advanced Architectures Integrated With Agentic AI for Next-Generation Wireless Networks
authors:
- Dev, Kapal
- Khowaja, Sunder Ali
- Zeydan, Engin
- Singh, Keshav
- Debbah, Merouane
venue: IEEE Communications Standards Magazine
venue_type: journal
year: 2025
doi: 10.1109/MCOMSTD.2025.3632205
url: https://www.scopus.com/pages/publications/105022695036?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Energy efficiency
- Energy utilization
- Green computing
- Intelligent agents
- Network architecture
- Next generation networks
- Real time control
- Advanced architecture
- Architectural innovation
- Control planes
- Cutting edge technology
- Network operations
- New services
- Operational expenditures
- Service modeling
- Technology innovation
- User planes
- Wireless networks
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: O abstract descreve o paper como 'investigates a range of cutting-edge technologies and architectural innovations' e lista quatro tópicos (1–4) formulados como 'proposing', 'exploring',
      'identifying', 'introducing' — padrão de survey multi-tópico, não de sistema avaliado. Nenhum resultado experimental é mencionado. A estrutura multi-tópico (6G architectures + constrained AI + serverless
      + optical switching) reforça o caráter de survey.
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

# paper-1514 — Advanced Architectures Integrated With Agentic AI for Next-Generation Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates a range of cutting-edge technologies and architectural innovations aimed at simplifying network operations, reducing operational expenditure (OpEx), and enabling the deployment of new service models. The focus is on: 1) proposing novel, more efficient 6G architectures, with both Control and User planes enabling the seamless expansion of services, while addressing long-term 6G network evolution; 2) exploring advanced techniques for constrained artificial intelligence (AI) operations, particularly the design of AI agents for real-time learning, optimizing energy consumption, and the allocation of computational resources; 3) identifying technologies and architectures that support the orchestration of back-end services using serverless computing models across multiple domains, particularly for vertical industries; and 4) introducing optically-based, ultra-high-speed, low-latency network architectures, with fast optical switching and real-time control, replacing conventional electronic switching to reduce power consumption by an order of magnitude. © 2017 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Agentic" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "AI agents" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "O abstract descreve o paper como 'investigates a range of cutting-edge technologies and architectural innovations' e lista quatro tópicos (1–4) formulados como 'proposing', 'exploring', 'identifying', 'introducing' — padrão de survey multi-tópico, não de sistema avaliado. Nenhum resultado experimental é mencionado. A estrutura multi-tópico (6G architectures + constrained AI + serverless + optical switching) reforça o caráter de survey."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1514.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
