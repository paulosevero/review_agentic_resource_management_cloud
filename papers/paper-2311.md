---
id: paper-2311
title: 'FLAD: Federated-Trained Large Language Models for Autonomous Driving'
authors:
- Xiang, Tianao
- Bi, Yuanguo
- Zhi, Mingjian
- Cai, Lin
venue: IEEE Network
venue_type: journal
year: 2025
doi: 10.1109/MNET.2025.3634409
url: https://www.scopus.com/pages/publications/105025647586?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Autonomous vehicles
- Decision making
- Edge computing
- Intelligent vehicle highway systems
- Privacy-preserving techniques
- Autonomous driving
- Contextual understanding
- Cross-domain
- Decisions makings
- Driving systems
- Language model
- Model-based OPC
- Multi-modal fusion
- Personalizations
- Privacy concerns
- Constrained optimization
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

# paper-2311 — FLAD: Federated-Trained Large Language Models for Autonomous Driving

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) have demonstrated advanced capabilities in contextual understanding, multi-modal fusion and cross-domain reasoning, and improved decision-making and planning, making them a promising technology for advancing autonomous driving (AD). However, training and deploying LLM-based AD systems face significant challenges: high computation requirements, data privacy concerns, and the need for personalization across diverse driving environments. In this paper, we present Federated-Trained LLM for Autonomous Driving (FLAD), a novel framework that leverages distributed intelligence across vehicles, edge servers, and cloud infrastructure to address the above challenges. FLAD introduces three key innovations: 1) a cloud-edge-vehicle collaborative architecture that balances computational demands while preserving data privacy; 2) an intelligent training system that enables resource-constrained vehicles to participate in model development through optimized workload distribution; and 3) a knowledge distillation approach that personalizes models for specific regions. We deploy a working implementation to illustrate how to address practical deployment practical challenges. Then, we use the implementation to demonstrate how FLAD improves autonomous driving performance while efficiently utilizing distributed resources. This article sheds new light on how to apply privacy- preserving federated training on LLMs to enhance autonomous driving systems. © 1986-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2311.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
