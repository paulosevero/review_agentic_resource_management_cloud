---
id: paper-2399
title: A Human-in-Multi-Agent-Loop Intent Refinement Method for Task Offloading in
  Mobile Edge Computing
authors:
- Yuan, Shao
- Ni, Weichen
- Han, Boxiao
- Dai, Zuojun
- Yu, Yang
venue: 2025 IEEE 2nd International Conference on Electronics, Communications and Intelligent
  Science, ECIS 2025 - Proceeding
venue_type: conference
year: 2025
doi: 10.1109/ECIS65594.2025.11086847
url: https://www.scopus.com/pages/publications/105013616597?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- HIMAL
- LLM
- MEC
- QoSE
- Task Offloading
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
      management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_with_llm
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: 'HIMAL implementa loop agentic: LLM (brain) percebe estado MEC
      via prompt method, raciocina sobre QoS goals e ajustes de offloading, executa
      via multi-agent (dispatcher, analyst, customer). Seção II.B descreve arquitetura
      com perception, memory (RAG), action modules. Seção III apresenta avaliação
      experimental da qualidade de decisões LLM em escalonamento de tarefas. Atende
      C18 (design agentic com detalhe suficiente) e C19 (avaliação presente).'
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2399 — A Human-in-Multi-Agent-Loop Intent Refinement Method for Task Offloading in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC), intent recognition plays a pivotal role in task offloading. To address this challenge, this paper proposes a Human-in-Multi-Agent-Loop (HIMAL) intent refinement method for MEC that synergistically integrates multi-agent collaboration with human judgment to enhance resource allocation and task scheduling efficiency, thereby facilitating the advancement of the Industrial Internet of Things (IIoT). The proposed HIMAL system enhances AI decision-making through continuous integration of human feedback into the AI’s learning process, thereby enhancing both the precision of AI outputs and contextual awareness. Experimental results demonstrate that our approach achieves significant performance improvements by embedding human guidance within large language model (LLM) workflows, where human operators serve as contextual interpreters to refine AI responses. ©2025 IEEE.

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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_with_llm', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs

To investigate the impact of the HIMAL intent refinement method on the WBMS deployment" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment in medium enterprise to investigate the impact of CoT and SRR-CoT methods on the accuracy" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** HIMAL implementa loop agentic: LLM (brain) percebe estado MEC via prompt method, raciocina sobre QoS goals e ajustes de offloading, executa via multi-agent (dispatcher, analyst, customer). Seção II.B descreve arquitetura com perception, memory (RAG), action modules. Seção III apresenta avaliação experimental da qualidade de decisões LLM em escalonamento de tarefas. Atende C18 (design agentic com detalhe suficiente) e C19 (avaliação presente).
- **agrees_with_regex:** True
- **addressed_hint:** hint_categories=[quality] resolvido: avaliação do experimento mostra iteração prompt×human feedback, demonstrando ciclo fechado.
- **evidence_sections:** ['Section II.B.1: System Architecture (LLM generates strategies)', 'Section II.B.2: Multi-Agent Collaboration (agent model with brain, memory, action, perception)', 'Section II.B.3: HIMAL Workflow (iterative refinement loop)', 'Section III.C: Experiment 1 (scheduling accuracy)', 'Section III.E: LLM QoE evaluation accuracy']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
