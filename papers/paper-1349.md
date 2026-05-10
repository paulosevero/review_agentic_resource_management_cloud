---
id: paper-1349
title: 'LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization'
authors:
- Zheng, ZhenDong
- Cheng, Qianyu
- Wang, Teng
- Gong, Lei
- Chen, Xianglan
- Tang, Cheng
- Wang, Chao
- Zhou, Xuehai
venue: Proceedings - 2024 34th International Conference on Field-Programmable Logic and Applications, FPL 2024
venue_type: conference
year: 2024
doi: 10.1109/FPL64840.2024.00053
url: https://www.scopus.com/pages/publications/85207830144?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 332--338
keywords:
- Data Center
- GPT
- Multi-FPGA Acceleration
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
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
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

# paper-1349 — LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) have been widely deployed in data centers to provide various services, among which the most representative is the Generative Pre-trained Transformer (GPT). The GPT model has heavy memory and computing overhead, and its inference process has two stages with distinct computing characteristics: Prefill and Decode. Utilizing existing GPUs and FPGA accelerators to construct a platform for deploying GPT in data centers faces the challenges of needing more effective synchronization schemes or structures with higher computational intensity. This paper proposes LORA, a low latency end-to-end GPT acceleration platform utilizing multiple FPGAs. Firstly, we optimize the synchronization timing of the GPT model to reduce the computation and communication overhead. Secondly, we devise some efficient synchronization steps for specific layers of the GPT model that overlap part of the computation and communication delay to improve the latency of our platform. Finally, we deploy recurrent structures on each FPGA to accelerate the different stages of the GPT model. Implemented on the Xilinx Alveo U280 FPGAs, LORA achieves an average 11.1 × speedup over NVIDIA V100 GPUs on the modern GPT-2 model. Compared to the existing multi-FPGA accelerator appliance, LORA shows performance improvements of up to 4 × and 2.7 × in the Prefill and Decode stages.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1349.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
