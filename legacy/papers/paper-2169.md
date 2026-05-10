---
id: "paper-2169"
title: "Scalable cosmic AI inference using cloud serverless computing"
authors: ["Staylor, Mills", "Dolatpour Fathkouhi, Amirreza", "Islam, Md Khairul", "O\u2019Hara, Kaleigh", "Goudjil, Ryan Ghiles", "Fox, Geoffrey", "Fox, Judy"]
year: 2025
venue: "International Journal of High Performance Computing Applications"
venue_type: "journal"
doi: "10.1177/10943420251399942"
url: "https://www.scopus.com/pages/publications/105023195814?origin=resultslist"
publisher: "SAGE Publications Inc."
pages: ""
keywords: ["astronomy", "cloud computing", "foundation models", "scaling", "serverless"]
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

# paper-2169 — Scalable cosmic AI inference using cloud serverless computing

## Metadata

- **Authors:** Staylor, Mills and Dolatpour Fathkouhi, Amirreza and Islam, Md Khairul and O’Hara, Kaleigh and Goudjil, Ryan Ghiles and Fox, Geoffrey and Fox, Judy
- **Year:** 2025
- **Venue:** International Journal of High Performance Computing Applications
- **DOI:** 10.1177/10943420251399942
- **URL:** https://www.scopus.com/pages/publications/105023195814?origin=resultslist
- **Publisher:** SAGE Publications Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** astronomy; cloud computing; foundation models; scaling; serverless

### Abstract

Large-scale astronomical image data processing and prediction are essential for astronomers, providing crucial insights into celestial objects, the universe’s history, and its evolution. While modern deep learning models offer high predictive accuracy, they often demand substantial computational resources, making them resource-intensive and limiting accessibility. We introduce the Cloud-based Astronomy Inference (CAI) framework to address these challenges. This scalable solution integrates pre-trained foundation models with serverless cloud infrastructure through a Function-as-a-Service (FaaS). CAI enables efficient and scalable inference on astronomical images without extensive hardware. Using a foundation model for redshift prediction as a case study, our extensive experiments cover user devices, HPC (High-Performance Computing) servers, and Cloud. Using redshift prediction with the AstroMAE model demonstrated CAI’s scalability and efficiency, achieving inference on a 12.6 GB dataset in only 28 seconds compared to 140.8 seconds on HPC GPUs and 1793 seconds on HPC CPUs. CAI also achieved significantly higher throughput, reaching 18.04 billion bits per second (bps), and maintained near-constant inference times as data sizes increased, all at minimal computational cost (under $5 per experiment). We also process large-scale data up to 1 TB to show CAI’s effectiveness at scale. CAI thus provides a highly scalable, accessible, and cost-effective inference solution for the astronomy community. The code is accessible at https://github.com/UVA-MLSys/AI-for-Astronomy. © The Author(s) 2025

## 04 — Title Screening

**Title:** Scalable cosmic AI inference using cloud serverless computing

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Scalable cosmic AI inference using cloud serverless computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Scalable cosmic AI inference using cloud serverless computing
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
