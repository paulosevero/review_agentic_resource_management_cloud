---
id: "paper-2644"
title: "EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference"
authors: ["Kumar, Aayush"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3683784"
url: "https://www.scopus.com/pages/publications/105036014078?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Cloudflare Workers AI", "cross-review", "edge AI", "ensemble learning", "hallucination mitigation", "serverless AI", "small language models", "Truthful question answering", "uncertainty labeling"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2644 — EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference

## Metadata

- **Authors:** Kumar, Aayush
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3683784
- **URL:** https://www.scopus.com/pages/publications/105036014078?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloudflare Workers AI; cross-review; edge AI; ensemble learning; hallucination mitigation; serverless AI; small language models; Truthful question answering; uncertainty labeling

### Abstract

Hallucinations hinder reliable question answering, especially in resource-constrained deployments where frontier-scale models or retrieval-heavy pipelines may be impractical. We present EdgeJury, a four-stage ensemble framework that improves truthfulness using only small instruction-tuned language models (3B–8B) suitable for serverless edge inference. EdgeJury combines role-specialized generation, anonymized cross-review, chairman synthesis, and claim-level agreement labeling. On TruthfulQA (MC1), EdgeJury reaches 76.2% accuracy (95% CI: 72.8–79.6%), a +21.4% relative improvement over a single 8B baseline, and outperforms self-consistency and majority voting under transparent compute accounting. On a 200-question adversarial EdgeCases set, it achieves +48.2% relative gains, while manual error analysis shows an approximately 55% reduction in factual hallucination errors versus the single-model baseline. Beyond end-to-end gains, we analyze why the framework works and when it is worth its cost. Stage 1 agents exhibit non-trivial complementarity, blind synthesis preserves most of the full system’s accuracy while reducing chairman self-preference, structured critique outperforms open-ended critique in orchestration reliability, and scaling/pruning experiments show that most of the gain is obtained by four agents with substantial latency recovery available through early exit. Deployed on Cloudflare Workers AI, EdgeJury achieves 8.4 s median end-to-end latency, showing that coordinated small-model ensembles can improve truthfulness on misconception-heavy QA benchmarks without external retrieval or proprietary large-model APIs. © 2013 IEEE.

## 04 — Title Screening

**Title:** EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeJury: Cross-Reviewed Small-Model Ensembles for Truthful Question Answering on Serverless Edge Inference
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
