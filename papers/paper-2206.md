---
id: paper-2206
title: Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF
authors:
- Tatsumi, Riku
- Mizutani, Kimihiro
venue: 2025 IEEE VTS Asia Pacific Wireless Communications Symposium, APWCS 2025
venue_type: conference
year: 2025
doi: 10.1109/APWCS67981.2025.11151933
url: https://www.scopus.com/pages/publications/105017688649?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- containerized streaming
- eBPF
- mobile edge computing
- system call monitoring
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2206 — Monitoring and Predicting Streaming Performance in Containerized Edge Systems Using eBPF

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Container-based streaming services are increasingly deployed at the mobile edge to deliver low-latency content to users. However, understanding and optimizing their runtime performance remains challenging due to the complexity of system-level interactions in containerized environments. In this paper, we present a lightweight performance analysis framework using eBPF to monitor fine-grained system call metrics in containerized streaming cache servers. Our system collects approximately 360 kernel-level metrics from running containers at one-second intervals and correlates them with chunk-level download time observed at the reverse proxy.We formulate a regression problem to predict download latency using these metrics and evaluate four machine learning approaches: linear regression, ridge regression, random forest regression, and histogram-based gradient boosting regression. Experimental results show that the histogram-based gradient boosting model achieves the highest prediction accuracy with a mean squared error of 2.26 × 10<sup>-4</sup>. Feature importance analysis further reveals that a small subset of system calls contributes most to performance variability, suggesting opportunities for dimensionality reduction and lightweight modeling.Our findings demonstrate that eBPF-based monitoring, combined with regression analysis, offers a practical and accurate solution for understanding the performance behavior of containerized edge streaming systems. The proposed framework is readily extensible to other low-latency services such as LLM inference clusters and GPU-intensive workloads.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2206.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
