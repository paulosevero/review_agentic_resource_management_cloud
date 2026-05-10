---
id: paper-1160
title: Optimizing point-of-sale services in MEC enabled near field wireless communications using multi-agent reinforcement learning
authors:
- Rehman, Ateeq Ur
- Maashi, Mashael
- Alsamri, Jamal
- Mahgoub, Hany
- Allafi, Randa
- Dutta, Ashit Kumar
- Khan, Wali Ullah
- Nauman, Ali
venue: Computer Communications
venue_type: journal
year: 2024
doi: 10.1016/j.comcom.2024.107962
url: https://www.scopus.com/pages/publications/85206255011?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Mobile edge computing
- Multi-agent reinforcement learning
- Near field communication
- Resource optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1160 — Optimizing point-of-sale services in MEC enabled near field wireless communications using multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the next-generation communication system, near-field communication (NFC) is a key enabler of contactless transactions, including mobile payments, ticketing, and access control. With the growing demand for contactless solutions, NFC technology will play a pivotal role in enabling secure and convenient payment experiences across various sectors. In contrast, Internet of Things (IoT) devices such as phones’ Point of Sale (PoS) constitute limited battery life and finite computational resources that act as a bottleneck to doing the authentication in a minimal amount of time. Because of this, it garnered considerable attention in both academic and industrial realms. To overcome this, in this work we consider the Multiple Mobile Edge Computing (MEC) as an effective solution that provides extensive computation to PoS connected to it. To address the above, this work considers the PoS-enabled multi-MEC network to guarantee NFC communication reliably and effectively. For this, we formulate the joint optimization problem to maximize the probability of successful authentication while minimizing the queueing delay by jointly optimizing the computation and communication resources by utilizing a multi-agent reinforcement learning optimization approach. Through extensive simulations based on real-world scenarios, the effectiveness of the proposed approach was demonstrated. The results demonstrate that adjusting the complexity and learning rates of the model, coupled with strategic allocation of edge resources, significantly increased authentication success rates. Furthermore, the optimal allocation strategy was found to be crucial in reducing latency and improving authentication success by approximately 9.75%, surpassing other approaches. This study highlights the importance of resource management in optimizing MEC systems, paving the way for advancements in establishing secure, efficient, and dependable systems within the Internet of Things framework. © 2024 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1160.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
