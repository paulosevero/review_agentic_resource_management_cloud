---
id: paper-1405
title: A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks
authors:
- Ayepah-Mensah, Daniel
- Ghebreziabiher, Amine Kidane
- Boateng, Gordon Owusu
- Mizouni, Rabeb
- Mourad, Azzam
- Otrok, Hadi
- Bentahar, Jamal
- Muhaidat, Sami
venue: International Conference on Wireless and Mobile Computing, Networking and Communications
venue_type: conference
year: 2025
doi: 10.1109/WiMob66857.2025.11257559
url: https://www.scopus.com/pages/publications/105029900367?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Deep Reinforcement Learning
- Edge-Cloud Orchestration
- Large Language Models (LLMs)
- Microservice Deployment
- Retrieval-Augmented Generation (RAG)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1405 — A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern edge cloud platforms must efficiently deploy and route containerized microservice DAGs under strict latency and cost constraints, while adapting to rapidly changing workloads and infrastructure states. Deep Reinforcement Learning (DRL) schedulers adapt well to dynamics but often lack semantic awareness of service intent and task dependencies, resulting in suboptimal decisions in unseen scenarios. To overcome these limitations, we introduce a Retrieval-Augmented Generation-assisted DRL (RAG-DRL) framework that integrates a lightweight DRL agent with a graph-based RAG module powered by a partially frozen LLM. A dynamic memory graph encodes contextual information such as node resources, network latencies, and SLA feedback. The LLM retrieves relevant historical deployments and current service intents to generate soft placement plans and reward estimates, which guide the DRL agent. These priors accelerate convergence, improve generalization across diverse conditions, and ensure real-time responsiveness. Evaluations on a realistic urban-scale edge cloud testbed confirm that RAG-DRL significantly reduces SLA violations, end-to-end latency, and resource imbalance, outperforming modern container-based schedulers. Our framework converges faster, maintains latency below 65 ms on scale, limits SLA violations to 12% under heavy load, and achieves 90 % resource utilization with balanced distribution.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1405.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
