---
id: paper-0900
title: Cross-Technology Federated Matching for Age of Information Minimization in Heterogeneous IoT
authors:
- Esmat, Haitham H.
- Xia, Xiaohao
- Wu, Yinxuan
- Lorenzo, Beatriz
- Guo, Linke
venue: IEEE/ACM Transactions on Networking
venue_type: journal
year: 2024
doi: 10.1109/TNET.2024.3436712
url: https://www.scopus.com/pages/publications/85213451982?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4901--4916
keywords:
- Age of information (AoI)
- cross-technology offloading
- federated learning
- heterogeneous IoT
- mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0900 — Cross-Technology Federated Matching for Age of Information Minimization in Heterogeneous IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Heterogeneous Internet of Things (IoT) networks, which operate using various protocols and spectrum bands like WiFi, Bluetooth, Zigbee, and LoRa, bring many opportunities to collaborate and achieve timely data collection. However, several challenges must be addressed due to heterogeneous data patterns, coverage, spectrum bands, and mobility. This paper introduces a cross-technology IoT network architecture design that facilitates collaboration between service providers (SPs) to share their spectrum bands and offload computing tasks from heterogeneous IoT devices using multi-protocol mobile gateways (M-MGs). The objective is to minimize the age of information (AoI) and energy consumption by jointly optimizing collaboration between M-MGs and SPs for bandwidth allocation, relaying, and cross-technology data scheduling. A pricing mechanism is presented to incentivize different levels of collaboration and matching between M-MGs and SPs. Given the uncertainty due to mobility and task requests, we design a cross-technology federated matching algorithm (CT-Fed-Match) based on a multi-agent actor-critic approach in which M-MGs and SPs learn their strategies in a distributed manner. Furthermore, we incorporate federated learning to enhance the convergence of the learning process. The numerical results demonstrate that our CT-Fed-Match-RC algorithm with cross-technology and relaying collaboration reduces the AoI by 30 times and collects 8 times more packets than existing approaches.  © 1993-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0900.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
