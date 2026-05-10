---
id: paper-0385
title: Multiobjective Edge Server Placement in Mobile-Edge Computing Using a Combination of Multiagent Deep Q-Network and Coral Reefs Optimization
authors:
- Asghari, Ali
- Sohrabi, Mohammad Karim
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2022.3161950
url: https://www.scopus.com/pages/publications/85138777883?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17503--17512
keywords:
- Access latency
- deep Q-network (DQN)
- load balancing
- mobile-edge computing (MEC)
- server placement
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0385 — Multiobjective Edge Server Placement in Mobile-Edge Computing Using a Combination of Multiagent Deep Q-Network and Coral Reefs Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growth of telecommunication technologies, especially 5G, the growing popularity of smart mobile devices, the emergence of smart cities and Internet of Things (IoT), and the easy use of these equipments have led the cloud users to utilize their various services. Real-time applications and the use of big data have caused cloud service providers (CSPs) to move their servers to the edge of the network and in the vicinity of users to maintain the quality of their services. For this purpose, the concept of mobile-edge computing (MEC) was formed. Applications often have heavy computing complexity on mobile devices or require a lot of data to process. Moreover, in order to save energy consumption of the batteries of this equipment, offloading them on the network resources can transfer the computational complexity from the users' equipment to the network resources. The resource placement (RP) is one of the major challenges in this area. Improper resource topology upsets their load balancing and increases access latency. In the proposed method of this article, the cellular mobile network is divided into smaller areas and using the coral reefs optimization (CRO) algorithm, the optimal placement of resources in each of these areas will be locally performed. The deep Q -network (DQN) and Markov game (MG) are used to optimize global RP to reduce global latency and to improve resource load balancing as its two objectives. The results of the experiments show that the proposed method has significantly improved its objectives and server's energy efficiency, compared to some similar works in this area. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0385.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
