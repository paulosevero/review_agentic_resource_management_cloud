---
id: paper-2070
title: Computation-Offloading Optimization for Satellite Edge Computing via Diffusion and Lyapunov-Based Deep Reinforcement Learning
authors:
- Rao, Zheheng
- Zhu, Zhenyu
- Yao, Ye
- Xu, Yanyan
- Cheng, Yanyu
- Du, Hongyang
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3584469
url: https://www.scopus.com/pages/publications/105009611318?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 37747--37762
keywords:
- Computation offloading
- deep reinforcement learning (DRL)
- diffusion model
- satellite edge computing (SEC)
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2070 — Computation-Offloading Optimization for Satellite Edge Computing via Diffusion and Lyapunov-Based Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Satellite edge computing (SEC) extends the capabilities of edge computing technology to satellite networks, facilitating rapid local processing of global task requirements. Deep reinforcement learning (DRL) has emerged as a promising approach for SEC scenarios due to its inherent dynamic adaptability, complex state modeling capability, and long-term optimization potential. However, existing DRL-based computing offloading techniques continue to encounter challenges, including low sample efficiency, poor decision quality, and insufficient long-term stability, which constrain their performance in real satellite network environments. To address these challenges, this study proposes a diffusion and DRL-based approach for computation offloading in SEC networks called the generative artificial intelligence-DRL. First, by implementing the cooperative computing model of the multiSEC, this study comprehensively considers the heterogeneous computing and communication capabilities of satellite nodes, diversity of task types, and dynamic distribution of resources in an offloading strategy, thereby ensuring long-term system sustainability under dynamic resource constraints and provides a solid foundation for computation offloading in satellite networks with time-varying resource. Second, we integrate generative diffusion modeling into the DRL framework to enhance policy generation by producing contextually relevant and high-quality action samples. This not only reduces the dependence on large-scale training data but also improves decision precision and generalization in complex, high-dimensional environments. Finally, a Lyapunov optimization framework is introduced to transform the offloading problem into an online per-slot optimization process, thereby ensuring the long-term stability of the SEC system under dynamic and unpredictable task arrivals and environmental conditions. The experimental results demonstrate that the method proposed offers significant advantages over the existing approaches in reducing task latency and enhancing system stability. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2070.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
