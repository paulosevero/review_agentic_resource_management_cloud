---
id: "paper-2393"
title: "Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip"
authors: ["Yu, Xingmao", "Jiang, Dingcheng", "Deng, Jinyi", "Liu, Jingyao", "Li, Chao", "Yin, Shouyi", "Hu, Yang"]
year: 2025
venue: "Proceedings - International Symposium on Computer Architecture"
venue_type: "conference"
doi: "10.1145/3695053.3731016"
url: "https://www.scopus.com/pages/publications/105009587404?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "631--645"
keywords: ["Computing and hardware architecture", "Datacenter", "Wafer-scale integration"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2393 — Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip

## Metadata

- **Authors:** Yu, Xingmao and Jiang, Dingcheng and Deng, Jinyi and Liu, Jingyao and Li, Chao and Yin, Shouyi and Hu, Yang
- **Year:** 2025
- **Venue:** Proceedings - International Symposium on Computer Architecture
- **DOI:** 10.1145/3695053.3731016
- **URL:** https://www.scopus.com/pages/publications/105009587404?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 631--645
- **Language:** English
- **Keywords:** Computing and hardware architecture; Datacenter; Wafer-scale integration

### Abstract

The rapid advancements in large language models (LLMs) have significantly increased hardware demands. Wafer-scale chips, which integrate numerous compute units on an entire wafer, offer a highdensity computing solution for data centers and can extend Moore's Law at system level. However, current wafer-scale data center architectures face inefficiencies, such as uncoordinated resource allocation and lack of co-optimization for system area, preventing optimal integration density and performance within given cost and physical constraints. We propose a co-exploration approach of computing and hardware architectures to bridge this gap. We first develop an optimized wafer-scale single-cabinet data center model, integrating configurable on-chip memory dies and employing a vertically stacked hardware architecture. Based on this model, we introduce Titan, an automated exploration framework for intra-chip and inter-chip architecture design and optimization. Based on the architecture features of wafer-scale systems with optimal integration density, Titan establishes parameter dependencies to co-design the computing and hardware architectures. To reduce the design cycle for wafer-scale systems, Titan introduces vertical area constraints and pre-checks physical limits by integrating a series of reliability prediction models. It also integrates hardware capacity and cost evaluations to enable multi-objective optimization. Under the same cost constraint, on average, Titan's cabinet design architecture improves system computing capacity by 2.90×, communication bandwidth by 2.11×, and memory bandwidth by 11.23× compared to the state-of-the-art Dojo-like wafer-scale single tray architecture. Simulated in different scenarios, Titan's design delivers 3.17× and 10.66× performance improvement for Llama2-7B and Llama2-72B. Moreover, we leverage Titan to uncover insights into the optimal single-chip area choice within a cabinet under different cost constraints.  © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cramming a Data Center into One Cabinet, a Co-Exploration of Computing and Hardware Architecture ofWaferscale Chip
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
