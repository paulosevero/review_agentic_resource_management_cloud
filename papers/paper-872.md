---
id: "paper-872"
title: "Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence"
authors: ["Choi, Pyeongjun", "Kim, Jeongsoo", "Kwak, Jeongho"]
year: 2024
venue: "NetAISys 2024 - Proceedings of the 2024 2nd International Workshop on Networked AI Systems"
venue_type: "conference"
doi: "10.1145/3662004.3663555"
url: "https://www.scopus.com/pages/publications/85197303352?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "31--36"
keywords: ["DVFS", "Offloaded analytics", "On-device AI", "Thermal and memory aware control"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-872 — Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence

## Metadata

- **Authors:** Choi, Pyeongjun and Kim, Jeongsoo and Kwak, Jeongho
- **Year:** 2024
- **Venue:** NetAISys 2024 - Proceedings of the 2024 2nd International Workshop on Networked AI Systems
- **DOI:** 10.1145/3662004.3663555
- **URL:** https://www.scopus.com/pages/publications/85197303352?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 31--36
- **Language:** English
- **Keywords:** DVFS; Offloaded analytics; On-device AI; Thermal and memory aware control

### Abstract

Recently, consumer demand for artificial intelligence (AI) applications using deep neural network (DNN) model such as large language model (LLM), miXed Reality (XR), and AI assistants has been steadily increasing. Hitherto, on-device AI and offloaded analytics with the help of mobile edge computing (MEC) have been extensively studied to realize AI services on top of mobile devices. However, both technologies suffer from the limited resources of mobile devices, such as thermal resilience, battery capacity, and memory size. To tackle this problem, we first extensively examine the impact of heat and memory constraints of a mobile device when networking and processing resources and multi-dimensional DNN model sizes are dynamically managed for AI applications via motivating measurement. From the experimental results, we conjecture that the threshold-based approach for joint consideration of heat and memory constraints would increase the performance of AI applications in terms of energy, frames per second (FPS), and inference accuracy. Hence, we propose a threshold-based H&M algorithm that jointly adjusts offloading, Dynamic Voltage and Frequency Scaling (DVFS), and DNN model size, aiming to maximize inference accuracy while keeping target FPS with memory and heat constraints in various environments. Finally, we implement the proposed scheme on a mobile device and an MEC server and evaluate its performance and adaptability via extensive experiments. © 2024 Owner/Author.

## 04 — Title Screening

**Title:** Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
