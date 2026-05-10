---
id: paper-1918
title: Study on Dynamic Principal Component Allocation Strategy for Data in Cloud-Fog Hybrid Management System
authors:
- Luo, Ningzhao
- Huang, Jing
- Chen, Cheng
- Wu, Benxiang
venue: 2025 10th International Conference on Electronic Technology and Information Science, ICETIS 2025
venue_type: conference
year: 2025
doi: 10.1109/ICETIS66286.2025.11143991
url: https://www.scopus.com/pages/publications/105017121416?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 329--334
keywords:
- Cloud-fog hybrid management
- PCA
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

# paper-1918 — Study on Dynamic Principal Component Allocation Strategy for Data in Cloud-Fog Hybrid Management System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In a cloud-fog hybrid environment, the introduction of multi-agent architecture makes the dynamic resource allocation and rapid task offloading decision-making process more efficient, which are critical for optimizing system performance. The combination of cloud computing and edge computing integrates into a heterogeneous network that combines both. This network architecture leverages the complementary strengths of cloud and edge computing, maximizing their advantages while minimizing their weaknesses. The cloud utilizes its powerful computing and storage capabilities to provide flexible configurations, low latency, and high bandwidth network environments for edge devices. This paper employs principal component analysis to address the large amount of data generated in cloud-fog hybrid management systems and conducts dynamic analysis for resource allocation strategies. The principal component analysis algorithm extracts both dynamic and static features of the data, revealing hidden patterns within it. After analysis, this enhances understanding of the data and constructs a feature-based principal component model that adapts to changes in the cloud-fog environment. This model can also adjust the allocation plan of the cloud-fog hybrid system in real-time based on current system resource status, leading to more efficient resource utilization. Compared with the traditional data allocation strategy, the strategy proposed in this study has significant advantages in improving the system response speed, saving network bandwidth, and enhancing the organization efficiency of the related devices, which can balance the computational power demand of IoT data processing more efficiently. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1918.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
