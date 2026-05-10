---
id: paper-1744
title: 'CloudInfraBot: Reinforcement Learning-Driven Infrastructure Automation for Azure-Based MLOps Environments'
authors:
- Kripa, Radhakrishnan Krishna
venue: 2025 IEEE 2nd International Conference on Green Industrial Electronics and Sustainable Technologies, GIEST 2025
venue_type: conference
year: 2025
doi: 10.1109/GIEST66547.2025.11387299
url: https://www.scopus.com/pages/publications/105035300312?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Azure
- CI/CD
- Cloud Computing
- DevOps
- Infrastructure Automation
- MLOps
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1744 — CloudInfraBot: Reinforcement Learning-Driven Infrastructure Automation for Azure-Based MLOps Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern MLOps pipelines deployed on cloud platforms such as Microsoft Azure face significant challenges in automating infrastructure provisioning due to dynamic workload variability, resource constraints, and cost-performance trade-offs. Traditional rule-based autoscaling systems lack the intelligence to adapt in real time, often leading to inefficient resource utilization, elevated operational costs, and service-level agreement (SLA) violations. In this paper, we introduce CloudInfraBot, a novel reinforcement learning-driven infrastructure automation framework tailored for Azure-based MLOps environments. CloudInfraBot learns to dynamically allocate compute and storage resources during CI/CD execution by observing workload patterns and optimizing a multi-objective reward function based on latency, cost, utilization, and reliability. The agent integrates natively with Azure DevOps, Azure Machine Learning Pipelines, and Azure Resource Manager APIs, enabling fine-grained control over provisioning decisions without human intervention. Experimental evaluations across real-world training and deployment workflows demonstrate that CloudInfraBot reduces pipeline latency by up to 31%, lowers compute cost by 33%, and minimizes SLA violations compared to baseline autoscaling techniques. This work establishes a foundation for intelligent infrastructure-as-code systems capable of self-adapting to the complexities of cloud-native AI operations. © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1744.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
