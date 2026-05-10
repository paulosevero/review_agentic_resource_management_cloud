---
id: paper-2285
title: A Deep Reinforcement Learning–Based Low Earth Orbit Satellite-Enhanced Mobile Edge Computing Framework for Efficient Task Off-Loading
authors:
- Wei, Erlong
- Wen, Yihong
- Liu, Xuebo
venue: IET Signal Processing
venue_type: journal
year: 2025
doi: 10.1049/sil2/9674618
url: https://www.scopus.com/pages/publications/105015567858?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- cloud-edge collaboration
- low earth orbit satellite network
- mobile edge computing
- multiagent deep reinforcement learning
- resources allocation
- task off-loading
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

# paper-2285 — A Deep Reinforcement Learning–Based Low Earth Orbit Satellite-Enhanced Mobile Edge Computing Framework for Efficient Task Off-Loading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of the Internet of Things (IoTs) and 6G technologies, traditional terrestrial networks are becoming less capable of supporting demanding computational tasks. This limitation stems from their restricted coverage and poor adaptability to changing environmental conditions. Low earth orbit (LEO) satellite networks offer global coverage. However, existing mobile edge computing (MEC) frameworks struggle with unstable links, high decision complexity, and limited real-time performance. To overcome these challenges, this paper proposes a LEO satellite-enhanced MEC off-loading architecture based on improved multiagent deep reinforcement learning (MADRL). By integrating ground terminals, LEO satellite edge servers, cloud servers into a three-tier collaborative system, and introducing an independent Q-value mechanism, the proposed method jointly optimizes task off-loading and resource allocation in dynamic environments. This design reduces algorithm complexity and enhances decision flexibility. Experimental results show that the proposed method outperforms baseline approaches in end-to-end latency, energy efficiency, and convergence speed, while maintaining robust performance under varying satellite densities and user workloads. These results demonstrate the potential of the proposed approach for efficient task off-loading in dynamic 6G scenarios. Copyright © 2025 Erlong Wei et al. IET Signal Processing published by John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2285.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
