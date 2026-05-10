---
id: paper-2394
title: Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments
authors:
- Yu, Deshui
- Liu, Xianhui
- Ning, Jia
- Wang, Shengyi
- Zhu, Chenglin
- Zhao, Weidong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3620126
url: https://www.scopus.com/pages/publications/105019620716?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 54256--54273
keywords:
- AI task offloading
- cloud-edge-device computing
- deep reinforcement learning
- Industrial Internet of Things (IIoT)
- multiagents
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2394 — Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a key enabler of Industry 4.0, the Industrial Internet of Things (IIoT) has been rapidly advancing, driving the increasingly widespread adoption of artificial intelligence (AI) in industrial production. However, the high computational demands of AI tasks contrast sharply with the limited computing resources available in industrial environments, highlighting the need for efficient task offloading strategies. This article addresses AI task offloading under resource-constrained IIoT scenarios by proposing LSTM-enhanced hierarchical-classification offloading with DQN (LHC-DQN). The proposed framework adopts a two-layer offloading architecture: the first layer performs global scheduling by assigning tasks to cloud, edge, or device resources, while the second layer refines the allocation. Cloud and edge nodes apply mathematical optimization, whereas device nodes leverage DRL agents for autonomous decision-making. To handle AI task heterogeneity, a classification-aware mechanism is introduced in the first layer, deploying separate DQN agents for inference and training tasks to improve adaptability and efficiency. Furthermore, an LSTM module is integrated into the DQN backbone to capture temporal dependencies in task states. Experimental results in a simulated environment demonstrate that LHC-DQN significantly outperforms traditional methods, increasing task completion rates approximately from 47% to 68%. Ablation and generalization tests further confirm the robustness and effectiveness of the proposed method. Overall, LHC-DQN offers a practical and efficient solution for intelligent task offloading and resource scheduling in IIoT environments. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2394.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
