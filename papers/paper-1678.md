---
id: paper-1678
title: 'AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms'
authors:
- Idrees, Fatima
- Ambigapathy, Narmada
- Adelt, Peer
- Rettberg, Achim
venue: IAVVC 2025 - IEEE International Automated Vehicle Validation Conference, Proceedings
venue_type: conference
year: 2025
doi: 10.1109/IAVVC61942.2025.11219567
url: https://www.scopus.com/pages/publications/105025131025?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Autonomous vehicles
- CARLA simulation
- Edge computing
- Large language models
- Traffic regulation compliance
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1678 — AI-Driven Traffic Compliance in Autonomous Vehicles: A Scalable Framework with Large Language Models on Edge Platforms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents a scalable and modular framework for monitoring traffic compliance in autonomous vehicles by adapting large-language models (LLMs) and lightweight generative models on resource-constrained edge devices. The framework integrates CARLA as a digital twin to simulate diverse driving scenarios with deployments on Raspberry Pi 5 and Jetson Nano P3541 platforms. Large language models GPT-2, GPT-Neo, OPT, and BLOOM are fine-tuned and evaluated for their ability to generate structured output consisting of a compliance label and corresponding traffic regulation. To address deployment limitations on low-power hardware, two lightweight models DistilGPT2 and Flan-T5-small are also explored. The study evaluates platform-specific trade-offs: Raspberry Pi 5 demonstrated cost-efficiency and stable performance with smaller models, while Jetson Nano processed larger models such as BLOOM with reduced latency, with up to 25 % faster inference times. While DistilGPT2 and Flan-T5-small improved inference efficiency and memory usage, they exhibited reduced classification accuracy due to limited contextual representation and instruction tuning limitations. The decentralized architecture allows independent updates to simulation, inference, and communication components, enhancing adaptability within AV validation pipelines. Although the current implementation relies on simulated input, future work will focus on integrating real-world sensor data and optimizing memory, latency, and energy usage. These findings underscore the scalability and feasibility of deploying generative language models for edge-based, decentralized traffic compliance monitoring in autonomous driving systems.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1678.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
