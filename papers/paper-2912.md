---
id: paper-2912
title: Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]
authors:
- Zhang, Zhitao
- Zou, Benyao
- Hou, Peng
- Ye, Jinyang
- Gao, Zhensen
- Li, Fan
- Qin, Yuwen
venue: Guangzi Xuebao/Acta Photonica Sinica
venue_type: journal
year: 2026
doi: 10.3788/gzxb20265503.0306001
url: https://www.scopus.com/pages/publications/105035723951?origin=resultslist
publisher: Chinese Optical Society
pages: ''
keywords:
- Adaptive equalization
- Baud-rate sampling
- Clock recovery
- Coherent optical communication
- DSP
language: Chinese
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2912 — Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of cloud computing and large language models, global mobile data traffic has experienced exponential growth, imposing higher demands on data center interconnection technologies. To achieve high-speed data transmission at 800 Gbit/s, coherent optical communication with high spectral efficiency and support for advanced modulation formats has emerged as a key solution for short-reach optical interconnects. However, traditional coherent receivers are hindered by high Digital Signal Processing (DSP) complexity, which makes it difficult to meet stringent power and cost requirements. To address this, this paper proposes a low-complexity DSP scheme based on baud-rate sampling, which reduces computational complexity while maintaining performance for short-reach coherent optical communications. The proposed DSP architecture integrates a baud-rate clock recovery module with a two-stage adaptive equalizer, both designed for low complexity. The clock recovery module employs a split-path design comprising four independent units, each utilizing a sign-MM Timing Phase Error Detection (TPED) algorithm. Operating at the symbol rate, this module uses a sign function to extract timing errors from signal polarity changes. This approach enables robust compensation of Sampling Clock Offsets (SCO) and In-phase/Quadrature (I/Q) skew without requiring carrier recovery. Subsequently, a Two-stage Real-valued Multiple Input Multiple Output (RV-MIMO) adaptive equalizer is applied. Its tap configuration is flexible: the first stage uses N<sub>1</sub> main taps to mitigate intra-polarization impairments, such as chromatic dispersion and inter-symbol interference, while the second stage includes N<sub>2</sub> cross-term taps and a 4×4 RV-MIMO with N<sub>3</sub> taps to handle residual inter-polarization crosstalk and polarization demultiplexing. This tunable structure allows the equalizer's complexity to be dynamically adjusted based on channel conditions, thereby optimizing the performance-complexity balance. Simulation results under a 56 GBaud dual-polarization 16QAM transmission over 2 km standard single-mode fiber demonstrate the effectiveness of the proposed scheme. The sign-MM TPED exhibits robust performance against impairments such as carrier frequency offset and phase noise, with timing jitter remaining below − 45 dB under various conditions. The two-stage equalizer reliably achieves Bit Error Rate (BER) performance below the hard-decision forward error correction threshold, even in the presence of IQ skew. Compared to conventional oversampling-based DSP schemes, the proposed approach reduces the number of real multipliers required in the equalizer by approximately 50%. This complexity reduction is achieved with only minor penalties of 0.4 dB in Optical Signal-to-Noise Ratio (OSNR) tolerance and 1.1 dB in Received Optical Power (ROP) sensitivity. In summary, this work presents a low-complexity DSP solution for short-reach coherent optical interconnects, using baud-rate sampling to significantly reduce computational complexity while maintaining performance. The integrated architecture, which combines I/Q-independent clock recovery with a configurable-tap adaptive equalizer, enhances robustness against I/Q skew and sampling offsets, making it suitable for data center applications. These attributes collectively make the scheme a practical and efficient candidate for high-speed, power-and cost-sensitive applications such as intra-data center interconnects. © 2026, Chinese Optical Society. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2912.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
