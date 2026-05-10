---
id: paper-2766
title: 'RAGMail: a cloud-based retrieval-augmented framework for reducing hallucinations in LLM text generation'
authors:
- Sanyal, Priyodip
- Rathore, Kumud
- Arjunan, R. Vijaya
venue: Scientific Reports
venue_type: journal
year: 2026
doi: 10.1038/s41598-026-38913-w
url: https://www.scopus.com/pages/publications/105031598362?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- AI personalization
- Cloud native architecture
- Cold email generation
- Factualness evaluation
- Generative AI
- Large language models
- Natural language processing
- Weighting LLM
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

# paper-2766 — RAGMail: a cloud-based retrieval-augmented framework for reducing hallucinations in LLM text generation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cold emailing is used to personalize, target emails for outreach without prior contact. Automating this personalized cold email generation process can significantly improve outreach efficiency for job seekers, particularly in competitive industries. It streamlines the process of composition, saves time and increases engagement, tailored to a specific industry or role. In today’s competitive market, where job application is made easy, such a tool scales communication and boosts the conversion rate. The cold email generator. RAGMail, is an intelligent cold email generator that is cloud-integrated and uses Retrieval-Augmented Generation (RAG) to reduce hallucinations. The cloud-native infrastructure on which the system is built makes use of services including managed Large Language Model (LLMs) APIs, scalable vector databases, and object storage. With real-time document retrieval and cloud-hosted, metadata-aware templates, RAGMail guarantees high personalization accuracy and factual foundation. This cloud-native architecture provides elastic scalability, low-latency inference, and real-time personalization at scale, all while protecting data and user privacy with role-based access control and encrypted storage. Beyond job applications, the approach can be applied to a wide range of outreach sectors, including sales, academia, and commercial relationships, where factual accuracy and context sensitivity are critical. The system ensures high availability and load balancing during peak demand periods by utilizing distributed cloud resources. The models exhibit open-domain conversational capabilities, generalize effectively to scenarios beyond the trained data, and as verified by human evaluations, substantially reduce the well-known problem of knowledge hallucination in state-of-the-art chatbots. The proposed framework offers a scalable and reliable solution for generating contextually grounded, high-quality cold emails using Retrieval-Augmented Generation. © The Author(s) 2026.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2766.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
