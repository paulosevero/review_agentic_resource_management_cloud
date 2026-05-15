---
id: paper-2885
title: LLM-Aided Prediction and RL-Based Optimization for Secure Communications in
  Low-Altitude Economy Networks
authors:
- Ye, Ziqiang
- Gao, Yulan
- Xiao, Yue
- Lei, Xianfu
- Fan, Pingzhi
- Karagiannidis, George K.
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3647682
url: https://www.scopus.com/pages/publications/105025782335?origin=resultslist
publisher: IEEE Computer Society
pages: 5247--5261
keywords:
- hop-frequency planning
- IAA
- LAENet
- LLM
- security communication
- trajectory prediction
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
  06-full-text-screening: exclude
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource
      management signal); C3=0 (no infra signal)
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
    my_final_decision: Exclude
    my_justification: "LLM Telco-RAG faz intent prediction acoplado a DRL SAC para anti-jamming em Low-Altitude Economy networks — domínio é segurança/PHY de redes wireless, não RM em infraestrutura cloud/edge (Boundary B/C). Mantida exclusão."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2885 — LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Secure communications in low-altitude economy networks (LAENets) are critical because the broadcast nature of air-ground links, the strong line-of-sight (LoS) propagation, and the high mobility of intelligent aerial agents (IAAs) inherently expose transmissions to agile, coordinated jamming and eavesdropping. In this paper, we consider a dynamic adversarial scenario where a legitimate IAA simultaneously provides service to multiple terrestrial receivers, while being threatened by collaborative adversarial entities comprising an intelligent UAV-based jammer and a ground-level eavesdropper. The adversaries cooperatively optimize their spatial trajectories and spectrum allocation strategies through real-time adaptive coordination. To counter such coordinated threats, we propose a synergistic framework where a lightweight retrieval-augmented generation (RAG)-enhanced large language model (LLM) predicts, from sequential wireless observations, the probabilistic jamming/eavesdropping intent distributions across frequency bands and the jammer’s next-step trajectory. These predictions are then exploited by a soft actor-critic (SAC)-based reinforcement learning agent at the IAA to jointly optimize frequency-hopping selection, trajectory control, and power allocation, thereby enabling anticipatory and context-aware secure communication. Simulation results demonstrate that, compared to baseline models from deep learning (DL) and reinforcement learning (RL) approaches, our framework achieves an average secrecy-rate improvement of approximately 53.84%, while also delivering faster convergence and greater robustness against adaptive, coordinated attacks. The experiments are conducted under comparable training budgets, and our approach outperforms typical DL models (e.g., convolutional neural network (CNN), long short-term memory (LSTM), Transformer) and optimization baselines (e.g., proximal policy optimization (PPO), simulated annealing) across secrecy rate, convergence speed, and robustness. This establishes the proposed framework as a practical solution for securing next-generation LAENets under coordinated jamming and eavesdropping. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "retrieval-augmented generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "RAG" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Aided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Aided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-assisted" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** LLM Telco-RAG faz intent prediction acoplado a DRL SAC para anti-jamming em Low-Altitude Economy networks — domínio é segurança/PHY de redes wireless, não RM em infraestrutura cloud/edge (Boundary B/C). Mantida exclusão.
- **agrees_with_regex:** True
- **addressed_hint:** support — LLM provides intent prediction features to reward shaping; SAC controller makes resource decisions. Domain é also strictly LAENet security (não cloud/edge/continuum RM infra).
- **evidence_sections:** ["II.C: 'LLM-driven probabilistic intent prediction module with DRL framework' — LLM gera features para SAC", 'Abstract: LLM-aided prediction, RL-based optimization', '§boundary: agentic loop requerido; LLM como suporte a RL está FORA do escopo']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
