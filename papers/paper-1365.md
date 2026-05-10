---
id: paper-1365
title: Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs
authors:
- Adeseye, Aisvarya
- Isoaho, Jouni
- Virtanen, Seppo
- Tahir, Mohammad
venue: 2025 IEEE Nordic Circuits and Systems Conference, NORCAS 2025 - Proceedings
venue_type: conference
year: 2025
doi: 10.1109/NorCAS66540.2025.11231309
url: https://www.scopus.com/pages/publications/105029505782?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Energy-Efficient AI
- Local Deployment of LLMs
- Prompt Engineering
- Resource-Constrained Systems
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

# paper-1365 — Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The local deployment of Large Language Models (LLMs) is essential for privacy and latency in several domains. However, it faces significant challenges in terms of memory, power, and inference speed, particularly in resource-constrained systems such as Internet of Things (IoT) and edge computing devices. Most existing studies emphasize compression and hardware tuning, while holistic system-level optimization remains incomplete, and the role of prompt design is still underexplored. This study introduces a structured evaluation of prompt engineering strategies designed to enhance resource efficiency and accuracy in local LLMs, applied across three textual analysis tasks: theme extraction, frequency analysis, and impact analysis. Four experimental conditions were compared: Baseline, System Prompt Only (SP), User Prompt Only (UP), and System+User Prompt ($S P+U P$). Using multiple LLMs ranging from 1 B to 70B parameters, we audited tokens generated, latency, VRAM usage, hallucination rates, and other structural errors. The results show that System Prompts alone substantially reduced computational overhead, whereas User Prompts improved accuracy and task alignment. Their combination yields comprehensive improvements, maximizing both efficiency and reliability. The proposed prompt design enabled smaller LLMs to rival larger ones in efficiency and accuracy, with LLaMA-3.2, 3B with SP+UP reducing VRAM by 96%, latency by 85%, and hallucinations by 83% when compared to the 70B with Baseline. Even LLaMA-3.2, 1B proved to be a viable option, especially when VRAM size is a critical factor.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1365.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
