---
id: "paper-2484"
title: "Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems"
authors: ["Zhu, Shuntao", "Wang, Dan"]
year: 2025
venue: "E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems"
venue_type: "conference"
doi: "10.1145/3679240.3734609"
url: "https://www.scopus.com/pages/publications/105016379923?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "407--414"
keywords: ["Immersion Cooling", "LLM Training", "Thermal Control"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: ""
    human_justification: ""

---

# paper-2484 — Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems

## Metadata

- **Authors:** Zhu, Shuntao and Wang, Dan
- **Year:** 2025
- **Venue:** E-ENERGY 2025 - Proceedings of the 2025 16th ACM International Conference on Future and Sustainable Energy Systems
- **DOI:** 10.1145/3679240.3734609
- **URL:** https://www.scopus.com/pages/publications/105016379923?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 407--414
- **Language:** English
- **Keywords:** Immersion Cooling; LLM Training; Thermal Control

### Abstract

With the increase in AI applications, the energy consumption of datacenters that run AI jobs is greatly increasing. The overall energy consumption of a datacenter is closely linked with that of its cooling system. Recently, there has been a revolution in immersion cooling technologies, in which servers can be directly immersed in dielectric cooling liquid (coolant). However, there is a lack of understanding of how the performance of AI jobs is affected by immersion cooling systems. While the physics behind immersion cooling is understood, in this paper we observe key restricting factors: (1) the boiling state of the coolant and (2) the heat removal rate of the coolant may not match the heat generation rate of the GPUs, triggering the thermal-throttle mechanisms of the GPUs. In this paper, we study the energy-efficient and delay-ensured computing of large language model (LLM) training jobs over a cluster of GPUs in immersion cooling systems. We model the thermal characteristics of the system (e.g., heat generation, heat removal, and temperature) and develop an algorithm with workload assignment and frequency scaling to avoid the delay incurred by the thermal-throttle mechanisms and to execute the workloads in energy-efficient frequencies. In our evaluation, we simulate the computational fluid dynamics (CFD) of the immersion cooling systems through the Ansys Fluent software. We show that we outperform baseline algorithms by up to 53.2% in energy and 22.5% in delays. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Energy-efficient LLM Training in GPU datacenters with Immersion Cooling Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
