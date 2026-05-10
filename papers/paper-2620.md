---
id: paper-2620
title: 'Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework'
authors:
- Islam, Azharul
- Chang, Kyunghi
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2026.3676381
url: https://www.scopus.com/pages/publications/105034434120?origin=resultslist
publisher: IEEE Computer Society
pages: 7964--7986
keywords:
- 6G wireless networks
- deep joint source-channel coding
- knowledge base
- reinforcement learning
- Semantic communication
- unequal error protection
- variational autoencoder
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2620 — Beyond Bit Fidelity: Dual-Mode Domain-Aware Knowledge-Enhanced Semantic Text Communication Framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Semantic communication has emerged as a transformative paradigm for sixth-generation (6G) wireless networks, prioritizing meaning preservation over bit-level accuracy. However, existing frameworks face critical limitations including insufficient terminology preservation, prohibitive API costs for LLM-based reconstruction, and inability to adapt to varying channel conditions. This paper presents a dual-mode domain-aware semantic communication framework integrating knowledge-enhanced compression, content-adaptive unequal error protection (UEP), and reinforcement learning (RL)-driven intelligent reconstruction. Mode 1 (cloud/API-assisted) achieves 98.2% semantic similarity and 96.8% BLEU using GPT-4-turbo for quality-critical applications, while Mode 2 (edge/local) achieves 87.8% semantic similarity and 82.3% BLEU with zero external dependency using a local Mini-LLM (355 M parameters) for latency-critical scenarios. Key contributions include: (1) entropy-adaptive VAE compression with dynamic dimensionality and domain-specific knowledge base enhancement for improved terminology preservation; (2) gradient-based dimension-level UEP with multi-level modulation allocating stronger protection to semantically critical embedding dimensions; and (3) PPO-based multi-path reconstruction intelligently selecting among DVAE-enhanced, pattern-based, and ensemble strategies based on channel conditions and semantic quality indicators. Extensive evaluation on Europarl, News, and Technical corpora across SNR 0–20 dB demonstrates statistically significant improvements over DeepSC, R-DeepSC, and KG-LLM-SC while enabling flexible deployment from cloud-assisted to real-time edge computing. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2620.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
