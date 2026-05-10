---
id: paper-0585
title: 'Leftover: Improving Large Language Model Inference Efficiency by Leveraging Idle Resources'
authors:
- Duan, Xu
- Ye, Kejiang
venue: 2023 International Conference on High Performance Big Data and Intelligent Systems, HDIS 2023
venue_type: conference
year: 2023
doi: 10.1109/HDIS60872.2023.10499636
url: https://www.scopus.com/pages/publications/85191686029?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 60--65
keywords:
- Large Language Model Inference
- Preemptive Inference
- Resource Utilization
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

# paper-0585 — Leftover: Improving Large Language Model Inference Efficiency by Leveraging Idle Resources

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models and other deep learning models exist in many application areas that have large demands on computing resources but do not have strict real-time response requirements. While the recent algorithmic innovations have primarily focused on optimizing inference latency for large language models, without considering the throughput of inference tasks. On the other hand, data centers often host many underutilized idle resources or offer cost-effective preemptible instances, which can be used by the inference tasks to improve the inference efficiency. Thus, in this paper, we introduce Leftover, a general-purpose large language model inference system that encompasses model compilation, deployment, and task scheduling infrastructure. Leftover leverages idle or preemptible resources to handle inference tasks that are insensitive to latency but require substantial computational power, leading to significant improvements in cluster computing performance. We evaluate Leftover with real-world workloads and simulated preemptive experiments, achieving up to an 11.28x increase in resource utilization compared to baseline methods and a 1.45x performance improvement compared to basic preemptive inference approaches. ©2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0585.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
