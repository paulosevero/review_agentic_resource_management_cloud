---
id: "paper-239"
title: "A Blockchain-Based Model for Cloud Service Quality Monitoring"
authors: ["Taghavi, Mona", "Bentahar, Jamal", "Otrok, Hadi", "Bakhtiyari, Kaveh"]
year: 2020
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2019.2948010"
url: "https://www.scopus.com/pages/publications/85083232874?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers"
pages: "276--288"
keywords: ["cloud computing", "oracle", "quality verification", "service provider", "Smart contracts", "stackleberg differential game"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-239 — A Blockchain-Based Model for Cloud Service Quality Monitoring

## Metadata

- **Authors:** Taghavi, Mona and Bentahar, Jamal and Otrok, Hadi and Bakhtiyari, Kaveh
- **Year:** 2020
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2019.2948010
- **URL:** https://www.scopus.com/pages/publications/85083232874?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers
- **Pages:** 276--288
- **Language:** English
- **Keywords:** cloud computing; oracle; quality verification; service provider; Smart contracts; stackleberg differential game

### Abstract

This paper introduces a novel blockchain-based decentralized federation model that embodies quality verification for cloud providers who lease computing resources from each other. The blockchain structure removes the barriers of a traditional centralized federation and offers a fully distributed and transparent administration by enforcing the involved agents to maintain consensus on the data. For a blockchain-based federation, it is vital to avoid blind-trust on the claimed SLA guarantees and monitor the quality of service which is highly desirable considering the multi-tenancy characteristic of cloud services. Due to the fact that the blockchain network is unable to access the outside world, it cannot handle, by its own, providers misbehavior in terms of SLA violations. Thus, we introduce oracle as a verifier agent to monitor the quality of the service and report to the smart contract agents deployed on the blockchain. Oracle is a trusted third-party agent who can communicate with the outside world of the blockchain network. The interaction between cloud service providers (either providing a service or requesting it from another provider) and the oracle through smart contracts comprises a system of autonomous and utility maximizer agents. Cloud requesters seek to receive high quality services with constant monitoring at cheap prices or even with no charge, while cloud providers aim to have a balanced work-load with less preserved capacity, and the oracle tends to charge higher for their monitoring services. Therefore, to model this conflicting situation, we formulate a dynamic Stackelberg differential game to optimize the cost of using the oracle and maximize the profit of the agents with the role of provider agent as a leader, and the requester and verifier agents as followers. Our designed Stackelberg differential game can seize the dynamicity of users' demand and resource provisioning in a competitive cloud market. We implemented our proposed decentralized model using the Solidity language in the remix IDE on the Ethereum network. We further evaluated the optimal controls and agents' profit with real-world data simulated for three concrete cloud providers. The results revealed that the requester agent initiates most of the quality verification requests at the beginning to the middle time of the contract. Thus, the provider agent could reserve less computing resources considering the fact that it could share the workload among other customers' computing resources during the peak-time. Moreover, imposing a higher penalty on the provider agent increased the capacity and decreased the number of requests for quality verification at the equilibrium. The evaluation also disclosed that the impact of timing in the dynamic pricing strategy of the verifier agent is very minimal, and the provisioning capacity of the provider is strongly correlated with the monitoring price. © 2008-2012 IEEE.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
