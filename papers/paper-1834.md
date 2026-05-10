---
id: paper-1834
title: 'HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment'
authors:
- Lian, Zirui
- Cao, Qianyue
- Liang, Chao
- Cao, Jing
- Zhu, Zongwei
- Yang, Zhi
- Ji, Cheng
- Li, Changlong
- Zhou, Xuehai
venue: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
venue_type: journal
year: 2025
doi: 10.1109/TCAD.2025.3548003
url: https://www.scopus.com/pages/publications/86000654880?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3518--3531
keywords:
- Dynamic scenarios
- edge computing
- embedded systems
- federated learning (FL)
- heterogeneous training
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1834 — HaloFL: Efficient Heterogeneity-Aware Federated Learning Through Optimal Submodel Extraction and Dynamic Sparse Adjustment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated learning (FL) is an advanced framework that enables collaborative training of machine learning models across edge devices. An effective strategy to enhance training efficiency is to allocate the optimal submodel based on each device’s resource capabilities. However, system heterogeneity significantly increases the difficulty of allocating submodel parameter budgets appropriately for each device, leading to the straggler problem. Meanwhile, data heterogeneity complicates the selection of the optimal submodel structure for specific devices, thereby impacting training performance. Furthermore, the dynamic nature of edge environments, such as fluctuations in network communication and computational resources, exacerbates these challenges, making it even more difficult to precisely extract appropriately sized and structured submodels from the global model. To address the challenges in heterogeneous training environments, we propose an efficient FL framework, namely, HaloFL. The framework dynamically adjusts the structure and parameter budget of submodels during training by evaluating three dimensions: 1) model-wise performance; 2) layer-wise performance; and 3) unit-wise performance. First, we design a data-aware model unit importance evaluation method to determine the optimal submodel structure for different data distributions. Next, using this evaluation method, we analyze the importance of model layers and reallocate parameters from noncritical layers to critical layers within a fixed parameter budget, further optimizing the submodel structure. Finally, we introduce a resource-aware dual-UCB multiarmed bandit agent, which dynamically adjusts the total parameter budget of submodels according to changes in the training environment, allowing the framework to better adapt to the performance differences of heterogeneous devices. Experimental results demonstrate that HaloFL exhibits outstanding efficiency in various dynamic and heterogeneous scenarios, achieving up to a 14.80% improvement in accuracy and a 3.06× speedup compared to existing FL frameworks. © 1982-2012 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1834.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
