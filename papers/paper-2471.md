---
id: paper-2471
title: 'LORA: A Latency-Oriented Recurrent Architecture for Large Language Model on Multi-FPGA Platform with Communication Optimization'
authors:
- Zheng, ZhenDong
- Cheng, Qianyu
- Wang, Teng
- Lou, Wenqi
- Gong, Lei
- Chen, Xianglan
- Wang, Chao
- Zhou, Xuehai
venue: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
venue_type: journal
year: 2025
doi: 10.1109/TCAD.2025.3629537
url: https://www.scopus.com/pages/publications/105021231108?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Data Center
- LLM
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

# paper-2471 — LORA: A Latency-Oriented Recurrent Architecture for Large Language Model on Multi-FPGA Platform with Communication Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The remarkable performance of Large Language Models (LLMs) has driven their widespread deployment in data centers to support diverse user-facing applications. However, the rapidly growing computational and storage demands of these models have made single-device deployment increasingly impractical. Prior research on LLM inference has primarily addressed this challenge through algorithmic optimizations such as quantization or by integrating customized hardware acceleration frameworks. As model parameters continue to scale, multi-device deployment has become a necessary approach for enabling efficient LLM inference. Nevertheless, constructing low-latency multi-device platforms for LLMs inference using available FPGA or GPU accelerators remains constrained by inefficient synchronization schemes or limited compute intensity in current architectures. Furthermore, existing solutions often lack co-optimized designs that effectively integrate communication with computation. To address these limitations, this paper proposes LORA, a low-latency end-to-end LLMs acceleration platform utilizing multiple FPGAs. Firstly, we optimize the synchronization timing within the LLMs to minimize storage, computation, and BRAM overhead. Secondly, we tightly couple communication and computation through techniques such as pipeline overlapping and input data packing. Next, we deploy homogeneous accelerators on each FPGA device, leveraging a recurrent architecture to further reduce inference latency. Finally, we apply FPGA-specific optimizations and conduct performance modeling and analysis of the acceleration framework to select optimal deployment parameters for various computational tasks. Implemented on Xilinx Alveo U280 FPGAs, LORA-F and LORA-Q achieve average speedups of 14.4× and 32.6×, respectively, compared to NVIDIA V100 GPUs when running modern LLMs. Compared with existing multi-FPGA accelerator platforms, LORA-F and LORA-Q demonstrate average performance improvements of up to 2.6× and 4.3×, respectively. © 1982-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2471.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
