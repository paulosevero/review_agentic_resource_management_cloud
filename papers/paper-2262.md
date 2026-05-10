---
id: paper-2262
title: Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks
authors:
- Wang, Zixin
- Zhou, Yong
- Shi, Yuanming
- Letaief, Khaled B.
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2025
doi: 10.1109/TWC.2025.3531128
url: https://www.scopus.com/pages/publications/105002494727?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3450--3464
keywords:
- Federated learning
- parameter-efficient fine-tuning
- pre-trained foundation model
- resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2262 — Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Pre-trained foundation models (FMs), with extensive number of neurons, are key to advancing next-generation intelligence services, where personalizing these models requires massive amount of task-specific data and computational resources. The prevalent solution involves centralized processing at the edge server, which, however, raises privacy concerns due to the transmission of raw data. Instead, federated fine-tuning (FedFT) is an emerging privacy-preserving fine-tuning (FT) paradigm for personalized pre-trained foundation models. In particular, by integrating low-rank adaptation (LoRA) with federated learning (FL), federated LoRA enables the collaborative FT of a global model with edge devices, achieving comparable learning performance to full FT while training fewer parameters over distributed data and preserving raw data privacy. However, the limited radio resources and computation capabilities of edge devices pose significant challenges for deploying 3 LoRA over wireless networks. To this paper, we propose a split federated LoRA framework, which deploys the computationally-intensive encoder of a pre-trained model at the edge server, while keeping the embedding and task modules at the edge devices. The information exchanges between these modules occur over wireless networks. Building on this split framework, the paper provides a rigorous analysis of the upper bound of the convergence gap for the wireless federated LoRA system. This analysis reveals the weighted impact of the number of edge devices participating in FedFT over all rounds, motivating the formulation of a long-term upper bound minimization problem. To address the long-term constraint, we decompose the formulated long-term mixed-integer programming (MIP) problem into sequential sub-problems using the Lyapunov technique. We then develop an online algorithm for effective device scheduling and bandwidth allocation. Simulation results demonstrate the effectiveness of the proposed online algorithm in enhancing learning performance. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2262.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
