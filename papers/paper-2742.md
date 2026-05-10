---
id: paper-2742
title: 'CoMARL: A cooperative game and MARL-based intrusion-tolerant scheduling method for microservice in cloud-edge collaborative networks'
authors:
- Pei, Jinchuan
- Hu, Yuxiang
- Yu, Hongtao
- Tian, Le
- Wang, Zihao
- Pei, Xinglong
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2026.108430
url: https://www.scopus.com/pages/publications/105034263596?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cloud-edge collaborative networks
- Cooperative game
- Intrusion-tolerant scheduling
- Microservices
- Multi-agent reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2742 — CoMARL: A cooperative game and MARL-based intrusion-tolerant scheduling method for microservice in cloud-edge collaborative networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AbstractWith the rapid development of cloud-edge collaborative networks, microservice architecture is widely used due to its flexibility and scalability. However, the complex dependencies and attack surface expansion of microservices in the existing cloud-edge collaborative network make it possible for attackers to laterally penetrate through a single vulnerability, thereby threatening the security of the overall system, and the cloud side and the edge side lack an effective coordination mechanism in resource allocation and security protection, and it is difficult to achieve the global optimal defense while ensuring their respective interests. We propose CoMARL, a microservice intrusion tolerance scheduling method based on cooperative game and multi-agent reinforcement learning (MARL) in cloud-edge collaborative networks, aiming to solve the problem of “dynamic security-resource game” of cloud-edge nodes in the dynamic adversarial environment. Firstly, we model the complex characteristics of microservice intrusion tolerance scheduling in cloud-edge collaborative networks with multi-dimensions, and then construct the overall defense architecture of microservice intrusion tolerance. After that, MARL is used to enable multiple agents to learn independently in the complex cloud-edge environment, optimize the intrusion tolerance scheduling method of microservices. In addition, we design a cooperative game based on Nash bargaining to coordinate the interest relationship between the cloud side and the edge side, so that they can jointly maintain the overall benefit of the cloud-edge collaborative network while protecting their own interests. Experimental results show that the proposed method can effectively enhance the intrusion tolerance capability of microservices in cloud-edge collaborative networks, and achieve a better global balance between resource consumption and security protection. © 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2742.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
