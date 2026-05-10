---
id: paper-1978
title: Design and Simulation of Mobile Robots Operating Within Networked Architectures Tailored for Emergency Situations
authors:
- Mărieș, Marco
- Tătar, Mihai Olimpiu
venue: Applied Sciences (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/app15116287
url: https://www.scopus.com/pages/publications/105007786657?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- dynamic simulation
- emergency situations
- Kubernetes integration
- mobile robots
- security encryption
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1978 — Design and Simulation of Mobile Robots Operating Within Networked Architectures Tailored for Emergency Situations

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a simulation approach for mobile robots designed to operate within networks intended for emergency response scenarios. The simulation component is part of a broader and more complex system architecture focused on enhancing communication efficiency and operational coordination within robotic networks. This study leverages virtualization and robotic simulation technologies to develop a controlled environment in which the behavior and coordination of mobile robots can be analyzed and validated under simulated emergency conditions. To achieve this, a virtual machine was configured to host a ROS2 and Gazebo-based simulation environment. Custom packages were developed to enable the dynamic instantiation of mobile robots and the integration of essential sensing and control functionalities. The simulation process was carried out in two stages: initially, a single mobile robot was deployed and evaluated; subsequently, the configuration was extended to support a second robot, enabling multi-agent interaction within the simulated environment using flat surfaces. The proposed architecture demonstrates the potential for scalable deployment and simulation of mobile robotic instances. As a future direction, the authors aim to extend the system by optimizing data extraction from the simulation environment and implementing ROS2 microservices to facilitate secure and efficient communication with a centralized server deployed within a Kubernetes cluster. This integration will enable real-time coordination and data exchange between simulated agents and backend services, forming the foundation for a robust, distributed robotic system tailored to emergency operations. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1978.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
