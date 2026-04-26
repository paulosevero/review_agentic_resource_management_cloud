---
id: "paper-1412"
title: "Llama-Recipe - Fine-Tuned Meta's Llama LLM, PBOM and NFT Enabled 5G Network-Slice Orchestration and End-to-End Supply-Chain Verification Platform"
authors: ["Bandara, Eranga", "Bouk, Safdar H.", "Shetty, Sachin", "Roy, Sandip", "Mukkamala, Ravi", "Rahman, Abdul", "Foytik, Peter", "Liang, Xueping", "Keong, Ng Wee", "De Zoysa, Kasun"]
year: 2025
venue: "Proceedings - IEEE Consumer Communications and Networking Conference, CCNC"
venue_type: "conference"
doi: "10.1109/CCNC54725.2025.10976116"
url: "https://www.scopus.com/pages/publications/105005138381?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["5G", "6G", "DevSec-Ops", "Generative-AI", "Llama2", "LLM", "NFT", "PBOM"]
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

# paper-1412 — Llama-Recipe - Fine-Tuned Meta's Llama LLM, PBOM and NFT Enabled 5G Network-Slice Orchestration and End-to-End Supply-Chain Verification Platform

## Metadata

- **Authors:** Bandara, Eranga and Bouk, Safdar H. and Shetty, Sachin and Roy, Sandip and Mukkamala, Ravi and Rahman, Abdul and Foytik, Peter and Liang, Xueping and Keong, Ng Wee and De Zoysa, Kasun
- **Year:** 2025
- **Venue:** Proceedings - IEEE Consumer Communications and Networking Conference, CCNC
- **DOI:** 10.1109/CCNC54725.2025.10976116
- **URL:** https://www.scopus.com/pages/publications/105005138381?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 5G; 6G; DevSec-Ops; Generative-AI; Llama2; LLM; NFT; PBOM

### Abstract

Modern 5G networks offer a network-sliced infrastructure where each network slice contains a dedicated 5G core software service layer. The 5G core software services in each slice shares common core network resources to meet specific customer needs. A primary challenge in 5G network slicing involves resource sharing and efficient network slice orchestration. Container-based methodologies, including tools like Docker and Kubernetes, have become popular for orchestrating 5G network slice services and managing configurations in microservices-based cloud-native service deployment. However, despite their utility, these tools present significant challenges. Their complexity often necessitates dedicated DevOps teams for effective management, while configuration management can prove arduous, and end-to-end supply chain oversight is lacking. To address these challenges, this paper introduces 'Llama-Recipe,' a cloud-native 5G-core service deployment and orchestration platform integrating Generative AI, SBOM, PBOM and NFT. 5G-core service configurations across different network slices are represented as 'HOCON (Human-Optimized Config Object Notation)' config objects adhering to the GitOps paradigm. Leveraging custom-trained Meta's Llama2 LLM, Llama-Recipe generates the Kubernetes manifests for network-sliced 5G-core services based on the defined HOCON configurations. The generated Kubernetes manifests of the 5G-core services are deployed in designated Kubernetes clusters utilizing GitOps tools (e.g., ArgoCD), ensuring seamless and automated deployment processes. Additionally, Llama-Recipe introduced a novel mechanism to handle end-to-end supply chain verification of 5G-core software services using Software-Bill of Materials (SBOM) and Pipeline-Bill of Materials (PBOM). SBOMs track all the dependencies and PBOMs facilitate the comprehensive tracking of end-to-end supply chain data for 5G-core software services, enhancing transparency and security. These PBOMs are also generated using the fine-tuned Meta's Llama-2 LLM and are encoded as NFT tokens with a novel NFT token schema. This schema enables easy verification and validation of supply-chain data during deployments, thus helping to prevent various supply-chain attacks. To fine-tune the Meta's Llama2 LLM, we've undertaken a meticulous training process, collaborating with Qlora to transform a 4-bit quantized pre-trained language model into Low-Rank Adapters(LoRA). The effectiveness of the Llama-Recipe is demonstrated through a real-world test-bed deployment in a sliced network scenario, utilizing multiple 5G cores (i.e., Open5GS) across Ericsson's new Radio Access Network (RAN). © 2025 IEEE.

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
