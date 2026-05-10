---
id: paper-0371
title: Transfer Learning for Distributed Intelligence in Aerial Edge Networks
authors:
- Zhang, Ke
- Si, Dingxin
- Wang, Wei
- Cao, Jiayu
- Zhang, Yan
venue: IEEE Wireless Communications
venue_type: journal
year: 2021
doi: 10.1109/MWC.011.2100061
url: https://www.scopus.com/pages/publications/85119955270?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 74--81
keywords:
- Antennas
- Edge computing
- Efficiency
- Intelligent agents
- Knowledge management
- Machine learning
- Unmanned aerial vehicles (UAV)
- Computation intensives
- Distributed intelligence
- Edge computing
- EDGE Networks
- Edge services
- Learning agents
- Networks learning
- Service strategy
- Task offloading
- Transfer learning
- Multi agent systems
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

# paper-0371 — Transfer Learning for Distributed Intelligence in Aerial Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-enabled edge computing is a promising paradigm to provide task offloading service for computation-intensive applications. Catering for highly dynamic edge networks, learning agents are placed on the UAVs to perceive environmental changes and adjust edge service strategies. These multiple agents build distributed intelligence in edge service scheduling. However, the agents, which independently learn service strategies from scratch, always cost high computing resources, cause extra delays, and bring a critical challenge to UAVs' service efficiency. To address this challenge, we propose a transfer learning empowered aerial edge network (AEN), which uses multi-agent machine learning to draw optimal service strategies, while leveraging transfer learning to share and reuse knowledge between the UAVs for saving resource costs and reducing training latency. Furthermore, we develop efficient transfer learning schemes where the edge resources are optimally scheduled for knowledge sharing and task offloading. Numerical results indicate that the proposed schemes maximize edge service utility while significantly improving machine learning efficiency.  © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0371.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
