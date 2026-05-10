---
id: paper-0481
title: 'EdgeML: Towards network-accelerated federated learning over wireless edge'
authors:
- Pinyoanuntapong, Pinyarash
- Janakaraj, Prabhu
- Balakrishnan, Ravikumar
- Lee, Minwoo
- Chen, Chen
- Wang, Pu
venue: Computer Networks
venue_type: journal
year: 2022
doi: 10.1016/j.comnet.2022.109396
url: https://www.scopus.com/pages/publications/85140294752?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Federated learning
- Multi-agent reinforcement learning
- Multi-hop wireless edge
- Wireless networking
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0481 — EdgeML: Towards network-accelerated federated learning over wireless edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated learning (FL) is a distributed machine learning technology for next-generation AI systems that allows a number of workers, i.e., edge devices, collaboratively learn a shared global model while keeping their data locally to prevent privacy leakage. Enabling FL over wireless multi-hop networks can democratize AI and make it accessible in a cost-effective manner. However, the noisy bandwidth-limited multi-hop wireless connections can lead to delayed and nomadic model updates, which significantly slows down the FL convergence speed. To address such challenges, this paper aims to accelerate FL convergence over wireless edge by optimizing the multi-hop federated networking performance. In particular, the FL convergence optimization problem is formulated as a Markov decision process (MDP). To solve such MDP, multi-agent reinforcement learning (MA-RL) algorithms along with domain-specific action space refining schemes are developed, which online learn the delay-minimum forwarding paths to minimize the model exchange latency between the edge devices (i.e., workers) and the remote server. To validate the proposed solutions, EdgeML is developed and implemented, which is the first experimental framework in the literature for FL over multi-hop wireless edge computing networks. EdgeML allows us to fast prototype, deploy, and evaluate novel FL algorithms along with RL-based system optimization methods in real wireless devices. Moreover, a physical experimental testbed is implemented by customizing the widely adopted Linux wireless routers and ML computing nodes. Such testbed can provide valuable insights into the practical performance of FL in the field. Finally, our experimentation results on the testbed show that the proposed network-accelerated FL system can practically and significantly improve FL convergence speed, compared to the FL system empowered by the production-grade commercially-available wireless networking protocol, BATMAN-Adv. © 2022 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0481.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
