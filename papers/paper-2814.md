---
id: paper-2814
title: 'Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction'
authors:
- Wada, Akihiko
- Nishizawa, Mitsuo
- Yamamoto, Akira
- Akashi, Toshiaki
- Hagiwara, Akifumi
- Irie, Ryusuke
- Hayakawa, Yayoi
- Kikuta, Junko
- Shimoji, Keigo
- Sano, Katsuhiro
- Nakanishi, Atsushi
- Kamagata, Koji
- Aoki, Shigeki
venue: Scientific Reports
venue_type: journal
year: 2026
doi: 10.1038/s41598-026-36904-5
url: https://www.scopus.com/pages/publications/105029761189?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- Cloud Computing
- Computer Security
- Confidentiality
- East Asian People
- Humans
- Japan
- Japanese people
- cloud computing
- computer security
- confidentiality
- East Asian
- human
- Japan
- Japanese (people)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-2814 — Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-based Large Language Models (LLMs) excel at medical text processing, but privacy regulations impose significant constraints on transmitting Protected Health Information (PHI) to external services, creating barriers to AI adoption for many healthcare institutions. While contractual agreements (e.g., Business Associate Agreements under HIPAA) may permit such transmission under specific conditions, many institutions prefer or require complete data sovereignty. Local LLMs address this need but have historically underperformed. This study introduces a five-phase optimization framework to bridge this performance gap. Using 160 synthetic Japanese radiology reports, we benchmarked 14 local LLMs against cloud leaders. Our key finding is a notable performance pattern: models with baseline scores below 87–88 points gained an average of + 6.92 points (p < 0.001), while higher-scoring models did not, suggesting a potential threshold effect for targeted optimization that warrants further investigation. The optimized Mistral-Small-3.2 with Self-Refine achieved 91.54 points—97.8% of GPT-4.1's performance—with perfect rule adherence and a clinically acceptable processing time of 24.6 s per report for batch workflows. Our work demonstrates that systematically optimized local LLMs can approach cloud-leader performance. Importantly, it provides a strategic framework guiding institutions on when and where to apply advanced optimization, enabling efficient and trustworthy AI deployment while ensuring patient privacy. © The Author(s) 2026.

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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2814.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
