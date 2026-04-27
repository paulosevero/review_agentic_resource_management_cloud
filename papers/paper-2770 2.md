---
id: "paper-2770"
title: "A generative AI-based approach for resilient service composition under cybersecurity attacks in cloud-fog networks"
authors: ["Shahab, Erfan", "Taghipour, Sharareh", "Moghadam, Pourya"]
year: 2026
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2025.108273"
url: "https://www.scopus.com/pages/publications/105030102698?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Cloud computing", "Cybersecurity", "Generative AI", "Quality of service", "Resilience"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2770 — A generative AI-based approach for resilient service composition under cybersecurity attacks in cloud-fog networks

## Metadata

- **Authors:** Shahab, Erfan and Taghipour, Sharareh and Moghadam, Pourya
- **Year:** 2026
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2025.108273
- **URL:** https://www.scopus.com/pages/publications/105030102698?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud computing; Cybersecurity; Generative AI; Quality of service; Resilience

### Abstract

Cyberattacks such as distributed denial-of-service (DDoS) and ransomware degrade service quality in fog–cloud systems by overloading links and temporarily compromising nodes. This study proposes a conditional generative adversarial network (cGAN) with a fully connected (non-recurrent) generator and discriminator to produce task-to-server allocations at each scheduling cycle. The cGAN is trained offline on logged system states and Quality of Service (QoS) outcomes; at runtime, it maps the current state to a candidate allocation that is projected onto feasibility (capacity, bandwidth, and latency constraints). A lightweight anomaly detector runs in parallel and, upon detection, triggers a reactive migration policy that reallocates affected tasks to healthy resources. A discrete-event simulation evaluates bursty DDoS traffic and node-level ransomware compromises across multiple attack intensities and network sizes. Results show that the proposed allocator improves the composite quality-of-service (combining latency, completion rate, and energy) by approximately 7% under high-intensity attacks relative to non-generative baselines, while maintaining a balanced CPU utilization level. Ablation experiments (no-GAN, no-migration, no-QoS penalty) confirm that both the generative allocator and the migration trigger contribute materially to resilience. The approach offers a practical path to real-time, attack-aware orchestration in fog–cloud environments. © 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 04 — Title Screening

**Title:** A generative AI-based approach for resilient service composition under cybersecurity attacks in cloud-fog networks

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A generative AI-based approach for resilient service composition under cybersecurity attacks in cloud-fog networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A generative AI-based approach for resilient service composition under cybersecurity attacks in cloud-fog networks
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
