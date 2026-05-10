---
id: paper-1090
title: 'Securing AI Inference in the Cloud: Is CPU-GPU Confidential Computing Ready?'
authors:
- Mohan, Apoorve
- Ye, Mengmei
- Franke, Hubertus
- Srivatsa, Mudhakar
- Liu, Zhuoran
- Gonzalez, Nelson Mimura
venue: IEEE International Conference on Cloud Computing, CLOUD
venue_type: conference
year: 2024
doi: 10.1109/CLOUD62652.2024.00028
url: https://www.scopus.com/pages/publications/85203256755?origin=resultslist
publisher: IEEE Computer Society
pages: 164--175
keywords:
- cloud computing
- cloud security
- confidential computing
- foundation models
- high performance computing
- large language models
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1090 — Securing AI Inference in the Cloud: Is CPU-GPU Confidential Computing Ready?

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Many applications have been offloaded onto cloud environments to achieve higher agility, access to more powerful computational resources, and obtain better infrastructure management. Although cloud environments provide solid security solutions, users with highly sensitive data or regulatory compliance requirements, such as HIPAA (Health Insurance Portability and Accountability Act) and GDPR (General Data Protection Regulation), still hesitate to move such application domains to the cloud. To address these concerns, cloud service providers have started to offer solutions to protect data confidentiality and integrity through trusted execution environments (TEEs). While so far these were limited to CPU TEEs only, NVIDIA's Hopper architecture has shifted the landscape by enabling confidential computing features essential to protecting confidentiality and integrity for real-world applications offloaded to GPUs, such as large language models (LLMs). However, there lacks a sufficient study on how much performance overhead confidential computing introduces in a TEE comprised of a CPU-GPU configuration. In this paper we evaluate a confidential computing environment comprised of an Intel TDX system and NVIDIA H100 GPUs through various micro benchmarks and real workloads including BERT, LLaMA, and Granite large language models and provide discussions on the overhead incurred by confidential computing when GPUs are utilized. We show that while LLMs are sensitive to the model types and batch sizes, when larger models with pipelined processing are deployed, the performance of LLM inference in CPU-GPU TEEs can be close to par with their non-confidential setups.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1090.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
