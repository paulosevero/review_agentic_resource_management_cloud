---
id: paper-2718
title: 'Deep learning approaches for computation offloading in edge computing: A critical review'
authors:
- Miriyala, Sapthagiri
- Chirra, Venkata Ramireddy
venue: Telecommunication Systems
venue_type: journal
year: 2026
doi: 10.1007/s11235-026-01426-y
url: https://www.scopus.com/pages/publications/105031168569?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Computation Offloading
- Deep Reinforcement Learning
- Federated Learning
- IoT
- Multi-Access Edge Computing
- Resource Allocation
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
    my_justification: Review + DL
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

# paper-2718 — Deep learning approaches for computation offloading in edge computing: A critical review

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The paradigm shift from centralized cloud computing to Multi-Access Edge Computing (MEC) has been necessitated by the exponential growth of the Internet of Things (IoT) and the stringent latency requirements of 5G/6G applications. However, the inherent dynamism of edge environments, characterized by fluctuating channel conditions, heterogeneous device capabilities, and finite energy budgets, renders traditional static optimization techniques insufficient. This survey provides a critical review of Deep Learning (DL) and Deep Reinforcement Learning (DRL) as pivotal enablers for autonomous computation offloading. This work systematically dissects the algorithmic trade-offs between Value-Based (e.g., DQN) and Policy-Gradient (e.g., PPO, SAC, A3C) architectures, evaluating their suitability for continuous control, multi-agent coordination, and resource-constrained inference. We further bridge the gap between theoretical algorithms and practical telecommunications deployment by mapping DRL strategies to European Telecommunications Standards Institute (ETSI) MEC specifications and Open Radio Access Network (O-RAN) architectural standards. The review analyzes the "optimization trade-offs" inherent in offloading, specifically the conflict between service immediacy (latency) and resource conservation (energy/security). Finally, we synthesize key challenges hindering large-scale adoption, including the need for lightweight "extreme edge" models, robustness against non-stationary environments, and privacy-preserving federated learning, thereby providing a rigorous roadmap for the evolution of self-optimizing, intelligent edge ecosystems. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2026.

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
- **my_justification:** "Review + DL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2718.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
