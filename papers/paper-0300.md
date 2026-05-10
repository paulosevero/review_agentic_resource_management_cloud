---
id: paper-0300
title: Secure mobile edge server placement using multi-agent reinforcement learning
authors:
- Kasi, Mumraiz Khan
- Ghazalah, Sarah Abu
- Akram, Raja Naeem
- Sauveron, Damien
venue: Electronics (Switzerland)
venue_type: journal
year: 2021
doi: 10.3390/electronics10172098
url: https://www.scopus.com/pages/publications/85114426805?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- Edge security
- Mobile edge computing
- Mobile edge server placement
- Multiagent RL
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

# paper-0300 — Secure mobile edge server placement using multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing is capable of providing high data processing capabilities while ensuring low latency constraints of low power wireless networks, such as the industrial internet of things. However, optimally placing edge servers (providing storage and computation services to user equipment) is still a challenge. To optimally place mobile edge servers in a wireless network, such that network latency is minimized and load balancing is performed on edge servers, we propose a multi-agent reinforcement learning (RL) solution to solve a formulated mobile edge server placement problem. The RL agents are designed to learn the dynamics of the environment and adapt a joint action policy resulting in the minimization of network latency and balancing the load on edge servers. To ensure that the action policy adapted by RL agents maximized the overall network performance indicators, we propose the sharing of information, such as the latency experienced from each server and the load of each server to other RL agents in the network. Experiment results are obtained to analyze the effectiveness of the proposed solution. Although the sharing of information makes the proposed solution obtain a network-wide maximation of overall network performance at the same time it makes it susceptible to different kinds of security attacks. To further investigate the security issues arising from the proposed solution, we provide a detailed analysis of the types of security attacks possible and their countermeasures. © 2021 by the authors. Licensee MDPI, Basel, Switzerland.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0300.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
