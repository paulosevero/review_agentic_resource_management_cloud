---
id: paper-2840
title: 'UniOrch: A Unified Mixed Framework for High-Efficiency LLM Training on Heterogeneous AI Chips'
authors:
- Wang, Jingyi
- Wang, Jia
- Gao, Jun
- Cao, Yan
- Zhai, Yang
- Wang, Haojie
- Song, Wanxin
- Kong, Dezhi
- Liu, Liu
- Li, Wei
- He, Zhaofeng
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2026
doi: 10.1109/TPDS.2026.3668647
url: https://www.scopus.com/pages/publications/105031591900?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- AI Chips
- Data Centers
- Distributed Training
- Energy Efficiency
- Heterogeneous Computing
- Large Language Models
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
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

# paper-2840 — UniOrch: A Unified Mixed Framework for High-Efficiency LLM Training on Heterogeneous AI Chips

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient coordination of heterogeneous AI chips (GPU/NPU/DCU) in data centers is crucial for Large Language Model (LLM) training, but this process is hindered by architectural mismatches, protocol fragmentation, and network partitioning. Existing solutions fail to achieve unified resource management across different chips, resulting in severe resource fragmentation and reduced allreduce efficiency. To overcome these limitations, this paper proposes the unified coordination framework UniOrch, which not only integrates three core functionalities, including hardware abstraction, software standardization, and communication coordination, but also enables the training and inference of large models across heterogeneous AI chips. UniOrch's hardware-agnostic bare-metal cloud eliminates virtualization overhead through Border Gateway Protocol Ethernet Virtual Private Network (BGP EVPN) overlay networks and gateway-based chip integration; its PyTorch-based adaptation layer masks hardware differences and reduces migration costs; the Transformer Collective Communication Library (TCCL) unifies NCCL, HCCL, and OpenMPI protocols to support seamless hybrid parallel training. Furthermore, the framework ’ s core scheduling mechanism is the Heterogeneous Hybrid Estimation Model (HHEM), which employs a twostage cost model combining static analysis with dynamic runtime feedback to dynamically allocate computing power based on Transformer task loads, ensuring cross-chip task synchronization, resource pooling, and dynamic allocation. Deployment verification in real-world production environments (e.g., China Construction Bank) shows that UniOrch achieves significant improvements: resource utilization of heterogeneous AI infrastructure is increased by 35%, cross-chip latency is reduced by 42%, accuracy loss in heterogeneous environments is <1.5%, the GLM-130B model achieves near-linear scalability across heterogeneous AI chips (with 116.7 tokens processed per card per second). Notably, it realizes the first cross-vendor LLM training on diversified hybrid NPU-GPU clusters with convergence error <0.8%. © 1990-2012 IEEE.

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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2840.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
