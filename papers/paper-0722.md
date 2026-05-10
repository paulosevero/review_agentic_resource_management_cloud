---
id: paper-0722
title: Efficient Resource Provisioning in Critical Infrastructures Based on Multi-Agent Rollout Enabled by Deep Q-Learning
authors:
- Soumplis, Polyzois
- Kokkinos, Panagiotis
- Varvarigos, Emmanouel
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2023
doi: 10.1007/978-3-031-47969-4_17
url: https://www.scopus.com/pages/publications/85180621857?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 210--223
keywords:
- critical infrastructure
- Deep Q-Learning
- multi-Agent Rollout
- Reinforcement Learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0722 — Efficient Resource Provisioning in Critical Infrastructures Based on Multi-Agent Rollout Enabled by Deep Q-Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Next-generation smart environments, an integral part of our modern lives, integrate computing and networking technologies to enrich our experiences. Harnessing cutting-edge technologies like the Internet of Things, Artificial Intelligence, and Edge Computing, they function under the control of critical infrastructures often processing complex computer vision tasks such as object recognition and image segmentation in real-time. These infrastructures manage vast volumes of data with intensive computational demands. In response to these challenges, infrastructures have evolved to distributed that consists of resources of different capabilities and different operators. Within these environments, the security and communication among different domains are fundamental. Each domain potentially has different levels of security requirements and may use various protocols for communication. As data travels across these domains, it is exposed to a variety of threats, including data breaches, cyberattacks, and unauthorized access. In such a environment, where multiple domains co-exist, each with its own unique resources and security specifications, communication constraints across them further complicate the resource allocation process. This complexity is further increased by the diverse computing and networking constraints imposed by applications. In this work, we propose a multi-Agent Deep Reinforcement Learning mechanism that operates based on multi-Agent Rollout and deep Q-learning in order to serve the different applications’ requirements. The proposed optimization mechanism considers multiple objectives during the resource allocation process and tries to fulfill the specific constraints set by the demands and the broader objectives set by the infrastructure operator. Through rigorous evaluations, we showcase the effectiveness and efficiency of our proposed mechanisms in accommodating the heterogeneous and stringent workload requirements, whilst optimizing the use of infrastructure resources. Our simulation experiments confirm that the proposed mechanism can substantially enhance the efficiency of resource allocation in critical infrastructures. © 2023, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0722.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
