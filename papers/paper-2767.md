---
id: paper-2767
title: 'Agentic latency control and cooperative vehicle coordination in 5G-MEC: A prescriptive and explainable AI framework'
authors:
- Saqib, Sheikh Muhammad
- Mazhar, Tehseen
- Tariq, Muhammad Usman
- Shahzad, Tariq
- AlAlwan, Asem Ibrahim
- Hamam, Habib
venue: Computer Communications
venue_type: journal
year: 2026
doi: 10.1016/j.comcom.2026.108433
url: https://www.scopus.com/pages/publications/105034469438?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- 5G-MEC
- Agentic AI
- LIME
- SVM
- XAI
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

# paper-2767 — Agentic latency control and cooperative vehicle coordination in 5G-MEC: A prescriptive and explainable AI framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AbstractThe problem of supporting ultra-low latency in 5G-MEC vehicular networks requires moving beyond passive forecasting toward real-time, proactive traffic management. Current solutions often rely on computationally expensive deep learning predictors or centralized network optimization, yet they frequently stop at prediction and do not complete the vehicle-level prescriptive action loop. This paper proposes an Agentic AI Coordination Framework that links latency-state prediction to immediate, explainable, and cooperative mitigation actions at the vehicle edge. At the core of the framework is a lightweight Support Vector Machine (SVM) trained on the 5G-V2N communication dataset, which enables highly reliable latency_category classification (Accuracy = 0.97; Weighted F1-score = 0.97; High-latency class Precision = 1.00 and Recall = 1.00). The predicted latency state then activates an in-vehicle Agentic AI module that generates dashboard-level prescriptive outputs, including status alerts, action plans, and optimized routing guidance. In addition, the framework leverages 5G-MEC cooperative broadcast to disseminate rerouting alerts to neighboring vehicles, supporting distributed congestion avoidance. To ensure transparency and controllability, the system integrates LIME-based explanations and actionable counterfactual analysis to indicate the minimal feature-level adjustments required to transition between High, Medium, and Low latency states. Overall, the framework forms a unified perception–decision–action pipeline that connects low-overhead inference, rule-based prescriptive control, and cooperative vehicle coordination. To align with sustainable computing and the Special Issue focus on energy-efficient routing in 5G-enabled VANETs, the framework couples low-complexity on-board inference with MEC-assisted broadcast to support real-time coordination while constraining communication and compute overhead. © 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Agentic" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Agentic" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2767.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
