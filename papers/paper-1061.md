---
id: paper-1061
title: Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing
authors:
- Liu, Guoqiang
- Xu, Xiaolong
- Xu, Xiyuan
- Ji, Xinyue
- Qi, Lianyong
- Zhang, Xuyun
venue: Proceedings of the IEEE International Conference on Web Services, ICWS
venue_type: conference
year: 2024
doi: 10.1109/ICWS62655.2024.00127
url: https://www.scopus.com/pages/publications/85210226564?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1089--1096
keywords:
- Collaborative Service Placement
- Edge Computing
- Latency-Sensitive
- Leader-Follower Architecture
- MARL
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1061 — Optimized MARL for Latency-Sensitive Collaborative Service Placement in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> By distributing computing and storage resources to edge servers (ESs), edge computing enables service execution closer to requests, alleviating high latency caused by long-distance data transmission. The communication between ESs facilitates collaborative service placement (CSP) on multiple ESs, leading to latency reduction and thereby improving the quality of service. However, the discrepancies in service request distributions among ESs pose challenge to effective CSP, while limited prior knowledge further increases the difficulty in policy formation. Additionally, the delayed awareness of placement strategies among other ESs exacerbates the influence of non-Markovian nature. To overcome above challenges, a leader-follower based multi-agent reinforcement learning for CSP scheme, named LFMCSP, is proposed in this paper. Specifically, a CSP model is formulated, with ESs abstracted as intelligent agents within it. Then, the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm is utilized to explore potential patterns in complex requests by experience sharing. To achieve transparency of global states for all agents, the leader-follower architecture is integrated into MADDPG. Through rigorous experiments and comparisons with various baseline schemes, LFMCSP demonstrates effectiveness in reducing service execution delays.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1061.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
