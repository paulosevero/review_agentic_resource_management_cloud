---
title: "Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence"
authors:
  - name: Hannaneh B. Pasandi
    affiliation: University of California, Berkeley
    email: h.pasandi@berkeley.edu
  - name: Franck Rousseau
    affiliation: University of Grenoble Alpes
    email: Franck.Rousseau@imag.fr
  - name: Tamer Nadeem
    affiliation: Virginia Commonwealth University
    email: tnadeem@vcu.edu
  - name: Sina Darabi
    affiliation: Università della Svizzera italiana (USI)
    email: darabs@usi.ch
venue: "ACM Workshop on Access Networks with Artificial Intelligence (ANAI '25)"
year: 2025
publication_date: "November 4-8, 2025"
location: "Hong Kong, China"
doi: "10.1145/3737904.3768537"
license: "Creative Commons Attribution 4.0 International"
isbn: "979-8-4007-1981-3/2025/11"
keywords:
  - Satellite networks
  - Joint communication and sensing
  - Deep reinforcement learning
  - Federated learning
  - Large language models
  - Edge computing
abstract: "This paper presents simulation-based insights into Joint Communication and Sensing (JCAS) optimization for direct-to-satellite access networks. We investigate three complementary approaches: (i) a hierarchical deep reinforcement learning framework for satellite beamforming, achieving an 18% throughput gain over heuristic baselines; (ii) a multi-modal federated learning architecture fusing 10 m Sentinel-1 SAR with terrestrial sensing, providing a ∼ 15% detection accuracy improvement under ( ε, δ ) = ( 1 . 2 , 10⁻⁵ ) differential privacy guarantees; and (iii) a ground-based LLM-driven resource management system that reduces handover latency by 25% in vehicular mobility scenarios. Evaluations using NS-3, STK, TensorFlow, and OMNeT++ validate improvements with 95% confidence intervals across realistic traffic, IoT, and mobility settings. These results highlight opportunities and challenges for integrating AI techniques into satellite-terrestrial access networks, with implications for next-generation intelligent connectivity."
---

## Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence

Hannaneh B. Pasandi University of California, Berkeley h.pasandi@berkeley.edu

## Tamer Nadeem

Virginia Commonwealth University tnadeem@vcu.edu

## ABSTRACT

This paper presents simulation-based insights into Joint Communication and Sensing (JCAS) optimization for direct-to-satellite access networks. We investigate three complementary approaches: (i) a hierarchical deep reinforcement learning framework for satellite beamforming, achieving an 18% throughput gain over heuristic baselines; (ii) a multi-modal federated learning architecture fusing 10 m Sentinel-1 SAR with terrestrial sensing, providing a ∼ 15% detection accuracy improvement under ( ε, δ ) = ( 1 . 2 , 10⁻⁵ ) differential privacy guarantees; and (iii) a ground-based LLM-driven resource management system that reduces handover latency by 25% in vehicular mobility scenarios. Evaluations using NS-3, STK, TensorFlow, and OMNeT++ validate improvements with 95% confidence intervals across realistic traffic, IoT, and mobility settings. These results highlight opportunities and challenges for integrating AI techniques into satellite-terrestrial access networks, with implications for next-generation intelligent connectivity.

## CCS CONCEPTS

- Networks → Network protocols ; Network performance evaluation ; · Computing methodologies → Machine learning .

## KEYWORDS

Satellite networks, Joint communication and sensing, Deep reinforcement learning, Federated learning, Large language models, Edge computing

