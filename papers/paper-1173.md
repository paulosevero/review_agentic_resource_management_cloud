---
id: paper-1173
title: Automated Testing and Deployment Strategies for Quantum Algorithms
authors:
- Saxena, Mohit Chandra
- Tamrakar, Abhishek
- Arranz, Ulises
venue: Proceedings of International Conference on Contemporary Computing and Informatics, IC3I 2024
venue_type: conference
year: 2024
doi: 10.1109/IC3I61595.2024.10829232
url: https://www.scopus.com/pages/publications/85217400025?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 771--779
keywords:
- DevOps
- Quantum CD
- Quantum CI
- Quantum DevOps
- Quantum Software Testing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1173 — Automated Testing and Deployment Strategies for Quantum Algorithms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advent of quantum computing has ushered in a new era of technological innovation, promising unprecedented computational power and efficiency. As quantum technology matures, the need for robust, scalable, and efficient software development practices becomes increasingly critical. This paper proposes a novel DevOps framework tailored specifically for quantum software development, addressing unique challenges posed by quantum computing. The proposed architecture incorporates continuous integration and continuous deployment (CI/CD) pipelines, optimized for quantum algorithms, facilitating seamless integration and deployment of quantum applications. Key components include a Quantum Circuit Service for circuit design and optimization, a Quantum CI Service for continuous integration, and a comprehensive testing suite encompassing unit, integration, functional, and probabilistic testing. The framework emphasizes the use of large language models (LLMs) for automated microservice code generation, Kubernetes (K8s) cluster deployment for scalable infrastructure management, and a central quantum artifacts registry for efficient version control and resource management. A significant portion of this paper is dedicated to addressing the unique aspects of quantum computing, including the probabilistic nature of quantum algorithms, the need for specialized testing strategies, and the integration of classical and quantum software components. The proposed framework not only enhances the efficiency and reliability of quantum software development but also provides a structured approach to managing the complexities associated with quantum computing. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1173.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
