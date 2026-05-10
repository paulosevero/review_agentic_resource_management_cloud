---
id: paper-0596
title: Achieving Reinforcement Learning Speedup via Quantum Kernel Estimation
authors:
- Gilvarry, John
- Emeakaroha, Vincent C.
venue: International Symposium on Technology and Society, Proceedings
venue_type: conference
year: 2023
doi: 10.1109/ISTAS57930.2023.10305952
url: https://www.scopus.com/pages/publications/85178501434?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Artificial Intelligence
- Kernel Based Reinforcement Learning
- Quantum Kernel Estimation
- Quantum Machine Learning
- Sustainable Development
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0596 — Achieving Reinforcement Learning Speedup via Quantum Kernel Estimation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Reinforcement learning is playing a crucial role in sustainable developments and enabling wide applications in our daily lives ranging from self-driving cars, robotics, automation, personalised product suggestions, user notifications and many more. Kernel-based reinforcement learning holds theoretical guarantees of convergence to a unique solution for decision function approximation. This has motivated the development of implementations that exploit the advantage of kernel methods whilst overcoming the 'curse of dimensionality'. The theoretical properties of kernel-based methods also support the combination of learning agents in loosely coupled systems into a single combined model for composable learning. Learning speedup is achievable by introducing expert knowledge to the algorithm through the kernel, which reduces variance by increasing bias and thus learning speed. Despite the theoretical promise of kernel based reinforcement learning methods, and continued evolution of more efficient algorithms, practical implementation are not prevalent. Research in quantum machine learning has successfully applied quantum algorithms to achieve computational speed-ups for various machine-learning tasks, and has also identified potential quantum advantage through the identification of patterns not accessible to classical data mapping. To date, this has not been applied to kernel based reinforcement learning. Recent work in the field of quantum learning suggests an important duality between quantum machine learning and kernel machine learning methods. Therefore, this paper proposes a framework to complement kernel-based reinforcement learning with quantum generated feature maps for function approximation to improve learning speed. This has positive consequences for optimisation of reinforcement learning techniques already in use to support sustainability targets in applications such as industry innovation and infrastructure, power generation management, data centre cooling and self-driving cars. Our established framework enables the adoption of emerging quantum kernel methods for reinforcement learning applications. The achieved results show over 20 % improvement and positive impacts of quantum map selection on model performance for different problems.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0596.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
