---
id: "paper-753"
title: "Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service"
authors: ["Wobuyaga, Dinah", "Arzo, Sisay T", "Kumar, Harsh", "Granelli, Fabrizio", "Devetsikiotis, Michael"]
year: 2023
venue: "2023 IEEE 13th Annual Computing and Communication Workshop and Conference, CCWC 2023"
venue_type: "conference"
doi: "10.1109/CCWC57344.2023.10099225"
url: "https://www.scopus.com/pages/publications/85156262251?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "205--211"
keywords: ["Control Plane", "OpenFlow", "Role Delegation", "Software Defined Networks"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-753 — Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service

## Metadata

- **Authors:** Wobuyaga, Dinah and Arzo, Sisay T and Kumar, Harsh and Granelli, Fabrizio and Devetsikiotis, Michael
- **Year:** 2023
- **Venue:** 2023 IEEE 13th Annual Computing and Communication Workshop and Conference, CCWC 2023
- **DOI:** 10.1109/CCWC57344.2023.10099225
- **URL:** https://www.scopus.com/pages/publications/85156262251?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 205--211
- **Language:** English
- **Keywords:** Control Plane; OpenFlow; Role Delegation; Software Defined Networks

### Abstract

The emergency of machine type and ultra-reliable low latency communication is imposing stringent constraints for service provisioning. Addressing such constraints is challenging for network and cloud service providers. As a trending paradigm, software-defined networking (SDN) plays a significant role in future networks and services. However, the classical implementation of the SDN controller has limitations in-terms-of latency and reliability since the controller is decoupled from the forwarding device. Several research works have tried to tackle these challenges by proposing solutions such as Devoflow, DIFANE, and hierarchical and distributed controller deployment. Nonetheless, these approaches are not fully addressing these challenges. This paper tries to address the problem of latency and reliability by proposing a dynamic controller role delegation architecture for forwarding devices. To align with the microservice or multi-agent-based service-based architecture, the role delegation function as a service is proposed. The dynamic role delegation enables to predict and (pre-)installed flow rules in the forwarding devices based on various considerations such as network state, packet type, and service's stringent requirements. The proposed architecture is implemented and evaluated for latency and resiliency performance in comparison to the centralized and distributed deployment of the SDN controller. We used ComNetsEmu, a softwarized network emulation tool, to emulate SDN and NFV (Network Function Virtualization). The result indicated a significant decrease in latency and improved resilience in case of failure, yielding better network performance.  © 2023 IEEE.

## 04 — Title Screening

**Title:** Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Latency and Reliability Aware SDN Controller: A Role Delegation Function as a Service
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
