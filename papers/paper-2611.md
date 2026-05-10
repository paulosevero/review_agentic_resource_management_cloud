---
id: paper-2611
title: 'Multivehicles Cooperation: USV and AUV Cooperative Data Collection for Underwater Wireless Sensor Networks'
authors:
- Hu, Zheng
- Xu, Qichao
- Su, Zhou
- Dai, Minghui
- Li, Ruidong
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2026
doi: 10.1109/TITS.2025.3647120
url: https://www.scopus.com/pages/publications/105026390760?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4618--4634
keywords:
- autonomous underwater vehicle (AUV)
- data collection
- uncrewed surface vehicle (USV)
- Underwater wireless sensor networks (UWSNs)
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

# paper-2611 — Multivehicles Cooperation: USV and AUV Cooperative Data Collection for Underwater Wireless Sensor Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To advance the development of maritime intelligent transportation systems (MITS), underwater wireless sensor networks (UWSNs), composed of numerous sensor nodes, have been widely deployed for underwater information perception. However, UWSNs face critical challenges in achieving cost-effective and timely data collection due to their large-scale deployment and stringent data timeliness requirements. To address this challenge, this paper proposes an efficient data collection scheme for UWSNs through the collaboration between uncrewed surface vehicles (USVs) and autonomous underwater vehicles (AUVs). Specifically, we first introduce a cooperative framework where AUVs select appropriate USVs to form USV-AUV clusters. Within each cluster, AUVs are responsible for sensing data collection, while USVs act as relay nodes, moving toward the destination (e.g., data center). We then devise an evolutionary game-theoretic cluster forming mechanism, deriving evolutionarily stable strategies (ESS) through replicator dynamics analysis, which guarantees a provable Nash equilibrium. Next, we present a hierarchical optimization method that models the interaction between UWSNs and the cluster as a two-agent Markov decision process, where a dual-agent Q-learning algorithm is designed to jointly optimize the decisions of both entities. Finally, extensive simulations demonstrate that the proposed scheme outperforms conventional methods in improving the efficiency of sensing data collection for UWSNs.  © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2611.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
