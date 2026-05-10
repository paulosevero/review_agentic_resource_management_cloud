---
id: paper-2436
title: 'GenNet: Computing-Efficient Generative AI for Deterministic Transmission Scheduling in 6G Networks'
authors:
- Zhang, Weiting
- Ren, Jiadong
- Zheng, Tao
- Guo, Ruibin
- Zhang, Han
- Mao, Shiwen
- Zhang, Hongke
venue: IEEE Communications Magazine
venue_type: journal
year: 2025
doi: 10.1109/MCOM.001.2400588
url: https://www.scopus.com/pages/publications/105012193548?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 48--55
keywords:
- Diffusion
- Edge computing
- Energy utilization
- Green computing
- Intelligent computing
- Network layers
- Scheduling algorithms
- Transmissions
- Ubiquitous computing
- Computing services
- Deterministics
- Diffusion model
- Key characteristics
- Low delay
- Low energy consumption
- Network ubiquitous
- Transmission scheduling
- Ubiquitous intelligence
- Ubiquitous networking
- Network architecture
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
  05-abstract-screening: include
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: "Out of scope"
    winning_category: out_of_scope
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2436 — GenNet: Computing-Efficient Generative AI for Deterministic Transmission Scheduling in 6G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of the sixth generation (6G) networks, ubiquitous intelligence, computing, and networking integration, low energy consumption, and low delay have become the key characteristics. These characteristics pose significant challenges for traffic scheduling, particularly in the context of intelligent computing services. In recent years, generative artificial intelligence (AI) has demonstrated remarkable performance not only in natural language processing and image generation but also in network optimization. This article presents a generative AI-endogenous three-layer network architecture, named GenNet, to support more efficient scheduling of intelligent computing services in 6G networks by the dynamic adaptation of heterogeneous computing resources and diversified service requirements. Moreover, we propose a dueling double deep Q-network (D3QN)-based transmission scheduling algorithm that leverages diffusion models to achieve cross-domain end-to-end deterministic transmission. The proposed algorithm facilitates efficient interaction between edge devices and intelligent computing centers while reducing system cost and delay, and utilizes the denoising capability of the diffusion model to adaptively configure networks and optimize resource allocation. Finally, we present a case study, followed by a discussion of open research issues that are essential for generative AI and future networks.  © IEEE. 1979-2012 IEEE.

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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "natural language processing" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
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

## 06 — Full-Text Screening

### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Out of scope"
- **winning_category:** 'out_of_scope'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: out_of_scope, pattern_id: oos_smart_manufacturing, matched_substring: "smart manufacturing" }`

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
