---
id: paper-2788
title: 'MATE: A D2D-Enhanced Multi-Bitrate Video Caching Strategy for Cloud-Edge-Device Collaborative Networks'
authors:
- Sun, Haiyang
- Chen, Honglong
- Fan, Xinglong
- Ni, Zhichen
- Wu, Liantao
- Sun, Peng
- Liu, Weifeng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3641174
url: https://www.scopus.com/pages/publications/105024593421?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6966--6980
keywords:
- cloud-edge-device collaborative networks
- D2D caching
- deep reinforcement learning
- edge caching
- Multi-bitrate video caching
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

# paper-2788 — MATE: A D2D-Enhanced Multi-Bitrate Video Caching Strategy for Cloud-Edge-Device Collaborative Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge caching alleviates backhaul pressure and enhances video service quality by deploying video content near user devices. However, the limited storage capacity of edge servers struggles to cope with the exponential growth of video data, challenging the delivery of high-quality video services. While both Device-to-Device (D2D) caching and multi-bitrate video technology are promising solutions to relieve the pressure on edge servers, existing research suffers from a key limitation: studies on multi-bitrate caching are predominantly focused on the edge layer, while D2D caching is often limited to single-bitrate scenarios. This isolation neglects the significant benefits of integrating D2D caching with multi-bitrate technology and fails to develop a cross-layer caching strategy for multi-bitrate videos. To address this limitation, we propose a D2D-enhanced Multi-bitrate video cAching straTEgy (MATE) for cloud-edge-device collaborative networks. We formulate a joint service latency and caching replacement cost optimization problem, which can be modeled as a mixed-integer programming problem. To overcome the coupling between caching strategies at the edge layer and device layer, we employ an alternating iterative optimization approach to decouple the original problem into two subproblems. We design an edge-device double-layer joint caching strategy, i.e., a device-layer caching strategy based on greedy algorithm and Lagrange multipliers, and an edge-layer caching strategy based on multi-agent twin delayed deep deterministic policy gradient algorithm. Extensive simulations are conducted to demonstrate the effectiveness of the proposed MATE. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2788.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
