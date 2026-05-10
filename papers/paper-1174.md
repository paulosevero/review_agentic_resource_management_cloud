---
id: paper-1174
title: 'Resource Allocation and QoE Maximization in Aerial MEC-empowered Metaverse Service: A CCM-Multi-agent DRL approach'
authors:
- Seid, Abegaz Mohammed
- Abishu, Hayla Nahom
- Boateng, Gordon Owusu
- Erbad, Aiman
- Hamdi, Mounir
- Guizani, Mohsen
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901198
url: https://www.scopus.com/pages/publications/105000832602?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 608--613
keywords:
- CCM-MADRL
- meta-distance
- Metaverse
- Quality of experience
- Resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1174 — Resource Allocation and QoE Maximization in Aerial MEC-empowered Metaverse Service: A CCM-Multi-agent DRL approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of Mobile Edge Computing (MEC) with aerial platforms introduces novel potential for the Metaverse world by providing low-latency and highly reliable computing and communication services at the network edge. Nevertheless, this integration presents critical challenges, such as low Quality of Experience (QoE) due to the dynamic nature of aerial platforms, high resource demands, and the requirements for real-time data processing in the Metaverse environment. To address these challenges, we propose a Combinatorial Client-Master Multiagent Deep Reinforcement Learning (CCM-MADRL) based joint resource allocation and QoE maximization framework to enable intelligent real-time decision-making in aerial MEC enabled Metaverse services. We form a collaborative ecosystem where agents are designed to represent both Metaverse service providers and aerial platforms to promote fairness and efficiency in resource allocation, as well as optimize service delivery. By incorporating CCM, our approach considers diverse metrics, such as latency, reliability, meta-distance, and energy efficiency, to ensure a holistic optimization of Metaverse services. The MADRL approach enables adaptive decision-making, allowing the system to respond to the dynamic and unpredictable nature of Metaverse applications. Results from simulations that mimic realistic Metaverse scenarios demonstrate the effectiveness of the proposed CCM-MADRL framework in terms of improved service performance, reduced latency, cost, and virtual meta-distance, maximized average QoE utility of Metaverse users, and enhanced resource utilization compared to baseline algorithms. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1174.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
