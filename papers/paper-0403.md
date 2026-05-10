---
id: paper-0403
title: A Joint Intelligent Optimization Scheme of Computation Offloading and Resource Allocation for MEC; [MEC计算卸载与资源分配联合智能优化方案]
authors:
- Du, Mei
- Zhou, Junhua
- Li, Dunqiao
- Chen, Shizhao
- Wei, Yifei
venue: Beijing Youdian Daxue Xuebao/Journal of Beijing University of Posts and Telecommunications
venue_type: journal
year: 2022
doi: 10.13190/j.jbupt.2021-145
url: https://www.scopus.com/pages/publications/85129508984?origin=resultslist
publisher: Beijing University of Posts and Telecommunications
pages: 65--71
keywords:
- Computation offloading
- Mobile edge computing
- Multi-agent reinforcement learning
- Resource allocation
language: Chinese
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0403 — A Joint Intelligent Optimization Scheme of Computation Offloading and Resource Allocation for MEC; [MEC计算卸载与资源分配联合智能优化方案]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the distributed base station deployment, limited server resources and dynamic end-users in mobile edge computing (MEC), the design of computation offloading scheme is extremely challenging. Since the deep reinforcement learning has advantages in terms of dealing with dynamic complex problems, we design the optimal computation offloading and resource allocation strategies based on deep reinforcement learning to minimize the system energy consumption. First, the network framework of cloud edge-end collaboration is considered. Then, the joint computation offloading and resource allocation problem is defined as a Markov decision process. Next, a multi-agent deep deterministic policy gradient-based learning algorithm is proposed to minimize the system energy consumption. The experimental results show that our proposed scheme significantly reduces the energy consumption compared to the deep deterministic policy gradient-based algorithm and the full offloading policy. © 2022, Editorial Department of Journal of Beijing University of Posts and Telecommunications. All right reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0403.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
