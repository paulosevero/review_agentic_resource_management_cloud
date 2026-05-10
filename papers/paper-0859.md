---
id: paper-0859
title: Federated Prompt Learning for Weather Foundation Models on Devices
authors:
- Chen, Shengchao
- Long, Guodong
- Shen, Tao
- Jiang, Jing
- Zhang, Chengqi
venue: IJCAI International Joint Conference on Artificial Intelligence
venue_type: conference
year: 2024
doi: ''
url: https://www.scopus.com/pages/publications/85204286299?origin=resultslist
publisher: International Joint Conferences on Artificial Intelligence
pages: 5772--5780
keywords:
- Deep learning
- Weather forecasting
- Centralised
- Cloud-computing
- Collaborative modeling
- Data heterogeneity
- Foundation models
- Geographic difference
- Individual devices
- Learning models
- Model training
- Weather patterns
- Federated learning
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

# paper-0859 — Federated Prompt Learning for Weather Foundation Models on Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> On-device intelligence for weather forecasting uses local deep learning models to analyze weather patterns without centralized cloud computing, holds significance for supporting human activates. Federated Learning is a promising solution for such forecasting by enabling collaborative model training without sharing raw data. However, it faces three main challenges that hinder its reliability: (1) data heterogeneity among devices due to geographic differences; (2) data homogeneity within individual devices and (3) communication overload from sending large model parameters for collaboration. To address these challenges, this paper propose Federated Prompt learning for Weather Foundation Models on Devices (FedPoD), which enables devices to obtain highly customized models while maintaining communication efficiency. Concretely, our Adaptive Prompt Tuning leverages lightweight prompts guide frozen foundation model to generate more precise predictions, also conducts prompt-based multi-level communication to encourage multi-source knowledge fusion and regulate optimization. Additionally, Dynamic Graph Modeling constructs graphs from prompts, prioritizing collaborative training among devices with similar data distributions to against heterogeneity. Extensive experiments demonstrates FedPoD leads the performance among state-of-the-art baselines across various setting in real-world on-device weather forecasting datasets. © 2024 International Joint Conferences on Artificial Intelligence. All rights reserved.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0859.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
