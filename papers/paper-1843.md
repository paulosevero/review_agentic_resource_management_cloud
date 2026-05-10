---
id: paper-1843
title: 'UB-Mesh: A Hierarchically Localized nD-FullMesh Data Center Network Architecture'
authors:
- Liao, Heng
- Liu, Bingyang
- Chen, Xianping
- Guo, Zhigang
- Cheng, Chuanning
- Wang, Jianbing
- Chen, Xiangyu
- Dong, Peng
- Meng, Rui
- Liu, Wenjie
- Zhou, Zhe
- Zhang, Ziyang
- Gai, Yuhang
- Qian, Cunle
- Xiong, Yi
- Cheng, Zhongwu
- Xia, Jing
- Ma, Yuli
- Chen, Xi
- Du, Wenhua
- Xiao, Shizhong
- Li, Chungang
- Qin, Yong
- Xiong, Liudong
- Yu, Zhou
- Chen, Lv
- Chen, Lei
- Wang, Buyun
- Wu, Pei
- Gao, Junen
- Li, Xiaochu
- He, Jian
- Yan, Shizhuan
- McColl, Bill
venue: IEEE Micro
venue_type: journal
year: 2025
doi: 10.1109/MM.2025.3592688
url: https://www.scopus.com/pages/publications/105015203502?origin=resultslist
publisher: IEEE Computer Society
pages: 20--29
keywords:
- Architecture
- Cost effectiveness
- Efficiency
- Memory architecture
- Mesh generation
- Network topology
- Program processors
- Computational bandwidth
- Computational power
- Cost-efficiency
- Data center networks
- Language model
- Large-scales
- Localised
- Performance efficiency
- Scalings
- Symmetrical design
- Network architecture
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

# paper-1843 — UB-Mesh: A Hierarchically Localized nD-FullMesh Data Center Network Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The scaling of large-scale language models (LLMs) demands unprecedented computational power and bandwidth. We present unified bus (UB)-Mesh, an innovative artificial intelligence data center network architecture that enhances scalability, performance, and cost-efficiency through a hierarchical nD-FullMesh topology. Unlike traditional symmetrical designs, UB-Mesh optimizes LLM training by prioritizing localized data movement and minimizing switch usage. The architecture features UB-Mesh-Pod, a physical implementation of 4D-FullMesh using custom hardware, including neural network processing units, CPUs, low/high-radix switches, and network interface cards, interconnected via our UB technology for dynamic resource allocation. For network optimization, we introduce all-path routing to efficiently manage data traffic. Combined with topology-aware performance tuning and robust reliability mechanisms, like 64 + 1 backup, UB-Mesh achieves 2.04× better cost-efficiency and 7.2% higher availability than Clos networks. These innovations address the critical challenges of building practical, high-performance artificial intelligence infrastructure at scale. © 1981-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1843.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
