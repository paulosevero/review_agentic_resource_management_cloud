---
id: paper-1497
title: Management of Safety-Critical AI Services in the Compute Continuum
authors:
- Colombi, Lorenzo
- Tortonesi, Mauro
venue: 'Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025'
venue_type: conference
year: 2025
doi: 10.23919/CNSM67658.2025.11297570
url: https://www.scopus.com/pages/publications/105032081832?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Industry 5.0
- MLOps
- Zero-touch Service Management
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1497 — Management of Safety-Critical AI Services in the Compute Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing complexity and criticality of AIdriven services across the compute continuum, spanning from edge devices to cloud datacenters, necessitates resilient, intelligent, and explainable management strategies. This work addresses the challenges of deploying and orchestrating safetycritical AI services in dynamic and resource-constrained environments, such as Industry 5.0 and Human Assistance and Disaster Recovery (HADR). We present a suite of complementary solutions, including a cloud-native MLOps platform tailored for SMEs, a semi-supervised federated learning framework (FedEdge-Learn), and novel semantic communication mechanisms that optimize data transmission using LLM-driven embeddings. Furthermore, we introduce an intent-based Zerotouch Service Management (ZSM) architecture, leveraging neurosymbolic AI and collaborative intelligence to automate orchestration, model fine-tuning, and policy reasoning across federated Kubernetes clusters. These efforts pave the way for trustworthy, adaptive, and efficient AI service lifecycle management in environments characterized by disconnections, privacy constraints, and operational unpredictability. Future work focuses on extending the neuro-symbolic approach to support additional tasks, including dynamic node selection, optimized placement across the compute continuum with the goal of improving resilience and interpretability in distributed, resource-constrained environments like Industry 5.0 and HADR, while addressing challenges such as intermittent connectivity and evolving operational conditions.  © 2025 IFIP.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1497.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
