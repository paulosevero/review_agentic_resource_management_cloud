---
id: "paper-1526"
title: "Conversational Smart Assistant on a Microcontroller with Cloud-Based LLM Function Offloading"
authors: ["Do, Dang Quoc-Minh", "Nguyen, Nguyen Hoang", "Nguyen, Quang Nho-Dang", "Hoang, Tuan Anh", "Nguyen, Khoa Quoc", "Huynh, Thuan Huu"]
year: 2025
venue: "Proceedings - 2025 RIVF International Conference on Computing and Communication Technologies, RIVF 2025"
venue_type: "conference"
doi: "10.1109/RIVF68649.2025.11365064"
url: "https://www.scopus.com/pages/publications/105034491315?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "191--196"
keywords: ["Conversational Voice Assistant", "Edge-to-Cloud Computing Architecture", "Large Language Model (LLM) Integration", "Microcontroller-Based Devices"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-1526 — Conversational Smart Assistant on a Microcontroller with Cloud-Based LLM Function Offloading

## Metadata

- **Authors:** Do, Dang Quoc-Minh and Nguyen, Nguyen Hoang and Nguyen, Quang Nho-Dang and Hoang, Tuan Anh and Nguyen, Khoa Quoc and Huynh, Thuan Huu
- **Year:** 2025
- **Venue:** Proceedings - 2025 RIVF International Conference on Computing and Communication Technologies, RIVF 2025
- **DOI:** 10.1109/RIVF68649.2025.11365064
- **URL:** https://www.scopus.com/pages/publications/105034491315?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 191--196
- **Language:** English
- **Keywords:** Conversational Voice Assistant; Edge-to-Cloud Computing Architecture; Large Language Model (LLM) Integration; Microcontroller-Based Devices

### Abstract

This paper presents a conversational smart assistant architecture that integrates a resource-constrained microcontroller frontend with a cloud-based large language model (LLM) backend. The device captures user query audio, compresses it, and streams it in real time to the server over a lightweight custom TCP protocol. On the server, Google Speech-to-Text (STT) transcribes the input, which is then processed by OpenAI's Generative Pre-trained Transformer (GPT) model for natural language understanding. Depending on the query, the model either generates a direct response or issues structured function calls to access real-time information (e.g., breaking news) via public APIs or a headless browser, or to execute taskoriented functions such as reminder scheduling and voice note recording. The final response is synthesized into speech using Google Text-to-Speech (TTS), compressed and streamed back to the device for playback. Experimental results show low latency, efficient bandwidth usage, and cost-effective operation, demonstrating the practicality of the proposed architecture for embedded conversational interfaces and wearable IoT assistants. © 2025 IEEE.

## 04 — Title Screening

**Title:** Conversational Smart Assistant on a Microcontroller with Cloud-Based LLM Function Offloading

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Conversational Smart Assistant on a Microcontroller with Cloud-Based LLM Function Offloading
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Conversational Smart Assistant on a Microcontroller with Cloud-Based LLM Function Offloading
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
