---
id: "paper-2242"
title: "Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester"
authors: ["Vogt, Francisco Germano", "Yang, Zhiheng", "Lopes, Victor Hugo Schneider", "Rodr\u00edguez, Fabricio", "Luizelli, Marcelo Caggiani", "Rothenberg, Christian Esteve", "Papagianni, Chrysa"]
year: 2025
venue: "CoNEXT 2025 - Proceedings of the 21st International Conference on Emerging Networking EXperiments and Technologies"
venue_type: "conference"
doi: "10.1145/3765515.3771757"
url: "https://www.scopus.com/pages/publications/105023972677?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "41--42"
keywords: ["llm workloads", "network testing", "p4", "programmable switches", "rdma emulation"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2242 — Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester

## Metadata

- **Authors:** Vogt, Francisco Germano and Yang, Zhiheng and Lopes, Victor Hugo Schneider and Rodríguez, Fabricio and Luizelli, Marcelo Caggiani and Rothenberg, Christian Esteve and Papagianni, Chrysa
- **Year:** 2025
- **Venue:** CoNEXT 2025 - Proceedings of the 21st International Conference on Emerging Networking EXperiments and Technologies
- **DOI:** 10.1145/3765515.3771757
- **URL:** https://www.scopus.com/pages/publications/105023972677?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 41--42
- **Language:** English
- **Keywords:** llm workloads; network testing; p4; programmable switches; rdma emulation

### Abstract

Large Language Model (LLM) training generates synchronized Remote Direct Memory Access (RDMA) bursts that heavily stress datacenter fabrics and are highly sensitive to faults. However, access to full-scale training clusters is costly, and existing network testers fail to accurately reproduce such patterns. We introduce GPTraffic, a topology- and model-aware testing framework that predicts, emulates, and analyzes LLM training workloads on programmable hardware. By combining burst-accurate traffic generation, RDMA-aware semantics, and fine-grained fault injection, GPTraffic enables scalable, realistic, and reproducible experiments that faithfully reflect the dynamics of distributed LLM training. This allows researchers to explore performance bottlenecks, congestion behavior, and fault tolerance under conditions that closely mirror real-world AI training workloads. © 2025 Owner/Author.

## 04 — Title Screening

**Title:** Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester
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
