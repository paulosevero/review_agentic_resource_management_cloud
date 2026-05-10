---
id: paper-0321
title: 'Decentralized Edge-to-Cloud Load Balancing: Service Placement for the Internet of Things'
authors:
- Nezami, Zeinab
- Zamanifar, Kamran
- Djemame, Karim
- Pournaras, Evangelos
venue: IEEE Access
venue_type: journal
year: 2021
doi: 10.1109/ACCESS.2021.3074962
url: https://www.scopus.com/pages/publications/85105033527?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 64983--65000
keywords:
- Agent
- cloud computing
- collective learning
- distributed optimization
- edge computing
- fog computing
- Internet of Things (IoT)
- load-balancing
- service placement
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0321 — Decentralized Edge-to-Cloud Load Balancing: Service Placement for the Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Internet of Things (IoT) requires a new processing paradigm that inherits the scalability of the cloud while minimizing network latency using resources closer to the network edge. On the one hand, building up such flexibility within the edge-to-cloud continuum consisting of a distributed networked ecosystem of heterogeneous computing resources is challenging. On the other hand, IoT traffic dynamics and the rising demand for low-latency services foster the need for minimizing the response time and a balanced service placement. Load-balancing for fog computing becomes a cornerstone for cost-effective system management and operations. This paper studies two optimization objectives and formulates a decentralized load-balancing problem for IoT service placement: (global) IoT workload balance and (local) quality of service (QoS), in terms of minimizing the cost of deadline violation, service deployment, and unhosted services. The proposed solution, EPOS Fog, introduces a decentralized multi-agent system for collective learning that utilizes edge-to-cloud nodes to jointly balance the input workload across the network and minimize the costs involved in service execution. The agents locally generate possible assignments of requests to resources and then cooperatively select an assignment such that their combination maximizes edge utilization while minimizes service execution cost. Extensive experimental evaluation with realistic Google cluster workloads on various networks demonstrates the superior performance of EPOS Fog in terms of workload balance and QoS, compared to approaches such as First Fit and exclusively Cloud-based. The results confirm that EPOS Fog reduces service execution delay up to 25% and the load-balance of network nodes up to 90%. The findings also demonstrate how distributed computational resources on the edge can be utilized more cost-effectively by harvesting collective intelligence.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0321.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
