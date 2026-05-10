---
id: paper-1728
title: AI-Optimized Communication Protocols for Intelligent Control Systems
authors:
- Khan, Roohee
- Nayak, Ashu
venue: 4th International Conference on Applied Artificial Intelligence and Computing, ICAAIC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICAAIC64647.2025.11330863
url: https://www.scopus.com/pages/publications/105034893145?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1685--1694
keywords:
- adaptive network navigation
- AI communication enhancement
- cyber-physical systems
- edge computing
- intelligent control systems
- multi -agent reinforcement learning
- predictive congestion control in industrial automation
- real-time protocols
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
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
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

# paper-1728 — AI-Optimized Communication Protocols for Intelligent Control Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the context of Industry 4.0 and autonomous systems, communication protocols must be more than just low latency and high reliability; they must support intelligent, adaptable networks. This paper presents AICoPro, a framework of AI-Optimized Communication Protocols designed to improve the performance of real-time control systems in dynamically constrained resource environments. AICoPro implements machine learning-based congestion prediction, reinforcement learning for adaptive routing, and priority-aware packet scheduling to augment protocol behavior towards dynamic network control-loop requirements. The proposed architecture implements a Multi-Agent Reinforcement Learning (MARL) model distributed across edge and fog levels to support decision-making about communication paths and to provide real-time feedback on QoS, node condition, and command criticality. AICoPro marks the introduction of intelligent flow control by strategically predicting appropriate time intervals for packet transmission and balancing queues to optimally reduce industrial and robotic closed-loop system metrics such as end-to-end delay, jitter, and packet drop rate. The protocol stack is built using AI-managed switching over a TCP/UDP hybrid transport layer, which increases fault tolerance against both transient and persistent faults. The data presented from simulations and prototypes have confirmed that AICoPro successfully surpasses legacy industrial communication protocols like OPC UA and MQTT-SN by at least 38% in latencies while delivering control messages 22% faster and responding efficiently to adaptive network congestion. Furthermore, AICoPro excels in scenarios with diverse workload stability, making the system particularly advantageous for applications in intelligent grid control, cooperative robotics, and automated manufacturing. © 2025 IEEE.

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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "In the context of Industry 4.0" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Optimized" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Optimized" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1728.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
