---
id: paper-2567
title: A Multi-Agent Soft Actor-Critic Framework to Minimize Age of Information in UAV-Assisted Networks
authors:
- Fan, Tingshan
- Wang, Cong
- Yin, Yujie
- Yuan, Ying
- Li, Guorui
venue: IET Communications
venue_type: journal
year: 2026
doi: 10.1049/cmu2.70146
url: https://www.scopus.com/pages/publications/105032829476?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- internet of Things
- mobile computing
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

# paper-2567 — A Multi-Agent Soft Actor-Critic Framework to Minimize Age of Information in UAV-Assisted Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of artificial intelligence (AI) and the Internet of Things (IoT) has given rise to AIoT systems. However, the accelerated proliferation of AIoT ecosystems introduces substantial communication and networking difficulties. Mobile edge computing (MEC) has emerged as a promising solution to address time-sensitive computational demands. This paper addresses the improvement of information freshness, a critical enabler for real-time decision-making in dynamic, resource-constrained AIoT environments. We formulate the UAV-assisted MEC system as a Markov decision process with the objective of minimizing the age of information (AoI). To this end, we propose an adaptive federated multi-agent soft actor-critic framework for resource scheduling. This framework leverages maximum entropy to enable robust exploration and incorporates an innovative adaptive federated learning mechanism by adopting a trainable network to predict the parameter matrix of federated learning. This enables federated learning to better promote knowledge sharing among multiple agents, thereby accelerating convergence and improving performance. Experimental results validate that our approach significantly outperforms state-of-the-art reinforcement learning based algorithms in AoI minimization, stability enhancement, and task completion volume improvement, thereby advancing the safeguarding of communication and networking in AIoT systems. © 2026 The Author(s). IET Communications published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2567.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
