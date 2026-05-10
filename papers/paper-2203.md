---
id: paper-2203
title: 'ReinDSplit: Reinforced Dynamic Split Learning for Pest Recognition in Precision Agriculture'
authors:
- Tanwar, Vishesh Kumar
- Sarkar, Soumik
- Singh, Asheesh K.
- Das, Sajal K.
venue: Proceedings - 2025 21st International Conference on Distributed Computing in Smart Systems and the Internet of Things, DCOSS-IoT 2025
venue_type: conference
year: 2025
doi: 10.1109/DCOSS-IoT65416.2025.00022
url: https://www.scopus.com/pages/publications/105013846773?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 99--108
keywords:
- Distributed Machine Learning
- Heterogeneous Devices
- Precision Farming
- Smart Agriculture
- Split Learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2203 — ReinDSplit: Reinforced Dynamic Split Learning for Pest Recognition in Precision Agriculture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To empower precision agriculture through distributed machine learning (DML), split learning (SL) has emerged as a promising paradigm, partitioning deep neural networks (DNNs) between edge devices and servers to reduce computational burdens and preserve data privacy. However, conventional SL frameworks' one-split-fits-all strategy is a critical limitation in agricultural ecosystems where edge insect monitoring devices exhibit vast heterogeneity in computational power, energy constraints, and connectivity. This leads to straggler bottlenecks, inefficient resource utilization, and compromised model performance. Bridging this gap, we introduce ReinDSplit, a novel reinforcement learning (RL)-driven framework that dynamically tailors DNN split points for each device, optimizing efficiency without sacrificing accuracy. Specifically, a Q-learning agent acts as an adaptive orchestrator, balancing workloads and latency thresholds across devices to mitigate computational starvation or overload. By framing split layer selection as a finite-state Markov decision process, ReinDSplit convergence ensures that highly constrained devices contribute meaningfully to model training over time. Evaluated on three insect classification datasets using ResNet18, GoogleNet, and MobileNetV2, ReinDSplit achieves 94.31% accuracy with MobileNetV2. Beyond agriculture, ReinDSplit pioneers a paradigm shift in SL by harmonizing RL for resource efficiency, privacy, and scalability in heterogeneous environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2203.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
