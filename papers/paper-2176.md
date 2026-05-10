---
id: paper-2176
title: Dependency-Aware Task Offloading and Resource Allocation for Maritime Ultrareliable Applications
authors:
- Su, Xin
- Fang, Xin
- Lu, Liyang
- Wang, Zhaocheng
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TCCN.2024.3508784
url: https://www.scopus.com/pages/publications/85210919373?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2618--2631
keywords:
- Maritime multi-access edge computing
- maritime networks
- maritime ultrareliable applications
- multi-agent learning
- resource allocation
- task offloading
- ultrareliable applications
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

# paper-2176 — Dependency-Aware Task Offloading and Resource Allocation for Maritime Ultrareliable Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Compared to terrestrial networks, maritime networks lack centralized infrastructure, and tasks within maritime ultrareliable applications are interdependent, complicating task offloading and resource allocation. Additionally, in the public area of maritime networks, task offloading processes are vulnerable to malicious attacks. To ensure real-time and reliable performance while mitigating the risks of miscalculations, this paper proposes a multi-agent deep reinforcement learning algorithm for task offloading. The proposed algorithm features a real-time alerting mechanism and reliability constraints, focusing on minimizing system costs, including latency and energy consumption. Maritime applications are modeled as directed acyclic graphs, and the offloading problem is framed as a decentralized Markov decision process. We have developed an enhanced actor-critic architecture by transforming conventional fully connected networks into tailored parallel sequence-to-sequence networks, which improves task feature extraction. This approach allows the system to adapt more effectively to the dynamic challenges of marine environments. Experimental results show that the proposed algorithm outperforms existing solutions, demonstrating significant improvements in task offloading and resource allocation for interdependent tasks. © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2176.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
