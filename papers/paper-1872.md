---
id: paper-1872
title: Cooperative Task Offloading Through Asynchronous Deep Reinforcement Learning in Mobile Edge Computing for Future Networks
authors:
- Liu, Yuelin
- Li, Haiyuan
- Vasilakos, Xenofon
- Hussain, Rasheed
- Simeonidou, Dimitra
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11160823
url: https://www.scopus.com/pages/publications/105018451928?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1390--1395
keywords:
- 6G
- Asynchronous Deep Reinforcement Learning
- Cooperative Task Offloading
- Mobile Edge Computing
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

# paper-1872 — Cooperative Task Offloading Through Asynchronous Deep Reinforcement Learning in Mobile Edge Computing for Future Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Future networks (including 6G) are poised to accelerate the realisation of Internet of Everything. The latter will imply a high demand for computational resources to support new services. Mobile Edge Computing (MEC) is a promising solution that enables offloading computation-intensive tasks to nearby edge servers from the end-user devices, thereby reducing latency and energy consumption. Nevertheless, relying solely on a single MEC server for task offloading can lead to uneven resource utilisation and suboptimal performance in complex scenarios. Additionally, traditional task offloading strategies specialise in centralised policy decisions, which unavoidably entails extreme transmission latency and reach computational bottleneck. To address these gaps, we propose a latency-efficient and energy-efficient Cooperative Task Offloading framework with Transformer-driven Prediction (CTO-TP), leveraging asynchronous multi-agent deep reinforcement learning to address these challenges. This approach fosters edge-edge cooperation and decreases the synchronous waiting time by performing asynchronous training, optimising task offloading, and resource allocation across distributed networks. The performance evaluation demonstrates that the proposed CTO-TP algorithm reduces up to 80% overall system latency and 87% energy consumption compared to the baseline schemes.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1872.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
