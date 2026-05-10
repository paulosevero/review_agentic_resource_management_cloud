---
id: paper-1400
title: Hybrid deep reinforcement learning and genetic algorithm-based resource allocation framework for edge computing
authors:
- Arun, V.
- Azhagiri, M.
venue: Peer-to-Peer Networking and Applications
venue_type: journal
year: 2025
doi: 10.1007/s12083-025-02149-8
url: https://www.scopus.com/pages/publications/105020678694?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Deep reinforcement learning
- Internet of things
- Mobile edge computing
- Multi-agent reinforcement learning
- Resource allocation
- Resource management
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

# paper-1400 — Hybrid deep reinforcement learning and genetic algorithm-based resource allocation framework for edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> High-performance computing is in great demand in resource-constrained environments (e.g., Mobile Edge Computing (MEC) and Internet of Things (IoT) systems), making it necessary to have effective resource allocation strategies. In this paper, we propose a kind of elite approach that can combine Multi-Agent Reinforcement Learning (MRL) and Deep Reinforcement Learning (DRL) to optimize task offloading as well as resource management in MEC environments. Existing approaches suffer from non-negligible computational latency, inefficient energy consumption, and limited resource utilization under varying network and computation loads. Our methodology for confronting these challenges combines an adaptive resource allocation mechanism, which dynamically balances network bandwidth and CPU resource allocations according to task requirements in real-time. The proposed method is evaluated across several key metrics, including convergence performance, computation latency, energy consumption, and resource utilization rates. Experimental results show significant improvements over state-of-the-art methods. The proposed approach achieves a convergence performance of 1.00 at 250 iterations, which is superior to DRL (0.97), MRL (0.90). The proposed method achieves 0.068 s, outperforms the DRL (0.083 ms) and MRL (0.165 ms) in terms of computation latency, with an input size is 0.2 Mbits. The energy consumption is also reduced, where 0.038 Joules for 0.2 Mbits have been consumed in the proposed method; this value is much smaller compared to DRL (0.044 Joules) and CERAI (0.132 Joules). These results show that the proposed method is superior in a balanced performance, energy efficiency, and resource utilization perspective for MEC dense areas with limited resources. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1400.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
