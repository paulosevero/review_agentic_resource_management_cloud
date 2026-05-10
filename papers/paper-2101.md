---
id: paper-2101
title: Towards a Hybrid Hierarchical Digital Twin Architecture for the 6G Compute Continuum
authors:
- Santos, Jose
- Sameri, Javad
- Van Damme, Sam
- Schwarzmann, Susanna
- Wei, Qing
- Trivisonno, Riccardo
- Vega, Maria Torres
- De Turck, Filip
venue: 'Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025'
venue_type: conference
year: 2025
doi: 10.23919/CNSM67658.2025.11297525
url: https://www.scopus.com/pages/publications/105032162409?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud Computing
- Compute Continuum
- Digital Twin
- Orchestration
- Reinforcement Learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2101 — Towards a Hybrid Hierarchical Digital Twin Architecture for the 6G Compute Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of the 6 G era demands seamless orchestration across an increasingly heterogeneous and distributed compute continuum-spanning edge, fog, and cloud resources. Moreover, the next generation of the mobile network is poised to redefine the digital landscape by enabling pervasive intelligence, ultra-low latency communication, and extreme heterogeneity across the entire network infrastructure. This transformation introduces unprecedented orchestration challenges due to the dynamic, multi-domain, and resource-constrained nature of emerging workloads such as Generative Artificial Intelligence (GenAI) inference, immersive eXtended Reality (XR), and autonomous systems. To tackle this complexity, we advocate for a Hybrid Hierarchical Digital Twin (DT) architecture that serves as a foundation for intelligent, adaptive, and real-time orchestration in 6 G environments. We present a comprehensive vision for integrating DTs as enablers of intelligent, context-aware, and adaptive orchestration mechanisms that span across multiple domains. The proposed architecture introduces a multi-layered DT hierarchy combining local and global views, enabling scalable coordination and real-time decision-making. We highlight key architectural enhancements required to realize this vision, including inter-twin interoperability and behavioral modeling for QoE estimation. This work aims to guide researchers and practitioners in shaping the foundations of resilient and efficient orchestration frameworks for 6 G systems.  © 2025 IFIP.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2101.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
