---
id: "paper-833"
title: "RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics"
authors: ["Basit, Abdul", "Hussain, Khizar", "Hanif, Muhammad Abdullah", "Shafique, Muhammad"]
year: 2024
venue: "2024 18th International Conference on Control, Automation, Robotics and Vision, ICARCV 2024"
venue_type: "conference"
doi: "10.1109/ICARCV63323.2024.10821547"
url: "https://www.scopus.com/pages/publications/85217420538?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "710--717"
keywords: ["Automatic Speech Recognition", "Healthcare Assistance Robot", "Large language Models", "Low-Rank Adaptation (LoRA)", "Preliminary Diagnosis", "Reinforcement Learning from Human Feedback (RLHF)"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-833 — RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics

## Metadata

- **Authors:** Basit, Abdul and Hussain, Khizar and Hanif, Muhammad Abdullah and Shafique, Muhammad
- **Year:** 2024
- **Venue:** 2024 18th International Conference on Control, Automation, Robotics and Vision, ICARCV 2024
- **DOI:** 10.1109/ICARCV63323.2024.10821547
- **URL:** https://www.scopus.com/pages/publications/85217420538?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 710--717
- **Language:** English
- **Keywords:** Automatic Speech Recognition; Healthcare Assistance Robot; Large language Models; Low-Rank Adaptation (LoRA); Preliminary Diagnosis; Reinforcement Learning from Human Feedback (RLHF)

### Abstract

Large language models (LLMs) are revolutionizing numerous domains with their remarkable natural language processing (NLP) capabilities, attracting significant interest and widespread adoption. However, deploying LLMs in resource-constrained environments, such as edge computing and robotics systems without server infrastructure, while also aiming to minimize latency, presents significant challenges. Another challenge lies in delivering medical assistance to remote areas with limited healthcare facilities and infrastructure. To address this, we introduce RoboMed, an on-premise healthcare robot that utilizes compact versions of large language models (tiny-LLMs) integrated with LangChain as its backbone. Moreover, it incorporates automatic speech recognition (ASR) models for user interface, enabling efficient, edge-based preliminary medical diagnostics and support. RoboMed employs model optimizations to achieve minimal memory footprint and reduced latency during inference on embedded edge devices. The training process optimization involves low-rank adaptation (LoRA), which reduces the model's complexity without significantly impacting its performance. For fine-tuning, the LLM is trained on a diverse medical dataset compiled from online health forums, clinical case studies, and a distilled medicine corpus. This fine-tuning process utilizes reinforcement learning from human feedback (RLHF) to further enhance its domain-specific capabilities. The system is deployed on Nvidia Jetson development board and achieves 78% accuracy in medical consultations and scores 56 in USMLE benchmark, enabling an resource-efficient healthcare assistance robot that alleviates privacy concerns due to edge-based deployment, thereby empowering the community.  © 2024 IEEE.

## 04 — Title Screening

**Title:** RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** RoboMed: On-Premise Medical Assistance Leveraging Large Language Models in Robotics
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
