---
id: paper-2158
title: Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission
authors:
- Solat, Faranaksadat
- Lee, Joohyung
- Seif, Mohamed
- Niyato, Dusit
- Vincent Poor, H.
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3618095
url: https://www.scopus.com/pages/publications/105018357552?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 53574--53592
keywords:
- Federated learning (FL)
- hybrid language models (HLMs)
- large language models (LLMs)
- mobile edge computing
- small language models (SLMs)
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
    my_justification: LLM as workload
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

# paper-2158 — Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Hybrid language models (HLMs) are inference-time architectures that combine the low-latency efficiency of small language models (SLMs) on clients (edge devices) with the high accuracy of large language models (LLMs) in centralized servers. Unlike traditional end-to-end LLM inference, HLMs aim to reduce latency and communication by selectively invoking LLMs only when the local SLM’s predictions are uncertain—that is, when the model exhibits low confidence or high entropy in its token-level probability distribution. However, when the SLM encounters ambiguous or low-confidence predictions during inference, it must offload token-level probability distributions to the LLM for refinement. This frequent offloading leads to substantial communication overhead, particularly in bandwidth-constrained environments. To address this challenge, we propose federated learning (FL)-enabled HLM (FedHLM), a communication-efficient HLM framework that integrates uncertainty-aware inference with FL. The key innovation lies in collaboratively learning token-level uncertainty thresholds that determine when SLM predictions require LLM assistance. Instead of relying on static or hand-tuned thresholds, FedHLM uses FL to enable distributed threshold optimization across clients while preserving data privacy. Additionally, embedding-based token representations are employed to facilitate semantic similarity comparisons during peer-to-peer (P2P) resolution, allowing clients to reuse tokens inferred by similar peers without efficiently involving the LLM. Moreover, we propose hierarchical model aggregation as a strategy to reduce redundant token transmissions. At the edge server level, client updates are aggregated to refine local routing policies, while global coordination across clusters further synchronizes decision boundaries. This layered approach ensures that repeated uncertainty patterns are captured and resolved locally, significantly reducing unnecessary LLM queries. Extensive simulations on large-scale news classification tasks demonstrate that FedHLM achieves over 95% reduction in LLM transmissions with negligible accuracy loss, highlighting its potential for scalable and efficient edge-artificial intelligence (AI) deployment. © 2014 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2158.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
