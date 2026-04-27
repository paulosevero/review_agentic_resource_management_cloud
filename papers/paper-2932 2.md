---
id: "paper-2932"
title: "Local self-verified chain-of-thought and preference alignment: a two-stage ReVCoT-DPO fine-tuning framework for system log fault diagnosis"
authors: ["Zhen, Zhichao", "Ling, Chen", "Mi, Lizhu", "Zhang, Hongbin"]
year: 2026
venue: "Computing"
venue_type: "journal"
doi: "10.1007/s00607-026-01641-0"
url: "https://www.scopus.com/pages/publications/105035507514?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Chain of thought", "Direct preference optimization", "Fault diagnosis", "Large language model (LLM)"]
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

# paper-2932 — Local self-verified chain-of-thought and preference alignment: a two-stage ReVCoT-DPO fine-tuning framework for system log fault diagnosis

## Metadata

- **Authors:** Zhen, Zhichao and Ling, Chen and Mi, Lizhu and Zhang, Hongbin
- **Year:** 2026
- **Venue:** Computing
- **DOI:** 10.1007/s00607-026-01641-0
- **URL:** https://www.scopus.com/pages/publications/105035507514?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Chain of thought; Direct preference optimization; Fault diagnosis; Large language model (LLM)

### Abstract

In system fault diagnosis tasks, LLM can identify system errors as inputs and generate diagnostic results as outputs. However, while system monitoring data is abundant as input, high-quality annotated output data remains scarce, typically requiring manual labeling and validation. This asymmetry between input and output presents significant challenges for model training. To tackle this challenge, this paper proposes a method combining Reverse Verification Chain of Thought with Value-Driven Direct Preference Optimization. This approach injects a local reverse verification chain mechanism into the LLM through manually labeled data and introduces a score model to evaluate the generated reasoning chains. Based on these scores, secondary reinforcement learning fine-tuning is conducted. This fine-tuning strategy not only significantly enhances the model reasoning ability in complex fault scenarios but also greatly reduces the reliance on large amounts of manually labeled data. Experimental results show that it significantly improves the LLM reasoning ability at each fine-tuning stage, demonstrating stronger accuracy and interpretability compared to baseline methods. This research provides new insights and methodologies for the automated fault diagnosis of complex systems, advancing the development of fault diagnosis technologies and showing broad potential for practical applications in industries such as industrial systems, cloud computing, and software development. © The Author(s), under exclusive licence to Springer-Verlag GmbH Austria, part of Springer Nature 2026.

## 04 — Title Screening

**Title:** Local self-verified chain-of-thought and preference alignment: a two-stage ReVCoT-DPO fine-tuning framework for system log fault diagnosis

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Local self-verified chain-of-thought and preference alignment: a two-stage ReVCoT-DPO fine-tuning framework for system log fault diagnosis
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Local self-verified chain-of-thought and preference alignment: a two-stage ReVCoT-DPO fine-tuning framework for system log fault diagnosis
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
