---
id: "paper-2620"
title: "Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework"
authors: ["Islam, Azharul", "Chang, Kyunghi"]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2026.3676381"
url: "https://www.scopus.com/pages/publications/105034434120?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "7964--7986"
keywords: ["6G wireless networks", "deep joint source-channel coding", "knowledge base", "reinforcement learning", "Semantic communication", "unequal error protection", "variational autoencoder"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2620 — Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework

## Metadata

- **Authors:** Islam, Azharul and Chang, Kyunghi
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2026.3676381
- **URL:** https://www.scopus.com/pages/publications/105034434120?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 7964--7986
- **Language:** English
- **Keywords:** 6G wireless networks; deep joint source-channel coding; knowledge base; reinforcement learning; Semantic communication; unequal error protection; variational autoencoder

### Abstract

Semantic communication has emerged as a transformative paradigm for sixth-generation (6G) wireless networks, prioritizing meaning preservation over bit-level accuracy. However, existing frameworks face critical limitations including insufficient terminology preservation, prohibitive API costs for LLM-based reconstruction, and inability to adapt to varying channel conditions. This paper presents a dual-mode domain-aware semantic communication framework integrating knowledge-enhanced compression, content-adaptive unequal error protection (UEP), and reinforcement learning (RL)-driven intelligent reconstruction. Mode 1 (cloud/API-assisted) achieves 98.2% semantic similarity and 96.8% BLEU using GPT-4-turbo for quality-critical applications, while Mode 2 (edge/local) achieves 87.8% semantic similarity and 82.3% BLEU with zero external dependency using a local Mini-LLM (355 M parameters) for latency-critical scenarios. Key contributions include: (1) entropy-adaptive VAE compression with dynamic dimensionality and domain-specific knowledge base enhancement for improved terminology preservation; (2) gradient-based dimension-level UEP with multi-level modulation allocating stronger protection to semantically critical embedding dimensions; and (3) PPO-based multi-path reconstruction intelligently selecting among DVAE-enhanced, pattern-based, and ensemble strategies based on channel conditions and semantic quality indicators. Extensive evaluation on Europarl, News, and Technical corpora across SNR 0–20 dB demonstrates statistically significant improvements over DeepSC, R-DeepSC, and KG-LLM-SC while enabling flexible deployment from cloud-assisted to real-time edge computing. © 2013 IEEE.

## 04 — Title Screening

**Title:** Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
