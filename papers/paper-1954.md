---
id: paper-1954
title: 'AI-Augmented Cyber Labs: Enhancing Cloud-Native Security Education through Adaptive Feedback and Threat Simulation'
authors:
- Mittal, Akshay
- Shah, Harsh
- Keshap, Pragya
venue: ACM SIGCITE 2025 - Proceedings of the 26th ACM Annual Conference on Cybersecurity and Information Technology Education
venue_type: conference
year: 2025
doi: 10.1145/3769694.3771136
url: https://www.scopus.com/pages/publications/105028798950?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 174--179
keywords:
- adaptive learning
- artificial intelligence
- cloud-native security
- cybersecurity education
- reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1954 — AI-Augmented Cyber Labs: Enhancing Cloud-Native Security Education through Adaptive Feedback and Threat Simulation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern software development is increasingly driven by cloud-native technologies, yet cybersecurity education has not kept pace. Traditional training environments often rely on static, pre-configured labs that fail to capture the complexity of real-world cloud infrastructures or adapt to individual learner needs. As a result, students frequently struggle to develop practical skills for securing dynamic environments such as containerized workloads, Continuous Integration/Continuous Deployment (CI/CD) pipelines, and Kubernetes clusters.To address these challenges, we present an AI-augmented cyber lab designed to deliver adaptive, hands-on security training. Our platform integrates Large Language Models (LLMs) for semantic analysis of student-submitted artifacts, including code, YAML configurations, and infrastructure-as-code policies, while a Reinforcement Learning (RL) agent dynamically adjusts the level of instructional support. The system is deployed on Kubernetes, leveraging container orchestration and automated threat simulation to replicate realistic attack scenarios.We validate the framework through a three-part evaluation methodology combining technical validation, system simulation, and expert review. The LLM Analyzer achieves an F1-score of 0.92 on a corpus of 1,500 real-world cloud-native artifacts, demonstrating high accuracy in identifying security misconfigurations. Simulation-based testing confirms the RL agent's adaptive behavior across diverse learner personas. Expert evaluation by five domain specialists yields average ratings of 4.4/5 for pedagogical value and confirms the system's potential for classroom deployment. This work establishes a rigorously validated, AI-enhanced architecture for cloud-native security education.  © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1954.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
