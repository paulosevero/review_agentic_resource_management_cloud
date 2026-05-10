---
id: paper-2432
title: 'Energy-efficient blockchain-IIoT with mobile edge computing: optimizing resource allocation and multi-hop offloading'
authors:
- Zhang, Yiyi
- Xue, Xueyue
- Lin, Xianfu
- Wei, Wenchang
- Su, Zhicheng
venue: Results in Engineering
venue_type: journal
year: 2025
doi: 10.1016/j.rineng.2025.105379
url: https://www.scopus.com/pages/publications/105005520645?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Blockchain
- Industrial Internet of Things (IIoT)
- Mobile Edge Computing (MEC)
- Multi-agent deep reinforcement learning
- Multi-hop computation offloading
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

# paper-2432 — Energy-efficient blockchain-IIoT with mobile edge computing: optimizing resource allocation and multi-hop offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Blockchain and Mobile Edge Computing (MEC), both of which are edge computing paradigms characterized by strong security attributes, have become a research focus in the Industrial Internet of Things (IIoT) domain. However, current studies generally overlook the persistent energy consumption burden caused by the computational and mobile communication components required for these architectures, which further intensifies the energy supply constraints faced by IIoT devices. To this end, this article proposes an energy-efficient blockchain-enabled IIoT integrated with MEC to optimize resource allocation and multi-hop task offloading. Firstly, an innovative Modular Industrial Internet of Things Device (MIITD) is designed to reduce sustaining energy consumption by dynamically disabling non-essential computational and communication modules during multi-hop offloading. Secondly, a blockchain-MEC architecture is structured to incorporate multiple system-level variables, including multi-aggregation MIITDs deployment, offloading strategies, block size, and wireless link weights. Thirdly, a joint optimization framework is developed to prolong system lifetime, minimize packet loss, and manage computational overhead. Finally, a Multi-Agent Hybrid Trust Region Policy Optimization (MAHTRPO) algorithm is proposed to optimally solve the formulated problem. Experimental and simulation results validate that the proposed scheme substantially enhances system endurance and ensures low data packet loss rates in MIITD scaling scenarios. © 2025 The Author(s)

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2432.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