[This work is licensed under a Creative Commons Attribution 4.0 International License.](https://creativecommons.org/licenses/by/4.0/legalcode)

ANAI '25, November 4-8, 2025, Hong Kong, China © 2025 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-1981-3/2025/11 https://doi.org/10.1145/3737904.3768537

Franck Rousseau University of Grenoble Alpes Franck.Rousseau@imag.fr

## Sina Darabi

Università della Svizzera italiana (USI) darabs@usi.ch

## ACM Reference Format:

Hannaneh B. Pasandi, Franck Rousseau, Tamer Nadeem, and Sina Darabi. 2025. Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence. In ACM Workshop on Access Networks with Artificial Intelligence (ANAI '25), November 4-8, 2025, Hong Kong, China. ACM, New York, NY, USA, 5 pages. https://doi.org/10.1145/3737904.3768537

## 1 INTRODUCTION

LEO satellite constellations including SpaceX's Starlink and Amazon's Project Kuiper have expanded global communications infrastructure [12]. Recent measurement studies of operational Starlink networks demonstrate 20-40ms latency and 50-200 Mbps throughput capabilities [15 ? ], validating LEO potential for real-time applications. With IoT devices projected to reach 29 billion by 2030 [6], direct-to-satellite communication addresses connectivity gaps in remote areas, with comprehensive surveys highlighting both advances and implementation challenges [ ? ].

Recent AI advances enable network optimization through deep learning for beamforming [10] and resource management [ ? ]. Large Language Models offer potential for context-aware satellite resource allocation processing ground-based textual inputs [14].

Joint Communication and Sensing (JCAS) enables simultaneous use of radio resources for communication and sensing functions [13]. In satellite networks, JCAS faces unique challenges: (1) rapid topology changes from satellite orbital dynamics at 7.5 km/s; (2) propagation delays of 20-40ms one-way for LEO satellites compared to 250ms one-way for GEO satellites; (3) power constraints of 10-50W per satellite; (4) heterogeneous ground terminals from IoT sensors to vehicles; (5) terrestrial network integration requirements [1, 17].

This paper contributes a unified AI-driven JCAS framework integrating: i) A hierarchical deep reinforcement learning framework for satellite beamforming optimization validated on constellations up to 2,400 satellites with detailed energy modeling. ii) A multi-modal federated learning architecture fusing 10m resolution SAR with terrestrial sensing while preserving privacy through ( ε, δ ) -differential privacy. iii) A ground-based LLM system using optimized 6.7B parameter models processing traffic reports for vehicle trajectory prediction with comprehensive baseline comparisons. iv) Integrated system architecture demonstrating 31% energy efficiency improvement through coordinated AI components with quantified information exchange overhead and synergistic performance analysis. v) Simulation validation using NS-3, STK, and TensorFlow with statistical analysis and energy consumption models across realistic large-scale scenarios.

## 2 SYSTEM MODEL AND ENERGY MODELING

Consider a satellite-terrestrial network with Nₛ LEO satellites (66-2,400 range), Nₘ ground terminals, and Nᵥ vehicles. Each satellite has phased arrays generating B = 8 beams with 30W maximum power.

The satellite-ground channel incorporates path loss and Doppler-shifted phase:

<!-- formula-not-decoded -->

Total system energy consumption includes satellite transmission, processing, and ground infrastructure:

<!-- formula-not-decoded -->

where satellite transmission power Pₜₓ,ₛ = ∑ᴮᵦ₌₁ Pₛ,ᵦ, processing power Pₚᵣₒc,ₛ = 2 . 5 W (validated against Xilinx Zynq UltraScale+ specifications for space-qualified processors [8]), and ground infrastructure Pₘᵣₒᵤₙ𝒹 includes gateway stations (1.2 kW each, based on Intelsat gateway specifications [12]) and LLM servers (measured 45W for quantized model on NVIDIA A6000 [16]). Sensitivity Analysis: ±50% processor power variation affects total energy efficiency by <8%, validating robustness of our energy model across different satellite hardware configurations. Energy efficiency is measured as:

<!-- formula-not-decoded -->

The JCAS optimization problem with normalized objectives:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where Cₜₒₜₐₗ and Sₜₒₜₐₗ normalize communication capacity and sensing performance, with weights λc = 0 . 7 , λₛ = 0 . 3 selected through grid search validation.

## 3 AI-DRIVEN BEAMFORMING FRAMEWORK

Hierarchical Reinforcement Learning. We implement a two-level framework: constellation-level coordination using PPO (actor-critic with 512-256 hidden layers, Adam optimizer, learning rate 3e-4) and satellite-level beam management using DDPG (actor/critic networks: 256-128 layers, replay buffer: 1M samples, soft update =0.005). The state space includes channel matrix Hₜ ∈ ℝ^(Nₘ×Nₛ), traffic demands Dₜ ∈ ℝ^Nₘ, queue status Qₜ, sensing priorities Eₜ, orbital positions Oₜ, and connectivity matrix Wₜ ∈ {0, 1}^(Nₛ×Nₛ).

The reward function balances throughput and sensing:

<!-- formula-not-decoded -->

Implementation and Comprehensive Baseline Comparison. We use NS-3 v3.36, STK 12.3, TensorFlow 2.11 on 4 NVIDIA V100 GPUs. Training: 5,000 episodes × 60 minutes each, requiring 36 hours. Constellation parameters: 66-2,400 satellites, 20 GHz Ka-band, 500 MHz total bandwidth, 64×64 phased arrays.

Baselines. We compare against four approaches:

i) Heuristic proportional fair allocation ii) Q-learning with ε-greedy exploration [7] iii) Convex optimization using interior-point methods [3] iv) Random beam allocation

