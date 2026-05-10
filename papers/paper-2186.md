---
id: paper-2186
title: Research on Joint Task Offloading and Resource Allocation Strategy for Space-Air-Ground Vehicle Networks
authors:
- Sun, Aijing
- Jin, Simei
- Wu, Pengfei
- Yin, Jiangyao
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2025
doi: 10.1117/12.3094144
url: https://www.scopus.com/pages/publications/105026839917?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- deep reinforcement learning (DRL)
- edge computing
- resource allocation (RA)
- Space-Air-Ground Integrated Vehicular Network (SAGVN)
- task offloading (TO)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2186 — Research on Joint Task Offloading and Resource Allocation Strategy for Space-Air-Ground Vehicle Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing prevalence of delay-sensitive and computation-intensive vehicular applications, traditional vehicular networks struggle to adapt to highly dynamic scenarios due to limitations in ground infrastructure. The Space-Air-Ground Integrated Vehicular Network (SAGVN) provides a novel solution by offering ubiquitous connectivity and abundant computational resources, thereby enhancing vehicular network performance and efficiency. Resource management serves as the core of this system, directly impacting overall performance.To address this challenge, this paper proposes a joint task offloading and resource allocation scheme aimed at minimizing the Overall Response Time (ORT). The main contributions are as follows:1) We construct a SAGVN model that deeply integrates space-based and ground networks, expands vehicular task offloading options, and deploys edge servers to enhance system computational capabilities.2) Based on the diversity of tasks and vehicles, we characterize tasks according to attributes such as data volume and classify them based on vehicles’ offloading preferences.3) We propose an Integrated Sensing and Communication (ISAC)-based Environment-Aware Offloading Mechanism (EAOM) that reduces latency through dynamic offloading strategy selection.Considering vehicle mobility and environmental dynamics, we formulate the optimization problem as a Markov Decision Process (MDP) and solve it using the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm. Simulation results demonstrate that the proposed scheme significantly reduces task processing latency, verifying its effectiveness and superiority. © 2025 SPIE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2186.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
