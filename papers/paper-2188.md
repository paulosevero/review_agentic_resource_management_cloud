---
id: paper-2188
title: 'CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory'
authors:
- Suo, Jiashun
- Liao, Xiaojian
- Xiao, Limin
- Ruan, Li
- Wang, Jinquan
- Su, Xiao
- Huo, Zhisheng
venue: International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
venue_type: conference
year: 2025
doi: 10.1145/3676641.3715986
url: https://www.scopus.com/pages/publications/105002589582?origin=resultslist
publisher: Association for Computing Machinery
pages: 178--191
keywords:
- collaboration-of-experts (coe)
- edge computing
- ml inference
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
    - ovr_cls_llm_present
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

# paper-2188 — CoServe: Efficient Collaboration-of-Experts (CoE) Model Inference with Limited Memory

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models like GPT-4 are resource-intensive, but recent advancements suggest that smaller, specialized experts can outperform the monolithic models on specific tasks. The Collaboration-of-Experts (CoE) approach integrates multiple expert models, improving the accuracy of generated results and offering great potential for precision-critical applications, such as automatic circuit board quality inspection. However, deploying CoE serving systems presents challenges to memory capacity due to the large number of experts required, which can lead to significant performance overhead from frequent expert switching across different memory and storage tiers. We propose CoServe, an efficient CoE model serving system on heterogeneous CPU and GPU with limited memory. CoServe reduces unnecessary expert switching by leveraging expert dependency, a key property of CoE inference. CoServe introduces a dependency-aware request scheduler and dependency-aware expert management for efficient inference. It also introduces an offline profiler to automatically find optimal resource allocation on various processors and devices. In real-world intelligent manufacturing workloads, CoServe achieves 4.5× to 12× higher throughput compared to state-of-the-art systems. © 2025 ACM.

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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "Inference with Limited Memory" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Large language models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "GPT" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2188.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
