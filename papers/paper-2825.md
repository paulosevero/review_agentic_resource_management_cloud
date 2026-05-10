---
id: paper-2825
title: 'Interactive Fast Computation Offloading and Resource Allocation: A Joint Optimization Approach for Metaverse Applications'
authors:
- Wang, Qi
- Jin, Huiying
- Tai, Changhong
- Dong, Hai
- Zhang, Pengcheng
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3674125
url: https://www.scopus.com/pages/publications/105032790770?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1291--1304
keywords:
- computation offloading
- MADRL
- MEC
- Metaverse applications
- QoS optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2825 — Interactive Fast Computation Offloading and Resource Allocation: A Joint Optimization Approach for Metaverse Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The metaverse is a pioneering cyber-physical space that seamlessly blends the physical and virtual worlds, demanding a fully immersive and highly interactive user experience. However, existing communication designs and traditional offloading and allocation approaches fall short of meeting the dynamic network conditions and real-time performance demands of the metaverse. To tackle these challenges, we develop a wireless transmission architecture optimized for metaverse computation offloading and resource allocation. This design leverages the Rayleigh fading and Multiple Input Multiple Output (MIMO) technology to optimize transmission paths, enhancing the reliability and efficiency of signal transmission in high-concurrency connections. We further introduce MetaTMCO (Meta Transformer and MAPPO based Computation Offloading), a dynamic online computation offloading and resource allocation joint optimized method that meets critical QoS requirements for metaverse applications. MetaTMCO uses a metric named Interaction Frequency (IF) to evaluate resource competition between users and resource interaction between users and the environment, combining QoS to maximize utility under resource constraints. By integrating a Transformer-based encoder-decoder within the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm, MetaTMCO mitigates inefficiencies from partial observations, enabling dynamic optimization of real-time fast offloading strategies across multiple agents. Experimental results demonstrate that MetaTMCO significantly outperforms other approaches in metaverse environments, achieving superior strategy optimization and resource efficiency.  © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2825.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
