---
id: paper-2369
title: 'Privacy-Preserving Offloading for Mobile Edge Computing: A Deep Reinforcement Learning Approach'
authors:
- Yang, Qizhuo
- Sun, Yanhua
- Li, Jiali
- Wang, Zhuwei
- Fang, Chao
- Sun, Yang
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-5006-4_90
url: https://www.scopus.com/pages/publications/105022974062?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 1031--1042
keywords:
- Blockchain
- Computation offloading
- IoT
- Privacy
- UAVs
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

# paper-2369 — Privacy-Preserving Offloading for Mobile Edge Computing: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is now being utilized to address the growing demand for edge devices and high-throughput, low-latency computational tasks. Users can offload tasks to MEC servers, significantly reducing latency and energy consumption. However, traditional single-access-point networks often struggle to meet the needs of a large number of users, and issues such as privacy leakage during the offloading process and information theft on edge servers are frequently overlooked. This paper proposes a multi-access-point offloading framework and a privacy-preserving quality of service (QoS) model. We construct the framework and model, assess privacy risks and protection levels, and integrate blockchain technology to enhance information security. By comprehensively considering user experience and privacy protection, we model the problem as a Markov decision process (MDP). Furthermore, a multi-agent proximal policy optimization (MAPPO) algorithm is proposed to achieve the optimal offloading solution. Simulation results validate the effectiveness of the proposed algorithm. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2369.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
