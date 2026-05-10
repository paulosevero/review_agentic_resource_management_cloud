---
id: "paper-2634"
title: "Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments"
authors: ["Keum, Chaewon", "Song, Yelin", "Lee, Seoyoung", "Cho, Kyungwoon", "Bahn, Hyokyung"]
year: 2026
venue: "Applied Sciences (Switzerland)"
venue_type: "journal"
doi: "10.3390/app16073484"
url: "https://www.scopus.com/pages/publications/105035601821?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["decentralized scheduling", "distributed hash table (DHT)", "distributed orchestration", "fault tolerance", "task scheduling"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2634 — Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments

## Metadata

- **Authors:** Keum, Chaewon and Song, Yelin and Lee, Seoyoung and Cho, Kyungwoon and Bahn, Hyokyung
- **Year:** 2026
- **Venue:** Applied Sciences (Switzerland)
- **DOI:** 10.3390/app16073484
- **URL:** https://www.scopus.com/pages/publications/105035601821?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** decentralized scheduling; distributed hash table (DHT); distributed orchestration; fault tolerance; task scheduling

### Abstract

Featured Application: Decentralized resource orchestration for computing environments where nodes can freely join and leave, such as loosely coupled research infrastructures, community clusters, and edge systems. Today, many computing workloads are executed in loosely coupled, geographically distributed environments where resources are owned by different organizations. Examples include inter-institutional research infrastructures, community-operated clusters, and edge deployments. As disconnections are frequent in such environments, ensuring reliable task execution remains a fundamental challenge. Kubernetes, the de facto standard for cluster orchestration, provides centralized control and strong consistency, but suffers from slow recovery when node failures occur frequently. At the opposite extreme, blockchain-based orchestration removes centralized control but incurs substantial latency due to global consensus, making it unsuitable for time-sensitive task scheduling. This paper presents Mutual Cloud, a decentralized orchestration framework that operates between these two extremes. Mutual Cloud adopts a hybrid architecture where task admission and queue management are handled in a centralized manner similar to conventional public clouds, whereas most scheduling functions, including execution-node selection and failure handling, are performed in a decentralized manner by autonomous agents using a distributed hash table. We implement a prototype of Mutual Cloud and evaluate its performance through large-scale simulation studies. The results show that Mutual Cloud maintains stable performance comparable to centralized baselines under normal conditions while achieving approximately five-second-level recovery latency under substantial node failures. © 2026 by the authors.

## 04 — Title Screening

**Title:** Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Mutual Cloud: Decentralized Task Orchestration in Loosely Coupled Distributed Environments
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
