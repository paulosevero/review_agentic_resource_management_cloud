---
id: paper-1008
title: Automating Cloud Deployment for Real-Time Online Foundation Model Inference
authors:
- Li, Yang
- Li, Zhenhua
- Han, Zhenhua
- Zhang, Quanlu
- Ma, Xiaobo
venue: IEEE/ACM Transactions on Networking
venue_type: journal
year: 2024
doi: 10.1109/TNET.2023.3321967
url: https://www.scopus.com/pages/publications/85174846491?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1509--1523
keywords:
- Automating
- cloud configuration
- deep learning inference
- real-time services
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1008 — Automating Cloud Deployment for Real-Time Online Foundation Model Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deep neural network (DNN) foundation models are currently exhibiting high prediction accuracy and strong adaptability to broad tasks with remarkably large model scales. They are increasingly becoming the backend support of DNN-driven real-time online services, e.g., Siri and Instagram. Such services require low-latency and cost-efficiency for quality-of-service and commercial competitiveness. When deployed in a cloud environment, these services call for an appropriate selection of cloud configurations (i.e., specific types of VM instances), as well as a considerate device placement plan that places the operations of the model to multiple GPUs via model parallelism for cost-efficiency. Currently, the deployment mainly relies on service providers' manual efforts, which is not only onerous but also far from satisfactory oftentimes due to the huge joint search space of cloud configurations and device placement plans (for a same service, a poor deployment can incur significantly more costs by tens of times). In this paper, we attempt to efficiently automate the cloud deployment for real-time foundation model inference with minimum costs under the constraint of acceptably low latency. This attempt is enabled by 1) jointly leveraging the Bayesian Optimization and Deep Reinforcement Learning to adaptively unearth the (nearly) optimal cloud configuration and device placement with limited search time, and 2) enhancing the cost-efficiency of the deployment based on the probing-informed block multiplexing mechanism and Tensor Algebra SuperOptimizer. We implement a prototype system based on TensorFlow, conduct extensive experiments on top of Microsoft Azure, and demonstrate the generality and scalability of our solution. Results show that for lightweight DNN models and foundation models, our solution essentially saves inference costs by up to 15% and 47% with 57% and 38% lower search overheads respectively, compared with non-trivial baselines.  © 1993-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1008.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
