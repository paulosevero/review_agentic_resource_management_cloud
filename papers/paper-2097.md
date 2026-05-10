---
id: paper-2097
title: Hybrid CDN Architecture Integrating Edge Caching, MEC Offloading, and Q-Learning-Based Adaptive Routing
authors:
- Salman, Aymen D.
- Zeyad, Akram T.
- Al-karkhi, Asia Ali Salman
- Raafat, Safanah M.
- Humaidi, Amjad J.
venue: Computers
venue_type: journal
year: 2025
doi: 10.3390/computers14100433
url: https://www.scopus.com/pages/publications/105020170344?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- cache hit ratio
- computation offloading
- content popularity
- cooperative caching
- edge caching
- latency optimization
- multi-access edge computing
- Q-learning
- reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2097 — Hybrid CDN Architecture Integrating Edge Caching, MEC Offloading, and Q-Learning-Based Adaptive Routing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Content Delivery Networks (CDNs) have evolved to meet surging data demands and stringent low-latency requirements driven by emerging applications like high-definition video streaming, virtual reality, and IoT. This paper proposes a hybrid CDN architecture that synergistically combines edge caching, Multi-access Edge Computing (MEC) offloading, and reinforcement learning (Q-learning) for adaptive routing. In the proposed system, popular content is cached at radio access network edges (e.g., base stations) and computation-intensive tasks are offloaded to MEC servers, while a Q-learning agent dynamically routes user requests to the optimal service node (cache, MEC server, or origin) based on the network state. The study presented detailed system design and provided comprehensive simulation-based evaluation. The results demonstrate that the proposed hybrid approach significantly improves cache hit ratios and reduces end-to-end latency compared to traditional CDNs and simpler edge architectures. The Q-learning-enabled routing adapts to changing load and content popularity, converging to efficient policies that outperform static baselines. The proposed hybrid model has been tested against variants lacking MEC, edge caching, or the RL-based controller to isolate each component’s contributions. The paper concludes with a discussion on practical considerations, limitations, and future directions for intelligent CDN networking at the edge. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2097.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
