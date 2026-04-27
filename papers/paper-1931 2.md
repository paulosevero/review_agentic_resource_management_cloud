---
id: "paper-1931"
title: "When Silicon Fails Silently: Characterizing Hardware-Induced Corruption in LLM Training"
authors: ["Ma, Jeffrey", "Pei, Hengzhi", "Lausen, Leonard", "Karypis, George"]
year: 2025
venue: "Proceedings - 2025 IEEE 31st International Symposium on On-Line Testing and Robust System Design, IOLTS 2025"
venue_type: "conference"
doi: "10.1109/IOLTS65288.2025.11116834"
url: "https://www.scopus.com/pages/publications/105015644428?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["distributed training", "fault tolerance", "hardware failure", "language model", "silent data corruption"]
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

# paper-1931 — When Silicon Fails Silently: Characterizing Hardware-Induced Corruption in LLM Training

## Metadata

- **Authors:** Ma, Jeffrey and Pei, Hengzhi and Lausen, Leonard and Karypis, George
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE 31st International Symposium on On-Line Testing and Robust System Design, IOLTS 2025
- **DOI:** 10.1109/IOLTS65288.2025.11116834
- **URL:** https://www.scopus.com/pages/publications/105015644428?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** distributed training; fault tolerance; hardware failure; language model; silent data corruption

### Abstract

As the scale of training large language models (LLMs) increases, one emergent failure is silent data corruption (SDC), where hardware produces incorrect computations without explicit failure signals. In this work, we summarize the first investigation of the impact of real-world SDCs on LLM training presented in our ACL work [1]. In our investigation, we compare model training between healthy production nodes and unhealthy nodes exhibiting SDCs. With the help from a cloud computing platform, we access the unhealthy nodes that were swept out from production by automated fleet management. Using deterministic execution via XLA compiler and our proposed synchronization mechanisms, we isolate and analyze the impact of SDC errors on these nodes at three levels: at each submodule computation, at a single optimizer step, and at a training period. Our results reveal that the impact of SDCs on computation varies on different unhealthy nodes. Although in most cases the perturbations from SDCs on submodule computation and gradients are relatively small, SDCs can lead models to converge to different optima with different weights and even cause spikes in the training loss.  © 2025 IEEE.

## 04 — Title Screening

**Title:** When Silicon Fails Silently: Characterizing Hardware-Induced Corruption in LLM Training

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** When Silicon Fails Silently: Characterizing Hardware-Induced Corruption in LLM Training
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** When Silicon Fails Silently: Characterizing Hardware-Induced Corruption in LLM Training
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
