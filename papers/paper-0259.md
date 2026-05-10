---
id: paper-0259
title: Consistency Guaranteed Multi Container Migration for Smart Community Network Services
authors:
- Abeysiriwardhana, W.A.P. Shanaka
- Morishima, Ryo
- Miura, Tatsuki
- Nishi, Hiroaki
venue: IEEJ Transactions on Electronics, Information and Systems
venue_type: journal
year: 2021
doi: 10.1541/ieejeiss.141.1453
url: https://www.scopus.com/pages/publications/85138185184?origin=resultslist
publisher: Institute of Electrical Engineers of Japan
pages: 1453--1461
keywords:
- container migration
- data plane development
- network services
- smart community
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

# paper-0259 — Consistency Guaranteed Multi Container Migration for Smart Community Network Services

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Smart Community (SC) uses IoT sensors to provide smart grid control, traffic management, and similar IoT services. These services expect to run at the network edge or fog layer to provide low latency network services, encapsulate citizens' private information, support low-cost IoT terminals from cyber-attacks, and support other cutting-edge fog and edge services. SC edge is a service platform that supports edge/fog services for IoT terminals by using Docker containers. Initially, SC edge/fog computing nodes did not support the function of service migration. However, service migration is necessary to support remote deployment and service distribution in SC networks. The existing container migration techniques focus mainly on resource utilization. However, SC services should handle loss-free data stream processing and order-preservation of network packets to gather IoT sensor data after migration. In addition, SC services require one-to-many migration to support high throughput loads when required. Therefore, this paper focuses on enhancing SC service flexibility by introducing migration for relocatable and network consistency guaranteed containerized services. SC edge proposes multiple container migration techniques that are suitable for network services. The proposed techniques can improve resource consumption, guarantee network traffic consistency, and apply one-to-many migration patterns. Layer leveraging migration (LLM) reduces the overall migration time by 10.8% for an elastic search Docker container than available Docker migration methods. Additionally, consistency guaranteed migration (CGM) is proposed to guarantee network consistency. However, CGM consumes additional resources compared to LLM for IoT data management. Finally, One to N Consistency Guaranteed Migration (O2NCGM) is proposed to support one-to-many migration with data consistency that shows similar performance to CGM. © 2021 The Institute of Electrical Engineers of Japan.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0259.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
