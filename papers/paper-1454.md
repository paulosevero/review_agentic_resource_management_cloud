---
id: paper-1454
title: 'SEAL: Secure and Efficient Adaptive Layering for On-Device Language Models with TEE'
authors:
- Chang, Wen-Tzu
- Fang, Rui
- Chen, Ming-Syan
venue: Proceedings - 2025 IEEE 11th International Conference on Edge Computing and Scalable Cloud, EdgeCom 2025
venue_type: conference
year: 2025
doi: 10.1109/EdgeCom66327.2025.00030
url: https://www.scopus.com/pages/publications/105033584304?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 138--143
keywords:
- Edge Computing
- Energy Efficiency
- Model Stealing
- On-Device AI
- Security and Privacy
- Small Language Models
- Trusted Execution Environment (TEE)
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
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1454 — SEAL: Secure and Efficient Adaptive Layering for On-Device Language Models with TEE

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deployment of Small Language Models (SLMs) on edge devices presents a fundamental trade-off between performance and security: executing in the untrusted Rich Execution Environment (REE) risks model theft, while running entirely within a Trusted Execution Environment (TEE) incurs significant overhead. Existing approaches often sacrifice one for the other. To address this, we propose SEAL (Secure and Efficient Adaptive Layering), a framework that enables informed, quantitative trade-offs between security and efficiency for on-device inference. SEAL introduces two key components: Confidential Layer Analysis (CLA), which quantitatively assesses the confidentiality of each model layer, and the Layer Importance-Guided Adaptive Partition (LIAP) algorithm, which maps the most sensitive, low-overhead layers into the TEE based on device constraints, while retaining others in the REE to preserve performance. To evaluate security, we develop the Model Parameter Reconstruction Success Rate (MPRSR), a metric that measures behavioral, parametric, and functional similarity under model extraction attacks. Experiments using the INT4-quantized Qwen3-0.6B model on WikiQA demonstrate that SEAL reduces model theft risk by 65.8%—with only a 22% increase in latency and memory—by protecting a single critical layer. When securing the top five layers, SEAL reduces MPRSR to 7.9%, while reducing time and energy consumption by roughly 50% compared to full-TEE deployment. SEAL reframes security as an optimization problem, enabling practical and trustworthy secure inference for edge AI. ©2025 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Small Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLMs" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Language Models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Small Language Models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1454.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
