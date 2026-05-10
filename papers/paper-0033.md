---
id: paper-0033
title: 'AQUAMan: QoE-driven cost-Aware mechanism for saas acceptability rate adaptation'
authors:
- Najjar, Amro
- Mualla, Yazan
- Boissier, Olivier
- Picard, Gauthier
venue: Proceedings - 2017 IEEE/WIC/ACM International Conference on Web Intelligence, WI 2017
venue_type: conference
year: 2017
doi: 10.1145/3106426.3106485
url: https://www.scopus.com/pages/publications/85031027171?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 331--339
keywords:
- Multi-Agent negotiation
- QoE
- Saas
- User satisfaction
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0033 — AQUAMan: QoE-driven cost-Aware mechanism for saas acceptability rate adaptation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As more interactive and multimedia-rich applications are migrating to the cloud, end-user satisfaction and her ?ality of Experience (QoE) will become a determinant factor to secure success for any So.ware as a Service (SaaS) provider. Yet, in order to survive in this competitive market, SaaS providers also need to maximize their Quality of Business (QoBiz) and minimize costs paid to cloud providers. However, most of the existing works in the literature adopt a provider-centric approach where the end-user preferences are overlooked. In this article, we propose the AQUAMan mechanism that gives the provider a €ne-grained QoE-driven control over the service acceptability rate while taking into account both end-users' satisfaction and provider's QoBiz,e proposed solution is implemented using a multi-Agent simulation environment,e results show that the SaaS provider is capable of attaining the predefined acceptability rate while respecting the imposed average cost per user. Furthermore, the results help the SaaS provider identify the limits of the adaptation mechanism and estimate the best average cost to be invested per user. © 2017 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0033.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
