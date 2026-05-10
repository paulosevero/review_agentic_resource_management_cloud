---
id: paper-1248
title: Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks
authors:
- Wang, Zixin
- Zhou, Yong
- Shi, Yuanming
- Letaief, Khaled. B.
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901572
url: https://www.scopus.com/pages/publications/105000834215?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3063--3068
keywords:
- Edge computing
- Frequency allocation
- Integer programming
- Learning to rank
- Mixed-integer linear programming
- Problem oriented languages
- Resource allocation
- Critical challenges
- Device scheduling
- Distributed data
- Fine tuning
- Fine-tuning methods
- Global models
- Language model
- Learning performance
- On-line algorithms
- Radio resources
- Bandwidth
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

# paper-1248 — Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low-rank adaptation (LoRA) is an emerging fine-tuning method for personalized large language models (LLMs) due to its capability of achieving comparable learning performance to full fine-tuning by training a much smaller number of parameters. Federated fine-tuning (FedFT) combines LoRA with federated learning (FL) to enable collaborative fine-tuning of a global model with edge devices, leveraging distributed data while ensuring privacy. However, limited radio resources and computation capabilities of edge devices pose critical challenges on deploying FedFT over wireless networks. In this paper, we propose a split FedFT framework to separately deploy the computationally-intensive encoder of a pre-trained model at the edge server while reserving the embedding and the task modules at the edge devices, where the information exchanges between these modules are carried out over wireless networks. By exploiting the low-rank property of LoRA, the proposed FedFT framework reduces communication overhead by aggregating the gradient of the task module with respect to the output of a low-rank matrix. To enhance learning performance under stringent resource constraints, we formulate a joint device scheduling and bandwidth allocation problem while considering average transmission delay. By applying the Lyapunov technique, we decompose the formulated long-term mixed-integer programming (MIP) problem into sequential subproblems, followed by developing an online algorithm for effective device scheduling and bandwidth allocation. Simulation results demonstrate the effectiveness of our proposed online algorithm in enhancing learning performance. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1248.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
