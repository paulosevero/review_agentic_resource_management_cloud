---
id: paper-0027
title: Towards optimizing the usability of homomorphic encryption in cloud-based medical image processing
authors:
- Marwan, Mbarek
- Kartit, Ali
- Ouahmane, Hassan
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2017
doi: 10.1007/978-3-319-68179-5_19
url: https://www.scopus.com/pages/publications/85034566850?origin=resultslist
publisher: Springer Verlag
pages: 214--224
keywords:
- Cloud computing
- Homomorphic encryption
- Image processing
- Security
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0027 — Towards optimizing the usability of homomorphic encryption in cloud-based medical image processing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Undoubtedly, digital imaging continues to play a crucial role in the diagnosis and treatment of disease. In recent years, there has been growing interest in using Cloud services in the healthcare domain. Even though Cloud Computing offers many advantages, the shift to this new paradigm still poses many problems relating to privacy and data protection. Therefore, it is significantly important to revisit the issue of medical image processing adopting a new method namely Cloud services. We place heavy emphasis on homomorphic encryption schemes, which play a useful role in dealing with privacy and security challenges. In reality, running time is one of the major disadvantages of these types of algorithms. In this context, the present contribution can be conceived of as a novel approach to improve both performance and security. This is achieved by using Multi-Agent System (MAS) and encrypting only the content of a Region-of-Interest (RoI). This would dramatically minimize the size of the needed data. Consequently, it improves the response time of the proposed framework. Furthermore, the generated RoI is divided into certain number of shares, and hence, processed by different agents implemented in several nodes. Following this, this approach is meant to enhance both confidentiality and performance. The experimental results prove that this method is an efficient solution for data encryption in encrypted domain. In fact, the proposal is meant to reduce the running time required to process images that are encrypted using the homomorphic algorithms. © Springer International Publishing AG 2017.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0027.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
