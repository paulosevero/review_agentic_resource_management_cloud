---
id: paper-0981
title: Blockchain-Based Pseudonym Management for Vehicle Twin Migrations in Vehicular Edge Metaverse
authors:
- Kang, Jiawen
- Luo, Xiaofeng
- Nie, Jiangtian
- Wu, Tianhao
- Zhou, Haibo
- Wang, Yonghua
- Niyato, Dusit
- Mao, Shiwen
- Xie, Shengli
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3404559
url: https://www.scopus.com/pages/publications/85194050207?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 34254--34269
keywords:
- Cross-chain
- deep reinforcement learning
- pseudonym management
- twin migration
- vehicular metaverse
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0981 — Blockchain-Based Pseudonym Management for Vehicle Twin Migrations in Vehicular Edge Metaverse

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Driven by the great advances in metaverse and edge computing technologies, vehicular edge metaverses are expected to disrupt the current paradigm of intelligent transportation systems. As highly computerized avatars of vehicular metaverse users (VMUs), the vehicle twins (VTs) deployed in edge servers can provide valuable metaverse services to improve driving safety and on-board satisfaction for their VMUs throughout journeys. To maintain uninterrupted metaverse experiences, VTs must be migrated among edge servers following the movements of vehicles. This can raise concerns about privacy breaches during the dynamic communications among vehicular edge metaverses. To address these concerns and safeguard location privacy, pseudonyms as temporary identifiers can be leveraged by both VMUs and VTs to realize anonymous communications in the physical space and virtual spaces. However, existing pseudonym management methods fall short in meeting the extensive pseudonym demands in vehicular edge metaverses, thus dramatically diminishing the performance of privacy preservation. To this end, we present a cross-metaverse empowered dual pseudonym management framework. We utilize cross-chain technology to enhance management efficiency and data security for pseudonyms. Furthermore, we propose a metric to assess the privacy level and employ a multiagent deep reinforcement learning (MADRL) approach to obtain an optimal pseudonym generating strategy. Numerical results demonstrate that our proposed schemes are high-efficiency and cost-effective, showcasing their promising applications in vehicular edge metaverses.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0981.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
