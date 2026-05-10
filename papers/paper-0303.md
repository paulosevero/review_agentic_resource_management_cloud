---
id: paper-0303
title: Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications
authors:
- Khaleq, Abeer Abdel
- Ra, Ilkyeun
venue: IEEE Access
venue_type: journal
year: 2021
doi: 10.1109/ACCESS.2021.3061890
url: https://www.scopus.com/pages/publications/85101769830?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 35464--35476
keywords:
- Autonomous autoscaling
- Kubernetes
- microservices autoscaling
- real-time cloud applications
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0303 — Intelligent Autoscaling of Microservices in the Cloud for Real-Time Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud applications are becoming more containerized in nature. Developing a cloud application based on a microservice architecture imposes different challenges including scalability at the container level. What adds to the challenge is that cloud applications impose quality of service (QoS) requirements and have various resource demands requiring a customized scaling approach. For example, real-time applications require near real time response time as a QoS. Existing autoscaling technologies such as Kubernetes offer some customization to a set of threshold values for autoscaling. The challenge is identifying the right values for the different autoscaling parameters that will guarantee QoS in a changing dynamic environment. Advancements in machine learning and reinforcement learning (RL) provides a means for autoscaling in cloud applications with no domain knowledge. In this article, we introduce an intelligent autonomous autoscaling system for microservices autoscaling in the cloud with QoS constraints. The system consists of two modules. The first module identifies the microservice resource demand via a generic autoscaling algorithm deployed on the Google Kubernetes Engine (GKE). Our algorithm adapts the Kubernetes autoscaling paradigm based on the application resource requirements. The second module uses reinforcement learning agents to learn and identify the autoscaling threshold values based on the resource demand and QoS. Experimental results show an enhancement in the microservice response time up to 20% compared to the default autoscaling paradigm. In addition, the RL agents can identify the autoscaling threshold values while maintaining a response time below the QoS constraint. Our proposed work provides a customized autoscaling solution for microservices in cloud applications while adhering to QoS constraints with minimum user interaction.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0303.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
