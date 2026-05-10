---
id: paper-2364
title: 'Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes'
authors:
- Yang, Nanzi
- Liu, Xingyu
- Shen, Wenbo
- Li, Jinku
- Lu, Kangjie
venue: CCS 2025 - Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security
venue_type: conference
year: 2025
doi: 10.1145/3719027.3765106
url: https://www.scopus.com/pages/publications/105023835960?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 3401--3415
keywords:
- Access Control
- Implicit Permission
- Kubernetes
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

# paper-2364 — Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As the de-facto standard for container orchestration, Kubernetes is extensively adopted by numerous companies and cloud vendors, making its security critical. In this paper, we define a new attack surface called implicit permission: The execution of explicitly granted permissions in Kubernetes dynamically leads to implicit operations on other resources, enabling new permissions beyond the explicitly granted ones. Such implicit permissions create security vulnerabilities that attackers can exploit to compromise an entire cluster. Automatically identifying implicit permissions is challenging due to implicit relation reasoning and dynamic behaviors across diverse components of Kubernetes. To address that, we devise a systematic approach that combines static analysis techniques with the advanced capabilities of the large language model (LLM, e.g., GPT-4.5). Initially, we develop a static analysis to identify all Kubernetes resources. Building on this, we use static analysis to identify all explicit permissions for each resource. Finally, by combining the semantic reasoning capabilities of LLMs with the pattern-based precision of static analysis, we reason about what explicit permissions may dynamically lead to implicit permissions through complex interactions and uncover 593 implicit permissions derived from explicit permissions. We use the implicit permission references as insights to identify potential risks of CNCF projects and applications provided by the top four cloud vendors. With responsible disclosure, we obtain five new CVEs, six acknowledgments of cloud vendors, and a bounty awarded by Google. These acknowledgments underlie the practical impact of our attack. © 2025 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2364.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
