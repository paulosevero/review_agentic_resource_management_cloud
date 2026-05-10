---
id: paper-1986
title: 'A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach'
authors:
- Naydenov, Nikolas
- Ruseva, Stela
- Chemungor, Naomy Jerono
- Adewole, Kayode Sakariyah
venue: ISMSIT 2025 - 9th International Symposium on Multidisciplinary Studies and Innovative Technologies, Proceedings
venue_type: conference
year: 2025
doi: 10.1109/ISMSIT67332.2025.11268074
url: https://www.scopus.com/pages/publications/105031084139?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Anomaly Detection
- Cloud-Native
- Containerization
- eBPF
- Intrusion Detection
- Kubernetes
- Machine Learning
- Microservices
- Network Forensics
- Train-Serve Skew
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

# paper-1986 — A Framework for ML-Based Intrusion Detection and Prevention: A Containerized, Cloud-Native Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The operational deployment of machine learning (ML) based security systems in production cloud environments remains a significant challenge, often hindered by a disconnect between offline training and real-time inference known as train-serve skew. This paper presents a novel, dual-workflow, cloud-native architecture for an Intrusion Detection and Prevention System (IDPS) that bridges this gap. Our architecture builds upon a flexible ML framework from foundational research, which was validated in an offline-only proof-of-concept. The primary contributions of this paper are twofold: first, we provide a complete blueprint for orchestrating the framework as a containerized, microservice-based cluster using platforms like Kubernetes. Second, we introduce a minimal-overhead online workflow that uses high-performance, kernel-level probes and a real-time agent to replicate the feature-rich vectors required for accurate detection, thus solving the train-serve skew problem. This dual-workflow design separates low-latency real-time detection from deep offline analysis, which leverages the foundational two-stage ML pipeline and context-aware capture tools. This work provides a validated blueprint for an effective IDPS that achieves the scalability, resilience, and maintainability required for a modern cloud security service.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1986.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
