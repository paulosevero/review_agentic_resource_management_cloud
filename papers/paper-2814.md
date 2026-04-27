---
id: "paper-2814"
title: "Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction"
authors: ["Wada, Akihiko", "Nishizawa, Mitsuo", "Yamamoto, Akira", "Akashi, Toshiaki", "Hagiwara, Akifumi", "Irie, Ryusuke", "Hayakawa, Yayoi", "Kikuta, Junko", "Shimoji, Keigo", "Sano, Katsuhiro", "Nakanishi, Atsushi", "Kamagata, Koji", "Aoki, Shigeki"]
year: 2026
venue: "Scientific Reports"
venue_type: "journal"
doi: "10.1038/s41598-026-36904-5"
url: "https://www.scopus.com/pages/publications/105029761189?origin=resultslist"
publisher: "Nature Research"
pages: ""
keywords: ["Cloud Computing", "Computer Security", "Confidentiality", "East Asian People", "Humans", "Japan", "Japanese people", "cloud computing", "computer security", "confidentiality", "East Asian", "human", "Japan", "Japanese (people)"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2814 — Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction

## Metadata

- **Authors:** Wada, Akihiko and Nishizawa, Mitsuo and Yamamoto, Akira and Akashi, Toshiaki and Hagiwara, Akifumi and Irie, Ryusuke and Hayakawa, Yayoi and Kikuta, Junko and Shimoji, Keigo and Sano, Katsuhiro and Nakanishi, Atsushi and Kamagata, Koji and Aoki, Shigeki
- **Year:** 2026
- **Venue:** Scientific Reports
- **DOI:** 10.1038/s41598-026-36904-5
- **URL:** https://www.scopus.com/pages/publications/105029761189?origin=resultslist
- **Publisher:** Nature Research
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud Computing; Computer Security; Confidentiality; East Asian People; Humans; Japan; Japanese people; cloud computing; computer security; confidentiality; East Asian; human; Japan; Japanese (people)

### Abstract

Cloud-based Large Language Models (LLMs) excel at medical text processing, but privacy regulations impose significant constraints on transmitting Protected Health Information (PHI) to external services, creating barriers to AI adoption for many healthcare institutions. While contractual agreements (e.g., Business Associate Agreements under HIPAA) may permit such transmission under specific conditions, many institutions prefer or require complete data sovereignty. Local LLMs address this need but have historically underperformed. This study introduces a five-phase optimization framework to bridge this performance gap. Using 160 synthetic Japanese radiology reports, we benchmarked 14 local LLMs against cloud leaders. Our key finding is a notable performance pattern: models with baseline scores below 87–88 points gained an average of + 6.92 points (p < 0.001), while higher-scoring models did not, suggesting a potential threshold effect for targeted optimization that warrants further investigation. The optimized Mistral-Small-3.2 with Self-Refine achieved 91.54 points—97.8% of GPT-4.1's performance—with perfect rule adherence and a clinically acceptable processing time of 24.6 s per report for batch workflows. Our work demonstrates that systematically optimized local LLMs can approach cloud-leader performance. Importantly, it provides a strategic framework guiding institutions on when and where to apply advanced optimization, enabling efficient and trustworthy AI deployment while ensuring patient privacy. © The Author(s) 2026.

## 04 — Title Screening

**Title:** Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Bridging the performance gap: systematic optimization of local LLMs for Japanese medical PHI extraction
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
