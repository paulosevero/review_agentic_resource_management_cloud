---
id: paper-2028
title: LLM-based cost-aware task scheduling for cloud computing systems
authors:
- Pei, Haoran
- Gu, Yan
- Sun, Yajuan
- Wang, Qingle
- Liu, Cong
- Chen, Xiaomin
- Cheng, Long
venue: Journal of Cloud Computing
venue_type: journal
year: 2025
doi: 10.1186/s13677-025-00822-0
url: https://www.scopus.com/pages/publications/105026116476?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Cloud computing
- Deep reinforcement learning
- Large language models
- Task scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_llm_modifier
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
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
    my_justification: "Escopo cloud task scheduling (Boundary C IN). LarS: LLM é fine-tuned em dataset gerado offline por agentes DRL (RL como pré-processador no treinamento). Em produção, o LLM opera como high-level decision agent sozinho — é o decisor final em inferência. Per Gate B (LLM decisor com RL como pré-processador), inclusão."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2028 — LLM-based cost-aware task scheduling for cloud computing systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud task scheduling faces significant challenges due to resource heterogeneity, conflicting optimization objectives, and dynamic workload fluctuations. Traditional heuristic algorithms often necessitate comprehensive knowledge of environmental parameters, significantly constraining their efficacy in dynamic cloud computing environments. While Deep Reinforcement Learning (DRL) methods have shown promise in intelligent scheduling via continuous environment interaction, they suffer from limited generalization to diverse cloud scenarios and lack decision interpretability. To address these shortcomings, this paper proposes LarS, a scheduling framework that employs Large Language Models (LLMs) as high-level decision agents for cloud task scheduling. In LarS, DRL agents trained in carefully chosen representative cloud environments generate a high-quality dataset of scheduling decisions, which is used to fine-tune an LLM. By jointly optimizing average response time, task success rate, and average rental cost, LarS achieves strong generalization across heterogeneous cloud deployments. Experimental results demonstrate that LarS surpasses current approaches in average response time, success rate, and average cost, and maintains strong generalization performance under varied experimental settings. © The Author(s) 2025.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_llm_modifier']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_llm_modifier, matched_substring: "LLM-based" }`
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
- **regex_justification:** "O LLM aparece em papel de suporte (gera heurísticas, embeddings, features ou recompensas para RL/MARL/otimização clássica). Não há loop agentic AI dirigindo decisão de RM."
- **winning_category:** 'H_llm_supports_other_method'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-assisted" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Escopo cloud task scheduling (Boundary C IN). LarS: LLM é fine-tuned em dataset gerado offline por agentes DRL (RL como pré-processador no treinamento). Em produção, o LLM opera como high-level decision agent sozinho — é o decisor final em inferência. Per Gate B (LLM decisor com RL como pré-processador), inclusão.
- **agrees_with_regex:** True
- **evidence_sections:** ["Abstract — 'LLMs as high-level decision agents' (claim), mas pipeline revela offline fine-tuning", 'Seção System model — DRL agents train, generate dataset, LLM fine-tuned', 'Seção LLMs for cloud task scheduling (Related Work) — LLM como surrogate para DRL generalization', 'Seção Experimental results — LLM inference performance, não agent loop evaluation']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
