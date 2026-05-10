---
id: paper-1163
title: Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations
authors:
- Rovnyagin, Mikhail. M.
- Sinelnikov, Dmitry M.
- Eroshev, Artem A.
- Rovnyagina, Tatyana A.
- Tikhomirov, Alexander V.
venue: Proceedings of the 2024 Conference of Young Researchers in Electrical and Electronic Engineering, ElCon 2024
venue_type: conference
year: 2024
doi: 10.1109/ElCon61730.2024.10468250
url: https://www.scopus.com/pages/publications/85189968004?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 277--280
keywords:
- ChatGPT
- Context Embedding
- Large Language Model
- Memory Allocation
- Transformer-type Neural Network
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1163 — Optimizing Cache Memory Usage Methods for Chat LLM-models in PaaS Installations

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, LLM models have become widespread in industry. They are used as the basis for voice assistants, troubleshooting systems, chatbots and much more. The work of LLM is based on the architecture of transformer-type neural networks, where text is supplied as input (for example, text chat), and the model, estimating the character-by-character probability, returns the result also in the form of text. In this case, the model does not retrain. And the context itself is constantly accumulating. This paper proposes two ways to reduce the memory allocated for storing the test chat context. The first method is to periodically launch additional training in order to embed the chat context into the core of the model itself. The article discusses the pros and cons of this approach. The second method is to save in the text chat cache only with those users where this context has already been formed. The article describes the layout for conducting the experiment, provides the results of the experimental study and describes the method for assessing the 'maturity' of the chat correspondence context. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1163.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
