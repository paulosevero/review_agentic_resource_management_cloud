---
id: paper-0765
title: Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence
authors:
- Xu, Minrui
- Niyato, Dusit
- Zhang, Hongliang
- Kang, Jiawen
- Xiong, Zehui
- Mao, Shiwen
- Han, Zhu
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2023
doi: 10.1109/GLOBECOM54140.2023.10436771
url: https://www.scopus.com/pages/publications/85187323575?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3548--3553
keywords:
- generative artificial intelligence
- joint foundation model caching and inference
- Mobile edge computing
- pretrained foundation models
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
    my_justification: LLM as workload
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

# paper-0765 — Joint Foundation Model Caching and Inference of Generative AI Services for Edge Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of artificial general intelligence (AGI), various multimedia services based on pretrained foundation models (PFMs) need to be effectively deployed. With edge servers that have cloud-level computing power, edge intelligence can extend the capabilities of AGI to mobile edge networks. However, compared with cloud data centers, resource-limited edge servers can only cache and execute a small number of PFMs, which typically consist of billions of parameters and require intensive computing power and GPU memory during inference. To address this challenge, in this paper, we propose a joint foundation model caching and inference framework that aims to balance the tradeoff among inference latency, accuracy, and resource consumption by managing cached PFMs and user requests efficiently during the provisioning of generative AI services. Specifically, considering the in-context learning ability of PFMs, a new metric named the Age of Context (AoC), is proposed to model the freshness and relevance between examples in past demonstrations and current service requests. Based on the AoC, we propose a least context caching algorithm to manage cached PFMs at edge servers with historical prompts and inference results. The numerical results demonstrate that the proposed algorithm can reduce system costs compared with existing baselines by effectively utilizing contextual information. © 2023 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0765.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
