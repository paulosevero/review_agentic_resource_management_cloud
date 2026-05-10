---
id: paper-1554
title: Generative AI-driven edge-cloud system for intelligent road infrastructure inspection
authors:
- Ejaz, Naveed
- Alam, A.B.M. Bodrul
- Choudhury, Salimur
venue: Results in Engineering
venue_type: journal
year: 2025
doi: 10.1016/j.rineng.2025.105844
url: https://www.scopus.com/pages/publications/105009258501?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Anomaly detection
- Bandwidth optimization
- Cloud computing
- Drones
- Edge computing
- Generative AI
- Infrastructure inspection
- Real-time processing
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

# paper-1554 — Generative AI-driven edge-cloud system for intelligent road infrastructure inspection

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of edge computing and artificial intelligence (AI) has transformed infrastructure inspection by enabling real-time monitoring of roads, bridges, and pipelines. However, high bandwidth consumption, latency, and limited interpretability remain key challenges. This paper presents a novel hybrid edge-cloud framework for intelligent road infrastructure inspection, combining lightweight AI on edge devices with generative AI in the cloud. The Edge AI Module, built on MobileNetV3, performs real-time anomaly detection and generates concise reports with GPS-tagged severity information. Anomalous data is selectively transmitted to the cloud, where advanced models—EfficientNet-B4, MiDaS DPT-Large, and T5-XL—refine classification, estimate depth, compute road quality metrics, and generate structured, actionable reports. The system is evaluated on two diverse datasets: RDD2022, a multinational road damage dataset, and UAV-PDD2023, a high-resolution aerial imagery dataset. Results demonstrate the framework's real-time capability, achieving an edge inference time of 30 to 50 ms and reducing bandwidth usage by 50 to 70%. Cloud processing provides fine-grained analysis and high accuracy in natural language reporting. This dual-tier architecture balances low-latency anomaly detection and in-depth analysis, providing a scalable and interpretable solution for large-scale infrastructure monitoring in dynamic environments. © 2025 The Author(s)

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1554.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
