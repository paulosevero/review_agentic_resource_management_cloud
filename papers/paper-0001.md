---
id: paper-0001
title: Data caching and selection in 5G networks using F2F communication
authors:
- Al Ridhawi, Ismaeel
- Mostafa, Nour
- Kotb, Yehia
- Aloqaily, Moayad
- Abualhaol, Ibrahim
venue: IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC
venue_type: conference
year: 2017
doi: 10.1109/PIMRC.2017.8292681
url: https://www.scopus.com/pages/publications/85045265807?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1--6
keywords:
- 5G
- Big data
- Cloud
- E2e delay
- F2C
- F2F
- Fog
- Workflow-net
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0001 — Data caching and selection in 5G networks using F2F communication

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As an emergent technology the IoT promises to harness the computational and data resources distributed across different remote clouds. Fog computing extends cloud computing by bringing the network and cloud resources closer to the network edge. As the number of resources contributing to the cloud/fog system grows, so the problems associated with efficient and effective resource selection and allocation. In this paper, we introduce a fog-to-fog (F2F) data caching and selection method, which allows IoT devices to retrieve data in a faster and more efficient way. The proposed solution is based on a data caching and selection strategy using a multi-agent cooperation framework. Caching is achieved by decomposing cloud data into a set of files and then placed into fog storage sites. The selection process is based on a run-time file location prediction technique, which collects and maintains a repository of fog data in the form of log files. When data needs to be retrieved, prediction is made with the aid of these logs and previous successful search queries resulting in realistic run-time location estimates as well as best fog selection. Simulation results showcase the reduced data retrieval latency that enable tactile Internet in 5G. Additionally, results show increased successful file hit ratio leading to a reduced number of repeated downloads. © 2017 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0001.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
