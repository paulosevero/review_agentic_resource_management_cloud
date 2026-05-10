---
id: paper-2455
title: 'Secure Data Offloading and Resource Allocation Against Hybrid Intrusions for IIoT: A Fully Decentralized Framework'
authors:
- Zhang, Fan
- Han, Guangjie
- Liu, Li
- Jiang, Jinfang
- Li, Aohan
- Zhu, Shengchao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3506595
url: https://www.scopus.com/pages/publications/105001583693?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9218--9237
keywords:
- Fully decentralized multiagent deep reinforcement learning (DRL)
- Industrial Internet of Things (IIoT)
- Lagrange coded computing (LCC)
- resource allocation
- secure data offloading
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

# paper-2455 — Secure Data Offloading and Resource Allocation Against Hybrid Intrusions for IIoT: A Fully Decentralized Framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing is fundamental to filling the various quality-of-service needs for Industrial Internet of Things (IIoT) applications. However, introducing edge computing to IIoT inevitably results in hybrid intrusion problems and fails to satisfy the security demands of IIoT. Fortunately, Lagrange coded computing has emerged as a low-complexity and low-overhead solution for resisting hybrid intrusions during data offloading and processing. However, how to make decentralized, accurate, and real-time encoding/offloading/decoding decisions remains challenging. This article designs a fully decentralized training and decision-making framework to address the joint secure data offloading and resource allocation problem against hybrid intrusions for dynamic and uncertain IIoT, attempting to minimize the long-run energy and delay costs while improving the data confidentiality, integrity, and availability. It is proposed a fully decentralized multiagent actor-critic-based secure data offloading (FM-SDO) algorithm to solve the secure data offloading subproblem, wherein each industrial end device utilizes its local information to learn and execute its policy independently. This algorithm improves the structure of actor and critic networks and designs a multiagent alternant updating mechanism to increase learning accuracy, convergence, and stability. Based on the received offloading decisions of each device, each edge server leverages the Lagrange multiplier approach and Karush-Kuhn-Tucker condition to make fast and decentralized resource allocation decisions. Finally, we employed an IIoT intelligent production line platform named iCandyBox to test the performance of the FM-SDO algorithm. Experiment results suggest that the FM-SDO algorithm effectively reduces the total energy and delay costs while increasing the capability of resisting hybrid intrusions.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2455.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
