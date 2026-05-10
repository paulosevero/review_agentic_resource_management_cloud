---
id: paper-0769
title: Multi-Agent Deep Q-Network Based Dynamic Controller Placement for Node Variable Software-Defined Mobile Edge-Cloud Computing Networks
authors:
- Xu, Chenglin
- Xu, Cheng
- Li, Bo
venue: Mathematics
venue_type: journal
year: 2023
doi: 10.3390/math11051247
url: https://www.scopus.com/pages/publications/85149496878?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- controller placement problem
- Mobile Edge-Cloud Computing Networks
- Multi-Agent Deep Q-Network
- node-variable network
- software-defined networks
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0769 — Multi-Agent Deep Q-Network Based Dynamic Controller Placement for Node Variable Software-Defined Mobile Edge-Cloud Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Software-defined networks (SDN) can use the control plane to manage heterogeneous devices efficiently, improve network resource utilization, and optimize Mobile Edge-Cloud Computing Networks (MECCN) network performance through decisions based on global information. However, network traffic in MECCNs can change over time and affect the performance of the SDN control plane. Moreover, the MECCN network may need to temporarily add network access points when the network load is excessive, and it is difficult for the control plane to form effective management of temporary nodes. This paper investigates the dynamic controller placement problem (CPP) in SDN-enabled Mobile Edge-Cloud Computing Networks (SD-MECCN) to enable the control plane to continuously and efficiently serve the network under changing network load and network access points. We consider the deployment of a two-layer structure with a control plane and construct the CPP based on this control plane. Subsequently, we solve this problem based on multi-agent DQN (MADQN), in which multiple agents cooperate to solve CPP and adjust the number of controllers according to the network load. The experimental results show that the proposed dynamic controller deployment algorithm based on MADQN for node-variable networks in this paper can achieve better performance in terms of delay, load difference, and control reliability than the Louvain-based algorithm, single-agent DQN-based algorithm, and MADQN- (without node-variable networks consideration) based algorithm. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0769.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
