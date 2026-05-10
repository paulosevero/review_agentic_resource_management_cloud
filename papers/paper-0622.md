---
id: paper-0622
title: Automated Pricing-based Provisioning of SDN/NFV Services in Distributed Multi-access Edge Computing using Cooperative Multi-Agent Deep Reinforcement Learning
authors:
- Julien, Jean Jimmy
- Nuannimnoi, Sirapop
- Huang, Ching-Yao
venue: Proceedings - 2023 10th International Conference on Dependable Systems and Their Applications, DSA 2023
venue_type: conference
year: 2023
doi: 10.1109/DSA59317.2023.00027
url: https://www.scopus.com/pages/publications/85179511242?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 144--155
keywords:
- Charging Factors
- Charging Models
- Distributed Edge Computing
- Multi-Agent Deep Reinforcement Learning
- Network Function Virtualization
- Service Provisioning
- Software Defined Network
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

# paper-0622 — Automated Pricing-based Provisioning of SDN/NFV Services in Distributed Multi-access Edge Computing using Cooperative Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The disruption caused by Software Defined Network and Network Function Virtualization (SDN/NFV) technologies will have many impacts on the telecom network. Specifically, the network architecture based on ETSI MANO comprising Virtual Infrastructure Manager (VIM), Virtual Network Function Manager (VNFM), and NFV Orchestrator (NFVO) will significantly change how we operate and manage the telecom network. These impacts on the network architecture will be made gradually. Thus, the migration from non-virtualized networks to all virtualized networks will happen step by step. By introducing new actors into the telecom ecosystem, NFV-MANO will bring in new business models. It is envisaged that these new actors/models will promote competition hence the demand for more flexible charging models with real-time charging. In this research, we will address the architectural realization of the SDN/NFV charging model under the business model of MANO (MANagement and Orchestration) when the service provider (SP) uses the Network Function Virtualization Infrastructure (NFVI) from the NFVIaaS Provider in a distributed multi-access edge computing (MEC) environment. To optimize the Quality of Service (QoS) of MEC resource allocation for incoming services and maximize the overall operating profit of the service provider adopting our charging model, we also propose a new cooperative multi-agent actor-critic based deep reinforcement learning (MADRL) method trained with proximal policy optimization algorithm, namely Coop MAPPO. The results of our experiments showcase the superiority of the Coop-MAPPO multi-agent system over alternative decision-making approaches, with its potential for enhancing operational efficiency and profitability while minimizing failure rates.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0622.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
