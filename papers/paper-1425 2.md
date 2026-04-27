---
id: "paper-1425"
title: "VISPESAR: Video Summarization by Prompt Engineering and Serverless Architecture"
authors: ["Betir, Kerem", "Yakal, Hazar", "Mut, Emir", "Ari, Ismail"]
year: 2025
venue: "2025 Innovations in Intelligent Systems and Applications Conference, ASYU 2025"
venue_type: "conference"
doi: "10.1109/ASYU67174.2025.11208435"
url: "https://www.scopus.com/pages/publications/105022520546?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AWS", "cloud", "FFmpeg", "LLM", "prompt", "serverless architecture", "Video summarization", "WebSocket"]
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

# paper-1425 — VISPESAR: Video Summarization by Prompt Engineering and Serverless Architecture

## Metadata

- **Authors:** Betir, Kerem and Yakal, Hazar and Mut, Emir and Ari, Ismail
- **Year:** 2025
- **Venue:** 2025 Innovations in Intelligent Systems and Applications Conference, ASYU 2025
- **DOI:** 10.1109/ASYU67174.2025.11208435
- **URL:** https://www.scopus.com/pages/publications/105022520546?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AWS; cloud; FFmpeg; LLM; prompt; serverless architecture; Video summarization; WebSocket

### Abstract

This paper presents VISPESAR, a cloud-based video summarization service that extracts short clips from uploaded videos based on natural language queries or prompts. The current implementation uses Google Gemini API to interpret user prompts and identify content that matches user queries. FFmpeg software is used for video processing, mainly for keyframe extraction, video slicing, and concatenation to generate summaries. The backend employs a serverless architecture with Amazon Web Services (AWS) Lambda, Simple Storage Service (S3), Step Functions, and DynamoDB, while providing real-time feedback to the frontend user interfaces through WebSocket communication. The overall solution demonstrates how cloud computing and Artificial Intelligence (AI) can be used together to enable affordable and scalable video intelligence. Through careful design and experimentation, we find that quality of a modern video summarization service depends on: 1-clarity of the prompts used, 2-accuracy of the object detection and classification from frames, and 3- efficiency and scalability of the cloud-based system implementation. © 2025 IEEE.

## 04 — Title Screening

**Title:** VISPESAR: Video Summarization by Prompt Engineering and Serverless Architecture

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** VISPESAR: Video Summarization by Prompt Engineering and Serverless Architecture
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** VISPESAR: Video Summarization by Prompt Engineering and Serverless Architecture
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
