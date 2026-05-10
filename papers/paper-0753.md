---
id: paper-0753
title: 'Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service'
authors:
- Wobuyaga, Dinah
- Arzo, Sisay T
- Kumar, Harsh
- Granelli, Fabrizio
- Devetsikiotis, Michael
venue: 2023 IEEE 13th Annual Computing and Communication Workshop and Conference, CCWC 2023
venue_type: conference
year: 2023
doi: 10.1109/CCWC57344.2023.10099225
url: https://www.scopus.com/pages/publications/85156262251?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 205--211
keywords:
- Control Plane
- OpenFlow
- Role Delegation
- Software Defined Networks
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

# paper-0753 — Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergency of machine type and ultra-reliable low latency communication is imposing stringent constraints for service provisioning. Addressing such constraints is challenging for network and cloud service providers. As a trending paradigm, software-defined networking (SDN) plays a significant role in future networks and services. However, the classical implementation of the SDN controller has limitations in-terms-of latency and reliability since the controller is decoupled from the forwarding device. Several research works have tried to tackle these challenges by proposing solutions such as Devoflow, DIFANE, and hierarchical and distributed controller deployment. Nonetheless, these approaches are not fully addressing these challenges. This paper tries to address the problem of latency and reliability by proposing a dynamic controller role delegation architecture for forwarding devices. To align with the microservice or multi-agent-based service-based architecture, the role delegation function as a service is proposed. The dynamic role delegation enables to predict and (pre-)installed flow rules in the forwarding devices based on various considerations such as network state, packet type, and service's stringent requirements. The proposed architecture is implemented and evaluated for latency and resiliency performance in comparison to the centralized and distributed deployment of the SDN controller. We used ComNetsEmu, a softwarized network emulation tool, to emulate SDN and NFV (Network Function Virtualization). The result indicated a significant decrease in latency and improved resilience in case of failure, yielding better network performance.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0753.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
