---
id: paper-0341
title: Edge Intelligent Agent Assisted Hybrid Hierarchical Blockchain for continuous healthcare monitoring & recommendation system in 5G WBAN-IoT
authors:
- Sharmila, A. Helen
- Jaisankar, N.
venue: Computer Networks
venue_type: journal
year: 2021
doi: 10.1016/j.comnet.2021.108508
url: https://www.scopus.com/pages/publications/85116534897?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- 5G
- Edge computing
- Healthcare monitoring and recommendation
- Hybrid blockchain
- Internet of Things (IoT)
- WBAN
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0341 — Edge Intelligent Agent Assisted Hybrid Hierarchical Blockchain for continuous healthcare monitoring & recommendation system in 5G WBAN-IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Wireless Body Area Network (WBAN) is an emerging technology that faces many challenges for monitoring patient health state information and early diagnosis of any disease (e.g. COVID-19). In addition, WBAN has many issues such as high energy consumption, overhead and latency due to the scarcity in resources, for that we bring edge assisted 5G environment in WBAN. The patient information is sensitive and easily traced by the attackers due to insecurity, for that, we proposed the EiA-H2B model (Edge intelligent Agent Hybrid Hierarchical Blockchain) which includes five phases. Firstly we proposed Biological PUF based sensor authentication, which is a strong credential that provides high security. All the sensors are authenticated by the virtual authenticator that is deployed by a blockchain ledger. Due to the mobility of WBAN, we focused on handover that is done by Bi-Partite One to N matching theory. Secondly, we proposed high voting based virtual clustering, in this phase high voting sensor is elected as a super node and that is used to create a virtual cluster. Thirdly, we proposed duty cycle MAC scheduling protocol is used to predict the original state of the sensors which is done by Attention Matrix based Gated Recurrent Unit (AM-GRU), and then the timeslots are allocated for avoiding packet loss and retransmission. Fourth, we perform relay selection and routing that is done by Global Optimization based Artificial Electric Field Algorithm (AEFA). And finally, we predict emergency data and generate an alert in EiA using Human Learning aided State Action Reward State Action (SARSA) algorithm that finds the current state and predicts the corresponding action. Based on that current state information SARSA provides an efficient recommendation to the patients. Experiments are conducted by OMNeT ++ network simulator and evaluate the performance of the proposed EiA-H2B model in terms of energy consumption, success rate, network throughput, end to end delay, packet loss rate, authentication time and processing time. © 2021 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0341.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
