---
id: paper-2888
title: Deep Reinforcement Learning-Based QoE Optimization for Heterogeneous Services in Satellite-Terrestrial Integrated MEC Networks
authors:
- Yin, Fangfang
- Liu, Qihong
- Wu, Mulei
- Liu, Danpu
- Zhang, Yu
- Jin, Libiao
- Li, Shufeng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3683968
url: https://www.scopus.com/pages/publications/105036092051?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- MAPPO
- MEC
- resource allocation
- STIN
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2888 — Deep Reinforcement Learning-Based QoE Optimization for Heterogeneous Services in Satellite-Terrestrial Integrated MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of Internet of Things (IoT) and the diversity of services demand for a more efficient and intelligent resource allocation framework to enhance network performance. To this end, we construct a novel satellite-terrestrial integrated network (STIN) integrating multi-access edge computing (MEC) and millimeter wave (mmWave) technologies to explore the coordination gains of communication, caching, and computing resources from a perspective of joint optimization. To be specific, we first formulate the resource allocation issue of joint user association (UA), bandwidth allocation (BA), coded caching (CC), and computation allocation (CA), with the aim of maximizing the quality of experience (QoE) for heterogeneous services while guaranteeing diversified quality of service (QoS) requirements of user equipments (UEs). An alternating iterative optimization strategy is then developed, where convex optimization is applied to solve the CC and CA subproblems, while a multi-agent proximal policy optimization (MAPPO) algorithm is designed to jointly optimize UA and BA subproblem. Finally, extensive simulations demonstrate that our proposed algorithm achieves superior QoE performance compared to existing three benchmark algorithms. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2888.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
