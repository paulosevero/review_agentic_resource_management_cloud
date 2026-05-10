---
id: paper-2667
title: 'SPAD: Spatial Perception and Action Decoupling Empowered Multi-Agent AI Task Scheduling Framework in Cloud-Edge Computing'
authors:
- Li, Yinong
- Ding, Ding
- Xie, Huamao
- Zhao, Lihong
- Jin, Yaqing
- Xie, Yixuan
- Fang, Ziyun
venue: IEEE Transactions on Networking
venue_type: journal
year: 2026
doi: 10.1109/TON.2025.3635400
url: https://www.scopus.com/pages/publications/105024135471?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1896--1911
keywords:
- action decoupling
- Cloud-edge computing
- multi-agent reinforcement learning
- spatial perception
- task scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2667 — SPAD: Spatial Perception and Action Decoupling Empowered Multi-Agent AI Task Scheduling Framework in Cloud-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-agent reinforcement learning provides promising prospect for task scheduling in cloud-edge computing environment in recent years. However, there remains a formidable challenge due to partial observation and the rigid coupling between action spaces and schedulable devices. These limit the ability of agent to perceive global communication patterns and adapt to dynamic environments, resulting in unsatisfactory scheduling decisions. To address these issues, this work proposes SPAD, a novel spatial perception and action decoupling empowered distributed multi-agent AI task scheduling framework. By constructing a global spatial feature distillation mechanism, SPAD can approximate the implicit heterogeneous connection patterns and communication dynamics between devices and tasks under constrained observability, enhancing its ability to make robust decisions in dynamic environments with limited observations. Additionally, SPAD employs a Lyapunov-based action decoupling module to alleviate scalability challenges from rigid action-device coupling, while a novel intrinsic penalty mechanism augments the agent’s advantage function with the instantaneous Lyapunov cost, thereby aligning the policy optimization process with the decoupling module’s underlying stability constraints. Through a comprehensive empirical evaluation spanning synthetic, bursty, and real-world trace-driven workloads, we show that SPAD consistently outperforms state-of-the-art benchmarks in reducing task completion latency and improving resource utilization, while maintaining remarkable resilience and scalability across diverse network topologies and under non-stationary load conditions. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Multi-agent reinforcement lear" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agent AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "agent AI" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2667.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
