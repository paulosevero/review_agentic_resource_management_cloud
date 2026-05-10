---
id: paper-2812
title: A Privacy-Preserving Data Pipeline Architecture for Federated and Generative AI Collaboration
authors:
- Venkatesan, Vivek
- Balakumar, Gayathri
- Vasudevan, Girish
- Balu, Gunasekar Pullur
- Saha, Pranoy
venue: 2026 IEEE 16th Annual Computing and Communication Workshop and Conference, CCWC 2026
venue_type: conference
year: 2026
doi: 10.1109/CCWC67433.2026.11393736
url: https://www.scopus.com/pages/publications/105035611129?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 340--347
keywords:
- Collaboration
- Data Privacy
- Differential Privacy
- Federated Learning
- Internet-Scale Systems
- Metadata Governance
- Modular Architectures
- Privacy-Preserving Machine Learning
- Scalable AI Pipelines
- Secure Computation
- Serverless Computing
- Trustworthy AI
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2812 — A Privacy-Preserving Data Pipeline Architecture for Federated and Generative AI Collaboration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cross-organizational collaboration in artificial intelligence (AI) demands pipelines that protect privacy while maintaining scalability and trust. Centralized aggregation of sensitive data is increasingly untenable under modern regulations such as GDPR and HIPAA, and most existing federated or differentialprivacy systems remain siloed or limited to homogeneous, trusted environments. This paper presents a modular, cloud-agnostic architecture that embeds privacy enforcement and governance directly into federated AI pipelines. The proposed framework introduces a metadata-driven privacy controller that dynamically coordinates differential-privacy budgets, encrypted computation, and secure aggregation across heterogeneous organizations. It further incorporates adaptive trust management and gradient-validation mechanisms to mitigate malicious or compromised participants. A multi-node prototype evaluation using synthetic yet heterogeneous healthcare data demonstrates up to 75% reduction in analytics latency, over 70% lower infrastructure cost through serverless orchestration, and resistance to membership-inference attacks while preserving model utility (AUC ≈ 0.93). The architecture is intended as a reusable reference design that also generalizes to unstructured data via privacy-preserving feature embeddings. These results highlight a practical foundation for scalable, privacy-first AI collaboration across institutional and data-modality boundaries. © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2812.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
