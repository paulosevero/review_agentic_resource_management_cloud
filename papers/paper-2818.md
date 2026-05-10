---
id: paper-2818
title: 'AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units'
authors:
- Wang, Xinkai
- Zhuansun, Yiming
- Li, Chao
- Wang, Jing
- Hou, Xiaofeng
- Sun, Lingyu
- Wang, Luping
- Guo, Minyi
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-1021-4_17
url: https://www.scopus.com/pages/publications/105022150272?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 231--245
keywords:
- CPU Efficiency
- Intel AMX
- LLM Serving
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

# paper-2818 — AsymServe: Demystifying and Optimizing LLM Serving Efficiency on CPU Acceleration Units

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Current data centers are accommodating more AI-based workloads, especially large-language model (LLM) training and serving in recent years. Given the limited count and significant energy consumption of expensive GPUs, cloud providers tend to utilize more cost-efficient processors for LLM serving, such as Intel scalable CPU equipped with acceleration units AMX. To understand the improvements, bottlenecks, and opportunities on this new platform, we first undertake a comprehensive characterization of LLM serving using AMX on two generations of modern CPUs with various memory devices. Our characterization reveals that the hardware and software behaviors of LLM serving on CPU are distinct from conventional cloud workloads and vary greatly. In this paper, we propose AsymServe to maximize LLM serving efficiency on scalable CPU platforms via handling software and hardware asymmetry. It adjusts hardware allocation and software configurations adaptively to maximize CPU performance-per-watt. Through extensive evaluation, we show that AsymServe improves LLM serving performance. Specifically, it achieves up to 1.71x faster first-token generation, 3.13x greater throughput, and 11.09x better energy efficiency. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2818.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
