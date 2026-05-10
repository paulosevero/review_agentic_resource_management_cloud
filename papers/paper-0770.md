---
id: paper-0770
title: 'Trusted Collaboration for MEC-Enabled VR Video Streaming: A Multi-Agent Reinforcement Learning Approach'
authors:
- Xu, Yueqiang
- Zhang, Heli
- Li, Xi
- Yu, F. Richard
- Leung, Victor C.M.
- Ji, Hong
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2023.3267181
url: https://www.scopus.com/pages/publications/85153518415?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12167--12180
keywords:
- edge collaboration
- multi-agent DDPG
- Trust evaluation
- wireless virtual reality
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0770 — Trusted Collaboration for MEC-Enabled VR Video Streaming: A Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Collaboration among mobile edge computing (MEC) has been envisioned as a promising paradigm to meet the requirements of wireless virtual reality (VR) applications. However, trust risks create tremendous challenges in MEC collaboration due to the distributed, complex, and unreliable nature of resource providers. In this paper, we present a trusted collaboration framework for VR video streaming to manage the video buffer in VR devices (VDs) under a more realistic distributed environment. In the framework, the rendering tasks can be processed collaboratively among edge servers (ESs) by exploring their behaviors (e.g., selfish behavior, malicious behavior, and cooperative behavior). Considering the collaborator may not be fully trustworthy, we present a novel trust evaluation method by combining direct and indirect values, aiming to ensure reliable collaborator selection. Then, we formulate an optimization problem to maintain an effective buffer state in VR devices (VDs) through jointly optimizing collaborator selection, spectrum allocation, and rendering resource allocation. Due to the fluctuating wireless fading channel and the dynamic video rate, the optimization problem is intractable by adopting traditional methods. Then, we adopt the multi-agent deep deterministic policy gradient (MADDPG) to tackle this dynamic and distributed problem. Simulation results indicate that the proposed approach can achieve a good performance. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0770.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
