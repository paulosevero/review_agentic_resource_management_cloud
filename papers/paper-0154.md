---
id: paper-0154
title: Regression training using model parallelism in a distributed cloud
authors:
- Reijonen, Joel
- Opsenica, Miljenko
- Morabito, Roberto
- Komu, Miika
- Elmusrati, Mohammed
venue: Proceedings - IEEE 17th International Conference on Dependable, Autonomic and Secure Computing, IEEE 17th International Conference on Pervasive Intelligence and Computing, IEEE 5th International
  Conference on Cloud and Big Data Computing, 4th Cyber Science and Technology Congress, DASC-PiCom-CBDCom-CyberSciTech 2019
venue_type: conference
year: 2019
doi: 10.1109/DASC/PiCom/CBDCom/CyberSciTech.2019.00139
url: https://www.scopus.com/pages/publications/85075166650?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 741--747
keywords:
- Intelligent agent
- Intelligent cloud
- Model parallelism
- Regression training
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

# paper-0154 — Regression training using model parallelism in a distributed cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Machine learning requires a relevant amount of computational resources and it is usually executed in high-capacity centralized cloud infrastructures (e.g., data centers). In such infrastructures, resources are shared in a scalable manner through instantiation and orchestration of multiple virtualized services. Emerging trends in machine learning are distribution and parallelization of model training, which allows the execution of model training tasks in multiple distributed computational domains, with the aim of reducing the overall training time. A possible drawback in decentralization of machine learning is that performance latency issues may arise when the computation of training is geographically distributed to nodes with long distance from each other. One way to reduce latency is to utilize edge computing infrastructure, i.e., to distribute computation near the origin of the request. As edge resources can be scarce, it is important to orchestrate the model training in a parallelized manner. To this extent, in order to effectively ease the use of parallelization both in centralized and in distributed scenarios, we propose and implement a concept that we refer to Intelligent Agent (IA). An IA is responsible for instantiating and scheduling of the machine learning tasks (e.g., model training), and deriving inferences. In our solution, model training is distributed to multiple IAs in parallel. Each IA is packaged into a Linux container in order to take advantage of container portability across heterogenous deployments and to reuse existing container orchestration tools. We validate our proposal by deploying and instantiating multiple IAs across a distributed cloud environment, where each IA is accounting for a fixed amount of computational resources. Keywords - Intelligent agent, Model parallelism, Regression training, Intelligent cloud. © 2019 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0154.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
