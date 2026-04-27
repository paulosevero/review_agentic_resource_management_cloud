---
id: "paper-1365"
title: "Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs"
authors: ["Adeseye, Aisvarya", "Isoaho, Jouni", "Virtanen, Seppo", "Tahir, Mohammad"]
year: 2025
venue: "2025 IEEE Nordic Circuits and Systems Conference, NORCAS 2025 - Proceedings"
venue_type: "conference"
doi: "10.1109/NorCAS66540.2025.11231309"
url: "https://www.scopus.com/pages/publications/105029505782?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Energy-Efficient AI", "Local Deployment of LLMs", "Prompt Engineering", "Resource-Constrained Systems"]
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

# paper-1365 — Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs

## Metadata

- **Authors:** Adeseye, Aisvarya and Isoaho, Jouni and Virtanen, Seppo and Tahir, Mohammad
- **Year:** 2025
- **Venue:** 2025 IEEE Nordic Circuits and Systems Conference, NORCAS 2025 - Proceedings
- **DOI:** 10.1109/NorCAS66540.2025.11231309
- **URL:** https://www.scopus.com/pages/publications/105029505782?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Energy-Efficient AI; Local Deployment of LLMs; Prompt Engineering; Resource-Constrained Systems

### Abstract

The local deployment of Large Language Models (LLMs) is essential for privacy and latency in several domains. However, it faces significant challenges in terms of memory, power, and inference speed, particularly in resource-constrained systems such as Internet of Things (IoT) and edge computing devices. Most existing studies emphasize compression and hardware tuning, while holistic system-level optimization remains incomplete, and the role of prompt design is still underexplored. This study introduces a structured evaluation of prompt engineering strategies designed to enhance resource efficiency and accuracy in local LLMs, applied across three textual analysis tasks: theme extraction, frequency analysis, and impact analysis. Four experimental conditions were compared: Baseline, System Prompt Only (SP), User Prompt Only (UP), and System+User Prompt ($S P+U P$). Using multiple LLMs ranging from 1 B to 70B parameters, we audited tokens generated, latency, VRAM usage, hallucination rates, and other structural errors. The results show that System Prompts alone substantially reduced computational overhead, whereas User Prompts improved accuracy and task alignment. Their combination yields comprehensive improvements, maximizing both efficiency and reliability. The proposed prompt design enabled smaller LLMs to rival larger ones in efficiency and accuracy, with LLaMA-3.2, 3B with SP+UP reducing VRAM by 96%, latency by 85%, and hallucinations by 83% when compared to the 70B with Baseline. Even LLaMA-3.2, 1B proved to be a viable option, especially when VRAM size is a critical factor.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Efficient Prompt Design for Resource-Constrained Deployment of Local LLMs
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
