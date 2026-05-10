---
id: paper-1532
title: Large-Small Model Synergy for High-Recall and Efficient UAV-based Aerial Surveillance
authors:
- Dong, Lingji
- Zhao, Wei
- Lan, Zheng
- Liu, Yanan
- Shi, Xiupeng
venue: 2025 4th International Conference on Artificial Intelligence, Human-Computer Interaction and Robotics, AIHCIR 2025
venue_type: conference
year: 2025
doi: 10.1109/AIHCIR67580.2025.11404852
url: https://www.scopus.com/pages/publications/105035992602?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Algorithm-Hardware Co-Design
- Chip Accelerator
- Edge Intelligence
- Multi-Objective Optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Large-Small Model? Pode ter conexão com LLMs e/ou SLMs.
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
    - ovr_cls_llm_present
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

# paper-1532 — Large-Small Model Synergy for High-Recall and Efficient UAV-based Aerial Surveillance

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) has become essential for environmental monitoring and disaster response, yet its effectiveness is severely limited by the computational constraints of onboard hardware. Existing systems face a prohibitive tradeoff: lightweight edge models provide real-time responsiveness but suffer from poor detection reliability, while deep learning models offer high accuracy but exceed the energy and processing budgets of autonomous platforms. Here we show a hierarchical "large-small"model synergy that reconciles these conflicting demands by integrating ultra-efficient edge screening with deep cloud-based reasoning. We employ an algorithm-hardware co-designed neural network on the UAV to screen video streams at millisecond latency, utilizing a recall-first strategy to ensure zero missed detections. Potential threats are subsequently verified in the cloud by a specialized segmentation network and a Vision-Language Model (VLM) that interprets scene context. In wildfire detection experiments, our system achieved 100% recall and 99.1% overall accuracy while maintaining onboard inference speeds of approximately 1000 frames per second. These results demonstrate that heterogeneous edge-cloud intelligence can enable efficient, robust, high-fidelity surveillance for safety-critical applications. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Large-Small Model? Pode ter conexão com LLMs e/ou SLMs."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Vision-Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "VLM" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Vision-Language Model" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "VLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_lang_model, matched_substring: "Language Model" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1532.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
