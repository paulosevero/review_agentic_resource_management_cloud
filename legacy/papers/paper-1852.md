---
id: "paper-1852"
title: "Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model"
authors: ["Lin, Yinxiang", "Huang, Haishang", "Gong, Zeyu", "Chen, Pei"]
year: 2025
venue: "Proceedings of the International Astronautical Congress, IAC"
venue_type: "conference"
doi: "10.52202/083091-0016"
url: "https://www.scopus.com/pages/publications/105035996626?origin=resultslist"
publisher: "International Astronautical Federation, IAF"
pages: "153--160"
keywords: ["DeepSeek distillation model", "LLM", "Question answering", "Time series data"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1852 — Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model

## Metadata

- **Authors:** Lin, Yinxiang and Huang, Haishang and Gong, Zeyu and Chen, Pei
- **Year:** 2025
- **Venue:** Proceedings of the International Astronautical Congress, IAC
- **DOI:** 10.52202/083091-0016
- **URL:** https://www.scopus.com/pages/publications/105035996626?origin=resultslist
- **Publisher:** International Astronautical Federation, IAF
- **Pages:** 153--160
- **Language:** English
- **Keywords:** DeepSeek distillation model; LLM; Question answering; Time series data

### Abstract

The advancement of commercial space technology has driven satellites toward higher functional density, with accelerated adoption of innovative hardware/software solutions. This rapid iteration, however, leads to insufficient reliability of long-term operational data, presenting new challenges for autonomous satellite management. This study proposes an embedded architecture for autonomous satellite data analysis and diagnosis employing a low-cost reasoning payload based on the DeepSeek distillation model. By integrating an onboard low-cost reasoning unit, the system aggregates extensive operational data aligned with autonomous objectives while sharing analytical outcomes with ground experts via structured sparse interactions. Experimental validation was conducted on an upcoming CubeSat mission: For novel on-orbit deployable payloads, the satellite captures multidimensional datasets including current, voltage, temperature, sensor readings, and continuous acceleration, exceeding conventional telemetry resolution thresholds. These datasets feed into the reasoning payload, which synergizes preloaded ground-test references to perform closed-loop orbital status diagnosis and generate actionable insights for optimizing subsequent ground tests to achieve full coverage of orbital operational regimes. Regarding satellite-level management, the reasoning payload processes fused datasets combining ground-uploaded mission plans with time-synchronized internal telemetry to identify dynamic efficiency bottlenecks in task execution. It further delivers prescriptive analytics for adaptive mission sequence optimization. This implementation utilizes an ARM processor (16GB RAM) hosting the distilled DeepSeek-R1-14b model, demonstrating a paradigm shift toward edge-computing-enabled satellite autonomy and establishing a resource-efficient human-AI co-evolution framework for space systems. Copyright ©2025 by the International Astronautical Federation (IAF). All rights reserved.

## 04 — Title Screening

**Title:** Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
