---
id: "paper-1826"
title: "Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]"
authors: ["Li, Jingyu", "Zhang, Zongzhe", "Yang, Jing", "Han, Lin", "Wang, Hao", "Wang, Yunping", "Gao, Hongwei", "Wang, Xiaojun", "Xu, Zuyan"]
year: 2025
venue: "Zhongguo Jiguang/Chinese Journal of Lasers"
venue_type: "journal"
doi: "10.3788/CJL240755"
url: "https://www.scopus.com/pages/publications/85218643434?origin=resultslist"
publisher: "Science Press"
pages: ""
keywords: ["artificial intelligence", "cavity mirror tuning", "deep reinforcement learning", "solid-state laser"]
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
    human_justification: "RL"

---

# paper-1826 — Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]

## Metadata

- **Authors:** Li, Jingyu and Zhang, Zongzhe and Yang, Jing and Han, Lin and Wang, Hao and Wang, Yunping and Gao, Hongwei and Wang, Xiaojun and Xu, Zuyan
- **Year:** 2025
- **Venue:** Zhongguo Jiguang/Chinese Journal of Lasers
- **DOI:** 10.3788/CJL240755
- **URL:** https://www.scopus.com/pages/publications/85218643434?origin=resultslist
- **Publisher:** Science Press
- **Pages:** 
- **Language:** Chinese
- **Keywords:** artificial intelligence; cavity mirror tuning; deep reinforcement learning; solid-state laser

### Abstract

Objective High<sup>-</sup>power, high-beam-quality lasers have wide applications in industry, medicine, scientific research, and national defense. However, in practical applications, factors such as vibration shocks and environmental temperature changes can cause the cavity mirrors of the laser resonator to deviate, thus resulting in a phenomenon known as detuning. Consequently, the laser resonator no longer functions in the optimal operating state. First, it affects the fundamental mode operation, thereby deteriorating the output-beam quality. In severe cases, this may affect the safe operation of the laser. In recent years, owing to the continuous expansion of laser applications, the autonomous monitoring and optimization of lasers have been urgently demanded in scenarios such as unmanned factories, vibration environments, and space environments, where manual maintenance cannot be achieved easily in real time. Methods In this study, a dual<sup>-</sup>factor fusion evaluation criterion is proposed that reflects the operating state of a laser by calculating the beam power and morphology in real time, as well as by performing correlation calculations in the theoretical Gaussian optical<sup>-</sup>field mode, while considering both the mode<sup>-</sup>field distribution and output power of the laser. Subsequently, a mirror control scheme based on the proximal policy optimization (PPO) algorithm is proposed by combining the mode and intensity of the laser spot with the posture of the cavity mirror using deep reinforcement learning (DRL). This establishes an intelligent agent that can perceive and control the laser cavity. The experimental setup is shown in Fig. 2. Results and Discussions Generally, deviations in the cavity mirror not only decrease the laser power but may also damage certain optical components owing to the deviated optical path. As a side<sup>-</sup>pumped laser head is used in this experiment, the deviated laser beams may damage the end<sup>-</sup>face seal, thereby affecting the normal output of the measuring pump head. Therefore, we intervene in the active control when the power fluctuates within 3%‒5%. For the first 50% power loss, the output power of the laser is more sensitive to the misalignment angle of the cavity mirror (Fig. 3). The health status of the laser is described by a reward function that combines the beam quality and output power. A pretrained deep neural network using the DRL algorithm is employed to control the laser resonant cavity. The results show that the DRL<sup>-</sup>based laser control agent can intelligently stabilize a misaligned laser resonant cavity within seconds (Fig. 8). This method presents a path advantage over previous algorithms (Fig. 9). Figure 11 shows the stability test results for the resonant cavity agent within 30 min. The average output power is 90.7 W, with a root mean square (RMS) value of 0.95. This indicates that the output power is highly stable over a long period and that the operational decisions regarding the cavity mirror remain stable over time. A spot output with a high beam quality close to the diffraction limit is obtained (Fig. 10). Conclusions In this study, an intelligent laser<sup>-</sup>cavity stabilization technique based on a DRL algorithm is introduced and demonstrated. A deep neural network pretrained using the DRL algorithm is utilized to control the laser cavity. The results show that the DRL<sup>-</sup>based laser control agent can intelligently stabilize a misaligned laser cavity within seconds. This approach avoids the disadvantages of conventional control methods such as model building, variable decoupling, and parameter tuning. In addition to linear resonant cavities, the agent can be used for various other types of resonant cavities, including folded and ring cavities. Using a simple feedforward neural network architecture that requires minimal computational and storage resources, the agent is easy to integrate into embedded or edge computing devices, facilitating large<sup>-</sup>scale deployment of intelligent hardware. Compared with other optimization algorithms, the agent offers more efficient strategies and is thus applicable to higher<sup>-</sup>dimensional control problems. The perception and operational space of the laser can be extended by integrating artificial intelligence (AI)<sup>-</sup>based adjustment systems and multiple sensors. Such intelligent lasers can autonomously adjust the optical components based on real<sup>-</sup>time requirements and environmental changes, thereby achieving highly personalized laser outputs, enhancing the system robustness, and improving the laser performance metrics. In conclusion, the resonant-cavity control agent is crucial for the design, intelligent diagnosis, and state stabilization of future complex laser systems. Furthermore, it is expected to be applicable to the AI diagnosis and maintenance of laser systems in harsh environments such as deep seas and outer space. © 2025 Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]
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
