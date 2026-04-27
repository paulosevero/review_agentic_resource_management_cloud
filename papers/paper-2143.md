---
id: "paper-2143"
title: "Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage"
authors: ["Silva, Willian P.", "Rocha, Helder O.", "Faber, Menno", "Deters, Jan K.", "Bergsma, Ewout", "Silva, Jair L."]
year: 2025
venue: "2025 16th IEEE International Conference on Industry Applications, INDUSCON 2025 - Proceedings"
venue_type: "conference"
doi: "10.1109/INDUSCON66435.2025.11241782"
url: "https://www.scopus.com/pages/publications/105029903177?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2214--2219"
keywords: ["bandwidth optimization", "dementia monitoring", "edge computing", "fine-tuning", "LLM"]
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
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2143 — Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage

## Metadata

- **Authors:** Silva, Willian P. and Rocha, Helder O. and Faber, Menno and Deters, Jan K. and Bergsma, Ewout and Silva, Jair L.
- **Year:** 2025
- **Venue:** 2025 16th IEEE International Conference on Industry Applications, INDUSCON 2025 - Proceedings
- **DOI:** 10.1109/INDUSCON66435.2025.11241782
- **URL:** https://www.scopus.com/pages/publications/105029903177?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2214--2219
- **Language:** English
- **Keywords:** bandwidth optimization; dementia monitoring; edge computing; fine-tuning; LLM

### Abstract

In this paper, we propose a novel edge-AI architecture for real-time monitoring of dementia patients using finetuned Large Language Models (LLMs) to detect and classify high-risk scenarios in a low-bandwidth environment. We use LLaMA 3.8B with 4-bit quantization and Low-Rank Adaptation (LoRA) to fine-tune the pre-trained model effectively on a specialized 'Dementia Risk Dataset' of 50,000 labeled text samples. The optimized LLM is built to execute on the network edge (e.g., on border routers), with real-time transcriptions of patient speech analyzed for identifying key events such as disorientation, wandering, refusal of care, and medication management errors, and short, structured alerts sent to the cloud. Experimental results provide quick convergence at training, accurate classification of different risk categories, and reduction in message length compared to lengthy raw transcripts. Our approach ensures patient confidentiality by avoiding continuous audio streaming, reduces communication overhead in lowbandwidth networks, and enables timely intervention by clinical professionals and caregivers. The proposed system offers an extensible solution to cognitive dementia care and demonstrates the viability of LLM deployment on low-resource edge devices for domain-specific use cases.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Fine-Tuning Large Language Models to Detect Critical Scenarios in Dementia Patient Monitoring and to Reduce Bandwidth Usage
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
