---
id: "paper-2544"
title: "Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems"
authors: ["Coviello, Giuseppe", "Rao, Kunal", "Khojastepour, Mohammad A.", "Chakradhar, Srimat"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-3-031-99854-6_19"
url: "https://www.scopus.com/pages/publications/105015502014?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "279--291"
keywords: ["Agentic AI systems", "Distributed systems", "Function as a Service", "Load balancing"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2544 — Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems

## Metadata

- **Authors:** Coviello, Giuseppe and Rao, Kunal and Khojastepour, Mohammad A. and Chakradhar, Srimat
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-3-031-99854-6_19
- **URL:** https://www.scopus.com/pages/publications/105015502014?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 279--291
- **Language:** English
- **Keywords:** Agentic AI systems; Distributed systems; Function as a Service; Load balancing

### Abstract

Agentic AI systems rely on Large Language Models (LLMs) to execute complex tasks by invoking external functions. The efficiency of these systems depends on how well function execution is managed, especially under heterogeneous and high-variance workloads, where function execution times can range from milliseconds to several seconds. Traditional load-balancing techniques, such as round-robin, least-loaded, and Peak-EWMA (used in Linkerd), struggle in such settings: round-robin ignores load imbalance, least-loaded reacts slowly to rapid workload shifts, and Peak-EWMA relies on latency tracking, which is ineffective for workloads with high execution time variability. In this paper, we introduce Bifröst, a peer-to-peer load-balancing mechanism that distributes function requests based on real-time active request count rather than latency estimates. Instead of relying on centralized load-balancers or client-side decisions, Bifröst enables function-serving pods to dynamically distribute load by comparing queue lengths and offloading requests accordingly. This avoids unnecessary overhead while ensuring better responsiveness under high-variance workloads. Our evaluation on open-vocabulary object detection, multi-modal understanding, and code generation workloads shows that Bifröst improves function completion time by up to 20% when processing 13,700 requests from 137 AI agents on a 32-node Kubernetes cluster, outperforming both OpenFaaS and OpenFaaS with Linkerd. In an AI-driven insurance claims processing workflow, Bifröst achieves up to 25% faster execution.   © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

## 04 — Title Screening

**Title:** Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems
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
