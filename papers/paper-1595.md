---
id: paper-1595
title: 'Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes'
authors:
- Godhani, Payal
- Bhat, Ajay
venue: Proceedings of IEEE International Conference for Women in Innovation, Technology and Entrepreneurship, ICWITE 2025
venue_type: conference
year: 2025
doi: 10.1109/ICWITE64848.2025.11306960
url: https://www.scopus.com/pages/publications/105032389556?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Inferencing on AMD
- Machine Learning Inferencing
- Sustainability On Kubernetes
- XGBoost ML Model
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

# paper-1595 — Green AI: A Dynamic Framework for Energy-Efficient Inference on Kubernetes

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Kubernetes has proven to be one of the most powerful platforms for containerization, offering unique features such as flexibility, scalability, and fault tolerance. The orchestration platform's ease of use and impressive orchestration capabilities have driven its widespread adoption in the machine learning domain for inferencing and training. However, Kubernetes has its own set of challenges with respect to its default resource configuration. Its inefficient CPU resource utilization has led to high power consumption during AI inferencing [1]. This paper conducts research on the energy efficiency of Kubernetes in the context of machine learning and also proposes a dynamic framework that aims at reducing the power consumption of the inferencing workload by adjusting the CPU allocation in real-time on an AMD cluster. The framework configures the containers to their most optimal CPU allocation settings on the Kubernetes cluster while maintaining the workloads latency thresholds defined by the service level agreement. We describe a holistic solution that can be leveraged by all the inferencing workloads using Kubernetes, taking into account the inferencing performance and its power consumption. We discuss the results of a tree-based XGBoost (Extreme Gradient Boost) inferencing workload where the power consumption was reduced by 75% as compared to the default settings for the SLA used in this research. We show that by introducing a dynamic CPU-allocation framework, we can see significant improvements in the power consumption for machine learning inferencing workloads on Kubernetes clusters without substantially compromising inferencing performance. This research also highlights that Kubernetes potential is not just limited to container orchestration but is capable of dynamically optimizing energy usage in cloud-native AI applications. This research contributes to the growing need for more sustainable and greener AI deployments, especially in the age of generative AI.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1595.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
