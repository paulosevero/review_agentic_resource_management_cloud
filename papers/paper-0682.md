---
id: paper-0682
title: Multi-objectives reinforcement federated learning blockchain enabled Internet of things and Fog-Cloud infrastructure for transport data
authors:
- Mohammed, Mazin Abed
- Lakhan, Abdullah
- Abdulkareem, Karrar Hameed
- Khanapi Abd Ghani, Mohd
- Abdulameer Marhoon, Haydar
- Nedoma, Jan
- Martinek, Radek
venue: Heliyon
venue_type: journal
year: 2023
doi: 10.1016/j.heliyon.2023.e21639
url: https://www.scopus.com/pages/publications/85175705934?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Agents
- Blockchain
- Cloud
- MORFLB
- Self-autonomous vehicle
- Training
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

# paper-0682 — Multi-objectives reinforcement federated learning blockchain enabled Internet of things and Fog-Cloud infrastructure for transport data

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> For the past decade, there has been a significant increase in customer usage of public transport applications in smart cities. These applications rely on various services, such as communication and computation, provided by additional nodes within the smart city environment. However, these services are delivered by a diverse range of cloud computing-based servers that are widely spread and heterogeneous, leading to cybersecurity becoming a crucial challenge among these servers. Numerous machine-learning approaches have been proposed in the literature to address the cybersecurity challenges in heterogeneous transport applications within smart cities. However, the centralized security and scheduling strategies suggested so far have yet to produce optimal results for transport applications. This work aims to present a secure decentralized infrastructure for transporting data in fog cloud networks. This paper introduces Multi-Objectives Reinforcement Federated Learning Blockchain (MORFLB) for Transport Infrastructure. MORFLB aims to minimize processing and transfer delays while maximizing long-term rewards by identifying known and unknown attacks on remote sensing data in-vehicle applications. MORFLB incorporates multi-agent policies, proof-of-work hashing validation, and decentralized deep neural network training to achieve minimal processing and transfer delays. It comprises vehicle applications, decentralized fog, and cloud nodes based on blockchain reinforcement federated learning, which improves rewards through trial and error. The study formulates a combinatorial problem that minimizes and maximizes various factors for vehicle applications. The experimental results demonstrate that MORFLB effectively reduces processing and transfer delays while maximizing rewards compared to existing studies. It provides a promising solution to address the cybersecurity challenges in intelligent transport applications within smart cities. In conclusion, this paper presents MORFLB, a combination of different schemes that ensure the execution of transport data under their constraints and achieve optimal results with the suggested decentralized infrastructure based on blockchain technology. © 2023 The Authors

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0682.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
