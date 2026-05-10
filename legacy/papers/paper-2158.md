---
id: "paper-2158"
title: "Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission"
authors: ["Solat, Faranaksadat", "Lee, Joohyung", "Seif, Mohamed", "Niyato, Dusit", "Vincent Poor, H."]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3618095"
url: "https://www.scopus.com/pages/publications/105018357552?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "53574--53592"
keywords: ["Federated learning (FL)", "hybrid language models (HLMs)", "large language models (LLMs)", "mobile edge computing", "small language models (SLMs)"]
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
    human_justification: "LLM as workload"

---

# paper-2158 — Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission

## Metadata

- **Authors:** Solat, Faranaksadat and Lee, Joohyung and Seif, Mohamed and Niyato, Dusit and Vincent Poor, H.
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3618095
- **URL:** https://www.scopus.com/pages/publications/105018357552?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 53574--53592
- **Language:** English
- **Keywords:** Federated learning (FL); hybrid language models (HLMs); large language models (LLMs); mobile edge computing; small language models (SLMs)

### Abstract

Hybrid language models (HLMs) are inference-time architectures that combine the low-latency efficiency of small language models (SLMs) on clients (edge devices) with the high accuracy of large language models (LLMs) in centralized servers. Unlike traditional end-to-end LLM inference, HLMs aim to reduce latency and communication by selectively invoking LLMs only when the local SLM’s predictions are uncertain—that is, when the model exhibits low confidence or high entropy in its token-level probability distribution. However, when the SLM encounters ambiguous or low-confidence predictions during inference, it must offload token-level probability distributions to the LLM for refinement. This frequent offloading leads to substantial communication overhead, particularly in bandwidth-constrained environments. To address this challenge, we propose federated learning (FL)-enabled HLM (FedHLM), a communication-efficient HLM framework that integrates uncertainty-aware inference with FL. The key innovation lies in collaboratively learning token-level uncertainty thresholds that determine when SLM predictions require LLM assistance. Instead of relying on static or hand-tuned thresholds, FedHLM uses FL to enable distributed threshold optimization across clients while preserving data privacy. Additionally, embedding-based token representations are employed to facilitate semantic similarity comparisons during peer-to-peer (P2P) resolution, allowing clients to reuse tokens inferred by similar peers without efficiently involving the LLM. Moreover, we propose hierarchical model aggregation as a strategy to reduce redundant token transmissions. At the edge server level, client updates are aggregated to refine local routing policies, while global coordination across clusters further synchronizes decision boundaries. This layered approach ensures that repeated uncertainty patterns are captured and resolved locally, significantly reducing unnecessary LLM queries. Extensive simulations on large-scale news classification tasks demonstrate that FedHLM achieves over 95% reduction in LLM transmissions with negligible accuracy loss, highlighting its potential for scalable and efficient edge-artificial intelligence (AI) deployment. © 2014 IEEE.

## 04 — Title Screening

**Title:** Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission
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
