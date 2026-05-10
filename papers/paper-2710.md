---
id: paper-2710
title: 'Machine Learning-Driven Edge Caching for Industry 5.0: A Survey of Collaborative and Inference-Enabled Techniques'
authors:
- Maiti, Ritabrata
- Madhukumar, As
- Hui Ernest, Tan Zheng
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2026
doi: 10.1109/OJCOMS.2026.3669379
url: https://www.scopus.com/pages/publications/105033589480?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2464--2503
keywords:
- age of information
- deep learning
- edge caching
- Industrial Internet of Things
- machine learning
- multi-access edge computing
- reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2710 — Machine Learning-Driven Edge Caching for Industry 5.0: A Survey of Collaborative and Inference-Enabled Techniques

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Industry 5.0 is transforming edge caching from a passive traffic offloading mechanism into an active enabler of distributed intelligence and real-time analytics. However, conventional caching strategies lack the collaborative adaptability, inference-awareness, and domain-specific customization required for dynamic Industry 5.0 workloads. This survey provides a comprehensive and systematic review of machine learning (ML)-driven edge caching organized around two fundamental pillars: collaborative caching (distributed, federated, and multi-agent reinforcement learning paradigms) and inference-enabled caching (content and model placement accelerating real-time edge analytics). We systematically examine how traditional ML, deep learning (DL), deep reinforcement learning (DRL), and multi-agent RL (MARL) techniques address domain-specific challenges across five Industry 5.0 applications: robotics, manufacturing, logistics, immersive training, and healthcare. For each domain, we provide comparative assessments based on latency requirements, scalability targets, and collaboration needs. Our analysis reveals fundamental tradeoffs: MARL excels for distributed coordination with promising efficiency gains but requires higher computational resources, while DRL balances adaptation and complexity, and federated learning enables privacy-preserving collaboration across multiple sites. Each application section concludes with Key Insights synthesizing technique suitability, domain requirements, performance gains, and unresolved challenges. We identify five critical research directions: Bayesian optimization for sample-efficient learning, federated workflow-aware caching with sub-second staleness, resilient caching under intermittent connectivity, scalable multi-modal caching with low latency, and mission-critical prioritization meeting industry standards. This work provides a roadmap for designing adaptive, safe, and scalable ML-driven edge caching systems for intelligent industrial operations. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2710.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