With QPSK modulation and 3/4 coding rate (2.25 bps/Hz theoretical), our approach achieves 8.9 Gbps system throughput (avg 3.56 bps/Hz accounting for fading, interference) compared to baselines: heuristic 7.5 Gbps, Q-learning 7.9 Gbps, convex optimization 8.1 Gbps, random 5.2 Gbps. This represents 18% improvement over heuristic, 12% over Q-learning, and 10% over convex methods. Sensing accuracy: 68.2% vs baselines (heuristic 57.8%, Q-learning 61.2%). Energy efficiency: 2.8 Mbits/J vs 2.4 Mbits/J (heuristic) representing 15% improvement.

Large-scale testing up to 2,400 satellites demonstrates algorithmic scalability with <15% performance degradation, as shown in Figure 1(b). This scale approaches Starlink Phase 1 deployment targets, validating practical relevance.

## 4 MULTI-MODAL EDGE INTELLIGENCE

Federated Learning with Privacy-Utility Analysis. Our architecture fuses Sentinel-1 SAR (10m resolution), Wi-Fi CSI, and IoT sensors through federated learning. Each edge node trains locally with differential privacy noise injection achieving ( ε, δ ) = ( 1 . 2 , 10⁻⁵ ) -DP:

<!-- formula-not-decoded -->

where σ = 0 . 8 calibrated using privacy accounting [2].

Privacy-Utility Tradeoff Analysis: We define utility as F1-score for object detection across privacy levels. Our analysis reveals: strong privacy ( ε = 0 . 5) reduces F1-score to 0.62 but provides formal privacy guarantees against membership inference attacks; moderate privacy ( ε = 1 . 2) achieves F1 = 0.68 representing 18% improvement over SAR-only baseline (F1 = 0.58) while maintaining reasonable privacy protection; weak privacy ( ε = 2 . 0) achieves F1 = 0.71 but increases vulnerability to reconstruction attacks. The noise variance σ = 0 . 8 ensures composition privacy under 100 federation rounds. Communication overhead scales linearly with privacy level: stronger privacy requires larger noise, increasing model updates from 2.1MB ( ε = 2 . 0) to 2.6MB ( ε = 0 . 5) per round.

The privacy-utility analysis in Figure 2(b) demonstrates that our chosen ε = 1 . 2 provides meaningful privacy protection while achieving significant utility improvements over single-modality approaches.

Testing scales up to 250 edge nodes across urban/rural scenarios validates federated convergence. Communication overhead: 2.3 MB per federation round vs 15.2 MB for centralized approaches-an 85% reduction.

## 5 GROUND-BASED LLM RESOURCE MANAGEMENT

Architecture and Optimized Deployment. Our system processes traffic reports using a ground-deployed 6.7B parameter model (LLaMA-2 architecture) with 4-bit quantization and tensor parallelism [5]. The LLM runs on terrestrial edge servers with measured power consumption: 45W average (including cooling), 38W inference-only on NVIDIA A6000 GPUs [16].

Computational Overhead Analysis: LLM inference latency: 180ms for 1024-token contexts vs LSTM: 45ms for equivalent trajectory prediction. However, LLM processing occurs offline during non-critical periods (traffic report updates every 5-10 minutes), while LSTM requires real-time processing during handover events. Total system latency benefits from LLM's superior prediction accuracy (reducing handover frequency by 18%) offsetting the higher per-inference cost. The 25% latency improvement reflects end-to-end handover completion time, not individual model inference time.

Trajectory prediction combines LLM context with kinematic models:

<!-- formula-not-decoded -->

where α = 0 . 25 (empirically tuned) weights LLM contributions.

Comprehensive ML Baseline Comparison. We compare against:

i) LSTM-based trajectory prediction (3-layer, 512 hidden units) [9] ii) Random Forest ensemble (100 trees) [4] iii) Traditional Kalman filtering [11] iv) Static resource allocation

Testing on SUMO traffic simulation (up to 1,000 vehicles) and OMNeT++ satellite networks shows our LLM approach achieves 135ms average handover latency vs baselines: LSTM 180ms, Random Forest 195ms, Kalman 210ms, static 245ms. This represents 25% improvement over LSTM and 43% over Kalman methods.

Handover Success Definition: Successful handover requires: (1) <500ms total switching time; (2) <1% packet loss during transition; (3) maintained QoS requirements post-handover. Success rate: LLM 78% vs LSTM 65%, Random Forest 62%, Kalman 59%.

