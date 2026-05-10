---
id: paper-1390
title: An end-to-end four tier remote healthcare monitoring framework using edge-cloud computing and redactable blockchain
authors:
- Alsharabi, Naif
- Alayba, Abdulaziz
- Alshammari, Gharbi
- Alsaffar, Mohammad
- Jadi, Amr
venue: Computers in Biology and Medicine
venue_type: journal
year: 2025
doi: 10.1016/j.compbiomed.2025.109987
url: https://www.scopus.com/pages/publications/86000639246?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- And redactable blockchain
- Cloud server
- Distributed edge server
- Medical internet of things (MIoT)
- Remote healthcare
- Wireless body sensors (WBS)
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
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
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

# paper-1390 — An end-to-end four tier remote healthcare monitoring framework using edge-cloud computing and redactable blockchain

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Medical Internet of Things (MIoTs) encompasses compact, energy-efficient wireless sensor devices designed to monitor patients' body outcomes. Healthcare networks provide constant data monitoring, enabling patients to live independently. Despite advancements in MIoTs, critical issues persist that can affect the Quality of Service (QoS) in the network. The wearable IoT module collects data and stores it on cloud servers, making it vulnerable to privacy breaches and attacks by unauthorized users. To address these challenges, we propose an end-to-end secure remote healthcare framework called the Four Tier Remote Healthcare Monitoring Framework (FTRHMF). This framework comprises multiple entities, including Wireless Body Sensors (WBS), Distributed Gateway (DGW), Distributed Edge Server (DES), Blockchain Server (BS), and Cloud Server (CS). The framework operates in four tiers. In the first tier, WBS and DGW are authenticated to the BS using secret credentials, ensuring privacy and security for all entities. In the second tier, authenticated WBS transmit data to the DGW via a two-level Hybridized Metaheuristic Secure Federated Clustered Routing Protocol (HyMSFCRP), which leverages Mountaineering Team-Based Optimization (MTBO) and Sea Horse Optimization (SHO) algorithms. In the third tier, sensor reports are prioritized and analyzed using Multi-Agent Deep Reinforcement Learning (MA-DRL), with the results fed into the Hybrid-Transformer Deep Learning (HTDL) model. This model combines Lite Convolutional Neural Network and Swin Transformer networks to detect patient outcomes accurately. Finally, in the fourth tier, patients' outcomes are securely stored in a cloud-assisted redactable blockchain layer, allowing modifications without compromising the integrity of the original data. This research enhance the network lifetime by 18.3 %, reduce the transmission delays by 15.6 %, ensures classification accuracy of 7.4 %, with PSNR of 46.12 dB, SSIM of 0.8894, and MAE of 22.51 when compared to the existing works. © 2025 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1390.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
