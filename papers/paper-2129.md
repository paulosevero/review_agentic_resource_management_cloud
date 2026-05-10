---
id: paper-2129
title: Characteristics and Link Congestion Awareness
authors:
- Shen, Zhipeng
- Li, Lei
- Zhang, Lihong
- Liu, Bing
- Cai, Anning
- Huang, Shan
venue: Proceedings - 2025 IEEE Cyber Science and Technology Congress, CyberSciTech 2025
venue_type: conference
year: 2025
doi: 10.1109/CyberSciTech68397.2025.00012
url: https://www.scopus.com/pages/publications/105032631668?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 45--54
keywords:
- AI
- Dynamic Traffic Regulation
- GPU Communication Path
- Load Balance
- Network Topology
- RoCE
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2129 — Characteristics and Link Congestion Awareness

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the context of AI computing RoCE networks, the low-entropy traffic characteristics of training and inference services lead to load imbalance in RoCE networks, reducing GPU communication efficiency and affecting AI service operations. To address this issue, this paper proposes RNL (RoCE Network Load-balance), a framework specifically designed for load balancing in AI RoCE networks. RNL conducts real-time modeling of AI task communication relationships and paths, as well as network link loads. It uses a multi-dimensional link congestion assessment algorithm to accurately calculate the congestion score of all network paths and based on in-depth analysis of the communication primitives of AI business GPU, identifies communication bandwidth and delay requirements. It achieves precise scheduling and orchestration of AI business communication paths, ensuring balanced load distribution of RoCE network for AI business.The RNL design leverages existing commercial high-performance network interface cards and RoCE switches, eliminating dependence on special hardware and ensuring good compatibility with existing AI computing data center networks. Experimental results show that the proposed scheme significantly enhances RoCE network performance, GPU communication primitives, and inference performance of large AI language models. Specifically, it improves network link bandwidth utilization by 85%, link balance dispersion by 90%, bandwidth of AllReduce/AllGather communication primitives by over 50%, and throughput/TTFT/TPOT of large AI model inference by over 30%, providing an effective solution for constructing high-performance AI RoCE networks.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2129.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