Figure 3 demonstrates consistent performance advantages of the LLM approach across different vehicle speeds and over 24-hour operational cycles, with 25% latency reduction and 20% higher success rates compared to LSTM baselines.

## 6 INTEGRATED SYSTEM EVALUATION

Information Flow and Integration Assumptions. Under coordinated operation with 5-minute information exchange intervals (aligned with 3GPP NTN standards for satellite network management [1]), the three AI components integrate as follows: (i) Federated learning produces regional traffic density maps ρ ( x,y, t ) updated every 5 minutes following established traffic monitoring protocols [12]; (ii) LLM generates mobility prediction vectors vₚᵣₑ𝒹 ( t + Δt ) for 15-minute horizons (typical vehicle trajectory prediction window [15]); (iii) DRL beamforming incorporates both density maps and mobility predictions as additional state features: sᵢₙₜₑₘᵣₐₜₑ𝒹 = [ sᵦₐₛᵢc , ρₗₒcₐₗ , vₚᵣₑ𝒹 ] where sᵦₐₛᵢc includes original channel and queue states.

Integration Overhead: Information exchange adds 2.1MB /5min bandwidth (consistent with satellite telemetry data rates [12]) and 150ms processing latency for density map compression and mobility vector updates (typical edge computing processing times [ ? ]). These overheads are acceptable given the 5-minute update cycle and terrestrial backbone capacity.

Synergistic Performance Analysis. Figure 4 compares standalone vs. integrated system performance under varying mobility scenarios. The integrated system achieves additional 8% energy efficiency improvement over standalone DRL by reducing unnecessary beam switches (predicted via LLM mobility forecasting) and 12% sensing accuracy improvement by focusing SAR collection on high-traffic regions identified through federated density maps.

Figure 4: Integrated system achieves 8% higher energy efficiency through coordinated sensing-beamforming vs. standalone approaches.

## 7 COMPREHENSIVE ANALYSIS

Performance Summary and Energy Analysis. Table 1 presents validated results with comprehensive baselines and detailed energy modeling. We measure energy efficiency as successful packet transmissions per Joule, normalized by satellite transmit power and edge server consumption. Energy efficiency calculated using Eq. (3) with measured power consumption values from space-qualified hardware specifications and ground infrastructure requirements.

Starlink Validation: Our simulation parameters align with published Starlink measurements [15 ? ]: latency ranges (20-50ms), throughput variability (20-200 Mbps), and handover frequency (every 15-60 seconds) match empirical observations, increasing confidence in simulation realism.

Scalability and Real-World Validation Large-scale testing up to 2,400 satellites (approaching Starlink Phase 1 scale) demonstrates algorithmic scalability. Performance degradation remains <15% when scaling from 66 to 2,400 satellites, validating the hierarchical approach for practical deployment.

Limitations and Future Validation: While simulation-based evaluation provides controlled analysis across large scales, real-world deployment faces additional challenges: atmospheric effects, regulatory constraints, and hardware imperfections not fully captured in simulation. Future work should include: (i) testbed validation using software-defined radios and satellite emulators; (ii) partnership with satellite operators for limited field trials; (iii) validation of AI model robustness under real channel conditions and interference patterns. Implementation challenges include: satellite processor limitations (1-10 GFLOPS), requiring 8× model compression; thermal management in space environment; radiation hardening costs ($50K-100K per satellite) [8]; ground infrastructure scaling (1 gateway per 1,000 users).

Table 1: Performance comparison with comprehensive baselines and energy modeling

| Metric                                                                                                                                                                                                                 | Topic 1 DRL Beamform                                                                                | Topic 2 Multi-Modal                                                                     | Topic 3 LLM Ground                                                                                | Integrated System                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Primary Improvement vs. Q-Learning/LSTM vs. Convex/Random Forest Energy Efficiency (Mbits/J) Baseline Energy (Mbits/J) Energy Improvement Max Tested Scale Privacy Protection Training/Setup Time Integration Overhead | 18% ± 2.1% 12% ± 1.8% 10% ± 1.5% 2.8 ± 0.15 2.4 ± 0.12 15% ± 2.0% 2,400 satellites N/A 36 hours N/A | 15% ± 2.5% N/A N/A 1.9 ± 0.12 1.7 ± 0.10 12% ± 1.5% 250 nodes ε = 1 . 2 DP 18 hours N/A | 25% ± 2.2% 25% ± 3.2% 31% ± 3.8% 1.6 ± 0.18 1.4 ± 0.15 14% ± 2.2% 1,000 vehicles N/A 12 hours N/A | 31% ± 2.8% 35% ± 3.5% 38% ± 4.1% 3.2 ± 0.18 2.4 ± 0.15 31% ± 3.1% 400 satellites ε = 1 . 2 DP 48 hours 2.1 MB/5min |

