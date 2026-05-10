---
id: "paper-1844"
title: "A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers"
authors: ["Lin, Wenjun", "Lin, Weiwei", "Lin, Jianpeng", "He, Ligang", "Wang, Jiangtao", "Jiang, Hongliang"]
year: 2025
venue: "Journal of Building Engineering"
venue_type: "journal"
doi: "10.1016/j.jobe.2025.112811"
url: "https://www.scopus.com/pages/publications/105005082223?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Cooling system", "Data center", "Energy optimization", "Multi-agent reinforcement learning"]
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
    human_justification: "RL"

---

# paper-1844 — A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers

## Metadata

- **Authors:** Lin, Wenjun and Lin, Weiwei and Lin, Jianpeng and He, Ligang and Wang, Jiangtao and Jiang, Hongliang
- **Year:** 2025
- **Venue:** Journal of Building Engineering
- **DOI:** 10.1016/j.jobe.2025.112811
- **URL:** https://www.scopus.com/pages/publications/105005082223?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Cooling system; Data center; Energy optimization; Multi-agent reinforcement learning

### Abstract

Cooling systems within data centers (DCs) have attracted significant attention due to their high energy consumption. Existing optimization methods for cooling systems typically follow a two-stage process: first, constructing the simulation model of data centers based on physical laws; subsequently, applying optimization algorithms to determine the optimal cooling operations. However, purely physical models rely heavily on extensive underlying parameters and often lose accuracy when dealing with complex systems. Moreover, conventional optimization algorithms are usually based on best practices or heuristics, encountering challenges in generalization due to their reliance on prior knowledge specific to individual data centers. To address these problems, this paper applies a data-driven approach to develop simulation models for the air–liquid hybrid cooling system in data centers. Then, a multi-agent reinforcement learning-based method is proposed to achieve the joint control optimization of air-cooled and liquid-cooled equipment, aiming to reduce total energy consumption without thermal risks. Furthermore, to tackle the inherent challenge of credit assignment in the multi-agent system, a rewarding mechanism based on baseline comparison is designed to allocate the global reward according to each agent's actual contribution to the environment, thereby facilitating efficient learning. Numerical experiments conducted on the Marconi-100 dataset verify the effectiveness of the proposed method, achieving an average energy saving (RCI) of 7.7% while maintaining the rack cooling index above 99%. © 2025 Elsevier Ltd

## 04 — Title Screening

**Title:** A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A multi-agent reinforcement learning-based method for cooling control optimization in hybrid cooling data centers
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
