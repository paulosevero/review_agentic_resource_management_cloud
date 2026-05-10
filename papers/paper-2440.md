---
id: paper-2440
title: Intelligent Task Offloading and Resource Allocation in Knowledge Defined Edge Computing Networks
authors:
- Zhang, Chuangchuang
- He, Qiang
- Li, Fuliang
- Yu, Keping
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2024.3522253
url: https://www.scopus.com/pages/publications/105002326426?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4312--4325
keywords:
- Edge computing
- knowledge defined networking
- resource allocation
- task offloading
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

# paper-2440 — Intelligent Task Offloading and Resource Allocation in Knowledge Defined Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As an emerging architecture, edge computing enables resource limited terminal devices to offload their computation tasks to edge servers in the vicinity, to efficiently reduce delay and energy consumption. However, the continuous expansion of network scale and rapid growth of network traffic in recent years have brought huge challenges to task offloading and resource allocation. To tackle the challenges, by integrating Knowledge Defined Networking (KDN) and edge computing technologies, we design a novel Knowledge defined Edge Computing (KEC) architecture, to achieve intelligent resource allocation and task offloading in dynamic large-scale edge computing networks. We formulate the task offloading and resource allocation optimization problem, to minimize delay and energy consumption, by considering resource requirements and controller deployment. To solve it, we present an intelligent Resource Allocation based Task Offloading (TORA) mechanism, where a Multi-Agent SD3 based resource allocation (MASD3) algorithm is devised to perform efficient resource allocation. To adapt to the rapid expansion of network scale, we design a resource Allocation based Controller Deployment and task offloading Decision (DACD) algorithm, to perform the optimal controller deployment and task offloading. Extensive simulation experiments demonstrate the effectiveness and efficiency of our proposed solution, and TORA mechanism outperforms comparison mechanisms on delay and energy consumption.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2440.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
