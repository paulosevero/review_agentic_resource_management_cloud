---
id: paper-0239
title: A Blockchain-Based Model for Cloud Service Quality Monitoring
authors:
- Taghavi, Mona
- Bentahar, Jamal
- Otrok, Hadi
- Bakhtiyari, Kaveh
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2020
doi: 10.1109/TSC.2019.2948010
url: https://www.scopus.com/pages/publications/85083232874?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers
pages: 276--288
keywords:
- cloud computing
- oracle
- quality verification
- service provider
- Smart contracts
- stackleberg differential game
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

# paper-0239 — A Blockchain-Based Model for Cloud Service Quality Monitoring

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper introduces a novel blockchain-based decentralized federation model that embodies quality verification for cloud providers who lease computing resources from each other. The blockchain structure removes the barriers of a traditional centralized federation and offers a fully distributed and transparent administration by enforcing the involved agents to maintain consensus on the data. For a blockchain-based federation, it is vital to avoid blind-trust on the claimed SLA guarantees and monitor the quality of service which is highly desirable considering the multi-tenancy characteristic of cloud services. Due to the fact that the blockchain network is unable to access the outside world, it cannot handle, by its own, providers misbehavior in terms of SLA violations. Thus, we introduce oracle as a verifier agent to monitor the quality of the service and report to the smart contract agents deployed on the blockchain. Oracle is a trusted third-party agent who can communicate with the outside world of the blockchain network. The interaction between cloud service providers (either providing a service or requesting it from another provider) and the oracle through smart contracts comprises a system of autonomous and utility maximizer agents. Cloud requesters seek to receive high quality services with constant monitoring at cheap prices or even with no charge, while cloud providers aim to have a balanced work-load with less preserved capacity, and the oracle tends to charge higher for their monitoring services. Therefore, to model this conflicting situation, we formulate a dynamic Stackelberg differential game to optimize the cost of using the oracle and maximize the profit of the agents with the role of provider agent as a leader, and the requester and verifier agents as followers. Our designed Stackelberg differential game can seize the dynamicity of users' demand and resource provisioning in a competitive cloud market. We implemented our proposed decentralized model using the Solidity language in the remix IDE on the Ethereum network. We further evaluated the optimal controls and agents' profit with real-world data simulated for three concrete cloud providers. The results revealed that the requester agent initiates most of the quality verification requests at the beginning to the middle time of the contract. Thus, the provider agent could reserve less computing resources considering the fact that it could share the workload among other customers' computing resources during the peak-time. Moreover, imposing a higher penalty on the provider agent increased the capacity and decreased the number of requests for quality verification at the equilibrium. The evaluation also disclosed that the impact of timing in the dynamic pricing strategy of the verifier agent is very minimal, and the provisioning capacity of the provider is strongly correlated with the monitoring price. © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0239.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
