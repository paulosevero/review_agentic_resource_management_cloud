---
id: paper-2157
title: 'HRL-GT: A Hybrid Reinforcement Learning and Game Theory Framework for Energy-Efficient Cluster Head Election and Routing in Underwater Sensor Networks'
authors:
- Sivsakthiselvan, S.
- Palanivelan, M.
- Sridevi, N.
- Purushothaman, K.E.
venue: 2025 2nd International Conference on Computing and Data Science, ICCDS 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCDS64403.2025.11209597
url: https://www.scopus.com/pages/publications/105023858115?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Clustering
- Edge Computing
- Energy Efficiency
- Internet of Underwater Things (IoUT)
- Reinforcement Learning
- Routing
- SEP
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2157 — HRL-GT: A Hybrid Reinforcement Learning and Game Theory Framework for Energy-Efficient Cluster Head Election and Routing in Underwater Sensor Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Underwater Wireless Sensor Networks (UWSNs) are critical for various marine applications, including environmental monitoring, disaster prediction, and military surveillance. However, these networks face persistent challenges such as energy constraints, dynamic topology, and high propagation delays. To address these limitations, this paper proposes a novel Hybrid Reinforcement Learning with Game Theory (HRL-GT) framework for cluster head (CH) election and adaptive routing in UWSNs. The proposed model integrates a Deep Q-Network (DQN)-based learning agent for optimizing routing decisions with a game-theoretic approach for fair and energy-efficient CH selection. By jointly considering factors such as residual energy, node depth, and link quality, HRL-GT ensures both stability and adaptability in routing and clustering mechanisms. Performance evaluation through MATLAB simulations demonstrates that HRL-GT significantly improves network lifetime, reduces energy consumption, enhances packet delivery ratio (PDR), and minimizes CH change rates when compared to existing protocols such as EA-DBSEP-IoUT, DBSEP, and EEACA. The results validate the effectiveness of HRL-GT in extending the operational longevity and reliability of UWSNs in harsh underwater environments. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2157.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
