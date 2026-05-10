---
id: paper-2386
title: Architecture and Key Technologies of Large-Scale Space Optical Transport Networks (Invited); [大 规 模 空 间 光 传 送 网 架 构 与 关 键 技 术(特 邀)]
authors:
- Yongli, Zhao
- Huibin, Zhang
- Kunpeng, Zheng
- Wei, Wang
- Yuan, Cao
- Lihan, Zhao
- Jie, Zhang
venue: Guangxue Xuebao/Acta Optica Sinica
venue_type: journal
year: 2025
doi: 10.3788/AOS250873
url: https://www.scopus.com/pages/publications/105011256234?origin=resultslist
publisher: Chinese Optical Society
pages: ''
keywords:
- netw ork architecture
- optical transport netw ork
- satellite laser com m unication
- the sixth generation fixed network
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

# paper-2386 — Architecture and Key Technologies of Large-Scale Space Optical Transport Networks (Invited); [大 规 模 空 间 光 传 送 网 架 构 与 关 键 技 术(特 邀)]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Significance Information and communication serve as fundamental pillars of modern civilization and drivers of societal progress. Optical transport network (OTN) technology has achieved significant advancements as the core bearer in modern communication infrastructure, supporting ultra-high-speed backbone networks globally through functionalities like hard pipe isolation, transparent multi-service transmission, and multi-layer coordinated management. With per channel capacities exceeding 100 Gbit/s and end-to-end ms-level scheduling, OTN has become a cornerstone for large-capacity data transmission and cloud computing interconnections. However, terrestrial networks are inherently constrained by geographical environments and deployment costs, resulting in coverage gaps in remote areas such as oceans, deserts, and polar regions, and exhibiting insufficient resilience during natural disasters. To overcome these limitations, space networks, particularly low earth orbit (LEO) satellite constellations, are rapidly advancing, characterized by wide coverage, survivability, and flexible on-demand access, serving as a crucial complement to terrestrial infrastructure. Space optical communication is widely recognized as a promising solution for high-speed connectivity in space, offering distinct advantages such as ultra-high bandwidth, low transmission latency, and high security. Industry progress, including the deployment of optical inter-satellite links (OISL) on SpaceX's second-generation Starlink satellites demonstrating single-link rate reaching 200 Gbit/s, demonstrate the engineering feasibility of large-capacity space optical networking based on inter-satellite laser links. The integration of advanced optical transport network technologies from the terrestrial domain with satellite laser communication capabilities gives rise to the space optical transport network (S-OTN). S-OTN is positioned as the optical layer transmission base for the future integrated space-air-ground-sea network, aligning with the ITU-T's Network 2030 Vision and the objectives of the upcoming sixth-generation fixed network (F6G) to achieve ubiquitous coverage and intelligent connectivity by deeply integrating space network resources into its core architecture. Compared to traditional satellite microwave relay, S-OTN offers substantial improvements, including a capacity leap with single-satellite optical interface capacity potentially exceeding 400 Gbit/s, a reduction in cross-ocean end-to-end transmission delay to within hundreds of ms, and the ability to establish end-to-end trusted service pipelines in less than 1 s. By providing high-speed data transmission through large-capacity optical transport and ensuring low latency and high reliability through flexible optical networking techniques, S-OTN is poised to become a critical infrastructure supporting future F6G applications such as intelligent agent interconnectivity and ubiquitous sensing. However, deploying sophisticated optical transport technologies in the dynamic and challenging space environment presents a series of unique technical hurdles that necessitate dedicated research and development. Progress This review undertakes a systematic analysis of the pivotal technologies essential for the realization of S-OTN, building upon a proposed networking architecture suitable for large-scale deployments. We delve into critical technological domains, commencing with high-capacity inter-satellite optical transmission. This forms the high-speed backbone of the space layer but faces formidable challenges. These include long-distance signal degradation, precise pointing requirements, and dynamic disturbances such as satellite mobility and solar interference, all of which must be overcome to ensure reliable multi-Gbit/s to Tbit/s connectivity. Recent progress is evidenced by industry deployments demonstrating significant capacity, such as the optical inter-satellite links deployed by Starlink. Prior researches by Gao et al. and Li et al. have advanced adaptive optical interfaces and anti-disturbance control for inter-satellite links, specifically targeting stability and performance enhancement under dynamic conditions. Subsequently, we examine high-availability space-to-ground optical transmission, recognizing that the atmospheric channel presents a major impediment due to turbulence, scattering, and absorption. Progress in this area focuses on developing robust techniques to mitigate signal fading and interruptions. This includes advancements in adaptive optics and site diversity, as well as innovative adaptive reception schemes. For instance, Guo et al. have contributed research on utilizing mode mismatching multi-mode photonic lanterns to improve coupling efficiency despite atmospheric distortion. Furthermore, the integration of optical links with more weather-tolerant microwave systems through cooperative free space optical/radio frequency (FSO/RF) approaches with adaptive combining, analyzed by teams like Xu et al., shows promise for enhanced link reliability. The review further investigates multi-granularity onboard optical switching, a necessity for efficient traffic routing and resource management within dynamic satellite constellations. Research efforts, including those reviewed by Wu et al., address the complexities of implementing flexible switching fabrics capable of handling diverse data rates and protocols in a resource-constrained and radiation-hardened environment, often involving hybrid electro-optical approaches. Finally, we analyze large-scale elastic laser networking. As constellation sizes grow, the challenge of managing a highly dynamic topology with potentially thousands of nodes necessitates innovative networking paradigms beyond traditional terrestrial methods. Progress includes developing scalable control plane architectures that balance centralized coordination with distributed autonomy, as well as sophisticated techniques for dynamic routing, resource scheduling, and enhanced survivability. Notable work in this area includes the development of advanced survivability mechanisms like time window-based shared path protection designed for the specific dynamics of optical satellite networks by teams such as Yan et al. to maintain network resilience against frequent link state changes and failures. For each of these areas, we synthesize the state-of-the-art technological advancements and identify future evolution directions, analyzing the associated technical challenges from transmission, switching, and networking dimensions. The systematic analysis within this review is framed by a proposed multi-layered S-OTN architecture, which provides a functional basis for understanding the interactions and requirements across the orchestration, control, and transport planes essential for efficient management and coordination of the integrated spaceground network. Conclusions and Prospects S-OTN is progressively transitioning from technological verification towards engineering deployment and large-scale application. This review highlights that while significant progress has been made, in-depth and detailed explorations are still required across various technical fronts to fully realize the potential of S-OTN. Future research should focus on developing intelligent perception-driven adaptive optical communication mechanisms, integrated communication and control collaborative processing architectures, enhanced robustness and redundancy optimization schemes for non-ideal environments, unified electro-optical switching structures with efficient encapsulation mechanisms, resource self-organization capabilities, multi-level protection strategies, and the evolution of space-ground integrated control architectures towards multi-level collaboration. Addressing these challenges is crucial for enhancing the transmission efficiency, anti-interference capability, and resource utilization of S-OTN, thereby supporting the future F6G infrastructure while guiding the practical deployment of S-OTN. © 2025 Chinese Optical Society. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2386.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
