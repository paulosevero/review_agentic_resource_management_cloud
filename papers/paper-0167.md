---
id: paper-0167
title: Resource trading in blockchain-based industrial internet of things
authors:
- Yao, Haipeng
- Mai, Tianle
- Wang, Jingjing
- Ji, Zhe
- Jiang, Chunxiao
- Qian, Yi
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2019
doi: 10.1109/TII.2019.2902563
url: https://www.scopus.com/pages/publications/85067355735?origin=resultslist
publisher: IEEE Computer Society
pages: 3602--3609
keywords:
- Blockchain
- cloud mining
- industrial Internet of Things (IIoT)
- multiagent reinforcement learning
- Stackelberg game
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0167 — Resource trading in blockchain-based industrial internet of things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Past few years have witnessed the compelling applications of the blockchain technique in our daily life ranging from the financial market to health care. Considering the integration of the blockchain technique and the industrial Internet of Things (IoT), blockchain may act as a distributed ledger for beneficially establishing a decentralized autonomous trading platform for industrial IoT (IIoT) networks. However, the power and computation constraints prevent IoT devices from directly participating in this proof-of-work process. As a remedy, in this treatise, the cloud computing service is introduced into the blockchain platform for the sake of assisting to offload computational task from the IIoT network itself. In addition, we study the resource management and pricing problem between the cloud provider and miners. More explicitly, we model the interaction between the cloud provider and miners as a Stackelberg game, where the leader, i.e., cloud provider, makes the price first, and then miners act as the followers. Moreover, in order to find the Nash equilibrium of the proposed Stackelberg game, a multiagent reinforcement learning algorithm is conceived for searching the near-optimal policy. Finally, extensive simulations are conducted to evaluate our proposed algorithm in comparison to some state-of-the-art schemes. © 2005-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0167.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
