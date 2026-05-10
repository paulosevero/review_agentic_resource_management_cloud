---
id: paper-0379
title: Crypto-Deep Reinforcement Learning Based Cloud Security For Trusted Communication
authors:
- Abirami, P.
- Bhanu, S. Vijay
- Thivakaran, T.K.
venue: Proceedings - 4th International Conference on Smart Systems and Inventive Technology, ICSSIT 2022
venue_type: conference
year: 2022
doi: 10.1109/ICSSIT53264.2022.9716429
url: https://www.scopus.com/pages/publications/85127324420?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- cloud security
- linear classification
- machine learning algorithm
- Multi Agent Deep reinforcement Learning Multi Agent Deep Reinforcement Learning(MADRL)
- Side-channel attack
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

# paper-0379 — Crypto-Deep Reinforcement Learning Based Cloud Security For Trusted Communication

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> One of the most essentialbusiness models in modern information technology is cloud computing. It offers a variety of services for user interaction as well as low-cost hardware and software. Cloud services are built on newline virtualization designs that use multi-tenancy for improved resource management and newline strong isolation across several Virtual Machines (VMs). Despite advancements in virtualization, data security and isolation assurances continue to be the major difficulties faced by cloud providers using existing approaches. To overcome this problem, Deep Reinforcement Learning is applied to offload the task and also to detect the generalized attackers in the cloud network. This proposed solution enables remote data monitoring approaches such as identity-based linear classification algorithms for VM attack classification channels. It can minimise data secrecy and increase communication by using a reinforcement learning technique. The attacker channel is identified using identity-based linear classification when data is transferred/retrieved from the VM cloud server. When the classifier finds channel misbehaviour, the port or channel may be blocked, and the communication of other accessible ports may be modified maintaining the end to end communication secrecy using the improved Multi Agent Deep Reinforcement Learning(MADRL). The service verification is done to ensure that users have secure access to the cloud server. When an unknown request to the cloud server runs the key authentication to check the user authorization, this linear classification trains the existing side-channel attack datasets to the classifier and detects the VM cloud's attack channel. In terms of overall performance, the proposed methodology is investigated and compared to the existing approaches. © 2022 IEEE

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0379.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
