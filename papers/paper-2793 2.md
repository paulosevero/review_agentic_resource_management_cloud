---
id: "paper-2793"
title: "EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing"
authors: ["Taher, Bahaa Hussein", "Luo, Juan", "Ghrabat, Fadhil", "Qiao, Ying"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3656811"
url: "https://www.scopus.com/pages/publications/105028274819?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "15514--15532"
keywords: ["Blockchain-lite security", "constrained reinforcement learning", "low-latency networks", "multiagent systems", "resource allocation", "sixth-generation (6G) edge computing"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-2793 — EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing

## Metadata

- **Authors:** Taher, Bahaa Hussein and Luo, Juan and Ghrabat, Fadhil and Qiao, Ying
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3656811
- **URL:** https://www.scopus.com/pages/publications/105028274819?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 15514--15532
- **Language:** English
- **Keywords:** Blockchain-lite security; constrained reinforcement learning; low-latency networks; multiagent systems; resource allocation; sixth-generation (6G) edge computing

### Abstract

In smart-city air-quality monitoring, millions of IoT sensors generate time-sensitive data that must be processed within strict end-to-end deadlines, under dynamic mobility conditions, and with strong security guarantees. In this study, we present EdgePlus, a unified sixth-generation (6G) framework that couples 1) masked cooperative PPO (CCPPO) enforcing feasibility at sampling time (routing order, slice quotas, resource limits), 2) a constricted particle swarm optimization (PSO) outer loop that escapes local optima under strict SLA gates, 3) a lightweight advisory layer (Nash sharing, Ziegler–Nichols-initialized PID, and leader election) that biases logits without breaking masks, and 4) a two-tier blockchain-lite ledger [edge proof-of-authority (PoA), cloud Byzantine fault-tolerant BFT)] whose reputation and debt signals feedback into state, reward, and masks. In a 100 km<sup>2</sup> city-scale simulator (ten clusters; three load regimes of 50 000, 100 000, and 150 000 tasks). Under light load, all methods reach 100% success with seconds-level latencies and no observable penalty from masking or security. At stress (150k), EdgePlus achieves the highest on-time completion rate (82.77%), highest throughput (206.93), lowest violation rate (17.23%), and lowest 15 percentile latency (L<sub>p</sub><sub>50</sub> of 53.23 s). Ablations confirmed that feasibility masks dominate performance: removing them increases violations by 5.5%–10.0% points and tail latency (L<sub>p</sub><sub>95</sub>) by 26–47 s, while advisory and PSO deliver smaller but consistent gains. The PID controller remains robust under ±20% gain drift (settling ≈ 2.7–2.9 s) by design-time Jury certification. In security experiments, baseline confidentiality, integrity, and availability (CIA)/auth attacks are mitigated at 98%–99% and advanced (nonphysical-layer) threats achieve 70%–83% defense with strong efficiency. Edge-tier PoA validation adds a median ≈ 0.39 ms per partial block for validator sets up to 10 and remains sub-ms with partitioned sub-quorums up to 30, while cloud BFT provides accountable finality off the critical path. In short, EdgePlus delivers a single, coherent scheduling–control–security stack for 6G edge computing, built on a feasibility-first design that preserves reliability, locality, and security at scale. © 2014 IEEE. All rights reserved.

## 04 — Title Screening

**Title:** EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
