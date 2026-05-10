---
id: paper-1640
title: QoE-Driven Proactive Caching With DRL in Sustainable Cloud-to-Edge Continuum
authors:
- He, Xiaoming
- Jiang, Yunzhe
- Cui, Huajun
- Liu, Yinqiu
- Chen, Mingkai
- Guizani, Maher
- Mumtaz, Shahid
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3577197
url: https://www.scopus.com/pages/publications/105007600512?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10992--11004
keywords:
- deep reinforcement learning
- proactive edge caching
- QoE
- sustainable multi-agent learning
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

# paper-1640 — QoE-Driven Proactive Caching With DRL in Sustainable Cloud-to-Edge Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-assisted edge computing scenarios can intelligently cache and update the content periodically, thereby enhancing users’ overall perception of service, which is called quality of experience (QoE). To maximize QoE in cloud-to-edge continuum, we formulate a multi-objective optimization problem, which optimizes the cache hit ratio while simultaneously minimizing traffic load and time latency. Particularly, we present an innovative algorithm named Hyperdimensional Transformer with Priority Experience Playback-based Agent Deep network (HT-PAD), which provides a complete solution for prediction and decision-making for proactive caching. First, to improve the prediction accuracy of cached content, we use the encoding layer in hyperdimensional (HD) computing to extract the information features. Second, HD-Transformer, as the prediction part of HT-PAD, is proposed to make predictions based on user preferences, historical information, and popular information. HD-Transformer uses deep neural networks to predict user preferences and process time series data by combining hyperdimensional computation with the Transformer. Third, to avoid errors in the prediction content, we employ PER-MADDPG as the decision-making part of HT-PAD, which consists of Multi-Agent Deep Deterministic Policy Gradient (MADDPG) and Prioritized Experience Replay (PER). We use MADDPG to improve content decision-making and utilize PER to select appropriate training samples for PER-MADDPG. Finally, our experiments show that our proposed approach achieves strong performance in terms of edge hit ratio, latency, and traffic load, thus improving QoE. © 2002-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1640.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
