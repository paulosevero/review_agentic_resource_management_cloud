---
id: paper-1287
title: An efficient parallel optimization method for large model based on cloud computing
authors:
- Xu, Zilong
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2024
doi: 10.1117/12.3033037
url: https://www.scopus.com/pages/publications/85200353311?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- 3D parallelism
- Cloud computing
- Large model
- NLP
- Optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1287 — An efficient parallel optimization method for large model based on cloud computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent advancements in large-scale language models, as exemplified by ChatGPT, have undergone rapid and substantial development. Their efficacy in natural language processing (NLP) and related domains has notably surpassed that of traditional models. The pivotal role of cloud computing technology in supporting these advancements cannot be overstated. In this paper, we propose an effective and scalable 3D parallel optimization method for large-scale models, leveraging cloud computing capabilities to combine data, pipelines, and tensor slice-based parallelism, where the amalgamation of tensor slicing and pipeline parallelism operates with optimal efficiency in targeted areas. Specially, we curate a high-quality natural language training corpus comprising hundreds of billions of tags and collaboratively develop training methodologies to enhance optimization efficiency and stability. Furthermore, a data parallelization strategy is proposed to expedite the training of large models, utilizing specialized hardware and software tailored for deep learning to augment training speed. To further reduce training time delays, we advocate for the use of more efficient optimization algorithms. This comprehensive approach addresses the intricate technical requisites of large language models in cloud computing, adapting to the burgeoning resource demands anticipated in future AIGC applications, thereby reinforcing the advancement of artificial intelligence. Experimentation has underscored the effectiveness and potential of our system. © 2024 SPIE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "ChatGPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "natural language processing" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NLP" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1287.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
