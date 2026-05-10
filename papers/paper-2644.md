---
id: paper-2644
title: 'EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference'
authors:
- Kumar, Aayush
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3683784
url: https://www.scopus.com/pages/publications/105036014078?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloudflare Workers AI
- cross-review
- edge AI
- ensemble learning
- hallucination mitigation
- serverless AI
- small language models
- Truthful question answering
- uncertainty labeling
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

# paper-2644 — EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Hallucinations hinder reliable question answering, especially in resource-constrained deployments where frontier-scale models or retrieval-heavy pipelines may be impractical. We present EdgeJury, a four-stage ensemble framework that improves truthfulness using only small instruction-tuned language models (3B–8B) suitable for serverless edge inference. EdgeJury combines role-specialized generation, anonymized cross-review, chairman synthesis, and claim-level agreement labeling. On TruthfulQA (MC1), EdgeJury reaches 76.2% accuracy (95% CI: 72.8–79.6%), a +21.4% relative improvement over a single 8B baseline, and outperforms self-consistency and majority voting under transparent compute accounting. On a 200-question adversarial EdgeCases set, it achieves +48.2% relative gains, while manual error analysis shows an approximately 55% reduction in factual hallucination errors versus the single-model baseline. Beyond end-to-end gains, we analyze why the framework works and when it is worth its cost. Stage 1 agents exhibit non-trivial complementarity, blind synthesis preserves most of the full system’s accuracy while reducing chairman self-preference, structured critique outperforms open-ended critique in orchestration reliability, and scaling/pruning experiments show that most of the gain is obtained by four agents with substantial latency recovery available through early exit. Deployed on Cloudflare Workers AI, EdgeJury achieves 8.4 s median end-to-end latency, showing that coordinated small-model ensembles can improve truthfulness on misconception-heavy QA benchmarks without external retrieval or proprietary large-model APIs. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2644.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
