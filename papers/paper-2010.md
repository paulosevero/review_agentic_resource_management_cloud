---
id: paper-2010
title: 'RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models'
authors:
- Pan, Xiaojian
- Zeng, Chuxuan
- Liang, Du
- Cheng, Ma
- Huang, Dan
venue: 2025 5th International Conference on Communication Technology and Information Technology, ICCTIT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCTIT68197.2025.11406447
url: https://www.scopus.com/pages/publications/105036197843?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 119--123
keywords:
- Inference
- LLM
- Model Loading
- RDMA
- Serverless
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2010 — RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing facilitates elastic scaling for large language model (LLM) inference, but cold start latency - caused by inefficient loading of massive model parameters - limits its real-world applicability. Traditional TCP/IP-based remote loading suffers from high latency and CPU overhead, while local SSD caching solutions incur severe storage redundancy and underutilize distributed caches. To address these challenges, this paper proposes rtLoad, an efficient and scalable LLM parameter loading system based on RDMA (Remote Direct Memory Access) mechanism, integrating a client-server (CS) architecture with client-to-client (C2C) data sharing. rtLoad partitions models into 32MB fine-grained blocks, leverages GPUDirect RDMA to bypass the OS kernel call, and overlaps SSD I/O with RDMA transmission asynchronously. Clients holding model caches can act as data providers to enable C2C transmission, and a dynamic scheduling algorithm optimizes block distribution based on node load and network proximity. Experimental results on DeepSeek-R1-Distill-Qwen-7B and 14B models show that rtLoad outperforms existing methods significantly: compared with ServerlessLLM, rtLoad reduces loading time by up to 67% in warm start scenarios and 46% in dual-server cold start scenarios. For 4 concurrent clients loading the 14B model, rtLoad achieves a loading time of 3.16s, which is 20× faster than NFS-based loading. rtLoad effectively addresses the scalability and efficiency bottlenecks of LLM loading in serverless environments.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2010.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
