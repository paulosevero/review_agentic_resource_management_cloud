---
id: paper-0743
title: An Overview on Generative AI at Scale With Edge-Cloud Computing
authors:
- Wang, Yun-Cheng
- Xue, Jintang
- Wei, Chengwei
- Kuo, C. -C. Jay
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2023
doi: 10.1109/OJCOMS.2023.3320646
url: https://www.scopus.com/pages/publications/85174821496?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2952--2971
keywords:
- AI-generated content
- Artificial intelligence
- artificial intelligence of things
- distributed system
- edge-cloud computing
- lightweight models
- metaverse
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

# paper-0743 — An Overview on Generative AI at Scale With Edge-Cloud Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a specific category of artificial intelligence (AI), generative artificial intelligence (GenAI) generates new content that resembles what humans create. The rapid development of GenAI systems has created a huge amount of new data on the Internet, posing new challenges to current computing and communication frameworks. Currently, GenAI services rely on the traditional cloud computing framework due to the need for large computation resources. However, such services will encounter high latency because of data transmission and a high volume of user requests. On the other hand, edge-cloud computing can provide adequate computation power and low latency at the same time through the collaboration between edges and the cloud. Thus, it is attractive to build GenAI systems at scale by leveraging the edge-cloud computing paradigm. In this overview paper, we review recent developments in GenAI and edge-cloud computing, respectively. Then, we use two exemplary GenAI applications to discuss technical challenges in scaling up their solutions using edge-cloud collaborative systems. Finally, we list design considerations for training and deploying GenAI systems at scale and point out future research directions.  © ; 2023 The Authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0743.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
