---
id: paper-0542
title: Multiagent RL Aided Task Offloading and Resource Management in Wi-Fi 6 and 5G Coexisting Industrial Wireless Environment
authors:
- Zhou, Fanqin
- Feng, Lei
- Kadoch, Michel
- Yu, Peng
- Li, Wenjing
- Wang, Zhili
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2022
doi: 10.1109/TII.2021.3106973
url: https://www.scopus.com/pages/publications/85113882902?origin=resultslist
publisher: IEEE Computer Society
pages: 2923--2933
keywords:
- Industrial Internet of Things (IoT)
- mobile edge computing (MEC)
- multiagent learning
- resource management
- task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0542 — Multiagent RL Aided Task Offloading and Resource Management in Wi-Fi 6 and 5G Coexisting Industrial Wireless Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of industrial Internet of Things (IIoT), intensive computation workload will be imposed to industrial end units (IEUs). By leveraging mobile edge computing (MEC), the local computational tasks can be offloaded to servers deployed in mobile edge networks with low latency. This article proposes the intelligent cost-and-energy-effective task offloading in the 5G and Wi-Fi 6 coexisting heterogeneous IIoT networks. The novel joint task scheduling and resource allocation approach comprises the following two parts: a Lyapunov optimization-based component to decide local task scheduling and computing power and an online multiagent reinforcement learning component together with a game theory-based algorithm to select offloading link and decide transmit power, respectively. Simulation results demonstrate the proposed approach holds obvious advantage over the compared 'intuition' and 'cost optimal' approaches in the efficiency of making comprehensive decision that improves energy efficiency and cost while controlling task delay in the multi-IEU and multiaccess-node MEC systems.  © 2005-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0542.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
