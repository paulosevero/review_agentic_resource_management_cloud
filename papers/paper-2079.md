---
id: "paper-2079"
title: "P2PLLMEdge: Peer-to-Peer Framework for Localized Large Language Models using CPU only Resource-Constrained Edge"
authors: ["Ray, Partha Pratim", "Pradhan, Mohan Pratap"]
year: 2025
venue: "EAI Endorsed Transactions on AI and Robotics"
venue_type: "journal"
doi: "10.4108/airo.9292"
url: "https://www.scopus.com/pages/publications/105011332607?origin=resultslist"
publisher: "European Alliance for Innovation"
pages: ""
keywords: ["Decentralized generative AI", "Edge computing", "Peer-to-peer", "Quantized LLMs", "Resource-constrained edge", "Web frameworks"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2079 — P2PLLMEdge: Peer-to-Peer Framework for Localized Large Language Models using CPU only Resource-Constrained Edge

## Metadata

- **Authors:** Ray, Partha Pratim and Pradhan, Mohan Pratap
- **Year:** 2025
- **Venue:** EAI Endorsed Transactions on AI and Robotics
- **DOI:** 10.4108/airo.9292
- **URL:** https://www.scopus.com/pages/publications/105011332607?origin=resultslist
- **Publisher:** European Alliance for Innovation
- **Pages:** 
- **Language:** English
- **Keywords:** Decentralized generative AI; Edge computing; Peer-to-peer; Quantized LLMs; Resource-constrained edge; Web frameworks

### Abstract

In this research, we present P2PLLMEdge, a pioneering peer-to-peer framework designed to enable localized Large Language Models (LLMs) to operate efficiently in resource-constrained edge environments, exemplified by devices such as the Raspberry Pi 4B and CPU-only laptops. The framework addresses critical challenges, including limited computational capacity, network overhead, and scalability, by leveraging lightweight RESTful communication protocols, model-specific quantization, and decentralized task distribution. Key results demonstrate that P2PLLMEdge achieves substantial performance improvements. On average, Peer 2 (CPU-only laptop) achieves a 44.7% reduction in total duration (t<sub>peer2, total</sub> = 15.87 × 10<sup>9</sup> ns) compared to Peer 1 (Raspberry Pi 4B, t<sub>peer1, total</sub> = 28.18 × 10<sup>9</sup> ns). The framework processes tokens at a rate of 21.77 tokens/second on advanced LLMs like Granite3.1-moe:1b, significantly outperforming the baseline. Peer 1, employing quantized LLMs such as smolm2:360m-instruct-q8_0, reduces prompt evaluation duration by 23.2% (t<sub>peer1, prompt_eval</sub> = 0.76 × 10<sup>9</sup> ns) compared to larger models like qwen2.5:0.5b-instruct (t<sub>peer1, prompt_eval</sub> = 0.99 × 10<sup>9</sup> ns). Peer 2 demonstrates superior summarization capabilities, with evaluation durations (t<sub>peer2, eval</sub>) reduced by 72.8% (t<sub>peer2, eval</sub> = 5.15 × 10<sup>9</sup> ns) for explanation-type prompts relative to Peer 1 (t<sub>peer1, eval</sub> = 18.93 × 10<sup>9</sup> ns). The framework also achieves significant network efficiency, reducing inter-peer communication durations by up to 44.9% (t<sub>peer2, network</sub> = 25.83 × 10<sup>9</sup> ns vs. t<sub>peer1, network</sub> = 46.92 × 10<sup>9</sup> ns). Peer-to-peer synergy ensures seamless task execution, where Peer 1 generates text and offloads computationally intensive summarization tasks to Peer 2, achieving a balance between performance and resource utilization. The novelty of P2PLLMEdge lies in its ability to seamlessly integrate lightweight LLMs with decentralized edge devices, achieving advanced natural language processing functionalities entirely on edge devices traditionally deemed unsuitable for such tasks. This framework provides an adaptable, and cost-effective approach for deploying quantized LLM-driven applications. Future directions include scaling the framework to multi-peer environments, optimizing task scheduling algorithms, and exploring integration with heterogeneous LLM-enabled systems. The codes are available on https://github.com/ParthaPRay/peer_to_peer_local_llm_interaction. © 2025 Partha Pratim Ray et al.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
