---
id: paper-1412
title: Llama-Recipe - Fine-Tuned Meta's Llama LLM, PBOM and NFT Enabled 5G Network-Slice Orchestration and End-to-End Supply-Chain Verification Platform
authors:
- Bandara, Eranga
- Bouk, Safdar H.
- Shetty, Sachin
- Roy, Sandip
- Mukkamala, Ravi
- Rahman, Abdul
- Foytik, Peter
- Liang, Xueping
- Keong, Ng Wee
- De Zoysa, Kasun
venue: Proceedings - IEEE Consumer Communications and Networking Conference, CCNC
venue_type: conference
year: 2025
doi: 10.1109/CCNC54725.2025.10976116
url: https://www.scopus.com/pages/publications/105005138381?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 5G
- 6G
- DevSec-Ops
- Generative-AI
- Llama2
- LLM
- NFT
- PBOM
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1412 — Llama-Recipe - Fine-Tuned Meta's Llama LLM, PBOM and NFT Enabled 5G Network-Slice Orchestration and End-to-End Supply-Chain Verification Platform

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern 5G networks offer a network-sliced infrastructure where each network slice contains a dedicated 5G core software service layer. The 5G core software services in each slice shares common core network resources to meet specific customer needs. A primary challenge in 5G network slicing involves resource sharing and efficient network slice orchestration. Container-based methodologies, including tools like Docker and Kubernetes, have become popular for orchestrating 5G network slice services and managing configurations in microservices-based cloud-native service deployment. However, despite their utility, these tools present significant challenges. Their complexity often necessitates dedicated DevOps teams for effective management, while configuration management can prove arduous, and end-to-end supply chain oversight is lacking. To address these challenges, this paper introduces 'Llama-Recipe,' a cloud-native 5G-core service deployment and orchestration platform integrating Generative AI, SBOM, PBOM and NFT. 5G-core service configurations across different network slices are represented as 'HOCON (Human-Optimized Config Object Notation)' config objects adhering to the GitOps paradigm. Leveraging custom-trained Meta's Llama2 LLM, Llama-Recipe generates the Kubernetes manifests for network-sliced 5G-core services based on the defined HOCON configurations. The generated Kubernetes manifests of the 5G-core services are deployed in designated Kubernetes clusters utilizing GitOps tools (e.g., ArgoCD), ensuring seamless and automated deployment processes. Additionally, Llama-Recipe introduced a novel mechanism to handle end-to-end supply chain verification of 5G-core software services using Software-Bill of Materials (SBOM) and Pipeline-Bill of Materials (PBOM). SBOMs track all the dependencies and PBOMs facilitate the comprehensive tracking of end-to-end supply chain data for 5G-core software services, enhancing transparency and security. These PBOMs are also generated using the fine-tuned Meta's Llama-2 LLM and are encoded as NFT tokens with a novel NFT token schema. This schema enables easy verification and validation of supply-chain data during deployments, thus helping to prevent various supply-chain attacks. To fine-tune the Meta's Llama2 LLM, we've undertaken a meticulous training process, collaborating with Qlora to transform a 4-bit quantized pre-trained language model into Low-Rank Adapters(LoRA). The effectiveness of the Llama-Recipe is demonstrated through a real-world test-bed deployment in a sliced network scenario, utilizing multiple 5G cores (i.e., Open5GS) across Ericsson's new Radio Access Network (RAN). © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Llama" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1412.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
