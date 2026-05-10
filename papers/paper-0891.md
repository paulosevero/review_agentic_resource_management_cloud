---
id: paper-0891
title: An Integrated Communication and Computing Scheme for Wi-Fi Networks based on Generative AI and Reinforcement Learning
authors:
- Du, Xinyang
- Fang, Xuming
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901620
url: https://www.scopus.com/pages/publications/105000823002?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2009--2014
keywords:
- computing-communication integration
- generative artificial intelligence
- mobile edge computing
- offloading decision
- reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0891 — An Integrated Communication and Computing Scheme for Wi-Fi Networks based on Generative AI and Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The continuous evolution of future mobile communication systems is heading towards the integration of communication and computing, with Mobile Edge Computing (MEC) emerging as a crucial means of implementing Artificial Intelligence (AI) computation. MEC could enhance the computational performance of wireless edge networks by offloading computing-intensive tasks to MEC servers. However, in edge computing scenarios, the sparse sample problem may lead to high costs of time-consuming model training. This paper proposes an MEC offloading decision and resource allocation solution that combines generative AI and deep reinforcement learning (DRL) for the communication-computing integration scenario in the 802.11ax Wi-Fi network. Initially, the optimal offloading policy is determined by the joint use of the Generative Diffusion Model (GDM) and the Twin Delayed DDPG (TD3) algorithm. Subsequently, resource allocation is accomplished by using the Hungarian algorithm. Simulation results demonstrate that the introduction of Generative AI significantly reduces model training costs, and the proposed solution exhibits significant reductions in system task processing latency and total energy consumption costs. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0891.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
