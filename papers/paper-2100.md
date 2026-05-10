---
id: paper-2100
title: Dynamic Resource Provisioning in Cloud Computing Using Optimized Wasserstein Deep Convolutional Generative Adversarial Networks
authors:
- Santhiya, C.
- Padmavathi, S.
venue: Transactions on Emerging Telecommunications Technologies
venue_type: journal
year: 2025
doi: 10.1002/ett.70128
url: https://www.scopus.com/pages/publications/105003138618?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- Adaptive Self-Guided Filtering
- Artificial Hummingbird Algorithm
- cloud computing
- dynamic resource provisioning
- software as a service
- virtual machines
- Wasserstein Deep Convolutional Generative Adversarial Network
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: GAN
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

# paper-2100 — Dynamic Resource Provisioning in Cloud Computing Using Optimized Wasserstein Deep Convolutional Generative Adversarial Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing (CC) has revolutionized the way resources are managed and delivered by providing scalable, on-demand services. However, dynamic resource provisioning remains a complex challenge due to unpredictable workloads, varying user demands, and the need to maintain cost efficiency. Traditional resource allocation techniques lack the adaptability required to optimize resource usage under dynamic conditions. This manuscript presents a novel approach for dynamic resource provisioning using an Optimized Wasserstein Deep Convolutional Generative Adversarial Network (DRP-WDCGAN-AHBA). Initially, the input data are collected from the Grid Workloads Dataset, which provides a comprehensive representation of workload patterns in cloud environments. The input data undergo rigorous preprocessing using Adaptive Self-Guided Filtering (ASGF) to ensure data quality. Then, Wasserstein Deep Convolutional Generative Adversarial Network (WDCGAN) is used to forecast CPU utilization over specified time intervals of 5, 15, 30, and 60 min. The Adaptive Hybrid Bat Algorithm (AHBA) is employed to optimize resource allocation dynamically and ensure efficient utilization. The proposed DRP-WDCGAN-AHBA model attains 20.36%, 18.63%, and 21.24% lower energy consumption and 16.78%, 23.64%, and 26.32% lower response time when compared with existing models, such as Multi-agent QoS-aware autonomic resource provisioning method BPM in containerized multi-cloud environs for elastic (DRP-QoS-EDSAE), Multi-objective dependent Scheduling Method for Effective Resource Utilization in Cloud Computing (DRP-LS-CSO-ARNN), and Energy-aware fully adaptive resource provisioning in collaborative CPU-FPGA cloud environs: Journal of Parallel and Distributed Computing (EFARP-CPU-FPGA). © 2025 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "GAN"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2100.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
