---
id: "paper-211"
title: "Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]"
authors: ["Jiang, Yu-Bin", "Liu, Quan", "Hu, Zhi-Hui"]
year: 2020
venue: "Jisuanji Xuebao/Chinese Journal of Computers"
venue_type: "journal"
doi: "10.11897/SP.J.1016.2020.01897"
url: "https://www.scopus.com/pages/publications/85092468719?origin=resultslist"
publisher: "Science Press"
pages: "1897--1908"
keywords: ["Actor-critic algorithm", "Deep learning", "Maximum entropy", "Policy gradient", "Reinforcement learning"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-211 — Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]

## Metadata

- **Authors:** Jiang, Yu-Bin and Liu, Quan and Hu, Zhi-Hui
- **Year:** 2020
- **Venue:** Jisuanji Xuebao/Chinese Journal of Computers
- **DOI:** 10.11897/SP.J.1016.2020.01897
- **URL:** https://www.scopus.com/pages/publications/85092468719?origin=resultslist
- **Publisher:** Science Press
- **Pages:** 1897--1908
- **Language:** Chinese
- **Keywords:** Actor-critic algorithm; Deep learning; Maximum entropy; Policy gradient; Reinforcement learning

### Abstract

In recent years, Deep Reinforcement Learning (DRL) combines deep learning with reinforcement learning, and has become one of the research hotspots in the field of artificial intelligence. Deep learning combines intensive learning with amazing results in robot control, Atari 2600 games and more. The first algorithm that combines reinforcement learning with deep learning is TD-Gammon, which surpasses professional chess players in the problem of backgammon. Then there is a series of algorithms from Deep Q-Network (DQN), which has achieved extraordinary performance in Atari 2600 games. But limited by the value function method, DQN cannot be applied to continuous motion tasks. Therefore, the Actor-Critic (AC) algorithm is widely used in DRL because of its excellent scalability. It consists of two parts: the actor and the critic. Usually, the critic uses value function methods to evaluate the action, and the actor uses policy gradient methods for the action generation. This means that the AC method can be applied to continuous motion and discrete motion tasks. Researchers have proposed many AC algorithms, such as Asynchronous Advantage Actor-Critic (A3C) using asynchronous updates, Advantage Actor-Critic (A2C) using multi-agent updates, and Proximal Policy Optimization (PPO) with guaranteed policy improvement. One of the core challenges in reinforcement learning (RL) is how to balance the exploration and exploitation. In order to ensure a high return, the algorithm needs to find those actions that expect high returns in the experience explored in the past. The Immediate rewards for certain actions are high but their expected return is low, and the Agent needs to explore all untraversed actions to prevent the policy from entering local optimum. In other words, the Agent must use the previous experience to obtain higher expectations, and on the other hand must explore to find better action options. In the policy gradient, the maximum entropy regularity term is usually used to increase the randomness of the policy to ensure exploration. The randomness of the policy enables the Agent to traverse all the actions but it will cause the underestimation of the value function and affect the convergence speed and stability of the algorithm. In order to solve the underestimation problem caused by the maximum entropy regular term in the policy gradient, the Maximum-Entropy Correction (MEC) algorithm is proposed. The algorithm has two characteristics: (1) constructing a state action value function estimation using state value function and policy function, the constructed state action value function satisfies the distribution of the real value function; (2) The Berman optimal equation is combined with the constructed state action value function as the objective function of the MEC algorithm. The performance degradation and instability caused delete u the maximum entropy regular term can be solved by using the new objective function MEC algorithm. In order to verify the effectiveness of the algorithm, the algorithm was compared with PPO and A2C on the seven Atari 2600 games: BeamRide, Breakout, Enduro, Pong, Qbert, Seaquest and SpaceInvaders. Experimental results show that MEC improves the stability of the algorithm while improving performance. © 2020, Science Press. All right reserved.

## 04 — Title Screening

**Title:** Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Actor-Critic Algorithm with Maximum-Entropy Correction; [带最大熵修正的行动者评论家算法]
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
