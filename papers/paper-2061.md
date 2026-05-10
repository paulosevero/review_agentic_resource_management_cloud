---
id: paper-2061
title: 'Mobile Edge Intelligence for Large Language Models: A Contemporary Survey'
authors:
- Qu, Guanqiao
- Chen, Qiyuan
- Wei, Wei
- Lin, Zheng
- Chen, Xianhao
- Huang, Kaibin
venue: IEEE Communications Surveys and Tutorials
venue_type: journal
year: 2025
doi: 10.1109/COMST.2025.3527641
url: https://www.scopus.com/pages/publications/85214799561?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3820--3860
keywords:
- 6G
- edge intelligence
- foundation models
- Large language models
- mobile edge computing
- split learning
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
    my_justification: Review
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

# paper-2061 — Mobile Edge Intelligence for Large Language Models: A Contemporary Survey

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> On-device large language models (LLMs), referring to running LLMs on edge devices, have raised considerable interest since they are more cost-effective, latency-efficient, and privacy-preserving compared with the cloud LLM paradigm. Nonetheless unlike cloud LLMs, the performance of on-device LLMs is intrinsically constrained by resource limitations on edge devices. Sitting between cloud and on-device AI, mobile edge intelligence (MEI) may address this dilemma by provisioning AI capabilities at the edge of mobile networks, e.g., on base stations. This article provides a contemporary survey on harnessing MEI for LLM deployment. We begin by illustrating several killer applications to demonstrate the urgent need for deploying LLMs at the network edge. Next, we present the preliminaries of LLMs, MEI, and resource-efficient LLM techniques. We then provide an architectural overview of MEI for LLMs (MEI4LLM), outlining its core components and how it supports LLM deployment. Subsequently, we delve into various aspects of MEI4LLM, extensively covering edge LLM caching and delivery, edge LLM training, and edge LLM inference. Finally, we identify future research opportunities. We hope this article inspires researchers in the field to leverage mobile edge computing to facilitate LLM deployment, thereby unleashing the potential of LLMs across various privacy- and delay-sensitive applications. © 1998-2012 IEEE.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2061.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