Future Research Directions Promising directions include hardware-software co-design for satellite AI processing, quantum-enhanced optimization algorithms, neuromorphic computing for power efficiency, and integration with 6G terrestrial networks. Standardization through 3GPP NTN evolution [1] and regulatory frameworks will be critical for practical deployment at megaconstellation scale.

## REFERENCES

- [1] 3GPP. 2023. Study on Non-Terrestrial Networks (NTN) - Release 17 . Technical Report TR 38.821 V17.0.0. 3rd Generation Partnership Project.
- [3] Stephen Boyd, Stephen P Boyd, and Lieven Vandenberghe. 2004. Convex optimization . Cambridge university press.
- [2] Martin Abadi, Andy Chu, Ian Goodfellow, H Brendan McMahan, Ilya Mironov, Kunal Talwar, and Li Zhang. 2016. Deep learning with differential privacy. In Proceedings of the 2016 ACM SIGSAC conference on computer and communications security . 308-318.
- [4] Leo Breiman. 2001. Random forests. Machine learning 45, 1 (2001), 5-32.
- [6] Ericsson. 2023. Ericsson Mobility Report: Q4 2023 Update. White Paper. Available: https://www.ericsson.com/mobility-report.
- [5] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. 2023. QLoRA: Efficient finetuning of quantized LLMs. Advances in Neural Information Processing Systems 36 (2023), 10088-10115.
- [7] Paulo VR Ferreira, Randy Paffenroth, Alexander M Wyglinski, Timothy M Hackett, Sven G Bilen, Richard C Reinhart, and Dale J Mortensen. 2022. Reinforcement learning for satellite communications: From LEO to deep space operations. IEEE Communications Magazine 60, 10 (2022), 92-98.
- [9] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. Neural computation 9, 8 (1997), 1735-1780.
- [8] Alan D George and Conner M Wilson. 2019. Space-qualified processing architectures for satellite applications. In Proceedings IEEE Aerospace Conference . IEEE, 1-12.
- [10] Hongji Huang, Yaxiong Song, Jian Yang, Guan Gui, and Fumiyuki Adachi. 2021. Deep-learning-based millimeter-wave massive MIMO for hybrid precoding. IEEE Transactions on Vehicular Technology 70, 3 (2021), 3027-3032.
- [11] Rudolph Emil Kalman. 1960. A new approach to linear filtering and prediction problems. Journal of basic Engineering 82, 1 (1960), 35-45.
- [13] Fan Liu, Yuanhao Cui, Christos Masouros, Jie Xu, Tony X Han, Yonina C Eldar, and Stefano Buzzi. 2022. Integrated sensing and communications: Toward dual-functional wireless networks for 6G and beyond. IEEE Journal on Selected Areas in Communications 40, 6 (2022), 1728-1767.
- [12] Oltjon Kodheli, Eva Lagunas, Nicola Maturo, Shree Krishna Sharma, Bhavani Shankar, Juan Fernando Montoya Montoya, James C M Duncan, Danilo Spano, Symeon Chatzinotas, Steven Kisseleff, Jorge Querol, Lei Lei, Thang X Vu, and George Goussetis. 2021. Satellite communications in the new space era: A survey and future challenges. IEEE Communications Surveys & Tutorials 23, 1 (2021), 70-109.
- [14] Sifan Long, Jingjing Tan, Bomin Mao, Fengxiao Tang, Yangfan Li, Ming Zhao, and Nei Kato. 2024. A Survey on Intelligent Network Operations and Performance Optimization Based on Large Language Models. IEEE Communications Surveys & Tutorials (2024). https://doi.org/10.1109/COMST.2024.3526606 Early Access.
- [16] NVIDIA. 2023. NVIDIA A6000 Power and Performance Specifications. Technical Specification. Available: https://www.nvidia.com/en-us/design-visualization/rtx-a6000/.
- [15] Florian Michel, Simon Kassing, Thomas Holterbach, and Adrian Perrig. 2022. Performance characterization of LEO satellite networks: A Starlink-based measurement study. IEEE/ACM Transactions on Networking 30, 6 (2022), 2374-2387.
- [17] J Andrew Zhang, Fan Liu, Christos Masouros, Robert W Heath, Zhiyong Feng, Linling Zheng, and Athina Petropulu. 2021. An overview of signal processing techniques for joint communication and radar sensing. IEEE Journal of Selected Topics in Signal Processing 15, 6 (2021), 1295-1315.
