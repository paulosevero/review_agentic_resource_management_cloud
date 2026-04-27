---
id: "paper-2871"
title: "WDMoE: Wireless Distributed Mixture of Experts for Large Language Models"
authors: ["Xue, Nan", "Sun, Yaping", "Chen, Zhiyong", "Tao, Meixia", "Xu, Xiaodong", "Qian, Liang", "Cui, Shuguang", "Zhang, Wenjun", "Zhang, Ping"]
year: 2026
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2025.3585163"
url: "https://www.scopus.com/pages/publications/105011204186?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "559--572"
keywords: ["Distributed large language models", "expert selection", "mixture of experts", "resource allocation", "wireless communications"]
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

# paper-2871 — WDMoE: Wireless Distributed Mixture of Experts for Large Language Models

## Metadata

- **Authors:** Xue, Nan and Sun, Yaping and Chen, Zhiyong and Tao, Meixia and Xu, Xiaodong and Qian, Liang and Cui, Shuguang and Zhang, Wenjun and Zhang, Ping
- **Year:** 2026
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2025.3585163
- **URL:** https://www.scopus.com/pages/publications/105011204186?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 559--572
- **Language:** English
- **Keywords:** Distributed large language models; expert selection; mixture of experts; resource allocation; wireless communications

### Abstract

Large Language Models (LLMs) have achieved significant success in various natural language processing tasks, but the role of wireless networks in supporting LLMs has not been thoroughly explored. In this paper, we propose a wireless distributed Mixture of Experts (WDMoE) architecture to enable collaborative deployment of LLMs across edge servers at the base station (BS) and mobile devices in wireless networks. Specifically, we decompose the MoE layer in LLMs by placing the gating network and the preceding neural network layer at BS, while distributing the expert networks among the devices. This deployment leverages the parallel inference capabilities of expert networks on mobile devices, effectively utilizing the limited computing and caching resources of these devices. Accordingly, we develop a performance metric for WDMoE-based LLMs, which accounts for both model capability and latency. To minimize the latency while maintaining accuracy, we jointly optimize expert selection and bandwidth allocation based on the performance metric. Moreover, we build a hardware testbed using NVIDIA Jetson kits to validate the effectiveness of WDMoE. Both theoretical simulations and practical hardware experiments demonstrate that the proposed method can significantly reduce the latency without compromising LLM performance. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** WDMoE: Wireless Distributed Mixture of Experts for Large Language Models

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** WDMoE: Wireless Distributed Mixture of Experts for Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** WDMoE: Wireless Distributed Mixture of Experts for Large Language Models
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
