---
id: paper-1997
title: 'EdgePrompt: A Distributed Key-Value Inference Framework for LLMs in 6G Networks'
authors:
- Ning, Jiahong
- Zhu, Pengyan
- Zheng, Ce
- Lee, Gary
- Sun, Sumei
- Yang, Tingting
venue: IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2025
venue_type: conference
year: 2025
doi: 10.1109/INFOCOMWKSHPS65812.2025.11152752
url: https://www.scopus.com/pages/publications/105017961553?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- EdgePrompt
- Key-value pair (KV pair)
- Large Language Models (LLMs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1997 — EdgePrompt: A Distributed Key-Value Inference Framework for LLMs in 6G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As sixth-generation (6G) networks advance, large language models (LLMs) are increasingly integrated into 6G infrastructure to enhance network management and intelligence. However, traditional LLMs architecture struggle to meet the stringent latency and security requirements of 6G, especially as the increasing in sequence length leads to greater task complexity. This paper proposes EdgePrompt, a cloud-edge collaborative framework based on a hierarchical attention splicing mechanism. EdgePrompt employs distributed key-value (KV) pair optimization techniques to accelerate inference and adapt to network conditions. Additionally, to reduce the risk of data leakage, EdgePrompt incorporates a privacy preserving strategy by isolating sensitive information during processing. Experiments on public dataset show that EdgePrompt effectively improves the inference throughput and reduces the latency, which provides a reliable solution for LLMs deployment in 6G environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1997.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
