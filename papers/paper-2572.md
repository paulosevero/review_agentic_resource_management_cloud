---
id: paper-2572
title: 'Distributed replica allocation and load balancing for Edge–Cloud FaaS: A cooperative multi-agent orchestration approach'
authors:
- Filippini, Federica
- Lujak, Marin
- Ciavotta, Michele
venue: Journal of Systems Architecture
venue_type: journal
year: 2026
doi: 10.1016/j.sysarc.2026.103787
url: https://www.scopus.com/pages/publications/105034568383?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Distributed optimization
- Edge–Cloud continuum
- Function-as-a-Service
- Load balancing
- Multi-agent orchestration
- Privacy-preserving coordination
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    winning_category: classical_agents
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-2572 — Distributed replica allocation and load balancing for Edge–Cloud FaaS: A cooperative multi-agent orchestration approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Function-as-a-Service (FaaS) paradigm supports many Cloud-native applications, but rising demand for low-latency services exceeds what the Cloud alone can deliver. Edge computing addresses this limitation; however, its heterogeneity and fragmented administrative domains, together with the workload dynamicity, greatly complicate resource coordination and function replica allocation across the Edge–Cloud continuum. This paper addresses these challenges through two complementary contributions. First, we formalize the Function Replica Allocation and Load Balancing (FRALB) problem in the Edge–Cloud continuum as a Distributed orchestration problem referred to as DiFRALB. The formulation jointly optimizes function placement, horizontal offloading among Edge nodes, and vertical offloading toward Cloud resources. Computation offloading plays a central role in this setting, as it enables workloads to be distributed across heterogeneous Edge and Cloud infrastructures while meeting performance requirements. Second, recognizing that centralized orchestration approaches suffer from scalability limitations and raise privacy concerns in multi-stakeholder environments, we propose FaaS-MACrO, a distributed multi-agent orchestration architecture designed to solve the DiFRALB problem. In FaaS-MACrO, each Edge node operates as an independent agent making local decisions, while a lightweight coordinator ensures global consistency by iteratively updating offloading prices to resolve conflicts among neighboring nodes. Crucially, coordination requires only minimal information exchange, thereby preserving operational privacy. Our solution approach jointly optimizes processing and offloading decisions by capturing the trade-offs among local execution efficiency, horizontal offloading latency, and vertical offloading costs. Extensive experiments across heterogeneous node configurations, diverse network topologies, and varying function characteristics demonstrate that FaaS-MACrO achieves solutions within 0.03–12.14% of the centralized optimum on average while significantly improving scalability, reducing solution times by up to three orders of magnitude in large-scale deployments with 200 nodes. © 2026

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **winning_category:** 'classical_agents'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2572.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
