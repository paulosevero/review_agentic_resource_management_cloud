---
id: paper-2118
title: Dynamic Architectures Leveraging AI Agents and Human-in-the-Loop for Data Center Management
authors:
- Sera, Violet Deepa
- Kalra, Sumit
venue: Proceedings - 2025 IEEE 22nd International Conference on Software Architecture, ICSA-C 2025
venue_type: conference
year: 2025
doi: 10.1109/ICSA-C65153.2025.00053
url: https://www.scopus.com/pages/publications/105007894657?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 324--333
keywords:
- Adaptive Architecture
- AI Agents
- Data Center Management
- Dynamic software architecture
- Human-in-the-Loop
- MAPE-K Loop
- Self-adaptation
- Self-Managing Systems
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Usa 'AI Agents' expandindo o MAPE-K loop (Execute phase) mas nenhum sinal LLM explícito no abstract. 'Agentic digital workers' é usado coloquialmente. Sem foundation model, LLM, generative
      AI ou técnicas distintivas LLM. Paper sobre self-adaptive systems com ML/RL clássico integrado ao MAPE-K.
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

# paper-2118 — Dynamic Architectures Leveraging AI Agents and Human-in-the-Loop for Data Center Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the growing data needs, data centers are being established in new and unexplored terrains. This necessitates the development of robust data center management platforms capable of self-management. To make these systems adaptable to new uncertainties, especially in space, underwater, and remote data centers aimed at long-running or mission-critical operations, the architectures of these robust data center management platforms need to be accurately modeled to be dynamic and evolve during execution. We argue that, in addition to making systems self-managing and autonomous, there is a need for a human-centric adaptive architecture in the data center management domain. This involves incorporating human-in-the-loop mechanisms to oversee the system's self-adaptation and control anomalies and other drifting pointers that could affect the system's quality attributes. This paper also introduces AI Agents in the self-managing system, which can further enhance autonomous management flexibility by enabling dynamic system architecture changes through these agentic 'digital workers.' We propose a dynamic architecture framework combining AI Agents and Human-in-the-Loop for continuously improving data center management. The architecture expands the MAPE-K loop by introducing human-in-the-loop at the Plan phase and AI Agents at the Execute phase to enhance the dynamic architecture setup for autonomous self-managing data centers. This paper details the foundational AI Agents that need to be set at the Execute phase and provides a use case simulation evaluating one of the AI Agents from the proposed architecture. We also define the quality requirements, which may change at runtime in such dynamic architectures, and outline the scope of future work in this domain. © 2025 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI Agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI Agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI Agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI Agents" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Usa 'AI Agents' expandindo o MAPE-K loop (Execute phase) mas nenhum sinal LLM explícito no abstract. 'Agentic digital workers' é usado coloquialmente. Sem foundation model, LLM, generative AI ou técnicas distintivas LLM. Paper sobre self-adaptive systems com ML/RL clássico integrado ao MAPE-K."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2118.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
