---
id: paper-1687
title: 'The Carbon Footprint of Intelligence: The Environment cost of LLMs'
authors:
- Jain, Devyansh
- Agarwal, Archit
- Baliyan, Subhanshu
- Kanagaraj, R.
venue: Proceedings of the 9th International Conference on Electronics, Communication and Aerospace Technology, ICECA 2025
venue_type: conference
year: 2025
doi: 10.1109/ICECA66444.2025.11383190
url: https://www.scopus.com/pages/publications/105034877357?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2069--2075
keywords:
- Artificial Intelligence
- Carbon Emissions
- Carbon Footprint
- Data Centers
- Energy Consumption
- Environmental Impact
- Large Language Models (LLMs)
- Model Training
- Power Usage Effectiveness (PUE)
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-1687 — The Carbon Footprint of Intelligence: The Environment cost of LLMs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models achieve state-of-the-art benchmarks across a variety of NLP tasks yet involve significant compute demands during training, raising important questions regarding environmental impact and sustainable practices in AI. To address the need for transparency and comparability when assessing emissions impact, a reproducible pipeline that converts published training FLOPs to energy (MWh) using an empirically derived FLOP→MWh conversion (benchmarked on PaLM), and maps energy to CO<sub>2</sub>-equivalent emissions using widely available region-specific grid intensity reports. We apply the pipeline to fifteen foundational LLMs and examine relationships between dense versus sparsely activated (Mixture-Of-Experts) designs, token-budget strategies (e.g., Chinchilla-Style data scaling), and system-level overheads. We find that emissions during training have rapidly accelerated through 2022, with PaLM-scale runs producing emissions on the order of 10<sup>6</sup> kg CO<sub>2</sub>e. However, more efficient data representations and/or Mixture-Of-Experts (MoE) architectures can significantly reduce emissions per unit of performance. A low-carbon grid case study yields approximately an order-of-magnitude reduction in CO<sub>2</sub>e compared with typical U.S. averages. The proposed work recommendations for standardizing reporting practices, adopting compute-aware architectural choices, and pursuing green siting to guide lower-carbon LLM development. © 2025 IEEE.

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
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NLP" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1687.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
