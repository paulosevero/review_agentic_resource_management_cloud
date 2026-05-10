---
id: paper-2452
title: Reinforcement Fine-Tuning of Large Language Models for Anomaly Log Analysis in AIDC Switches
authors:
- Zhang, Dongyue
- Niu, Yuer
- Xu, Bohua
- Liu, Qianren
- Tong, Junjie
- Cao, Chang
- Li, Xiangbin
venue: Proceedings - 2025 27th IEEE International Conference on High Performance Computing and Communications, 11th IEEE International Conference on Data Science and Systems, 23rd IEEE International Conference
  on Smart City, 11th IEEE International Conference on Dependability in Sensor, Cloud, and Big Data Systems and Applications and 21st IEEE International Conference on Embedded Software and Systems, HPCC/DSS/SmartCity/DependSys/ICESS
  2025
venue_type: conference
year: 2025
doi: 10.1109/HPCC67675.2025.00215
url: https://www.scopus.com/pages/publications/105022705259?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1477--1482
keywords:
- AIDC
- anomaly detection
- GRPO
- log analysis
- reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_anomaly_log
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Fine-tuning por RL de LLMs para análise de logs de anomalia — LLM como workload e tarefa de análise, não RM.
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

# paper-2452 — Reinforcement Fine-Tuning of Large Language Models for Anomaly Log Analysis in AIDC Switches

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of AI and big data technologies, analyzing network device anomaly logs in AIDC (Artificial intelligence data centers) faces significant challenges. This paper proposes a reinforcement fine-tuning method based on large-scale models, leveraging GRPO (Group relative policy optimization) combined with a multi-dimensional reward function to achieve deep feature extraction and efficient analysis of switch anomaly logs. The method improves anomaly detection accuracy and robustness, outperforming traditional supervised fine-tuning approaches, demonstrating broad application potential in network anomaly detection for AIDC. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_anomaly_log', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: llm_as_workload, pattern_id: wl_train_llm_a, matched_substring: "Fine-Tuning of Large Language" }`
  - `{ category: llm_as_workload, pattern_id: ovr_anomaly_log, matched_substring: "Anomaly Log Analysis" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_large_lang_model, matched_substring: "Large Language Models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Fine-tuning por RL de LLMs para análise de logs de anomalia — LLM como workload e tarefa de análise, não RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2452.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
