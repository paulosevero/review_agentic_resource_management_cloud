---
id: paper-2723
title: 'AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks'
authors:
- Moreira, Rodrigo
- Rodrigues Moreira, Larissa Ferreira
- Leone Maciel Peixoto, Maycon
- de Oliveira Silva, Flávio
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3672699
url: https://www.scopus.com/pages/publications/105032804808?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 43519--43532
keywords:
- Agentic
- B5G
- energy-aware
- intents
- MEC
- monitoring
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
  05-abstract-screening: include
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
      management signal); C3=0.5 (infra/cloud-edge signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Tarefa de DevOps/observabilidade (incident triage, RCA,
      geração de manifestos) — não é decisão de resource management.
    winning_category: D_devops_or_logs_not_rm
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2723 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Effective management and operational decision-making for complex mobile network systems present significant challenges, particularly when addressing conflicting requirements such as efficiency, user satisfaction, and energy-efficient traffic steering. The literature presents various approaches aimed at enhancing network management, including the Zero-Touch Network (ZTN) and Self-Organizing Network (SON); however, these approaches often lack a practical and scalable mechanism to consider human sustainability goals as input, translate them into energy-aware operational policies, and enforce them at runtime. In this study, we address this gap by proposing the AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks. AGORA embeds a local tool-augmented Large Language Model (LLM) agent in the mobile network control loop to translate natural-language sustainability goals into telemetry-grounded actions, actuating the User Plane Function (UPF) to perform energy-aware traffic steering. The findings indicate a strong latency-energy coupling in tool-driven control loops and demonstrate that compact models can achieve a low energy footprint while still facilitating correct policy execution, including non-zero migration behavior under stressed Multi-access Edge Computing (MEC) conditions. Our approach paves the way for sustainability-first, intent-driven network operations that align human objectives with executable orchestration in Beyond-5G infrastructures. © 2013 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management."
- **winning_category:** 'D_devops_or_logs_not_rm'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "log analysis" }`
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "root cause analysis" }`


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
