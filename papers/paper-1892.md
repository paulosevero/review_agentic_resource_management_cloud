---
id: paper-1892
title: Optimizing lightweight neural networks for efficient mobile edge computing
authors:
- Liu, Liu
- Xu, Zhifei
venue: Scientific Reports
venue_type: journal
year: 2025
doi: 10.1038/s41598-025-04652-7
url: https://www.scopus.com/pages/publications/105009617025?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- Internet of things
- Mobile edge computing
- Neural networks
- Reinforcement learning
- Resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1892 — Optimizing lightweight neural networks for efficient mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the era of rapid technological advancement, Mobile Edge Computing (MEC) has become essential for supporting latency-sensitive applications such as internet of things, autonomous driving, and smart cities. However, efficient resource allocation remains a challenge due to the dynamic nature of MEC environments. The primary difficulties stem from fluctuating workloads, varying network conditions, and heterogeneous computational capabilities, which make real-time task offloading and resource management complex. Traditional centralized approaches suffer from high computational overhead and poor scalability, while conventional machine learning-based methods often require extensive labeled data and fail to adapt quickly in dynamic settings. To address these issues, this study proposes an advanced Multi-Agent Reinforcement Learning (MARL) framework combined with a lightweight neural network, LtNet, to optimize task offloading and resource management in MEC. MARL enables decentralized decision-making, allowing each device to learn optimal offloading strategies and adapt dynamically. Compared to prior single-agent or heuristic methods, our approach improves scalability and efficiency while reducing computational complexity. LtNet further enhances performance using H-Swish activation and selective Squeeze-and-Excitation modules, ensuring lower computational overhead. Experimental results demonstrate that the proposed methods achieve a 12–22% reduction in task completion time, a 5–8% decrease in energy consumption, and consistently high resource utilization, making them highly effective in managing dynamic MEC environments. © The Author(s) 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1892.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
