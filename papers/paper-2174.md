---
id: paper-2174
title: EVALUATION OF THE PERFORMANCE OF LLMs DEPLOYMENTS IN SELECTED CLOUD-BASED CONTAINER SERVICES; [OCENA WYDAJNOŚCI WDROŻEŃ LLM W WYBRANYCH USŁUGACH KONTENEROWYCH OPARTYCH NA CHMURZE]
authors:
- Stęgierski, Mateusz
- Szpak, Piotr
- Przyłucki, Sławomir
venue: Informatyka, Automatyka, Pomiary w Gospodarce i Ochronie Srodowiska
venue_type: journal
year: 2025
doi: 10.35784/iapgos.8206
url: https://www.scopus.com/pages/publications/105026487493?origin=resultslist
publisher: Politechnika Lubelska
pages: 142--150
keywords:
- auto-scaling
- language models
- load testing
- performance comparison
- serverless containers
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2174 — EVALUATION OF THE PERFORMANCE OF LLMs DEPLOYMENTS IN SELECTED CLOUD-BASED CONTAINER SERVICES; [OCENA WYDAJNOŚCI WDROŻEŃ LLM W WYBRANYCH USŁUGACH KONTENEROWYCH OPARTYCH NA CHMURZE]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growing adoption of serverless container services has created challenges in selecting optimal cloud platforms for production LLM deployments, yet comparative performance evaluations remain limited. This study evaluates AWS Fargate and Azure Container Apps for LLM deployments, investigating whether architectural differences cause substantial performance variations under diverse load patterns. We conducted systematic experiments using containerized Llama 3.2:1b across multiple scenarios: baseline measurements, inference tests with varying prompt lengths, streaming API performance, and concurrent load testing with progressive scaling. Each scenario was executed on both standard and auto-scaled infrastructure with 10 runs per configuration to ensure statistical reliability. Key findings reveal distinct platform characteristics: AWS Fargate demonstrates superior baseline API response times and time-to-first-token performance, while Azure Container Apps consistently outperforms AWS in inference processing for short and medium prompts with better consistency across test runs. Streaming performance shows platform-specific trade-offs, with AWS achieving lower initial latency but Azure providing superior token generation consistency. Under concurrent loads, both platforms maintain full capacity at lower concurrency levels, but AWS exhibits exponential response time degradation at higher loads while Azure shows more linear, predictable scaling behavior. Statistical analysis confirms significant performance differences across all metrics, validating that platform architecture fundamentally impacts LLM deployment performance. These findings indicate platform selection should align with specific workload requirements: AWS Fargate for latency-critical applications with steady loads, and Azure Container Apps for inference-intensive workloads requiring robust scaling and consistency. This study offers crucial benchmarking data for businesses deploying production-grade AI services on serverless container platforms. © 2025, Politechnika Lubelska. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2174.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
