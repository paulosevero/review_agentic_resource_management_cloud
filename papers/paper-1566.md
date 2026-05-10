---
id: paper-1566
title: An innovative edge-driven social IoT service recommender framework utilizing multi-agent deep reinforcement learning
authors:
- Farhadi, Babak
- Asghari, Parvaneh
- Zamanifar, Azadeh
- Javadi, Hamid Haj Seyyed
venue: Knowledge-Based Systems
venue_type: journal
year: 2025
doi: 10.1016/j.knosys.2025.113465
url: https://www.scopus.com/pages/publications/105002052282?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Edge computing
- Friendship path selection
- Multi-agent deep reinforcement learning
- Service recommendation
- Social internet of things
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1566 — An innovative edge-driven social IoT service recommender framework utilizing multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Social Internet of Things (SIoT) recommender systems are designed to enhance the functionality and efficiency of the Internet of Things (IoT) by incorporating social networking principles. They can recommend services, devices, or actions based on the social friendships and interactions between IoT devices and their users. Today, edge-driven, Multi-Agent Deep Reinforcement Learning (MADRL)-based recommender systems offer significant advantages for optimizing friendship paths and improving SIoT network navigability. Utilizing edge computing, these systems process cached services in proximity to their source, thereby improving real-time decision-making and decreasing latency. The edge-driven aspect distributes computational load, reducing central server dependency and enhancing scalability and resilience. On the other hand, MADRL enables adaptive learning from complex SIoT user interactions and network dynamics, ensuring contextually relevant and personalized recommendations. This approach improves network navigability by dynamically optimizing routes and efficiently utilizing network resources through distributed learning. Overall, these recommender systems provide scalable, adaptive, and efficient recommendations, fostering stronger social connections and improving the functionality of SIoT ecosystems. In this article, we have developed an innovative edge-driven, MADRL-based SIoT recommender framework that surpasses the performance of the leading baselines. By leveraging the decentralized processing power of edge computing and sophisticated MADRL-oriented algorithms, the suggested framework significantly enhances the optimization of SIoT friendship paths and network navigability. Extensive experimental results demonstrate that our approach achieves superior accuracy, efficiency, and scalability compared to existing state-of-the-art methods, thereby offering more personalized and contextually relevant service recommendations while reducing delay and improving real-time decision-making in dynamic SIoT environments. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1566.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
