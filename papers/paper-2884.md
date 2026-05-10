---
id: paper-2884
title: 'Privacy-preserving federated reinforcement learning for autonomous IoT intrusion response: A deep multi-agent hierarchical framework with advanced cryptographic security'
authors:
- Yaseen, Muhammad Bilal
- Wan, Fayu
- Riaz, Muhammad Bilal
- Rahman, Md Owahedur
- Fang, Xiang
venue: Results in Engineering
venue_type: journal
year: 2026
doi: 10.1016/j.rineng.2026.109458
url: https://www.scopus.com/pages/publications/105029777224?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Byzantine fault tolerance
- Differential privacy
- Edge computing
- Intrusion detection
- Multi-agent systems
- Privacy preservation
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
    my_justification: RL
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

# paper-2884 — Privacy-preserving federated reinforcement learning for autonomous IoT intrusion response: A deep multi-agent hierarchical framework with advanced cryptographic security

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The exponential growth of Internet of Things (IoT) devices has intensified cybersecurity challenges that demand autonomous, adaptive, and privacy-preserving intrusion response mechanisms. Traditional centralized solutions suffer from scalability bottlenecks, high communication costs, and privacy violations, making them unsuitable for modern heterogeneous IoT networks. To overcome these limitations, this paper introduces a Privacy-Preserving Federated Reinforcement Learning (PP-FRL) framework named Adaptive Contextual Multi-Agent Deep Q-Network (AC-MADQN). The framework enables distributed IoT edge devices to collaboratively learn optimal security policies without sharing raw data, combining hierarchical policy optimization with federated aggregation enhanced by quantum-resilient cryptography , differential privacy, and Byzantine fault-tolerant consensus. AC-MADQN incorporates four key innovations: (1) Dynamic State Representation Learning using temporal attention, (2) Multi-scale threat-intelligence fusion, (3) Adaptive resource-aware policy optimization, and (4) Cryptographically secure experience-replay sharing. Comprehensive experiments on a 2,000-device heterogeneous IoT testbed across 15 attack scenarios demonstrate that AC-MADQN achieves a 47.8% reduction in false positives, a 58.3% improvement in threat-mitigation effectiveness, and 99.7% privacy preservation under ε = 0.01 differential privacy, maintaining sub-second latency even with 40% Byzantine node compromise. The framework’s theoretical analysis confirms formal convergence guarantees and logarithmic communication-complexity O(N log T) improvement compared to existing federated RL methods. These results establish AC-MADQN as a scalable, resilient, and practical solution for autonomous IoT security deployments demanding both high performance and strict privacy protection. © 2026 The Authors.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2884.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
