---
id: paper-2492
title: 'Deployment and Synchronization for Reputation-Driven Vehicular Digital Twins: A Learning-Based Approach'
authors:
- Zou, Zirui
- Yang, Weiwei
- Zheng, Jinkai
- Zhang, Yanfeng
- Zeng, Xiaoyi
- Li, Xiaoyan
- Liu, Tao
venue: 2025 IEEE/CIC International Conference on Communications in China, ICCC Workshops 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCCWorkshops67136.2025.11148140
url: https://www.scopus.com/pages/publications/105017656484?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- age of information
- Digital twins
- reputation
- vehicular edge computing
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

# paper-2492 — Deployment and Synchronization for Reputation-Driven Vehicular Digital Twins: A Learning-Based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of the Internet of Vehicles (IoV), the integration of Digital Twin (DT) technology has shown considerable potential across a wide range of application scenarios. However, in high-density traffic environments, the overlapping coverage of edge nodes presents a challenge for vehicles in selecting appropriate nodes for DT deployment. Additionally, heterogeneous edge node reputations may result in suboptimal deployments, leading to issues such as resource imbalance and synchronization failures. To address these challenges, we propose a DT-assisted vehicular edge computing framework. By evaluating contributions of Roadside Units (RSUs) during the synchronization, we develop a reputation-driven DT deployment model. In this model, RSUs with higher reputation can receive greater deployment rewards, thereby incentivizing their active participation in the DT deployment. Furthermore, to minimize the system Age of Information and deployment cost, we develop a Transformer-Critic-based Multi-Agent Proximal Policy Optimization (TC-MAPPO) algorithm to jointly optimize DT placement and resource allocation. Extensive experiments demonstrate the effectiveness of the proposed TC-MAPPO approach and highlight its superiority in enhancing overall average reward. © 2025 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2492.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
