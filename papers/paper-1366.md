---
id: paper-1366
title: Agentic AI Decentralized Edge-Cloud Thermal Orchestration System
authors:
- Agarwal, Udhav
venue: Proceedings - 2025 IEEE 11th International Conference on Edge Computing and Scalable Cloud, EdgeCom 2025
venue_type: conference
year: 2025
doi: 10.1109/EdgeCom66327.2025.00018
url: https://www.scopus.com/pages/publications/105033595106?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 68--72
keywords:
- Agentic Orchestration
- Cloud Offloading
- Decentralized Edge Computing
- Edge AI
- Liquid Cooling
- Low Latency
- Power Usage Effectiveness (pPUE)
- Thermal Management
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
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

# paper-1366 — Agentic AI Decentralized Edge-Cloud Thermal Orchestration System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a research study and a working prototype to maximize energy efficiency in real-world data centers with autonomous, self-optimized agents and edge-cloud computing. The system employs the use of lightweight, rule-based decision-making algorithms on Raspberry Pi nodes to orchestrate resources in real-time at the edge. Each node runs a Python-based monitoring agent that utilizes threshold-based logic to trigger local cooling and to initiate load balancing or offloading for efficient and autonomous operation, even when there is no network connectivity. Experimental results demonstrate a 32% reduction in cooling overhead, improving partial Power Usage Effectiveness (pPUE) from 2.08 to 1.73, alongside more stable CPU temperatures and resilient workload migration across edge nodes and cloud servers. The architecture includes decentralized peer-to-peer orchestration, hierarchical offloading logic (local, peer, cloud), and instantaneous cloud fallback using AWS IoT Core, which combines hardware triggering and software smarts. This approach presents a highly available, energy efficient and scalable edge cloud integration for applications such as AI inference, smart buildings, and industrial IoT. Future work will focus on leveraging advanced AI algorithms (Reinforcement learning, lean neural networks) for dynamic orchestration and establishing end-to-end autonomy and internet independence. Further optimizations will be targeted toward minimizing the computational and memory footprint even further, enabling deployment on even more constrained hardware with embedding the use of liquid technology for increased cooling power in higher workload racks. The broader impact of this framework is its ability to transform resource management within data centers and edge environments through the support of sustainable, self-optimizing infrastructures in critical industries. ©2025 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Agentic" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_agentic, matched_substring: "Agentic" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1366.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
