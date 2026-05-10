---
id: paper-2900
title: 'Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs'
authors:
- Yun, Sanggeon
- Masukawa, Ryozo
- Hassan, Raheeb
- Na, Minhyoung
- Imani, Mohsen
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3653660
url: https://www.scopus.com/pages/publications/105027974073?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13702--13711
keywords:
- edge computing
- graph neural networks
- knowledge graph
- multimodal fusion
- Multimodal video anomaly detection
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2900 — Contextual Fusion Strategies for Multimodal GNN-Based Reasoning: Performance and Computational Trade-Offs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of multimodal data is critical for mission-specific tasks that require holistic reasoning over heterogeneous information sources, particularly in resource-constrained environments. MissionGNN, a hierarchical Graph Neural Network (GNN) framework, has demonstrated the feasibility of deploying complex task models on edge devices by leveraging knowledge graphs (KGs). However, effectively fusing multiple modalities remains a fundamental challenge, as fusion design directly affects the trade-off between computational efficiency and inference accuracy. In this paper, we introduce three novel KG-centric multimodal fusion strategies for video anomaly detection within a hierarchical GNN-based reasoning framework: KG-based early fusion, late fusion, and reasoning fusion. We further propose modality-aware knowledge graph generation to enable more targeted, modality-specific reasoning. We conduct extensive experiments on the XD-Violence dataset to evaluate these approaches in terms of detection performance, computational overhead, energy consumption, and the cost of large language model (LLM)-based KG generation. Our results reveal distinct trade-offs among the fusion strategies. Early KG-based fusion provides a well-balanced solution, achieving notable accuracy gains while reducing per-frame energy consumption by over 70%. Late fusion, which employs half-sized modality-aware KGs, yields additional accuracy improvements with only a modest increase in computational cost. Reasoning fusion delivers the highest performance, achieving 72.93% mAP and establishing state-of-the-art results, albeit at the expense of increased resource usage. These findings offer actionable insights for the design of efficient multimodal GNN-based reasoning systems. By systematically characterizing the trade-offs among fusion strategies, this work provides a practical framework to guide the selection of energy-efficient and accuracy-aware solutions for mission-critical applications operating under diverse resource constraints. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2900.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
