---
id: paper-1658
title: Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks
authors:
- Hu, Zihao
- Yan, Jia
- Zhang, Ying-Jun Angela
venue: IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025
venue_type: conference
year: 2025
doi: 10.1109/INFOCOMWKSHPS65812.2025.11152878
url: https://www.scopus.com/pages/publications/105017957435?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- edge intelligence
- federated prompt-tuning
- knowledge distillation
- model compression
- Vision-language foundation models
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1658 — Computation-Efficient Federated Prompt-Tuning with Vision-Language Foundation Model Compression over Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated prompt-tuning over edge networks opens up potential benefits for communication-efficient fine-tuning of the vision-language foundation model (VLFM) by leveraging the distributed data across edge devices. However, resource constraints on edge devices prevent the full deployment and execution of VLFMs locally, hindering local prompt updates before the global prompt aggregation. To tackle this challenge, we propose a computation-efficient federated prompt-tuning approach over resource-limited edge networks without the local placement of the full VLFM. Specifically, we first propose a computation-efficient knowledge distillation (KD) approach for VLFM model compression, which fine-tunes the splitting-based light-weight model over an unlabeled public dataset at the edge server by optimizing the associated low-dimensional prompts under the guidance of the full pretrained model. Building upon the optimized prompts as a good initialization, the textual and visual prompts are simultaneously updated locally, followed by which the edge server enhances the aggregated global prompts via KD in order to compensate for the compressed VLFM deployed at edge devices. Numerical results underscore the effectiveness of the proposed approach, showcasing the improvement of fine-tuning accuracy and communication efficiency compared with representative benchmarks. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Foundation Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "foundation model" }`
  - `{ category: llm_as_workload, pattern_id: wl_train_llm_a, matched_substring: "fine-tuning of the vision-lang" }`
  - `{ category: llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "Foundation Model Compression o" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Foundation Model" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1658.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
