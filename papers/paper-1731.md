---
id: paper-1731
title: 'Carbon-Aware Microservices Scheduling: Machine Learning for Sustainable Cloud-Native Applications'
authors:
- Khanna, Abhirup
- Negi, Dakshita
- Sah, Anushree
- Dewangan, Bhupesh Kumar
- Londhe, Gaurav Vishnu
venue: 4th International Conference on Applied Artificial Intelligence and Computing, ICAAIC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICAAIC64647.2025.11331008
url: https://www.scopus.com/pages/publications/105034850736?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1501--1506
keywords:
- Carbon-aware scheduling
- Cloud-native applications
- Machine learning
- Microservices
- Sustainable computing
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

# paper-1731 — Carbon-Aware Microservices Scheduling: Machine Learning for Sustainable Cloud-Native Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The paper presents a machine learning architecture of carbon-aware microservice scheduling in cloud-native environments. The goal is to reduce carbon emissions and maintain service reliability across the distributed cloud environments, such as deploying Kubernetes on Amazon Web Services. The methodology combines three supplementary frameworks. To begin with, the temporal forecasting model is based on attentionenhanced temporal convolutional networks to forecast regional carbon intensity and service load, enabling proactive decisionmaking. Second, the topology-aware placement oracle utilizes graph neural networks to execute microservice dependencies, calculate communication costs, and estimate carbon projections, thereby producing effective placement suggestions. Third, the tight, multi-agent reinforcement learning controller is a dynamic, dynamically scaling, migrating, and scheduling workload, realtime scheduling controller that meets service-level objectives. This is implemented across Kubernetes clusters that can be spread across several AWS regions, along with realistic load generation and power modelling being integrated. Empirical analysis illustrates that there are significant emissions and energy savings when compared to the carbon ignorant auto scaling and human schedulers, and observable with strict performance limitations. This article highlights the potential in the utilization of intelligent scheduling to support the development of sustainable cloud-native applications in the form of an integrated approach to forecasting, graph learning, and reinforcement learning. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1731.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
