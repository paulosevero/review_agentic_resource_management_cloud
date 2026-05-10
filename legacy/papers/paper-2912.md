---
id: "paper-2912"
title: "Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]"
authors: ["Zhang, Zhitao", "Zou, Benyao", "Hou, Peng", "Ye, Jinyang", "Gao, Zhensen", "Li, Fan", "Qin, Yuwen"]
year: 2026
venue: "Guangzi Xuebao/Acta Photonica Sinica"
venue_type: "journal"
doi: "10.3788/gzxb20265503.0306001"
url: "https://www.scopus.com/pages/publications/105035723951?origin=resultslist"
publisher: "Chinese Optical Society"
pages: ""
keywords: ["Adaptive equalization", "Baud-rate sampling", "Clock recovery", "Coherent optical communication", "DSP"]
language: "Chinese"
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2912 — Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]

## Metadata

- **Authors:** Zhang, Zhitao and Zou, Benyao and Hou, Peng and Ye, Jinyang and Gao, Zhensen and Li, Fan and Qin, Yuwen
- **Year:** 2026
- **Venue:** Guangzi Xuebao/Acta Photonica Sinica
- **DOI:** 10.3788/gzxb20265503.0306001
- **URL:** https://www.scopus.com/pages/publications/105035723951?origin=resultslist
- **Publisher:** Chinese Optical Society
- **Pages:** 
- **Language:** Chinese
- **Keywords:** Adaptive equalization; Baud-rate sampling; Clock recovery; Coherent optical communication; DSP

### Abstract

With the rapid development of cloud computing and large language models, global mobile data traffic has experienced exponential growth, imposing higher demands on data center interconnection technologies. To achieve high-speed data transmission at 800 Gbit/s, coherent optical communication with high spectral efficiency and support for advanced modulation formats has emerged as a key solution for short-reach optical interconnects. However, traditional coherent receivers are hindered by high Digital Signal Processing (DSP) complexity, which makes it difficult to meet stringent power and cost requirements. To address this, this paper proposes a low-complexity DSP scheme based on baud-rate sampling, which reduces computational complexity while maintaining performance for short-reach coherent optical communications. The proposed DSP architecture integrates a baud-rate clock recovery module with a two-stage adaptive equalizer, both designed for low complexity. The clock recovery module employs a split-path design comprising four independent units, each utilizing a sign-MM Timing Phase Error Detection (TPED) algorithm. Operating at the symbol rate, this module uses a sign function to extract timing errors from signal polarity changes. This approach enables robust compensation of Sampling Clock Offsets (SCO) and In-phase/Quadrature (I/Q) skew without requiring carrier recovery. Subsequently, a Two-stage Real-valued Multiple Input Multiple Output (RV-MIMO) adaptive equalizer is applied. Its tap configuration is flexible: the first stage uses N<sub>1</sub> main taps to mitigate intra-polarization impairments, such as chromatic dispersion and inter-symbol interference, while the second stage includes N<sub>2</sub> cross-term taps and a 4×4 RV-MIMO with N<sub>3</sub> taps to handle residual inter-polarization crosstalk and polarization demultiplexing. This tunable structure allows the equalizer's complexity to be dynamically adjusted based on channel conditions, thereby optimizing the performance-complexity balance. Simulation results under a 56 GBaud dual-polarization 16QAM transmission over 2 km standard single-mode fiber demonstrate the effectiveness of the proposed scheme. The sign-MM TPED exhibits robust performance against impairments such as carrier frequency offset and phase noise, with timing jitter remaining below − 45 dB under various conditions. The two-stage equalizer reliably achieves Bit Error Rate (BER) performance below the hard-decision forward error correction threshold, even in the presence of IQ skew. Compared to conventional oversampling-based DSP schemes, the proposed approach reduces the number of real multipliers required in the equalizer by approximately 50%. This complexity reduction is achieved with only minor penalties of 0.4 dB in Optical Signal-to-Noise Ratio (OSNR) tolerance and 1.1 dB in Received Optical Power (ROP) sensitivity. In summary, this work presents a low-complexity DSP solution for short-reach coherent optical interconnects, using baud-rate sampling to significantly reduce computational complexity while maintaining performance. The integrated architecture, which combines I/Q-independent clock recovery with a configurable-tap adaptive equalizer, enhances robustness against I/Q skew and sampling offsets, making it suitable for data center applications. These attributes collectively make the scheme a practical and efficient candidate for high-speed, power-and cost-sensitive applications such as intra-data center interconnects. © 2026, Chinese Optical Society. All rights reserved.

## 04 — Title Screening

**Title:** Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Low-complexity DSP Scheme Based on Baud-rate Clock Recovery and Adaptive Equalization for Short-reach Optical Interconnects; [基于波特率采样时钟恢复与自适应均衡的 低复杂度短距光互连 DSP 研究]
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
