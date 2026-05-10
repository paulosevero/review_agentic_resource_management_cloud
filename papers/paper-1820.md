---
id: paper-1820
title: Resilient Cooperative Computing for Satellite Mobile Edge Computing Using Multi-agent DRL
authors:
- Li, Yafei
- Wang, Huiqiang
- Feng, Guangsheng
- Zheng, Wenqi
- Lv, Hongwu
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-8731-2_8
url: https://www.scopus.com/pages/publications/105010141525?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 75--85
keywords:
- Inter-Satellite Cooperative Computing
- Multi-Agent Deep Reinforcement Learning
- Satellite Mobile Edge Computing
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

# paper-1820 — Resilient Cooperative Computing for Satellite Mobile Edge Computing Using Multi-agent DRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Inter-satellite cooperative computing empowers satellite edge computing to transcend the limitations of constrained onboard computing power, ushering in a new paradigm for in-orbit computation. However, within the large-scale LEO space environment characterized by abrupt failures, dynamic topologies and constrained resources, inter-satellite cooperative computing faces threats of reduced reliability and inefficiency. In this paper, we delve into the joint optimization of resilient computing networking, computation offloading, and resource allocation, with the goal of maximizing the quality of service for computing requests. Specifically, we propose a novel resilient inter-satellite computing collaboration architecture that enhances the reliability and serviceability of inter-satellite computing in unstable network space environments. Furthermore, we develop a trust-region-based multi-agent deep reinforcement learning algorithm to efficiently enable autonomous collaborative computation among satellites in a large-scale LEO space environment in a distributed manner. Finally, the effectiveness and superiority of our approach are validated through extensive simulation experiments. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1820.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
