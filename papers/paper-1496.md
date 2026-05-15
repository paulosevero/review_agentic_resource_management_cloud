---
id: paper-1496
title: Investigating Neurosymbolic AI for Intent-based Service Management
authors:
- Colombi, Lorenzo
- Cavicchi, Sara
- Poltronieri, Filippo
- Tortonesi, Mauro
- Stefanelli, Cesare
- Varga, Pal
venue: 'Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025'
venue_type: conference
year: 2025
doi: 10.23919/CNSM67658.2025.11297547
url: https://www.scopus.com/pages/publications/105032150681?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Intent-based Service Management
- Large Language Model
- Neurosymbolic AI
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez Intent-Based e Neurosymbolic AI sejam indicativos que o artigo é interessante para a review (e.g., intent-based é comumente usado em conjunto com LLM-based agents, e Neurosymbolic AI pode usar LLMs por baixo dos panos).
    agrees_with_regex: false
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
    proposed_decision: Exclude
    proposed_justification: Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management.
    winning_category: D_devops_or_logs_not_rm
    overrides_applied: []
    my_final_decision: Include
    my_justification: "Reanálise com critério mais flexível: LLM converte intents de usuário em representação estruturada (JSON) que alimenta o solver ASP (Clingo) responsável pela decisão de service management — pipeline análogo ao anchor paper-1644 (LLM gera entrada estruturada; módulo determinístico decide). Intent-based service management em ambiente cloud/edge está em escopo. Inclusão."
    agrees_with_regex: true
    divergence_reason: 'Categoria regex ''D_devops_or_logs_not_rm'' é imprecisa. O paper NÃO é DevOps/logging (não há incident triage, log summarization, RCA, ou IaC). O padrão real é ''LLM-support-to-symbolic-solver'': LLM faz intent translation (NL → JSON), ASP faz placement decisions. Classificação corrigida: H_llm_supports_other_method (suporte a método simbólico).'
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1496 — Investigating Neurosymbolic AI for Intent-based Service Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing complexity and increasing demands of IT applications, especially in federated multi-cluster environments, pose significant challenges for service orchestration. To address these, Zero-Touch Service Management (ZSM) and intent-based management paradigms are gaining traction, allowing users to specify high-level goals rather than low-level configurations. However, current intent-driven approaches often rely on rigid Domain Specific Languages (DSLs) or graphic user interfaces, limiting expressiveness and usability. In this work, we propose a neurosymbolic intent-based platform that leverages Large Language Models (LLMs) for natural language intent ingestion and Answer Set Programming (ASP), a declarative programming paradigm used for solving complex combinatorial problems. The system translates natural language descriptions of microservice requirements into structured policies, enabling explainable service-to-cluster matching across federated Kubernetes environments. We validate our approach through experiments that evaluate both the syntactic correctness and efficiency of various LLMs in intent translation, as well as the computational time of the symbolic placement algorithm.  © 2025 IFIP.

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
- **my_justification:** "Talvez Intent-Based e Neurosymbolic AI sejam indicativos que o artigo é interessante para a review (e.g., intent-based é comumente usado em conjunto com LLM-based agents, e Neurosymbolic AI pode usar LLMs por baixo dos panos)."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Neurosymbolic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "neurosymbolic" }`
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

- **regex_decision:** Exclude
- **regex_justification:** "Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management."
- **winning_category:** 'D_devops_or_logs_not_rm'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "log analysis" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Reanálise com critério mais flexível: LLM converte intents de usuário em representação estruturada (JSON) que alimenta o solver ASP (Clingo) responsável pela decisão de service management — pipeline análogo ao anchor paper-1644 (LLM gera entrada estruturada; módulo determinístico decide). Intent-based service management em ambiente cloud/edge está em escopo. Inclusão.
- **agrees_with_regex:** True
- **divergence_reason:** Categoria regex 'D_devops_or_logs_not_rm' é imprecisa. O paper NÃO é DevOps/logging (não há incident triage, log summarization, RCA, ou IaC). O padrão real é 'LLM-support-to-symbolic-solver': LLM faz intent translation (NL → JSON), ASP faz placement decisions. Classificação corrigida: H_llm_supports_other_method (suporte a método simbólico).


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
