---
id: paper-0992
title: Reliable information delivery and dynamic link utilization in MANET cloud using deep reinforcement learning
authors:
- Kuang, Shuhong
- Zhang, Jiyong
- Mohajer, Amin
venue: Transactions on Emerging Telecommunications Technologies
venue_type: journal
year: 2024
doi: 10.1002/ett.5028
url: https://www.scopus.com/pages/publications/85203109321?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- Adaptive resource allocations
- Cloud environments
- Dynamic links
- Information delivery
- Information dynamics
- Link utilization
- Mobile ad-hoc networks
- Multi agent
- Network environments
- Reinforcement learnings
- Cloud platforms
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

# paper-0992 — Reliable information delivery and dynamic link utilization in MANET cloud using deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern networking demands efficient and reliable information delivery within Mobile Ad-hoc Network (MANET) and cloud environments. This paper introduces a novel approach that employs Multi-Agent Deep Learning (MADL) for adaptive resource allocation, addressing the challenges of optimizing traffic and ensuring dependable information delivery while adhering to Service Level Agreement (SLA) constraints. Our method dynamically allocates resources across nodes, leveraging the synergy between Advanced Cloud Computing and Edge Computing to balance centralized processing and localized adaptability. The integration of Graph Neural Networks (GNNs) further enhances this process by adapting resource allocation decisions based on network topology. Through iterative learning, our algorithm fine-tunes continuous-time resource optimization policies, resulting in substantial improvements in throughput and latency minimization. Simulations validate the effectiveness of our approach, demonstrating its potential to contribute to the advancement of MANET cloud networks by offering adaptability, efficiency, and real-time optimization for reliable information delivery and dynamic link utilization. © 2024 John Wiley & Sons Ltd.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0992.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
