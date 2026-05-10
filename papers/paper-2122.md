---
id: paper-2122
title: A Next-Generation Cyber-Physical Architecture with Multi-Agent AI, IoT Sensing, and Autonomous Robotic Swarms
authors:
- Shaek Arif, A.
- Vijay, S.
- Tamizhselvi, A.
venue: Proceedings of 6th International Conference on IoT Based Control Networks and Intelligent Systems, ICICNIS 2025
venue_type: conference
year: 2025
doi: 10.1109/ICICNIS66685.2025.11315785
url: https://www.scopus.com/pages/publications/105032751495?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 299--305
keywords:
- Autonomous Robotics
- Brain-Computer Interface
- Cyber-Physical Systems
- IoT Networks
- Predictive Decision-Making
- Smart City Operations
- Smart Energy Management
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
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

# paper-2122 — A Next-Generation Cyber-Physical Architecture with Multi-Agent AI, IoT Sensing, and Autonomous Robotic Swarms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growing complexity and interconnectivity of cyber-physical systems pose challenges to real-time decision making, resource optimization, and security. Existing systems usually fail to incorporate autonomous robotics, IoT networks, and intelligent energy management with secure, adaptable operation. This project envisions a next-generation AI-enabled cyber-physical ecosystem that overcomes such challenges through the integration of autonomous robot and drone swarms, distributed IoT sensors, cloud computing, smart energy modules, sophisticated cybersecurity, and brain-computer interfacing. Multi-modal AI architectures analyze real-time data for predictive analysis and adaptable system behavior, while multi-agent reinforcement learning coordinates autonomous agents to perform tasks such as environmental monitoring, disaster management, logistics, and smart city operations. Firebase facilitates secure, real-time data storage with cross-platform accessibility, and a brain-computer interface facilitates the direct neural control of devices. The innovation in this system is the fully autonomous, cloud-united platform that offers intelligent, predictive, and secure management to future smart ecosystems. © 2025 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "The growing complexity and int" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agent AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-enabled" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2122.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
