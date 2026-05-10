---
id: paper-1985
title: A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments
authors:
- Naser, Zainab Saadoon
- Marouane, Hend
- Fakhfakh, Ahmed
- Almatwari, Zaid Abdulsalam
venue: Proceedings - International Conference on Informatics and Computational Sciences
venue_type: conference
year: 2025
doi: 10.1109/ICICoS68590.2025.11330010
url: https://www.scopus.com/pages/publications/105032385383?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 126--131
keywords:
- Adaptive traffic signal control
- cloud computing
- deep reinforcement learning
- multi-agent systems
- real-time traffic optimization
- scalable architecture
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
    my_justification: RL
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

# paper-1985 — A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient traffic signal control is a cornerstone of modern urban mobility, playing a critical role in reducing congestion, travel delays, and emissions. Traditional fixed-time or rule-based traffic signal systems often lack the flexibility to adapt to dynamic and non-uniform traffic patterns, particularly in densely populated cities. To address these limitations, this paper proposes a scalable, cloud-based framework for adaptive traffic signal optimization using multi-agent deep reinforcement learning (DRL). In the proposed system, each intersection is governed by an independent agent trained with the Proximal Policy Optimization (PPO) algorithm. Agents learn traffic signal policies from localized, real-time observations, including vehicle counts, waiting times, and signal states, enabling decentralized, context-aware control. The framework is designed for cloud deployment, leveraging Google Colab and Google Cloud Storage for scalable training, consistent metric logging, and reproducible post-simulation analysis. Traffic behavior is modeled using the Simulation of Urban Mobility (SUMO) platform, ensuring a realistic and flexible environment for evaluation. Extensive experiments demonstrate that the DRL-based system significantly outperforms traditional fixed-time control across key metrics such as average waiting time, vehicle queue length, throughput, and congestion levels. Performance improvements are especially evident under high-density and variable traffic conditions, where adaptability is most critical. In addition, the system exhibits robust convergence across episodes, while the cloud-integrated design ensures scalability, reproducibility, and practical applicability for smart city deployment.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1985.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
