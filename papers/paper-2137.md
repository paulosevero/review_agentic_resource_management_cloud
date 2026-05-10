---
id: paper-2137
title: 'Securing internet of things device data: An ABE approach using fog computing and generative AI'
authors:
- Shruti
- Rani, Shalli
- Boulila, Wadii
venue: Expert Systems
venue_type: journal
year: 2025
doi: 10.1111/exsy.13691
url: https://www.scopus.com/pages/publications/85200107381?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- encryption
- fog computing
- generative AI
- internet of things (IoT)
- multi-authority based CP-ABE
- security
- ubiquitous learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2137 — Securing internet of things device data: An ABE approach using fog computing and generative AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of fog computing, new paradigms for data processing and management for IoT devices have been established in the quickly changing world of teaching/learning. This study addresses the complex issues brought about by the infiltration of diverse data sources by investigating novel approaches to strengthen data security and enhance access control mechanisms in fog computing environments. The commonly used cryptographic technique known as CP-ABE is renowned for providing accurate access control. Unfortunately, current multi-authority CP-ABE methods have difficulties when implemented on low-resource IoT devices. These techniques are not appropriate for resource-constrained IoT devices since the sizes of the secret key and ciphertext grow in proportion to the number of attributes. In this paper, a novel multi-authority CP-ABE approach, called MA-based CP-ABE, efficiently tackles these issues by optimizing the length of secret keys and ciphertext. Users' secret keys are always the same size, no matter how many attributes they own. Moreover, MA-based CP-ABE ensures that the size of the ciphertext scales linearly with the number of authorities rather than characteristics, which makes it a sensible option for devices with restricted resources. A Generative AI approach has also been integrated along with CP-ABE to make sure that the IoT data is secure and privacy is maintained. As per the security and experimental analysis, the proposed approach is considered secure and suitable for IoT-based applications. © 2024 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2137.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
