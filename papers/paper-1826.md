---
id: paper-1826
title: Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]
authors:
- Li, Jingyu
- Zhang, Zongzhe
- Yang, Jing
- Han, Lin
- Wang, Hao
- Wang, Yunping
- Gao, Hongwei
- Wang, Xiaojun
- Xu, Zuyan
venue: Zhongguo Jiguang/Chinese Journal of Lasers
venue_type: journal
year: 2025
doi: 10.3788/CJL240755
url: https://www.scopus.com/pages/publications/85218643434?origin=resultslist
publisher: Science Press
pages: ''
keywords:
- artificial intelligence
- cavity mirror tuning
- deep reinforcement learning
- solid-state laser
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
    my_justification: RL
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

# paper-1826 — Stabilization of Intelligent Laser Cavity Based on Deep Reinforcement Learning Algorithm; [基 于 深 度 强 化 学 习 算 法 的 激 光 腔 智 能 体 稳 定 技 术]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Objective High<sup>-</sup>power, high-beam-quality lasers have wide applications in industry, medicine, scientific research, and national defense. However, in practical applications, factors such as vibration shocks and environmental temperature changes can cause the cavity mirrors of the laser resonator to deviate, thus resulting in a phenomenon known as detuning. Consequently, the laser resonator no longer functions in the optimal operating state. First, it affects the fundamental mode operation, thereby deteriorating the output-beam quality. In severe cases, this may affect the safe operation of the laser. In recent years, owing to the continuous expansion of laser applications, the autonomous monitoring and optimization of lasers have been urgently demanded in scenarios such as unmanned factories, vibration environments, and space environments, where manual maintenance cannot be achieved easily in real time. Methods In this study, a dual<sup>-</sup>factor fusion evaluation criterion is proposed that reflects the operating state of a laser by calculating the beam power and morphology in real time, as well as by performing correlation calculations in the theoretical Gaussian optical<sup>-</sup>field mode, while considering both the mode<sup>-</sup>field distribution and output power of the laser. Subsequently, a mirror control scheme based on the proximal policy optimization (PPO) algorithm is proposed by combining the mode and intensity of the laser spot with the posture of the cavity mirror using deep reinforcement learning (DRL). This establishes an intelligent agent that can perceive and control the laser cavity. The experimental setup is shown in Fig. 2. Results and Discussions Generally, deviations in the cavity mirror not only decrease the laser power but may also damage certain optical components owing to the deviated optical path. As a side<sup>-</sup>pumped laser head is used in this experiment, the deviated laser beams may damage the end<sup>-</sup>face seal, thereby affecting the normal output of the measuring pump head. Therefore, we intervene in the active control when the power fluctuates within 3%‒5%. For the first 50% power loss, the output power of the laser is more sensitive to the misalignment angle of the cavity mirror (Fig. 3). The health status of the laser is described by a reward function that combines the beam quality and output power. A pretrained deep neural network using the DRL algorithm is employed to control the laser resonant cavity. The results show that the DRL<sup>-</sup>based laser control agent can intelligently stabilize a misaligned laser resonant cavity within seconds (Fig. 8). This method presents a path advantage over previous algorithms (Fig. 9). Figure 11 shows the stability test results for the resonant cavity agent within 30 min. The average output power is 90.7 W, with a root mean square (RMS) value of 0.95. This indicates that the output power is highly stable over a long period and that the operational decisions regarding the cavity mirror remain stable over time. A spot output with a high beam quality close to the diffraction limit is obtained (Fig. 10). Conclusions In this study, an intelligent laser<sup>-</sup>cavity stabilization technique based on a DRL algorithm is introduced and demonstrated. A deep neural network pretrained using the DRL algorithm is utilized to control the laser cavity. The results show that the DRL<sup>-</sup>based laser control agent can intelligently stabilize a misaligned laser cavity within seconds. This approach avoids the disadvantages of conventional control methods such as model building, variable decoupling, and parameter tuning. In addition to linear resonant cavities, the agent can be used for various other types of resonant cavities, including folded and ring cavities. Using a simple feedforward neural network architecture that requires minimal computational and storage resources, the agent is easy to integrate into embedded or edge computing devices, facilitating large<sup>-</sup>scale deployment of intelligent hardware. Compared with other optimization algorithms, the agent offers more efficient strategies and is thus applicable to higher<sup>-</sup>dimensional control problems. The perception and operational space of the laser can be extended by integrating artificial intelligence (AI)<sup>-</sup>based adjustment systems and multiple sensors. Such intelligent lasers can autonomously adjust the optical components based on real<sup>-</sup>time requirements and environmental changes, thereby achieving highly personalized laser outputs, enhancing the system robustness, and improving the laser performance metrics. In conclusion, the resonant-cavity control agent is crucial for the design, intelligent diagnosis, and state stabilization of future complex laser systems. Furthermore, it is expected to be applicable to the AI diagnosis and maintenance of laser systems in harsh environments such as deep seas and outer space. © 2025 Science Press. All rights reserved.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1826.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
