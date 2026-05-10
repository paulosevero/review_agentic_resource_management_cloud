---
id: paper-0301
title: 'Malta: Multi-Agent Reinforcement Learning for Differentiated Services in Fat Tree Networks'
authors:
- Kattepur, Ajay
- David, Sushanth
venue: 2021 IEEE Conference on Network Function Virtualization and Software Defined Networks, NFV-SDN 2021 - Proceedings
venue_type: conference
year: 2021
doi: 10.1109/NFV-SDN53031.2021.9665119
url: https://www.scopus.com/pages/publications/85125018802?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 129--134
keywords:
- Datacenter Network
- Differentiated Service.
- Fat Trees
- Reinforcement Learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0301 — Malta: Multi-Agent Reinforcement Learning for Differentiated Services in Fat Tree Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fat tree topologies have been gaining traction in datacenter networking due to the benefits of scalability, efficiency and fault resilience. Fat tree networks typically employ Equal Cost Multi-Path (ECMP) routing techniques for traffic load balancing. However, ECMP techniques are sub-optimal at distinguishing and providing differentiated services to various flows, which is a necessary requirement for 5G networks. In this paper, we propose Malta, a Multi-Agent Reinforcement Learning technique to provide differentiated service guarantees in fat tree networks. Multi-Agent reinforcement learning techniques offer scale, flexibility in reward structure and can be used to learn optimal behaviour with respect to differing traffic patterns. We demonstrate the utility of such agents over a real use case involving multiple flows with heterogeneous actions at the leaf, spine and super-spine level. The efficacy of the approach is shown in resolving congestions at the spine and super-spine level, that are unable to be resolved by ECMP. In addition, Malta is shown to provide superior differentiated service guarantees with 46% latency improvement and 34% throughput improvement over vanilla ECMP.  © 2021 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0301.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
