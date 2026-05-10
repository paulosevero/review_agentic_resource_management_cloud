---
id: paper-1991
title: An Agentic Task Offloading Workflow Method for Intellicise Wireless Networks
  in the Industrial Internet of Things
authors:
- Ni, Guowei
- Ni, Weichen
- Han, Boxiao
- Dai, Zuojun
- Jia, Ziyan
venue: 2025 IEEE 2nd International Conference on Electronics, Communications and Intelligent
  Science, ECIS 2025 - Proceeding
venue_type: conference
year: 2025
doi: 10.1109/ECIS65594.2025.11086771
url: https://www.scopus.com/pages/publications/105013624026?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Agentic Workflow
- Industrial Internet of Thing
- LLMs
- Multi-Agent System
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: O LLM aparece em papel de suporte (gera heurísticas, embeddings,
      features ou recompensas para RL/MARL/otimização clássica). Não há loop agentic
      AI dirigindo decisão de RM.
    winning_category: H_llm_supports_other_method
    overrides_applied: []
    my_final_decision: Include
    my_justification: 'Seção II.C descreve 4 agentes LLM-driven (Account Manager,
      System Architect, Scheduler, OAM) que executam loop autônomo: percepção de intenção
      → planejamento → decisões de alocação → monitoramento. Agents invocam ferramentas
      para alocar subcarriers. Atende Boundary A (agentic loop) e B (RM decisions:
      scheduling + resource allocation).'
    agrees_with_regex: false
    divergence_reason: Classifier marcou H_llm_supports_other_method, mas fulltext
      mostra LLM como motor principal do agentic workflow, não suporte.
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1991 — An Agentic Task Offloading Workflow Method for Intellicise Wireless Networks in the Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —To address the challenge of inaccurate intent recognition in Intellicise (intelligent and concise) Wireless Networks-enabled edge-cloud-terminal computing scenarios, which utilize large language models (LLMs) for task offloading and resource allocation, we propose a two-tier multi-agent workflow method. This method employs slot-filling technology in the Intention Layer to parse user requests and subsequently coordinates multiple agents in the Efficiency Layer to collaboratively optimize scheduling policies by converting subjective intentions into measurable utility metrics. LLMs perceive key factors—such as device location, task type, and context—and adjust task allocation parameters dynamically. They then guide agents to use appropriate tools and perform optimized scheduling based on the task's nature. Experimental results demonstrate that our method accurately recognizes user intents by considering multi-dimensional factors such as edge device deployment-related regional economic factors, network conditions, and IoT device metrics, thereby meeting diverse user intent. ©2025 IEEE

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "O LLM aparece em papel de suporte (gera heurísticas, embeddings, features ou recompensas para RL/MARL/otimização clássica). Não há loop agentic AI dirigindo decisão de RM."
- **winning_category:** 'H_llm_supports_other_method'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Enhanced" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Seção II.C descreve 4 agentes LLM-driven (Account Manager, System Architect, Scheduler, OAM) que executam loop autônomo: percepção de intenção → planejamento → decisões de alocação → monitoramento. Agents invocam ferramentas para alocar subcarriers. Atende Boundary A (agentic loop) e B (RM decisions: scheduling + resource allocation).
- **agrees_with_regex:** False
- **divergence_reason:** Classifier marcou H_llm_supports_other_method, mas fulltext mostra LLM como motor principal do agentic workflow, não suporte.
- **evidence_sections:** ['II.C: All agents are LLM-driven', 'II.C: agents invoke tools to change resource allocation', 'Experiments: task offloading + subcarrier scheduling via agent decisions', 'Multi-agent planning + execution in closed loop']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
