---
id: paper-2064
title: 'Automated LLM Deployment and Evaluation: A Cloud-Native Approach Using LLM-as-a-Judge'
authors:
- Rafique, Ansar
- Marsden, Brian D.
venue: IEEE International Conference on Cloud Computing, CLOUD
venue_type: conference
year: 2025
doi: 10.1109/CLOUD67622.2025.00053
url: https://www.scopus.com/pages/publications/105015966505?origin=resultslist
publisher: IEEE Computer Society
pages: 448--450
keywords:
- Automated LLM Evaluation
- Cloud-Native LLM Deployment
- IaC
- LLM Benchmarking
- LLM-as-a-Judge
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2064 — Automated LLM Deployment and Evaluation: A Cloud-Native Approach Using LLM-as-a-Judge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of LLMs has led to widespread adoption across various domains, but it has also raised concerns about data security and privacy, particularly with publicly available and commercially operated platforms. Given their high computational demands, cloud environments are the obvious choice for deployment. As a result, organizations are increasingly deploying LLMs in confined cloud environments to protect sensitive data while leverazing scalable cloud resources. However, deploying LLMs in cloud environments remains a complex and time-consuming process that requires specialized skills and expertise in various areas, such as infrastructure management, resource allocation, and model setup. Testing and comparing LLMs to select the appropriate one is particularly challenging as different models are trained for different purposes, making the direct comparison nontrivial. Furthermore, differences in model architectures, training data, and fine-tuning strategies make objective evaluation difficult, limiting the effectiveness of traditional benchmarking approaches. To address these challenges, we present a cloud-native system that automates both the deployment and evaluation of LLMs. Our contributions are twofold: (i) we automate the provisioning and deployment of LLMs on various cloud platforms to stream-line infrastructure setup, and (ii) we develop a lightweight evaluation framework that leverages the LLM-as-a-Judge approach, where an independent LLM systematically assesses and compares different models based on predefined evaluation criteria. Our ongoing work aims to optimize LLM deployment by selecting cost-efficient cloud resources. We are also enhancing the evaluation framework with diverse prompts, broader metrics, and cross-model validation for fair, reproducible benchmarking.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2064.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
