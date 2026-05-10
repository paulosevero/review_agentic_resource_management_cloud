---
id: paper-1011
title: 'CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices'
authors:
- Li, Jinrong
- Han, Biao
- Li, Sudan
- Wang, Xiaoyan
- Li, Jie
venue: 2024 IEEE/CIC International Conference on Communications in China, ICCC 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCC62479.2024.10681712
url: https://www.scopus.com/pages/publications/85206484279?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 185--190
keywords:
- collaborative inference
- large language model
- resource-constrained
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

# paper-1011 — CoLLM: A Collaborative LLM Inference Framework for Resource-Constrained Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Over the past few years, there has been notable advancement in Large Language Models (LLMs), leading to their extensive utilisation across various domains. Running large-scale LLMs usually necessitates processing capacity at the level of data-centers, which deters numerous potential applications from researchers. However, certain applications with great potential in LLM, such as the Internet of Things(IoT) data analysis and multi-robot collaboration, are typically constrained by lack of resources, specifically graphics processing units(GPUs). As a result, these devices fail to execute LLM inference. To tackle the aforementioned issues, we first investigate the problem of 'Compute Bound' in devices with constrained resources, which are unavailable for hierarchical partitioning models. Furthermore, utilising the LLM tensor parallelization, we present a collaborative LLM inference framework on resource-constrained devices called CoLLM. In addition, we propose a minimal latency algorithm and an adaptive load balancing algorithm to optimize inference latency and balance energy consumption. (1) By considering the LLM model's size, device resources, and network conditions, we can calculate the optimum number of collaborative devices to minimise inference latency. (2) CoLLM is capable of dynamically distributing computational workloads based on the target device's status, balancing power consumption to extend overall working time. Experiments are conducted when the Llama2 model is executed on GPU-free devices such as Raspberry Pis. Evaluation results show that end-to-end inference speed outperforms current hierarchical LLM inference methods by a factor of 1.9 x-2.3 x. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1011.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
