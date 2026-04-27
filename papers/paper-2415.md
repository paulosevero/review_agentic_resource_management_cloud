---
id: "paper-2415"
title: "A Trustworthy and Efficient Inference Scheduling Scheme for Edge MoEs Using DRL"
authors: ["Zhang, Jinyang", "Pan, Shengli", "Chen, Shanwu", "Roy, Anandarup", "Li, Peng"]
year: 2025
venue: "Proceedings of the IEEE International Conference on Trust, Security and Privacy in Computing and Communications, TrustCom"
venue_type: "conference"
doi: "10.1109/Trustcom66490.2025.00330"
url: "https://www.scopus.com/pages/publications/105033695992?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2789--2794"
keywords: ["Edge Computing", "Inference Credibility", "Mixture of Experts", "Servicing Latency"]
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
    human_justification: "RL"

---

# paper-2415 — A Trustworthy and Efficient Inference Scheduling Scheme for Edge MoEs Using DRL

## Metadata

- **Authors:** Zhang, Jinyang and Pan, Shengli and Chen, Shanwu and Roy, Anandarup and Li, Peng
- **Year:** 2025
- **Venue:** Proceedings of the IEEE International Conference on Trust, Security and Privacy in Computing and Communications, TrustCom
- **DOI:** 10.1109/Trustcom66490.2025.00330
- **URL:** https://www.scopus.com/pages/publications/105033695992?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2789--2794
- **Language:** English
- **Keywords:** Edge Computing; Inference Credibility; Mixture of Experts; Servicing Latency

### Abstract

With the widespread popularity of Large Language Models (LLMs), the mixture of experts (MoE) has not only emerged as a key enabler for scaling up model capacity by significantly reducing computational demands, but also for giving rise to edge-computing empowered distributed LLMs with better prices, low latency, and regional privacy. Nonetheless, besides constraints in computational capability, edge-based LLM deployments also face challenges such as unreliable environments due to the limited security of edge devices. In this paper, we propose REMIS, an inference task scheduling scheme designed to enable MoE-based LLM services under untrustworthy computation conditions. Specifically, after an LLM is properly partitioned into shards and deployed across edge devices, REMIS dynamically schedules and activates experts on devices with lower loads and higher reliability. This strategy is effectively achieved through a deep reinforcement learning procedure that optimizes both servicing latency and inference credibility. Unlike most existing MoE-based schemes with fixed Top-K routing, REMIS operates in a novel plug-in manner, intelligently selecting experts to improve task adaptability. Numerical evaluations under various untrustworthy setups validate the superiority of our proposed scheme in both servicing latency and inference credibility. © 2025 IEEE.

## 04 — Title Screening

**Title:** A Trustworthy and Efficient Inference Scheduling Scheme for Edge MoEs Using DRL

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Trustworthy and Efficient Inference Scheduling Scheme for Edge MoEs Using DRL
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Trustworthy and Efficient Inference Scheduling Scheme for Edge MoEs Using DRL
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
