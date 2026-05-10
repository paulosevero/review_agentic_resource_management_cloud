---
id: paper-2147
title: A multi-agent deep reinforcement learning approach for optimal resource management in serverless computing
authors:
- Singh, Ashutosh Kumar
- Kumar, Satender
- Jain, Sarika
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-024-04820-w
url: https://www.scopus.com/pages/publications/85210372254?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Function instance
- Function scheduling
- Multi-agent
- Resource management
- Serverless computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2147 — A multi-agent deep reinforcement learning approach for optimal resource management in serverless computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The flexibility of serverless resources enables cloud service providers to scale up dynamically and down the resource requirements over time. However, the varying incoming workload and prefixed capacity of worker nodes can lead to resource under-utilization. To tackle this issue and to improve the performance of data centers, a Multi-Agent deep reinforcement learning-based Resource Management model (MARM) is presented, that reduces the overhead of resource under-utilization. It utilizes the resources efficiently by choosing the best worker node for the incoming workload resource requirements. It allows multiple agents to operate cooperatively while sharing communication. The proposed model keeps track of minimal resources requested by incoming function instances and schedules it to the most suited worker node to encourage efficient resource utilization. Extensive experiments are conducted using the proposed model in a simulated environment using a synthetic dataset and scaled-down Alibaba Cluster Trace. The experimental results show the efficacy of the proposed model in terms of improved CPU and memory utilization up to 39 and 30% over state-of-the-art schedulers, respectively. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2147.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
