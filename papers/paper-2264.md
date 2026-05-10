---
id: paper-2264
title: Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning
authors:
- Wang, Yang
- Tang, Tengda
- Fang, Zhou
- Deng, Yingnan
- Duan, Yifei
venue: 2025 IEEE 7th International Conference on Communications, Information System and Computer Engineering, CISCE 2025
venue_type: conference
year: 2025
doi: 10.1109/CISCE65916.2025.11065827
url: https://www.scopus.com/pages/publications/105011978021?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 585--589
keywords:
- A3C algorithm
- Microservice architecture
- reinforcement learning
- resource scheduling
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

# paper-2264 — Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of high resource dynamism and intensive task concurrency in microservice systems, this paper proposes an adaptive resource scheduling method based on the A3C reinforcement learning algorithm. The scheduling problem is modeled as a Markov Decision Process, where policy and value networks are jointly optimized to enable fine-grained resource allocation under varying load conditions. The method incorporates an asynchronous multi-threaded learning mechanism, allowing multiple agents to perform parallel sampling and synchronize updates to the global network parameters. This design improves both policy convergence efficiency and model stability. In the experimental section, a real-world dataset is used to construct a scheduling scenario. The proposed method is compared with several typical approaches across multiple evaluation metrics, including task delay, scheduling success rate, resource utilization, and convergence speed. The results show that the proposed method delivers high scheduling performance and system stability in multi-task concurrent environments. It effectively alleviates the resource allocation bottlenecks faced by traditional methods under heavy load, demonstrating its practical value for intelligent scheduling in microservice systems.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2264.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
