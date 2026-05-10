---
id: paper-2413
title: A collaborative inference strategy for medical image diagnosis in mobile edge computing environment
authors:
- Zhang, Shiqian
- Cui, Yong
- Xu, Dandan
- Lin, Yusong
venue: PeerJ Computer Science
venue_type: journal
year: 2025
doi: 10.7717/peerj-cs.2708
url: https://www.scopus.com/pages/publications/105000266043?origin=resultslist
publisher: PeerJ Inc.
pages: ''
keywords:
- Collaborative inference
- Feature compression
- Medical imaging
- Mobile edge computing
- Reinforcement learning
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

# paper-2413 — A collaborative inference strategy for medical image diagnosis in mobile edge computing environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The popularity and convenience of mobile medical image analysis and diagnosis in mobile edge computing (MEC) environments have greatly improved the efficiency and quality of healthcare services, necessitating the use of deep neural networks (DNNs) for image analysis. However, DNNs face performance and energy constraints when operating on the mobile side, and are limited by communication costs and privacy issues when operating on the edge side, and previous edge-end collaborative approaches have shown unstable performance and low search efficiency when exploring classification strategies. To address these issues, we propose a DNN edge-optimized collaborative inference strategy (MOCI) for medical image diagnosis, which optimizes data transfer and computation allocation by combining compression techniques and multi-agent reinforcement learning (MARL) methods. The MOCI strategy first uses coding and quantization-based compression methods to reduce the redundancy of image data during transmission at the edge, and then dynamically segments the DNN model through MARL and executes it collaboratively between the edge and the mobile device. To improve policy stability and adaptability, MOCI introduces the optimal transmission distance (Wasserstein) to optimize the policy update process, and uses the long short-term memory (LSTM) network to improve the model’s adaptability to dynamic task complexity. The experimental results show that the MOCI strategy can effectively solve the collaborative inference task of medical image diagnosis and significantly reduce the latency and energy consumption with less than a 2% loss in classification accuracy, with a maximum reduction of 38.5% in processing latency and 71% in energy consumption compared to other inference strategies. In real-world MEC scenarios, MOCI has a wide range of potential applications that can effectively promote the development and application of intelligent healthcare. © 2025 Zhang et al.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2413.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
