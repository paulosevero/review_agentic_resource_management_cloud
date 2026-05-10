---
id: paper-1898
title: 'ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models'
authors:
- Liu, Mingxuan
- Gu, Jianhua
- Zhao, Tianhai
venue: Proceedings of the IEEE International Conference on Web Services, ICWS
venue_type: conference
year: 2025
doi: 10.1109/ICWS67624.2025.00045
url: https://www.scopus.com/pages/publications/105018796381?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 305--315
keywords:
- GPU Management
- Large Language Model
- LLM Inference
- Prefill-Decoding Disaggregation
- RDMA
- Remote Fork
- Serverless Computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1898 — ServerlessPD: Fast RDMA-Codesigned Disaggregated Prefill-Decoding for Serverless Inference of Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Model (LLM) inference suffers from inefficiencies in coupled prefill (P) and decoding (D) phases, leading to resource underutilization and scheduling bottlenecks. While disaggregated P-D architectures address this by isolating phases across asymmetric clusters, serverless deployments introduce critical challenges: cold-start latency during autoscaling and costly intermediate state transfers (e.g., KV cache) between distributed prefill and decoding instances. We present ServerlessPD, a system that co-designs remote fork with RDMA to enable near-instant autoscaling and zero-copy state transferring for serverless LLM inference. ServerlessPD introduces a RDMA-based OS kernel-integrated primitive that remotely forks active prefill instances into decoding instances across machines, bypassing cold starts by reusing pre-materialized GPU states, which grants child containers direct copy-on-write access to parent GPU memory. The system further employs GPU context interception to efficiently capture and replicate execution states, ensuring seamless state transfer. To optimize resource utilization, ServerlessPD integrates a dynamic launch-point algorithm that schedules fork operations based on real-time prefill-decoding dynamics, minimizing idle time and overlapping computation with state transfers. ServerlessPD demonstrates that RDMA-codeigned remote fork can unlock near-instant autoscaling and efficient state disaggregation for LLM serving. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1898.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
