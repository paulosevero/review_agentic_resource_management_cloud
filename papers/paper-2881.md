---
id: paper-2881
title: 'LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things'
authors:
- Yang, Qingwen
- Li, Zhi
- Tang, Jiawei
- Liu, Yanyi
- Guo, Tiezheng
- Wen, Yingyou
venue: Computers, Materials and Continua
venue_type: journal
year: 2026
doi: 10.32604/cmc.2025.074384
url: https://www.scopus.com/pages/publications/105032721172?origin=resultslist
publisher: Tech Science Press
pages: ''
keywords:
- edge computing
- Industrial internet of things
- LLM-based agents
- small language models
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
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

# paper-2881 — LEAF: A Lightweight Edge Agent Framework with Expert SLMs for the Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying Large Language Model (LLM)-based agents in the Industrial Internet of Things (IIoT) presents significant challenges, including high latency from cloud-based APIs, data privacy concerns, and the infeasibility of deploying monolithic models on resource-constrained edge devices. While smaller models (SLMs) are suitable for edge deployment, they often lack the reasoning power for complex, multi-step tasks. To address these issues, this paper introduces LEAF, a Lightweight Edge Agent Framework designed for efficiently executing complex tasks at the edge. LEAF employs a novel architecture where multiple expert SLMs—specialized for planning, execution, and interaction—work in concert, decomposing complex problems into manageable sub-tasks. To mitigate the resource overhead of this multi-model approach, LEAF implements an efficient parameter-sharing scheme based on Scalable Low-Rank Adaptation (S-LoRA). We introduce a two-stage training strategy combining Supervised Fine-Tuning (SFT) and Group Relative Policy Optimization (GRPO) to significantly enhance each expert’s capabilities. Furthermore, a Finite State Machine (FSM)-based decision engine orchestrates the workflow, uniquely balancing deterministic control with intelligent flexibility, making it ideal for industrial environments that demand both reliability and adaptability. Experiments across diverse IIoT scenarios demonstrate that LEAF significantly outperforms baseline methods in both task success rate and user satisfaction. Notably, our fine-tuned 4-billion-parameter model achieves a task success rate over 90% in complex IIoT scenarios, demonstrating LEAF’s ability to deliver powerful and efficient autonomy at the industrial edge. Copyright © 2026 The Authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLMs" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2881.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
