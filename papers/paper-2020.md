---
id: paper-2020
title: 'KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud'
authors:
- Pasin, Andrea
- Ferro, Nicola
venue: SIGIR 2025 - Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval
venue_type: conference
year: 2025
doi: 10.1145/3726302.3730298
url: https://www.scopus.com/pages/publications/105011823475?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 3584--3594
keywords:
- Docker
- Evaluation
- Information Retrieval
- Infrastructure
- Kubernetes
- Large Language Models
- Quantum Computing
- Reproducibility
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

# paper-2020 — KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Experimental evaluation steers the development of Information Retrieval (IR) systems, and large-scale evaluation campaigns provide the field with a common infrastructure to conduct comparable evaluation exercises. Over the years, tools and platforms have been developed to manage and automate these activities, enhance the reproducibility of conducted experiments and facilitate data sharing. In this context, Evaluation-as-a-Service (EaaS) emerged as an approach to avoid distributing experimental collections, which may contain copyrighted or sensitive data, and instead execute containerised code on that data on remote servers. We propose Kubernetes Infrastructure for Managed Evaluation and Resource Access (KIMERA) as the next step from EaaS into Evaluation-in-the-Cloud (EitC), allowing researchers to directly code and execute their systems through their browsers, requiring only an internet connection. Moreover, recent advancements, such as Large Language Models, or new computing paradigms, such as quantum computers, require external third-party services and computational resources. In this respect, KIMERA streamlines and simplifies access to such services on-demand via their APIs. More in detail, KIMERA relies on state-of-the-art containerization and orchestration tools, such as Docker and Kubernetes, to provide a robust, scalable, secure, and fault-tolerant IR evaluation platform. KIMERA monitors and stores all the participants’ submissions, accurately keeping track of the resource usage, allowing for evaluating both the efficiency and the effectiveness of the deployed methods. Moreover, all participants can be assigned workspaces sharing the same resources (i.e., CPU and RAM), thus enhancing reproducibility and comparability among systems. Finally, KIMERA has been designed with modularity and extensibility in mind, allowing it to be easily adapted to new use cases and usage scenarios. KIMERA has been developed and adopted in the context of the QuantumCLEF lab, to allow for mixed experiments, comparing approaches running on traditional hardware and on real quantum annealers provided by external companies. KIMERA has also been used as a learning resource to provide Quantum Computing tutorials for IR at major conferences, such as ECIR and SIGIR. The source code of KIMERA is openly available at https://github.com/MjPaxter/KIMERA. © 2025 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2020.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
