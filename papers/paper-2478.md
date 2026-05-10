---
id: paper-2478
title: 'Reconfigurable photonic neural networks: distribution-aligned calibration and dynamic resource allocation for high-performance optical computing accelerators'
authors:
- Zhou, Songcheng
- He, Ziqiang
- Zhao, Yiheng
- Xu, Bo
- Zou, Peng
- Hu, Fangchen
- Chu, Wei
venue: Optics Express
venue_type: journal
year: 2025
doi: 10.1364/OE.574781
url: https://www.scopus.com/pages/publications/105019524947?origin=resultslist
publisher: Optica Publishing Group (formerly OSA)
pages: 45413--45435
keywords:
- Calibration
- Energy efficiency
- Energy utilization
- Green computing
- Photonics
- Reconfigurable hardware
- decitabine
- Computational scale
- Dynamic power allocation
- Dynamic resource allocations
- Generative model
- Network distributions
- Neural-networks
- Optical power
- Optical-
- Performance
- Reconfigurable photonics
- algorithm
- article
- bandwidth
- calibration
- energy consumption
- generative model
- large language model
- nerve cell network
- optics
- residual neural network
- resource allocation
- simulation
- simulator
- workload
- Optical data processing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2478 — Reconfigurable photonic neural networks: distribution-aligned calibration and dynamic resource allocation for high-performance optical computing accelerators

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the rapid adoption of generative models and large language models, the computational demand and scale of modern intelligent data centers have surged. Concurrently, the energy consumption and operational costs of AI workloads are rising exponentially. Photonic computing—offering large bandwidth, low energy consumption, and sub-nanosecond latency—has therefore emerged as a promising paradigm for large-scale AI deployment. However, most existing photonic-AI studies investigate only a single architecture with fixed parameter settings, neglecting dynamic configuration of key variables such as optical power and computational scale. This limitation constrains the attainable energy efficiency and compute density of the system. To overcome these constraints, we propose a distribution-alignment calibration (DAC) algorithm for photonic convolution on an optical computing accelerator (OCA), along with dynamic power allocation (DPA) and dynamic dimension allocation (DDA) schemes. Tested on a calibrated photonic-computing simulator, DAC increases inference accuracy from 12.93% to 75.77% at an input optical power of 5 dBm. In addition, DDA reduces power consumption by 18.7% and 20.9% on ResNet-18 and ResNet-50, respectively, while DPA boosts compute density by 24.84% and 28.19% on the same models. The hardware results demonstrate that applying DPA achieves optical power savings of 16.98% on ResNet-18 and 17.83% on ResNet-50, both slightly lower than those obtained in simulation. These results confirm that dynamically adjusting core size and optical power enables a more flexible, energy-efficient, and high-performance photonic computing system. © 2025 Optica Publishing Group under the terms of the Optica Open Access Publishing Agreement.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2478.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
