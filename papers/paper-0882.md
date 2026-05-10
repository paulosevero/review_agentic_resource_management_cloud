---
id: paper-0882
title: Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning
authors:
- Dan, Ningyun
- Zhao, Lun
- Pan, Wenjin
- Cai, Yan
venue: 2024 3rd International Conference on Cloud Computing, Big Data Application and Software Engineering, CBASE 2024
venue_type: conference
year: 2024
doi: 10.1109/CBASE64041.2024.10824501
url: https://www.scopus.com/pages/publications/85217187711?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 859--863
keywords:
- cloud infrastructure security
- Deep learning
- dynamic fuzzing
- reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0882 — Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As cloud infrastructure assumes an increasingly pivotal role in contemporary computing environments, ensuring its security becomes a matter of paramount importance. As a prevalent vulnerability detection technology, traditional fuzz testing encounters the challenge of scalability in the context of the intricate and evolving nature of cloud computing systems. Our approach employs deep neural networks (DNNs) to analyze the behavior of diverse software components within cloud systems. It incorporates multi-dimensional data, including system logs, network traffic, and resource utilization in virtualized environments. The neural network is capable of identifying potential vulnerability points through an automated process. To generate effective test cases, we introduce a reinforcement learning framework based on a policy gradient algorithm. This framework enables an intelligent agent to interact with the system in order to obtain feedback and subsequently update the policy in order to progressively generate more aggressive test cases. The framework is designed with an adaptive reward mechanism that not only encourages triggering crashes but also focuses on edge use cases that reveal system bottlenecks, thereby improving vulnerability coverage. Furthermore, in consideration of the dynamic nature of the cloud environment, we have developed a distributed test architecture that enables the parallel deployment of tasks in virtual machines or containers, simulates multi-tenancy and dynamic load change scenarios, and introduces a vulnerability detection mechanism at the virtualization layer. The proposed model is capable of adaptively generating highly targeted test cases and optimizing the test strategy through continuous learning, thereby markedly enhancing the detection capability of complex vulnerabilities in cloud infrastructure.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0882.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
