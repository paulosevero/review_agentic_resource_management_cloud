---
id: paper-2079
title: 'P2PLLMEdge: Peer-to-Peer Framework for Localized Large Language Models using CPU only Resource-Constrained Edge'
authors:
- Ray, Partha Pratim
- Pradhan, Mohan Pratap
venue: EAI Endorsed Transactions on AI and Robotics
venue_type: journal
year: 2025
doi: 10.4108/airo.9292
url: https://www.scopus.com/pages/publications/105011332607?origin=resultslist
publisher: European Alliance for Innovation
pages: ''
keywords:
- Decentralized generative AI
- Edge computing
- Peer-to-peer
- Quantized LLMs
- Resource-constrained edge
- Web frameworks
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

# paper-2079 — P2PLLMEdge: Peer-to-Peer Framework for Localized Large Language Models using CPU only Resource-Constrained Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this research, we present P2PLLMEdge, a pioneering peer-to-peer framework designed to enable localized Large Language Models (LLMs) to operate efficiently in resource-constrained edge environments, exemplified by devices such as the Raspberry Pi 4B and CPU-only laptops. The framework addresses critical challenges, including limited computational capacity, network overhead, and scalability, by leveraging lightweight RESTful communication protocols, model-specific quantization, and decentralized task distribution. Key results demonstrate that P2PLLMEdge achieves substantial performance improvements. On average, Peer 2 (CPU-only laptop) achieves a 44.7% reduction in total duration (t<sub>peer2, total</sub> = 15.87 × 10<sup>9</sup> ns) compared to Peer 1 (Raspberry Pi 4B, t<sub>peer1, total</sub> = 28.18 × 10<sup>9</sup> ns). The framework processes tokens at a rate of 21.77 tokens/second on advanced LLMs like Granite3.1-moe:1b, significantly outperforming the baseline. Peer 1, employing quantized LLMs such as smolm2:360m-instruct-q8_0, reduces prompt evaluation duration by 23.2% (t<sub>peer1, prompt_eval</sub> = 0.76 × 10<sup>9</sup> ns) compared to larger models like qwen2.5:0.5b-instruct (t<sub>peer1, prompt_eval</sub> = 0.99 × 10<sup>9</sup> ns). Peer 2 demonstrates superior summarization capabilities, with evaluation durations (t<sub>peer2, eval</sub>) reduced by 72.8% (t<sub>peer2, eval</sub> = 5.15 × 10<sup>9</sup> ns) for explanation-type prompts relative to Peer 1 (t<sub>peer1, eval</sub> = 18.93 × 10<sup>9</sup> ns). The framework also achieves significant network efficiency, reducing inter-peer communication durations by up to 44.9% (t<sub>peer2, network</sub> = 25.83 × 10<sup>9</sup> ns vs. t<sub>peer1, network</sub> = 46.92 × 10<sup>9</sup> ns). Peer-to-peer synergy ensures seamless task execution, where Peer 1 generates text and offloads computationally intensive summarization tasks to Peer 2, achieving a balance between performance and resource utilization. The novelty of P2PLLMEdge lies in its ability to seamlessly integrate lightweight LLMs with decentralized edge devices, achieving advanced natural language processing functionalities entirely on edge devices traditionally deemed unsuitable for such tasks. This framework provides an adaptable, and cost-effective approach for deploying quantized LLM-driven applications. Future directions include scaling the framework to multi-peer environments, optimizing task scheduling algorithms, and exploring integration with heterogeneous LLM-enabled systems. The codes are available on https://github.com/ParthaPRay/peer_to_peer_local_llm_interaction. © 2025 Partha Pratim Ray et al.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2079.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
