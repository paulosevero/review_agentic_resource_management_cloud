---
id: "paper-1038"
title: "Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence"
authors: ["Li, Danyang", "Zhao, Yishujie", "Xu, Jingao", "Zhang, Shengkai", "Shangguan, Longfei", "Ma, Qiang", "Ding, Xuan", "Yang, Zheng"]
year: 2024
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2024.3424452"
url: "https://www.scopus.com/pages/publications/105002087773?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "12983--12997"
keywords: ["drone-based applications", "Edge computing", "multi-agent collaboration", "software and hardware co-design", "visual SLAM"]
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

# paper-1038 — Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence

## Metadata

- **Authors:** Li, Danyang and Zhao, Yishujie and Xu, Jingao and Zhang, Shengkai and Shangguan, Longfei and Ma, Qiang and Ding, Xuan and Yang, Zheng
- **Year:** 2024
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2024.3424452
- **URL:** https://www.scopus.com/pages/publications/105002087773?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 12983--12997
- **Language:** English
- **Keywords:** drone-based applications; Edge computing; multi-agent collaboration; software and hardware co-design; visual SLAM

### Abstract

Edge-assisted visual SLAM plays a crucial role in enabling innovative mobile applications, such as autonomous swarm inspection, search-and-rescue, and smart logistics. Constrained by the computational capacities of lightweight mobile devices, current approaches delegate lightweight, time-sensitive tracking tasks to the mobile end while offloading resource-intensive, latency-tolerant map optimization tasks to the edge. However, our pilot study reveals several limitations of the tracking-optimization decoupled paradigm, stemming from the disruption of inter-dependencies between the two tasks. In this paper, we design and implement edgeSLAM2, an innovative system that reshapes the edge-assisted visual SLAM paradigm by tightly integrating tracking and partial-yet-crucial optimization on mobile. edgeSLAM2 harnesses the heterogeneous computing units offered by the commercial systems-on-chip (SoCs) to enhance the computational capacity of mobile devices, which in turn, allows edgeSLAM2 to design a suit of novel algorithms for map sync, optimization, and tracking that accommodate such architectural upgrade. By capitalizing on the full potential of on-chip intelligence, edgeSLAM2 supports both solitary and collaborative SLAM with accuracy and immediacy, underpinned by a cohesive software-hardware co-design. We deploy edgeSLAM2 on drones for industrial inspection. Comprehensive experiments in one of the world's largest oil fields over three months demonstrate its superior performance.  © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Reshaping Edge-Assisted Visual SLAM by Embracing On-Chip Intelligence
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
