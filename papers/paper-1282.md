---
id: paper-1282
title: Privacy-preserving offloading scheme in multi-access mobile edge computing based on MADRL
authors:
- Wu, Guowen
- Chen, Xihang
- Gao, Zhengjun
- Zhang, Hong
- Yu, Shui
- Shen, Shigen
venue: Journal of Parallel and Distributed Computing
venue_type: journal
year: 2024
doi: 10.1016/j.jpdc.2023.104775
url: https://www.scopus.com/pages/publications/85173254036?origin=resultslist
publisher: Academic Press Inc.
pages: ''
keywords:
- Computation offloading
- Mobile edge computing
- Multi-agent DRL
- Privacy-preservation
- Resource allocation
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

# paper-1282 — Privacy-preserving offloading scheme in multi-access mobile edge computing based on MADRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of industrialization and intelligence, the Industrial Internet of Things (IIoT) has gradually become the direction for traditional industries to transform into modern ones. In order to adapt to the emergence of a large number of edge access devices such as sensors, as well as the demand for high-consumption and low-latency computing tasks, Mobile Edge Computing (MEC) has been proposed as an effective paradigm by the academic community. Users can offload tasks to MEC servers, greatly reducing the computing latency and energy consumption when using services. However, traditional single access point edge computing networks cannot meet the usage requirements of a large number of users. In addition, the privacy leakage issues arising from the offloading process are also easily overlooked. In this paper, we propose a privacy-preserving offloading scheme based on stochastic game theory considering multiple access points. We first construct a multi-access point offloading framework and quality of service (QoS) model. In terms of privacy, the privacy risks caused by the offloading preferences of different edge nodes are studied, and the privacy entropy is used to evaluate the privacy protection level. We comprehensively consider the energy consumption, latency requirements, user experience, and privacy protection of the system and formulate the problem as a Markov Decision Process (MDP). Finally, a joint optimal DRL algorithm with privacy preservation (JODRL-PP) is proposed to achieve the optimal offloading scheme of the system. Simulation results verify the effectiveness of our model and algorithm. © 2023 Elsevier Inc.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1282.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
