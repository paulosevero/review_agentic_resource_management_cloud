---
id: paper-2505
title: Two-Tier heuristic search for ransomware-as-a-service based cyberattack défense analysis using explainable Bayesian deep learning model
authors:
- Almuflih, Ali Saeed
venue: Scientific Reports
venue_type: journal
year: 2026
doi: 10.1038/s41598-025-96083-7
url: https://www.scopus.com/pages/publications/105026895608?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- Bayesian neural network
- Cyberthreats
- Explainable artificial intelligence
- Metaheuristic
- Ransomware-as-a-service
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2505 — Two-Tier heuristic search for ransomware-as-a-service based cyberattack défense analysis using explainable Bayesian deep learning model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data security assurance is essential owing to the improving popularity of cloud computing and its extensive usage through several industries, particularly in light of the increasing number of cyber-security attacks. Ransomware-as-a-service (RaaS) attacks are prominent and widespread, allowing uniform individuals with minimum technology to perform ransomware processes. While RaaS methods have declined the access barriers for cyber threats, generative artificial intelligence (AI) growth might result in new possibilities for offenders. The high prevalence of RaaS-based cyberattacks poses essential challenges to cybersecurity, requiring progressive and understandable defensive mechanisms. Furthermore, deep or machine learning (ML) methods mainly provide a black box, giving no data about how it functions. Understanding the details of a classification model’s decision can be beneficial for understanding the work way to be identified. This study presents a novel Two-Tier Metaheuristic Algorithm for Cyberattack Defense Analysis using Explainable Artificial Intelligence based Bayesian Deep Learning (TTMCDA-XAIBDL) method. The main intention of the TTMCDA-XAIBDL method is to detect and mitigate ransomware cyber threats. Initially, the TTMCDA-XAIBDL method performs data preprocessing using Z-score normalization to ensure standardization and scalability of features. Next, the improved sand cat swarm optimization (ISCSO) technique is used for the feature selection. The Bayesian neural network (BNN) is employed to classify cyberattack defence. Moreover, the BNN’s hyperparameters are fine-tuned using the whale optimization algorithm (WOA) model, optimizing its performance for effective detection of ransomware threats. Finally, the XAI using SHAP is integrated to provide explainability, offering perceptions of the model’s decision-making procedure and adopting trust in the system. To demonstrate the effectiveness of the TTMCDA-XAIBDL technique, a series of simulations are conducted using a ransomware detection dataset to evaluate its classification performance. The performance validation of the TTMCDA-XAIBDL technique portrayed a superior accuracy value of 99.29% over the recent methods. © The Author(s) 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2505.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
