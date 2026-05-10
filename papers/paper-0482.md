---
id: paper-0482
title: Cybertwin-Driven Federated Learning Based Personalized Service Provision for 6G-V2X
authors:
- Prathiba, Sahaya Beni
- Raja, Gunasekaran
- Anbalagan, Sudha
- Gurumoorthy, Sugeerthi
- Kumar, Neeraj
- Guizani, Mohsen
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2022
doi: 10.1109/TVT.2021.3133291
url: https://www.scopus.com/pages/publications/85121381664?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4632--4641
keywords:
- 6G-V2X
- caching
- cybertwin
- federated learning
- multi-agent deep reinforcement learning
- personalized services
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0482 — Cybertwin-Driven Federated Learning Based Personalized Service Provision for 6G-V2X

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of Autonomous Vehicle (AV) technology and the integration of edge computing grasp new challenges along with the ever-increasing mobile internet traffic and services. Tackling such challenges through customized edge computing services is the critical research in 6G Vehicle-to-Everything (6G-V2X) communication. V2X contributes detailed information about the current navigation of vehicles, automatic payments for toll roads, parking fees and other services. With the countless, unique, and personalized service requirements of AVs over computation-intensive applications, exploring the edge resources for the excellent Quality of Service (QoS) provision is the greatest concern. This paper proposes a Federated Learning and edge Cache-assisted Cybertwin (FLCC) framework for personalized service provision in 6G-V2X. Integration of cybertwin in 6G enables the connectivity of the physical system to the digital realm, allowing for adequate instantaneous wireless access. The FLCC jointly considers the edge cooperation and optimizations through the proposed Federated Multi-agent Deep Reinforcement Learning based (FM-DRL) algorithm. The FM-DRL algorithm balances the FLCC's learning accuracy. It minimizes the time and cost by taking the factors such as cybertwin association, training data batch size, and bandwidth. Finally, caching is performed using the Federated Reinforcement Learning-based Edge Caching (FREC) algorithm to obtain the desired datasets required that train the model for providing personalized 6G-V2X services for the AVs. Numerical studies and simulation results reveal that the proposed system outperforms the baseline learning approaches by 17.6%.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0482.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
