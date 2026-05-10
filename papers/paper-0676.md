---
id: paper-0676
title: Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management
authors:
- Małota, Andrzej
- Koperek, Paweł
- Funika, Włodzimierz
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2023
doi: 10.1007/978-3-031-36021-3_55
url: https://www.scopus.com/pages/publications/85169661987?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 561--575
keywords:
- cloud resource management
- deep neural networks
- deep reinforcement learning
- explainable artificial intelligence
- explainable reinforcement learning
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

# paper-0676 — Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing resource management is a critical component of the modern cloud computing platforms, aimed to manage computing resources for a given application by minimizing the cost of the infrastructure while maintaining a Quality-of-Service (QoS) conditions. This task is usually solved using rule-based policies. Due to their limitations more complex solutions, such as Deep Reinforcement Learning (DRL) agents are being researched. Unfortunately, deploying such agents in a production environment can be seen as risky because of the lack of transparency of DRL decision-making policies. There is no way to know why a certain decision is made. To foster the trust in DRL generated policies it is important to provide means of explaining why certain decisions were made given a specific input. In this paper we present a tool applying the Integrated Gradients (IG) method to Deep Neural Networks used by DRL algorithms. This allowed to obtain feature attributions that show the magnitude and direction of each feature’s influence on the agent’s decision. We verify the viability of the proposed solution by applying it to a number of sample use cases with different DRL agents. © 2023, The Author(s), under exclusive license to Springer Nature Switzerland AG.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0676.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
