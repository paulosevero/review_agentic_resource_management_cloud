---
id: paper-1927
title: Dynamic Spectrum Access Algorithm for Evaluating Spectrum Stability in Cognitive Vehicular Networks.; [认知车联网中评估频谱稳定性的动态频谱接入算法]
authors:
- Ma, Bin
- Yang, Zumin
- Xie, Xianzhong
venue: Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
venue_type: journal
year: 2025
doi: 10.11999/JEIT240927
url: https://www.scopus.com/pages/publications/105007504749?origin=resultslist
publisher: Science Press
pages: 1474--1485
keywords:
- Cognitive Vehicular Network(CVN)
- Dynamic Spectrum Access(DSA)
- Reinforcement learning
- Stability assessment
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

# paper-1927 — Dynamic Spectrum Access Algorithm for Evaluating Spectrum Stability in Cognitive Vehicular Networks.; [认知车联网中评估频谱稳定性的动态频谱接入算法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Objective With the exponential growth of vehicle terminals and the widespread adoption of cognitive vehicular network applications, the existing licensed spectrum resources are inadequate to meet the communication demands of Cognitive Vehicular Networks (CVN). The rapid development of CVN and the increasing complexity of vehicular communication scenarios have intensified spectrum resource scarcity. Dynamic Spectrum Access (DSA) technology has emerged as a key solution to alleviate this scarcity by enabling efficient use of underutilized spectrum bands. While current DSA algorithms ensure basic spectrum utilization, they struggle to comprehensively evaluate spectrum stability and meet the differentiated stability requirements of vehicular network applications. For example, safety-critical applications such as collision avoidance systems demand ultra-reliable, low-latency communication, while infotainment applications prioritize high throughput. This paper proposes a novel framework integrating spectrum stability assessment with deep reinforcement learning. The framework constructs a multi-dimensional parameter-based model for spectrum stability, designs a reinforcement learning architecture incorporating gated mechanisms and dueling neural networks, and establishes a dynamically adaptive reward function to enable intelligent spectrum resource allocation. This research offers a solution for vehicular network spectrum management that combines theoretical depth with practical engineering value, paving the way for more reliable and efficient vehicular communication systems. Methods This study employs an integrated approach to address the spectrum allocation challenges in CVN. A time-series prediction model is developed using Long Short-Term Memory (LSTM) neural networks, which leverage three-dimensional time-series data of Signal-to-Noise Ratio (SNR), Received Signal Strength (RSS), and bandwidth to make multi-step predictions for future cycles. The rate of change for each parameter is calculated as a stability evaluation metric, providing a quantitative measure of spectrum stability. To ensure consistency in the evaluation process, the rate of change for each parameter is normalized using Min-Max normalization, and the standardized results are input into the K-Means algorithm for stability clustering of the rate-of-change vectors. By calculating the centroid coordinates of each cluster and their norms, a stability index is derived, forming the stability assessment model. Building upon the Deep Q-Network (DQN), a Gated Recurrent Unit (GRU) is introduced to create a temporal state encoder that captures the temporal dependencies in spectrum data. Additionally, a Dueling Network architecture is employed to decouple the state value and action advantage functions, enabling more accurate estimation of the long-term value of spectrum allocation decisions. The reward function incorporates trade-off coefficients to achieve a reasonable allocation of spectrum resources with different stability levels, ensuring a balance between spectrum utilization and collision probability while meeting the diverse stability requirements of vehicular network applications. The proposed framework is designed to be scalable and adaptable to various vehicular network scenarios, including urban, highway, and rural environments. Results and Discussions Simulation results show that the optimized stepwise prediction algorithm significantly improves performance. In both the training and test sets, the algorithm achieves a Root Mean Squared Error (RMSE) of less than 0.1, with no significant overfitting observed (Fig. 5, Fig. 6). This indicates that the algorithm generalizes well to unseen data, making it suitable for real-world deployment. Additionally, the loss function of the proposed algorithm decreases significantly as the number of iterations increases, converging around 150 iterations (Fig. 7). The prediction accuracy also stabilizes around 150 iterations (Fig. 8), suggesting that the algorithm achieves consistent performance within a reasonable training period. These results demonstrate that the proposed prediction algorithm can deliver high-accuracy multi-step predictions for stability parameters across a sufficient number of channels, providing a solid foundation for spectrum stability assessment. Furthermore, the proposed access algorithm consistently outperforms comparative algorithms in terms of spectrum utilization over 20 iterations, while maintaining lower collision probabilities (Fig. 9, Fig. 10). As the number of iterations increases, the cumulative stability index and throughput of the proposed algorithm steadily improve, exceeding the performance of comparative algorithms at all stages. This demonstrates that the proposed algorithm can meet the diverse requirements of vehicle terminals for channel stability and throughput, while ensuring high spectrum utilization and low collision probability. As the number of vehicle terminals increases, the proposed algorithm exhibits faster convergence compared to other algorithms, confirming its robustness in large-scale scenarios. These findings highlight the potential of the proposed framework to meet the growing demands of next-generation vehicular networks. Conclusions This study proposes an integrated “evaluation-decision-optimization” spectrum management paradigm for CVN. By proposing a multi-dimensional time-series feature-based spectrum stability quantification framework and designing a hybrid deep reinforcement learning architecture incorporating gated mechanisms and dueling networks, the research addresses the critical challenge of balancing spectrum efficiency with stability in dynamic vehicular environments. The development of an interpretable reward function enables intelligent spectrum allocation that adapts to diverse quality-of-service requirements, ensuring that both safety-critical and non-safety-critical applications receive the necessary resources. Experimental results show significant improvements in spectrum utilization, collision probability, and system throughput compared to traditional approaches, while maintaining robust performance in large-scale scenarios. These findings advance the theoretical understanding of spectrum management in CVN and provide a practical framework for implementing adaptive DSA solutions in next-generation intelligent transportation systems. Future research will explore extending the proposed framework to support multi-agent scenarios, where multiple vehicles and infrastructure nodes collaboratively optimize spectrum allocation. Additionally, integrating edge computing and federated learning techniques could further enhance the scalability and efficiency of the framework. The proposed methodology offers a scalable and efficient approach to spectrum resource allocation, paving the way for more reliable and high-performance vehicular communication networks. © 2025 Science Press. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1927.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
