---
id: paper-2450
title: Privacy-Preserving Task Offloading in Vehicular Edge Computing Using Federated Multi-Agent Reinforcement Learning
authors:
- Zhang, Peiying
- Wang, Enqi
- Guizani, Maher
- Liu, Kai
- Wang, Jian
- Tan, Lizhuang
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3588204
url: https://www.scopus.com/pages/publications/105012278347?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19642--19654
keywords:
- federated learning
- multi-agent reinforcement learning
- privacy preservation
- task offloading
- Vehicular edge computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2450 — Privacy-Preserving Task Offloading in Vehicular Edge Computing Using Federated Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) systems face critical challenges in balancing computational efficiency, task delay, and data privacy. This paper presents a Federated Multi-Agent Deep Reinforcement Learning (FMADRL) framework to achieve privacy-preserving task offloading in dynamic vehicular networks. The proposed method leverages federated learning to collaboratively train task offloading policies across vehicles, Mobile Edge Computing (MEC) servers, and the cloud, ensuring that sensitive data remains localized while enabling global optimization. A novel reward function is designed to balance task completion, delay, energy consumption, and privacy constraints, while a federated actor-critic model ensures robust decision-making under dynamic network conditions. Simulation results demonstrate that the FMADRL framework significantly reduces average task delay and energy consumption by 30% and 25%, respectively, compared to traditional methods, while maintaining data privacy. These findings underscore the potential of FMADRL to enhance the scalability, efficiency, and security of VEC systems in intelligent transportation networks. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2450.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
