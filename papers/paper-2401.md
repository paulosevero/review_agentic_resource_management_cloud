---
id: paper-2401
title: Digital Twin-Driven MADRL Approaches for Communication-Computing-Control Co-Optimization
authors:
- Yuan, Xiaoming
- Tian, Hansen
- Zhang, Xinling
- Du, Hongyang
- Zhang, Ning
- Huang, Kaibin
- Cai, Lin
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2025
doi: 10.1109/JSAC.2025.3574616
url: https://www.scopus.com/pages/publications/105006846302?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3596--3611
keywords:
- digital twin
- Internet of Medical Things
- mobile edge computing
- multi-agent deep reinforcement learning
- parameterized action space
- self-attention mechanism
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

# paper-2401 — Digital Twin-Driven MADRL Approaches for Communication-Computing-Control Co-Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The unpredictability of network environments, limited edge resources, and the high complexity of collaborative policies are significantly hindering the development of the Industrial Internet of Things (IIoT). These challenges are particularly pronounced in healthcare, where high-priority, delay-sensitive medical tasks and large-scale personalized services face substantial obstacles. To address these challenges, this paper proposes the Self-Attention Enhanced QMIX with Multi-Pass Multi-Task Execution (SAE-MT-QMIX) algorithm, aimed at optimizing communication and computing resource allocation as well as task offloading strategies. By leveraging Digital Twin (DT) support, the algorithm achieves collaborative optimization of communication, computing, and control within the Internet of Medical Things (IoMT), significantly enhancing the quality of service for massive personalized applications. The algorithm adopts a distributed execution and centralized training framework: the distributed execution component uses the Multi-Pass Multi-Task Deep Q-Network (MPMT-DQN) algorithm to handle the complexity of parameterized action spaces in multi-task scenarios, while the centralized training component employs the Self-Attention Enhanced QMIX (SAE-QMIX) algorithm to dynamically optimize credit assignment across multiple users. Simulation results demonstrate that SAE-MT-QMIX significantly reduces delay and energy consumption compared to baseline methods. It ensures effective optimization of communication, computing, and control in dynamic IoMT, efficiently addressing diverse demands and tasks while enhancing service quality and system adaptability.  © 1983-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2401.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
