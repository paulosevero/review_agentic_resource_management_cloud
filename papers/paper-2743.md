---
id: paper-2743
title: 'DRUDM-CFG: a Fairness-Aware Multi-Agent DRL Algorithm for AMEC-Assisted Task Offloading in Post-Disaster Scenarios'
authors:
- Peng, Xiting
- Qin, Chuanqi
- Zhang, Xiaoyu
- Xu, Lexi
- Zhang, Xiaoling
- Jiang, Li
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3676811
url: https://www.scopus.com/pages/publications/105034518411?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- aerial Multiaccess edge computing (AMEC)
- coverage fairness Guarantee(CFG)
- high-altitude airship (HAS)
- Task offloading
- unmanned aerial vehicles (UAVs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2743 — DRUDM-CFG: a Fairness-Aware Multi-Agent DRL Algorithm for AMEC-Assisted Task Offloading in Post-Disaster Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> High-altitude airships (HAS) and unmanned aerial vehicles (UAVs) equipped with Multiaccess Edge Computing (MEC) servers have emerged as promising aerial MEC nodes for providing task offloading (TO) services to intelligent mobile devices (IMDs) in post-disaster scenarios. HAS offers robust computing and energy resources, while UAVs provide flexible, low-altitude coverage for rapid deployment. However, direct task offloading from IMDs to HAS often leads to task failures due to high transmission delays. UAVs with limited onboard resources require to minimize resource waste. Additionally, IMDs in sparse areas face insufficient TO services due to unfair UAV coverage. This paper defines these challenges as a joint optimization problem involving TO, RA, and UAV coverage fairness. It proposes a cooperative aerial Multiaccess Edge Computing (AMEC) framework integrating HAS and UAVs to address the issue. Within this framework, a hybrid TO scheme is first developed to mitigate the high transmission delay between IMDs and HAS. Second, a Distance, Resource, Urgency-based Decision Mechanism (DRUDM) is designed to enhance the accuracy of UAVs in selecting target IMDs for TO services. Third, a Coverage Fairness Guarantee (CFG) strategy is proposed to optimize UAV flight trajectories, ensuring IMDs in sparse areas receive fair TO services. Finally, the joint optimization problem is modeled as a Multi-Agent Partially Observable Markov Decision Process (MA-POMDP), and a DRUDM–CFG algorithm is presented to efficiently solve this complex non convex optimization problem. Experimental results demonstrate that the proposed algorithm outperforms other compared algorithms in task completion rate and average delay, benefiting from the DRUDM mechanism. Meanwhile, the CFG strategy effectively improves TO service fairness for IMDs in sparse areas. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2743.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
