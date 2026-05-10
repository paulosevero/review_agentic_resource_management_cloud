---
id: paper-2044
title: Intelligent Cloud Deployment via GNNs
authors:
- Potti, Akash
- Nishaant, N.U.
- Reddy, Sharan
- Bharadwaj, Dhanya
- Asha Rani, K.P.
- Gowrishankar, S.
venue: 2025 9th International Conference on Computational System and Information Technology for Sustainable Solutions, CSITSS 2025
venue_type: conference
year: 2025
doi: 10.1109/CSITSS67709.2025.11295173
url: https://www.scopus.com/pages/publications/105031420634?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Graph neural networks (GNN)
- Infrastructure as cloud (IaC)
- Large language models (LLM'S)
- Natural Language Processing (NLP)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2044 — Intelligent Cloud Deployment via GNNs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid expansion of cloud computing has catalyzed an increasing demand for robust Infrastructure as Code (IaC) tools capable of facilitating automated deployment management. The traditional manual configuration of YAML/JSON within conventional IaC tools is time-consuming and elevates the risk of errors. This research introduces an innovative framework that integrates natural language processing (NLP) in conjunction with graph neural networks (GNNs) to automate the generation of Infrastructure as Code (IaC). Ollama Llama3 converts user prompts into structured components, which are subsequently transformed into a graph representing cloud service dependencies. A graph neural network constructed using PyTorch analyzes this graph to generate optimized YAML configurations that conform to cloud best practices. The system achieves an impressive 92% edge prediction accuracy over synthetic datasets while concurrently reducing deployment time when compared to manual methodologies. Furthermore, this system supports DevOps automation, optimizes costs, and effectively manages multi-cloud environments. This research bridges user requirements with IaC execution, rendering cloud resource management attainable for non-expert users. The approach demonstrated significant reduction in YAML configuration generation time, processing requests in around 15-20 seconds.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2044.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
