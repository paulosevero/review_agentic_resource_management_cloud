---
id: paper-0880
title: 'Computation Offloading with Privacy-Preserving in Multi-Access Edge Computing: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Dai, Xiang
- Luo, Zhongqiang
- Zhang, Wei
venue: Electronics (Switzerland)
venue_type: journal
year: 2024
doi: 10.3390/electronics13132655
url: https://www.scopus.com/pages/publications/85198345519?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- computation offloading
- deep reinforcement learning
- multi-access edge computing
- privacy-preserving
- quality of service
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

# paper-0880 — Computation Offloading with Privacy-Preserving in Multi-Access Edge Computing: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid development of mobile communication technologies and Internet of Things (IoT) devices has introduced new challenges for multi-access edge computing (MEC). A key issue is how to efficiently manage MEC resources and determine the optimal offloading strategy between edge servers and user devices, while also protecting user privacy and thereby improving the Quality of Service (QoS). To address this issue, this paper investigates a privacy-preserving computation offloading scheme, designed to maximize QoS by comprehensively considering privacy protection, delay, energy consumption, and the task discard rate of user devices. We first formalize the privacy issue by introducing the concept of privacy entropy. Then, based on quantified indicators, a multi-objective optimization problem is established. To find an optimal solution to this problem, this paper proposes a computation offloading algorithm based on the Twin delayed deep deterministic policy gradient (TD3-SN-PER), which integrates clipped double-Q learning, prioritized experience replay, and state normalization techniques. Finally, the proposed method is evaluated through simulation analysis. The experimental results demonstrate that our approach can effectively balance multiple performance metrics to achieve optimal QoS. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0880.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
