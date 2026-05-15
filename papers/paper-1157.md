---
id: paper-1157
title: 'ECO-LLM: LLM-based Edge Cloud Optimization'
authors:
- Rao, Kunal
- Coviello, Giuseppe
- Benedetti, Priscilla
- De Vita, Ciro Giuseppe
- Mellone, Gennaro
- Chakradhar, Srimat
venue: 'AI4Sys 2024 - Proceedings of the 2024 Workshop on AI For Systems, Part of:  HPDC
  2024 - 33rd International Symposium on High-Performance Parallel and Distributed
  Computing'
venue_type: conference
year: 2024
doi: 10.1145/3660605.3660941
url: https://www.scopus.com/pages/publications/85204973236?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 7--12
keywords:
- cloud computing
- customization
- edge computing
- generative artificial intelligence (GenAI)
- large language models (LLM)
- machine learning (ML)
- optimization
- video analytics
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
  06-full-text-screening: include
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource
      management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: 'Paper implementa loop agentic-AI completo para placement dinâmico
      de microserviços. Ciclo de percepção (coleta de workload via DataX) → raciocínio
      (análise de LLM via prompt estruturado) → ação (aplicar placement) → feedback
      (latência reportada) é explícito. LLM dirige decisão alocativa em tempo real
      respondendo a mudanças de workload na arquitetura edge-cloud. Atende critério
      essencial: agentic-AI loop DIRIGE resource management.'
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1157 — ECO-LLM: LLM-based Edge Cloud Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AI/ML techniques have been used to solve systems problems, but their applicability to customize solutions on-the-fly has been limited. Traditionally, any customization required manually changing the AI/ML model or modifying the code, configuration parameters, application settings, etc. This incurs too much time and effort, and is very painful. In this paper, we propose a novel technique using Generative Artificial Intelligence (GenAI) technology, wherein instructions can be provided in natural language and actual code to handle any customization is automatically generated, integrated and applied on-the-fly. Such capability is extremely powerful since it makes customization of application settings or solution techniques super easy. Specifically, we propose ECO-LLM (LLM-based Edge Cloud Optimization), which leverages Large Language Models (LLM) to dynamically adjust placement of application tasks across edge and cloud computing tiers, in response to changes in application workload, such that insights are delivered quickly with low cost of operation (systems problem). Our experiments with real-world video analytics applications i.e. face recognition, human attributes detection and license plate recognition show that ECO-LLM is able to automatically generate code on-the-fly and adapt placement of application tasks across edge and cloud computing tiers. We note that the trigger workload (to switch between edge and cloud) for ECO-LLM is exactly the same as the baseline (manual) and actual placement performed by ECO-LLM is only slightly different i.e. on average (across 2 days) only 1.45% difference in human attributes detection and face recognition, and 1.11% difference in license plate recognition. Although we tackle this specific systems problem in this paper, our proposed GenAI-based technique is applicable to solve other systems problems too. © 2024 is held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "- [4] Ali Belgacem, Saïd Mahmoudi, and Maria Kihl. 2022. Intelligent multi-agent reinforcement learn" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "ML techniques have been applied for resource allocation [4][13] and job scheduling [3][28] in variou" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Paper implementa loop agentic-AI completo para placement dinâmico de microserviços. Ciclo de percepção (coleta de workload via DataX) → raciocínio (análise de LLM via prompt estruturado) → ação (aplicar placement) → feedback (latência reportada) é explícito. LLM dirige decisão alocativa em tempo real respondendo a mudanças de workload na arquitetura edge-cloud. Atende critério essencial: agentic-AI loop DIRIGE resource management.
- **agrees_with_regex:** True


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
