---
id: paper-2226
title: AI-Driven Multi-Agent Systems for Automated Regulatory Analysis of Crypto Projects
authors:
- Trerotola, Mario
- Calvaresi, Davide
venue: Conference Proceedings - 2025 IEEE International Conference on Metrology for eXtended Reality, Artificial Intelligence and Neural Engineering, MetroXRAINE 2025
venue_type: conference
year: 2025
doi: 10.1109/MetroXRAINE66377.2025.11340415
url: https://www.scopus.com/pages/publications/105033214287?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 735--740
keywords:
- Commerce
- Intelligent agents
- Laws and legislation
- Multi agent systems
- Semantics
- Asset markets
- Due diligence
- Institutional investors
- Multi agent
- Multiagent systems (MASs)
- Normalisation
- Rapid expansion
- Regulatory analysis
- Specialized software
- Supervisory authority
- Compliance control
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

# paper-2226 — AI-Driven Multi-Agent Systems for Automated Regulatory Analysis of Crypto Projects

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid expansion of the crypto-asset market is stretching supervisory authorities and institutional investors, and although MiCAR mandates comprehensive disclosures, the sheer volume and heterogeneity of project whitepapers push regulators toward a largely passive, alert-driven form of oversight that leaves little room for timely, preventive intervention. To address this challenge, this article presents an AI -driven multi-agent sys-tem (MAS) that automates Markets in Crypto-Assets Regulation (MiCAR) due diligence by synergizing large language modEIS (LLMs) with specialized software agents. This MAS features a supervisory agent orchestrating specialized peers for evidence retrieval, document normalization, semantic extraction, and rule-based verification, culminating in an auditable compliance report and an associated knowledge graph. Key techniques include retrieval-augmented generation (RAG) for contextualizing legal texts, self-critique prompting to enhance LLM reliability, and containerized microservices for scalable deployment. Evaluated on a diverse corpus of public whitepapers, the system significantly reduces processing latency and expert workload, achieving com-pliance assessment accuracy comparable to human experts for critical MiCAR requirements. Furthermore, the system supports longitudinal monitoring by dynamically incorporating regulatory updates into its rule repository, ensuring ongoing alignment with evolving MiCAR standards. The MAS architecture's transparent division of labor enables fault isolation, parallel processing, and human-in-the-Ioop validation, providing superior robustness and interpretability over conventional monolithic AI modEIS. By translating complex legal obligations into reproducible computational workflows, our approach advances Regulatory Technology (RegTech), offers actionable intelligence to market participants, and fosters a more transparent and accountable digital finance ecosystem. Future work will focus on multilingual capabilities and enhancing adversarial robustness against deceptive disclosures. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2226.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
