---
id: paper-1629
title: Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction
authors:
- Harshith, P.
- Murthy, Anantha
- Harshitha, G.M.
- Prathwini
- Shetty, Keerthi
- Suvaris, Roshan D
venue: 2025 9th International Conference on Computational System and Information Technology for Sustainable Solutions, CSITSS 2025
venue_type: conference
year: 2025
doi: 10.1109/CSITSS67709.2025.11294975
url: https://www.scopus.com/pages/publications/105031361980?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- cost-efficient LLM inference
- LightGBM
- Prompt routing
- semantic difficulty
- Sentence-BERT
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
    my_justification: LLM as workload
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

# paper-1629 — Cost-Efficient Prompt Routing in Large Language Model Inference Using BERT-Based Difficulty Prediction

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) like GPT-4, Claude 3.5, and Gemini 2.5 are now widely used in natural language processing tasks. But their high inference cost and computing requirements make it hard to scale them, especially in areas with limited resources such as education, customer support, and interactive AI tools. This work proposes a cost-efficient inference setup that uses semantic embeddings from a BERT-based model, a LightGBM classifier to estimate prompt difficulty, and dynamic routing logic to pick the most appropriate LLM based on a balance between cost and accuracy. The system was tested on 990 prompts taken from OpenBookQA (Easy), GSM8K (Medium), and MMLU (Hard). It achieved a weighted F1 score of 0.89, while cutting average inference cost by over 95% from $12.08 to $0.34 per 1,000 prompts compared to always using high-end models. Both semantic embedding and routing logic were crucial in maint aining good performance at cheap cost, according to ablation stu dies, demonstrating that promptaware routing can be applied to real-world LLM inference systems and scale well. This research also evaluate routing framework end-to-end on a mixed workload of conversational, summarisation and code-generation tasks to measure its impact on latency and throughput. Across 1,200 real-world prompts, the system achieves a 40% reduction in average inference time and routes over 70% of queries to lower-capacity models without dropping overall response quality-maintaining an average human-judged acceptability score within 2% of always using the top-tier model. Finally, we release our implementation as a set of Dockerised microservices, complete with pre-trained difficulty predictors and REST endpoints, to simplify integration into existing LLM pipelines.  © 2025 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "BERT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1629.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
