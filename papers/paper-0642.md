---
id: paper-0642
title: Energy-Efficient Task Offloading with Statistic QoS Constraint Through Multi-level Sleep Mode in Ultra-Dense Network
authors:
- Li, Hongfei
- Dong, Chongwu
- Wen, Wushao
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2023
doi: 10.1007/978-3-031-48421-6_26
url: https://www.scopus.com/pages/publications/85178207949?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 378--392
keywords:
- Deep Reinforcement Learning
- Mobile Edge Computing
- Multi-level Sleep Mode
- Stochastic Network Calculus
- Ultra-Dense Network
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0642 — Energy-Efficient Task Offloading with Statistic QoS Constraint Through Multi-level Sleep Mode in Ultra-Dense Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> While ultra-dense networks (UDN) greatly enhances network performance, the extensive deployment of small base stations poses significant energy consumption challenges. Traditional ON/OFF base station sleep schemes can alleviate some energy issues. Still, complete shutdowns and lengthy reactivation times of base stations lead to coverage gaps in the network, severely impacting the quality of service delivered to users. In this paper, we introduce a multi-level Sleep Mode (SM) technique, focusing specifically on energy-efficient task offloading in the context of Mobile Edge Computing (MEC) scenarios. To ensure the performance of delay-sensitive services in user devices, we employ stochastic network calculus (SNC) theory to analyze the stability of the two-stage system. Combining the SNC-derived delay bounds, we propose a Multi-Agent Deep Deterministic Policy Gradient (MADDPG) based approach, which we refer to as SNC-MADDPG. This approach aims to minimize long-term system energy consumption. Numerical results demonstrate that the proposed algorithm achieves more significant energy savings under reliability constraints than other optimization algorithms. Furthermore, the results indicate that the multi-level sleep mode outperforms the traditional ON/OFF base station sleep schemes in meeting the reliability requirements of delay-sensitive applications. © 2023, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0642.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
