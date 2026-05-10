---
id: paper-0151
title: A wrapper based feature selection in bone marrow plasma cell gene expression data
authors:
- Ragunthar, T.
- Selvakumar, S.
venue: Cluster Computing
venue_type: other
year: 2019
doi: 10.1007/s10586-018-2094-2
url: https://www.scopus.com/pages/publications/85042423051?origin=resultslist
publisher: Springer
pages: 13785--13796
keywords:
- Artificial bee colony (ABC)
- B-cell (BC)
- Feature selection
- Hybrid ABC with SDS and support vector machine (SVM)
- Plasma cell (PC)
- Stochastic diffusion search (SDS)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0151 — A wrapper based feature selection in bone marrow plasma cell gene expression data

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Microarray technology permits simultaneous monitoring of several gene expressions for every sample. But unfortunately, this classification of such samples into the distinct classes has often been found to difficult as the actual number of genes (the features) will to a great extent exceed the actual number of the samples. There is a high dimensionality in gene and its expression data which is a huge challenge in many of the problems of classification. Cloud computing is that popular concept of computing which performs a processing of a data of huge volumes by making use of highly accessible resources that are geographically distributed and accessed by the users based on the policy of pay as per use. In spite of the several steps in that of the B Cell that are now elucidate the last few stages of that of the plasma cell (PC) based differentiation that have not been understood yet. The PCs had generated at the time of primary and humoral immune responses that have started their differentiation within their light zones for the germinal centers of such light zones of that of the lymph nodes or the ones in the red pulp of the spleen having a life span of about few days. The selection of the features will aim at the maintenance of their original features of such data and at this time it will seek at identifying their main features and will weed out all those that are irrelevant for building of a learning model that is impactful. Identifying one global maximum will be Non-deterministic Polynomial (NP)-hard and if the criterion is decomposable or possesses the properties that can make some approximate type of optimization easy. The artificial bee colony (ABC) is that one that is used widely and applied for solving all real world problems. The stochastic diffusion search (SDS) will be an efficient multi-agent global search based technique of optimization applied to that of several problems and here the hybrid ABC with that of the SDS feature selection will be proposed and these images will be grouped as either normal or abnormal PC of the bone marrow that is based on this gene expression data. The support vector machine is that algorithms of supervised learning that is capable of being able to solve the complex problems in classification. This proposed method of gene selection will yield a comparable performance for the classification on being compared to that of the currently existing classifiers providing another new insight in case of feature selection. © 2018, Springer Science+Business Media, LLC, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0151.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
