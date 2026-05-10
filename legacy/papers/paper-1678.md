---
id: "paper-1678"
title: "AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms"
authors: ["Idrees, Fatima", "Ambigapathy, Narmada", "Adelt, Peer", "Rettberg, Achim"]
year: 2025
venue: "IAVVC 2025 - IEEE International Automated Vehicle Validation Conference, Proceedings"
venue_type: "conference"
doi: "10.1109/IAVVC61942.2025.11219567"
url: "https://www.scopus.com/pages/publications/105025131025?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Autonomous vehicles", "CARLA simulation", "Edge computing", "Large language models", "Traffic regulation compliance"]
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
    human_justification: "Out of scope"

---

# paper-1678 — AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms

## Metadata

- **Authors:** Idrees, Fatima and Ambigapathy, Narmada and Adelt, Peer and Rettberg, Achim
- **Year:** 2025
- **Venue:** IAVVC 2025 - IEEE International Automated Vehicle Validation Conference, Proceedings
- **DOI:** 10.1109/IAVVC61942.2025.11219567
- **URL:** https://www.scopus.com/pages/publications/105025131025?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Autonomous vehicles; CARLA simulation; Edge computing; Large language models; Traffic regulation compliance

### Abstract

This paper presents a scalable and modular framework for monitoring traffic compliance in autonomous vehicles by adapting large-language models (LLMs) and lightweight generative models on resource-constrained edge devices. The framework integrates CARLA as a digital twin to simulate diverse driving scenarios with deployments on Raspberry Pi 5 and Jetson Nano P3541 platforms. Large language models GPT-2, GPT-Neo, OPT, and BLOOM are fine-tuned and evaluated for their ability to generate structured output consisting of a compliance label and corresponding traffic regulation. To address deployment limitations on low-power hardware, two lightweight models DistilGPT2 and Flan-T5-small are also explored. The study evaluates platform-specific trade-offs: Raspberry Pi 5 demonstrated cost-efficiency and stable performance with smaller models, while Jetson Nano processed larger models such as BLOOM with reduced latency, with up to 25 % faster inference times. While DistilGPT2 and Flan-T5-small improved inference efficiency and memory usage, they exhibited reduced classification accuracy due to limited contextual representation and instruction tuning limitations. The decentralized architecture allows independent updates to simulation, inference, and communication components, enhancing adaptability within AV validation pipelines. Although the current implementation relies on simulated input, future work will focus on integrating real-world sensor data and optimizing memory, latency, and energy usage. These findings underscore the scalability and feasibility of deploying generative language models for edge-based, decentralized traffic compliance monitoring in autonomous driving systems.  © 2025 IEEE.

## 04 — Title Screening

**Title:** AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
