---
id: paper-0700
title: Intelligent UAS-Edge-Server Collaboration and Orchestration in Disaster Response Management
authors:
- Qu, Chengyi
- Ballotti, Chaise
- De Sousa, Daniel
- Liu, Jiaqing
venue: 'Proceedings of the Workshop on Enabling Technologies: Infrastructure for Collaborative Enterprises, WETICE'
venue_type: conference
year: 2023
doi: 10.1109/WETICE57085.2023.10477828
url: https://www.scopus.com/pages/publications/85190385094?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Deep Q-learning
- Multi-access edge computing
- Multi-drone networks
- UAS Collaboration
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

# paper-0700 — Intelligent UAS-Edge-Server Collaboration and Orchestration in Disaster Response Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial systems (UAS) consist of a swarm of unmanned aerial vehicles (UAVs) with edge resources and collaboration with ground-control-servers (GCS) are useful for heavy computation use cases e.g., traffic management, public safety, and disaster response management. Inefficient setups and collaboration decisions, often stemming from edge/cloud network misconfigurations, can lead to suboptimal resource utilization and delayed response times. In this paper, we present a novel scheme for (soft) real-time learning-based UAS-Edge-Server collaboration and orchestration strategies to achieve pertinent allocations of both computation resources and communication strategies. Our approach includes i) policy-based pre-application collaboration and benchmark analysis as well as ii) learning-based multi-agent deep Q-network (DQN) algorithm that optimizes UAV swarm trajectories during application. Evaluation results demonstrate that our policy-based approach Pareto-optimally trade-off performance (e.g., accuracy, streaming) and disaster response time. In addition, our DQN approach significantly enhances edge-cloud resource cooperation, improving network performance metrics like throughput and round-trip time by a minimum of 12% compared to state-of-the-art edge-internet-of-things (EIoT) collaboration algorithms. Furthermore, through real-world emulations, we illustrate how our orchestration attains 87% of the Oracle baseline network throughput performance while maintaining a comparable disaster response time for various video analytics-based disaster scenarios. © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0700.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
