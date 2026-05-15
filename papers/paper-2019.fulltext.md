---
paper_id: "paper-2019"
source_pdf_sha: "680e37d123d1cb4ac287b9e59aea5c6326e5a21214bf8c0519f0bbc706671f1b"
extraction_quality: high
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 8
  page_count: 5
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-2019 — fulltext
## §unknown-1

Beyond Terrestrial: LLM-Orchestrated DtS-IoT
Networks for Ubiquitous Edge Intelligence
Hannaneh B. Pasandi
University of California, Berkeley
h.pasandi@berkeley.edu
Franck Rousseau
University of Grenoble Alpes
Franck.Rousseau@imag.fr
Tamer Nadeem
Virginia Commonwealth University
tnadeem@vcu.edu
Sina Darabi
Università della Svizzera italiana (USI)
darabs@usi.ch
ABSTRACT
This paper presents simulation-based insights into Joint Com-
munication and Sensing (JCAS) optimization for direct-to-
satellite access networks. We investigate three complemen-
tary approaches: (i) a hierarchical deep reinforcement learn-
ing framework for satellite beamforming, achieving an 18%
throughput gain over heuristic baselines; (ii) a multi-modal
federated learning architecture fusing 10 m Sentinel-1 SAR
with terrestrial sensing, providing a∼15% detection accuracy
improvement under (𝜀, 𝛿) = (1.2, 10−5) differential privacy
guarantees; and (iii) a ground-based LLM-driven resource
management system that reduces handover latency by 25%
in vehicular mobility scenarios. Evaluations using NS-3, STK,
TensorFlow, and OMNeT++ validate improvements with 95%
confidence intervals across realistic traffic, IoT, and mobility
settings. These results highlight opportunities and challenges
for integrating AI techniques into satellite-terrestrial access
networks, with implications for next-generation intelligent
connectivity.
CCS CONCEPTS
•Networks → Network protocols; Network performance
evaluation; •Computing methodologies → Machine learn-
ing.
KEYWORDS
Satellite networks, Joint communication and sensing, Deep
reinforcement learning, Federated learning, Large language
models, Edge computing
This work is licensed under a Creative Commons Attribution 4.0 
Interna-tional License.
ANAI ’25, November 4–8, 2025, Hong Kong, China
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1981-3/2025/11
https://doi.org/10.1145/3737904.3768537
ACM Reference Format:
Hannaneh B. Pasandi, Franck Rousseau, Tamer Nadeem, and Sina
Darabi. 2025. Beyond Terrestrial: LLM-Orchestrated DtS-IoT Net-
works for Ubiquitous Edge Intelligence. In ACM Workshop on Ac-
cess Networks with Artificial Intelligence (ANAI ’25), November 4–
8, 2025, Hong Kong, China. ACM, New York, NY, USA, 5 pages.
https://doi.org/10.1145/3737904.3768537

## §1 INTRODUCTION

LEO satellite constellations including SpaceX’s Starlink and
Amazon’s Project Kuiper have expanded global communi-
cations infrastructure [12]. Recent measurement studies of
operational Starlink networks demonstrate 20-40ms latency
and 50-200 Mbps throughput capabilities [15? ], validating
LEO potential for real-time applications. With IoT devices
projected to reach 29 billion by 2030 [6], direct-to-satellite
communication addresses connectivity gaps in remote areas,
with comprehensive surveys highlighting both advances and
implementation challenges [? ].
Joint Communication and Sensing (JCAS) enables simul-
taneous use of radio resources for communication and sens-
ing functions [13]. In satellite networks, JCAS faces unique
challenges: (1) rapid topology changes from satellite orbital
dynamics at 7.5 km/s; (2) propagation delays of 20-40ms one-
way for LEO satellites compared to 250ms one-way for GEO
satellites; (3) power constraints of 10-50W per satellite; (4)
heterogeneous ground terminals from IoT sensors to vehi-
cles; (5) terrestrial network integration requirements [1, 17].
Recent AI advances enable network optimization through
deep learning for beamforming [10] and resource manage-
ment [? ]. Large Language Models offer potential for context-
aware satellite resource allocation processing ground-based
textual inputs [14].
This paper contributes a unified AI-driven JCAS frame-
work integrating: i) A hierarchical deep reinforcement
learning framework for satellite beamforming optimization
validated on constellations up to 2,400 satellites with de-
tailed energy modeling. ii) A multi-modal federated learn-
ing architecture fusing 10m resolution SAR with terrestrial
41
ANAI ’25, November 4–8, 2025, Hong Kong, China Hannaneh B. Pasandi, Franck Rousseau, Tamer Nadeem, and Sina Darabi
sensing while preserving privacy through (𝜖, 𝛿)-differential
privacy. iii) A ground-based LLM system using optimized
6.7B parameter models processing traffic reports for vehicle
trajectory prediction with comprehensive baseline compar-
isons. iv) Integrated system architecture demonstrating 31%
energy efficiency improvement through coordinated AI com-
ponents with quantified information exchange overhead and
synergistic performance analysis. v) Simulation validation
using NS-3, STK, and TensorFlow with statistical analysis
and energy consumption models across realistic large-scale
scenarios.

## §2 SYSTEM MODEL AND ENERGY

MODELING
Consider a satellite-terrestrial network with𝑁𝑠 LEO satellites
(66-2,400 range), 𝑁𝑔 ground terminals, and 𝑁𝑣 vehicles. Each
satellite has phased arrays generating𝐵= 8beams with 30W
maximum power.
The satellite-ground channel incorporates path loss and
Doppler-shifted phase:
ℎ𝑠,𝑔 (𝑡)=
√︃
𝑃𝐿(𝑑 𝑠,𝑔 (𝑡)) ·𝛼 𝑠,𝑔 (𝑡) ·𝑒 𝑗(𝜙 0+2𝜋 𝑓𝐷 (𝑡)𝑡) (1)
Total system energy consumption includes satellite trans-
mission, processing, and ground infrastructure:
𝐸𝑡𝑜𝑡𝑎𝑙 =
𝑁𝑠∑︁
𝑠=1
(𝑃𝑡𝑥,𝑠 +𝑃 𝑝𝑟𝑜𝑐,𝑠 ) ·𝑇+𝑃 𝑔𝑟𝑜𝑢𝑛𝑑 ·𝑇(2)
where satellite transmission power 𝑃𝑡𝑥,𝑠 = Í𝐵
𝑏=1 𝑃𝑠,𝑏, pro-
cessing power 𝑃𝑝𝑟𝑜𝑐,𝑠 = 2.5𝑊 (validated against Xilinx Zynq
UltraScale+ specifications for space-qualified processors [8]),
and ground infrastructure 𝑃𝑔𝑟𝑜𝑢𝑛𝑑 includes gateway stations
(1.2 kW each, based on Intelsat gateway specifications [12])
and LLM servers (measured 45W for quantized model on
NVIDIA A6000 [16]).Sensitivity Analysis:±50% proces-
sor power variation affects total energy efficiency by <8%,
validating robustness of our energy model across different
satellite hardware configurations. Energy efficiency is mea-
sured as:
𝜂= Successful Operations×Data Volume (bits)
𝐸𝑡𝑜𝑡𝑎𝑙 (Joules) (3)
The JCAS optimization problem with normalized objec-
tives:
max
P,W
𝜆𝑐
∑︁
𝑔
𝑅𝑔/𝐶𝑡𝑜𝑡𝑎𝑙 +𝜆 𝑠
∑︁
𝑟
𝐴𝑟 /𝑆𝑡𝑜𝑡𝑎𝑙 (4)
s.t.
∑︁
𝑏
𝑃𝑠,𝑏 ≤𝑃 𝑚𝑎𝑥 ,∀𝑠;𝜆 𝑐 +𝜆 𝑠 =1(5)
where 𝐶𝑡𝑜𝑡𝑎𝑙 and 𝑆𝑡𝑜𝑡𝑎𝑙 normalize communication capacity
and sensing performance, with weights 𝜆𝑐 = 0.7, 𝜆𝑠 = 0.3
selected through grid search validation.

## §3 AI-DRIVEN BEAMFORMING

FRAMEWORK
Hierarchical Reinforcement Learning.We implement a
two-level framework: constellation-level coordination using
PPO (actor-critic with 512-256 hidden layers, Adam opti-
mizer, learning rate 3e-4) and satellite-level beam manage-
ment using DDPG (actor/critic networks: 256-128 layers,
replay buffer: 1M samples, soft update =0.005). The state
space includes channel matrix 𝐻𝑡 ∈R 𝑁𝑔 ×𝑁𝑠 , traffic demands
𝐷𝑡 ∈R 𝑁𝑔, queue status 𝑄𝑡, sensing priorities 𝐸𝑡, orbital
positions𝑂 𝑡, and connectivity matrix𝑊 𝑡 ∈ {0,1} 𝑁𝑠 ×𝑁𝑠 .
The reward function balances throughput and sensing:
𝑟𝑡 =0.4·𝑟 𝑡ℎ𝑟𝑜𝑢𝑔ℎ𝑝𝑢𝑡 +0.3·𝑟 𝑠𝑒𝑛𝑠𝑖𝑛𝑔 +0.2·𝑟 𝑓 𝑎𝑖𝑟𝑛𝑒𝑠𝑠 −0.1·𝑟 𝑝𝑒𝑛𝑎𝑙𝑡 𝑦
(6)
Implementation and Comprehensive Baseline Com-
parison.We use NS-3 v3.36, STK 12.3, TensorFlow 2.11 on 4
NVIDIA V100 GPUs. Training: 5,000 episodes×60 minutes
each, requiring 36 hours. Constellation parameters: 66-2,400
satellites, 20 GHz Ka-band, 500 MHz total bandwidth, 64×64
phased arrays.
Baselines.We compare against four approaches:
i) Heuristic proportional fair allocation ii) Q-learning with
𝜖-greedy exploration [7] iii) Convex optimization using interior-
point methods [3] iv) Random beam allocation
With QPSK modulation and 3/4 coding rate (2.25 bps/Hz
theoretical), our approach achieves 8.9 Gbps system through-
put (avg 3.56 bps/Hz accounting for fading, interference)
compared to baselines: heuristic 7.5 Gbps, Q-learning 7.9
Gbps, convex optimization 8.1 Gbps, random 5.2 Gbps. This
represents 18% improvement over heuristic, 12% over Q-
learning, and 10% over convex methods. Sensing accuracy:
68.2% vs baselines (heuristic 57.8%, Q-learning 61.2%). Energy
efficiency: 2.8 Mbits/J vs 2.4 Mbits/J (heuristic) representing
15% improvement.
Large-scale testing up to 2,400 satellites demonstrates al-
gorithmic scalability with <15% performance degradation, as
shown in Figure 1(b). This scale approaches Starlink Phase 1
deployment targets, validating practical relevance.

## §4 MULTI-MODAL EDGE INTELLIGENCE

Federated Learning with Privacy-Utility Analysis.Our
architecture fuses Sentinel-1 SAR (10m resolution), Wi-Fi
CSI, and IoT sensors through federated learning. Each edge
node trains locally with differential privacy noise injection
achieving(𝜖, 𝛿)=(1.2,10 −5)-DP:
𝑤 𝑡+1
𝑖 =𝑤 𝑡
𝑖 −𝜂∇𝐿 𝑖 (𝑤 𝑡
𝑖 , 𝐷𝑖 ) + N (0, 𝜎 2𝐼)(7)
where𝜎=0.8calibrated using privacy accounting [2].
Privacy-Utility Tradeoff Analysis:We define utility as
F1-score for object detection across privacy levels. Our anal-
ysis reveals: strong privacy (𝜖= 0.5) reduces F1-score to 0.62
42
Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence ANAI ’25, November 4–8, 2025, Hong Kong, China
0 1 2 3 4 54
6
8
10
Training Episodes (×1000)
Throughput (Gbps)
Proposed DRL
Q-Learning
Heuristic
Convex Opt
(a) Throughput convergence vs. strong baselines
0 500 1,000 1,500 2,000 2,5001.5
2
2.5
3
3.5
Constellation Size
Energy Efficiency (Mbits/J)
Proposed DRL
Heuristic
(b) Energy efficiency scaling to 2,400 satellites
Figure 1: DRL beamforming with comprehensive base-
lines
but provides formal privacy guarantees against membership
inference attacks; moderate privacy (𝜖= 1.2) achieves F1 =
0.68 representing 18% improvement over SAR-only baseline
(F1 = 0.58) while maintaining reasonable privacy protection;
weak privacy ( 𝜖= 2.0) achieves F1 = 0.71 but increases
vulnerability to reconstruction attacks. The noise variance
𝜎= 0.8ensures composition privacy under 100 federation
rounds. Communication overhead scales linearly with pri-
vacy level: stronger privacy requires larger noise, increasing
model updates from 2.1MB (𝜖= 2.0) to 2.6MB (𝜖= 0.5) per
round.
Testing scales up to 250 edge nodes across urban/rural
scenarios validates federated convergence. Communication
overhead: 2.3 MB per federation round vs 15.2 MB for cen-
tralized approaches—an 85% reduction.
The privacy-utility analysis in Figure 2(b) demonstrates
that our chosen 𝜖= 1.2provides meaningful privacy protec-
tion while achieving significant utility improvements over
single-modality approaches.

## §5 GROUND-BASED LLM RESOURCE

MANAGEMENT
Architecture and Optimized Deployment.Our system
processes traffic reports using a ground-deployed 6.7B param-
eter model (LLaMA-2 architecture) with 4-bit quantization
and tensor parallelism [5]. The LLM runs on terrestrial edge
servers with measured power consumption: 45W average
(including cooling), 38W inference-only on NVIDIA A6000
GPUs [16].
0 20 40 60 80 1000.5
0.6
0.7
Federation Rounds (10 local epochs each)
F1-Score
Multi-Modal FL
SAR Only
(a) FL convergence (F1-score utility metric)
0.5 1 1.5 2 2.5 30.55
0.6
0.65
0.7
0.75
Privacy Budget𝜖
F1-Score
Privacy-Utility Tradeoff
SAR Baseline
(b) Utility (F1-score) vs. privacy budget
Figure 2: Multi-modal federated learning with utility
analysis
Computational Overhead Analysis:LLM inference la-
tency: 180ms for 1024-token contexts vs LSTM: 45ms for
equivalent trajectory prediction. However, LLM processing
occurs offline during non-critical periods (traffic report up-
dates every 5-10 minutes), while LSTM requires real-time
processing during handover events. Total system latency ben-
efits from LLM’s superior prediction accuracy (reducing han-
dover frequency by 18%) offsetting the higher per-inference
cost. The 25% latency improvement reflects end-to-end han-
dover completion time, not individual model inference time.
Trajectory prediction combines LLM context with kine-
matic models:
x𝑡+1 =𝑓 𝑘𝑖𝑛𝑒𝑚𝑎𝑡𝑖𝑐 (x𝑡,u 𝑡 ) +𝛼·𝑓 𝐿𝐿𝑀 (c𝑡 )(8)
where 𝛼= 0.25(empirically tuned) weights LLM contribu-
tions.
Comprehensive ML Baseline Comparison.We com-
pare against:
i) LSTM-based trajectory prediction (3-layer, 512 hidden
units) [9] ii) Random Forest ensemble (100 trees) [4] iii) Tra-
ditional Kalman filtering [11] iv) Static resource allocation
Testing on SUMO traffic simulation (up to 1,000 vehicles)
and OMNeT++ satellite networks shows our LLM approach
achieves 135ms average handover latency vs baselines: LSTM
180ms, Random Forest 195ms, Kalman 210ms, static 245ms.
This represents 25% improvement over LSTM and 43% over
Kalman methods.
Handover Success Definition:Successful handover re-
quires: (1) <500ms total switching time; (2) <1% packet loss
during transition; (3) maintained QoS requirements post-
handover. Success rate: LLM 78% vs LSTM 65%, Random
Forest 62%, Kalman 59%.
43
ANAI ’25, November 4–8, 2025, Hong Kong, China Hannaneh B. Pasandi, Franck Rousseau, Tamer Nadeem, and Sina Darabi
50 100 150
100
150
200
250
Vehicle Speed (km/h)
Handover Latency (ms)
LLM-Enhanced
LSTM
Random Forest
Kalman Filter
(a) Handover latency vs. comprehensive ML baselines
0 5 10 15 20 25
60
70
80
Time (hours)
Handover Success Rate (%)
LLM-Enhanced
LSTM
Random Forest
Kalman Filter
(b) Success rate (seamless handover completion)
Figure 3: Ground-based LLM vs. comprehensive ML
baselines
Figure 3 demonstrates consistent performance advantages
of the LLM approach across different vehicle speeds and over
24-hour operational cycles, with 25% latency reduction and
20% higher success rates compared to LSTM baselines.

## §6 INTEGRATED SYSTEM EV ALUATION

Information Flow and Integration Assumptions.Under
coordinated operation with 5-minute information exchange
intervals (aligned with 3GPP NTN standards for satellite
network management [1]), the three AI components inte-
grate as follows:(i)Federated learning produces regional
traffic density maps 𝜌(𝑥, 𝑦, 𝑡) updated every 5 minutes fol-
lowing established traffic monitoring protocols [12];(ii)LLM
generates mobility prediction vectorsv 𝑝𝑟𝑒𝑑 (𝑡+Δ𝑡) for 15-
minute horizons (typical vehicle trajectory prediction win-
dow [15]);(iii)DRL beamforming incorporates both density
maps and mobility predictions as additional state features:
s𝑖𝑛𝑡𝑒𝑔𝑟𝑎𝑡𝑒𝑑 =[ s𝑏𝑎𝑠𝑖𝑐 , 𝜌𝑙𝑜𝑐𝑎𝑙 , v𝑝𝑟𝑒𝑑 ] wheres 𝑏𝑎𝑠𝑖𝑐 includes origi-
nal channel and queue states.
Integration Overhead:Information exchange adds 2.1MB
/5min bandwidth (consistent with satellite telemetry data
rates [12]) and 150ms processing latency for density map
compression and mobility vector updates (typical edge com-
puting processing times [?]). These overheads are acceptable
given the 5-minute update cycle and terrestrial backbone
capacity.
Synergistic Performance Analysis.Figure 4 compares
standalone vs. integrated system performance under vary-
ing mobility scenarios. The integrated system achieves ad-
ditional 8% energy efficiency improvement over standalone
DRL by reducing unnecessary beam switches (predicted via
LLM mobility forecasting) and 12% sensing accuracy im-
provement by focusing SAR collection on high-traffic regions
identified through federated density maps.
50 100 200 400 600
2
2.5
3
3.5
Mobility (vehicles/km2)
Energy Eff. (Mbits/J)
Integrated DRL Only
FL Only LLM Only
Figure 4: Integrated system achieves 8% higher energy
efficiency through coordinated sensing-beamforming
vs. standalone approaches.

## §7 COMPREHENSIVE ANALYSIS

Performance Summary and Energy Analysis.Table 1
presents validated results with comprehensive baselines and
detailed energy modeling. We measure energy efficiency
as successful packet transmissions per Joule, normalized
by satellite transmit power and edge server consumption.
Energy efficiency calculated using Eq. (3) with measured
power consumption values from space-qualified hardware
specifications and ground infrastructure requirements.
Scalability and Real-World ValidationLarge-scale test-
ing up to 2,400 satellites (approaching Starlink Phase 1 scale)
demonstrates algorithmic scalability. Performance degrada-
tion remains <15% when scaling from 66 to 2,400 satellites,
validating the hierarchical approach for practical deploy-
ment.
Starlink Validation:Our simulation parameters align
with published Starlink measurements [15?]: latency ranges
(20-50ms), throughput variability (20-200 Mbps), and han-
dover frequency (every 15-60 seconds) match empirical ob-
servations, increasing confidence in simulation realism.
Limitations and Future Validation:While simulation-
based evaluation provides controlled analysis across large
scales, real-world deployment faces additional challenges:
atmospheric effects, regulatory constraints, and hardware
imperfections not fully captured in simulation. Future work
should include: (i) testbed validation using software-defined
radios and satellite emulators; (ii) partnership with satellite
operators for limited field trials; (iii) validation of AI model
robustness under real channel conditions and interference
44
Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence ANAI ’25, November 4–8, 2025, Hong Kong, China
Table 1: Performance comparison with comprehensive baselines and energy modeling
Metric Topic 1 Topic 2 Topic 3 Integrated
DRL Beamform Multi-Modal LLM Ground System
Primary Improvement 18%±2.1% 15%±2.5% 25%±2.2% 31%±2.8%
vs. Q-Learning/LSTM 12%±1.8% N/A 25%±3.2% 35%±3.5%
vs. Convex/Random Forest 10%±1.5% N/A 31%±3.8% 38%±4.1%
Energy Efficiency (Mbits/J) 2.8±0.15 1.9±0.12 1.6±0.18 3.2±0.18
Baseline Energy (Mbits/J) 2.4±0.12 1.7±0.10 1.4±0.15 2.4±0.15
Energy Improvement 15%±2.0% 12%±1.5% 14%±2.2% 31%±3.1%
Max Tested Scale 2,400 satellites 250 nodes 1,000 vehicles 400 satellites
Privacy Protection N/A𝜖=1.2DP N/A𝜖=1.2DP
Training/Setup Time 36 hours 18 hours 12 hours 48 hours
Integration Overhead N/A N/A N/A 2.1 MB/5min
patterns. Implementation challenges include: satellite proces-
sor limitations (1-10 GFLOPS), requiring 8×model compres-
sion; thermal management in space environment; radiation
hardening costs ($50K-100K per satellite) [8]; ground infras-
tructure scaling (1 gateway per 1,000 users).
Future Research DirectionsPromising directions in-
clude hardware-software co-design for satellite AI process-
ing, quantum-enhanced optimization algorithms, neuromor-
phic computing for power efficiency, and integration with
6G terrestrial networks. Standardization through 3GPP NTN
evolution [1] and regulatory frameworks will be critical for
practical deployment at megaconstellation scale.

## § References

[1] 3GPP. 2023.Study on Non-Terrestrial Networks (NTN) - Release 17. Tech-
nical Report TR 38.821 V17.0.0. 3rd Generation Partnership Project.
[2] Martin Abadi, Andy Chu, Ian Goodfellow, H Brendan McMahan, Ilya
Mironov, Kunal Talwar, and Li Zhang. 2016. Deep learning with
differential privacy. InProceedings of the 2016 ACM SIGSAC conference
on computer and communications security. 308–318.
[3] Stephen Boyd, Stephen P Boyd, and Lieven Vandenberghe. 2004.Con-
vex optimization. Cambridge university press.
[4] Leo Breiman. 2001. Random forests.Machine learning45, 1 (2001),
5–32.
[5] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer.
2023. QLoRA: Efficient finetuning of quantized LLMs.Advances in
Neural Information Processing Systems36 (2023), 10088–10115.
[6] Ericsson. 2023. Ericsson Mobility Report: Q4 2023 Update. White
Paper. Available: https://www.ericsson.com/mobility-report.
[7] Paulo VR Ferreira, Randy Paffenroth, Alexander M Wyglinski, Timo-
thy M Hackett, Sven G Bilen, Richard C Reinhart, and Dale J Mortensen.
2022. Reinforcement learning for satellite communications: From LEO
to deep space operations.IEEE Communications Magazine60, 10 (2022),
92–98.
[8] Alan D George and Conner M Wilson. 2019. Space-qualified processing
architectures for satellite applications. InProceedings IEEE Aerospace
Conference. IEEE, 1–12.
[9] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term
memory.Neural computation9, 8 (1997), 1735–1780.
[10] Hongji Huang, Yaxiong Song, Jian Yang, Guan Gui, and Fumiyuki
Adachi. 2021. Deep-learning-based millimeter-wave massive MIMO
for hybrid precoding.IEEE Transactions on Vehicular Technology70, 3
(2021), 3027–3032.
[11] Rudolph Emil Kalman. 1960. A new approach to linear filtering and
prediction problems.Journal of basic Engineering82, 1 (1960), 35–45.
[12] Oltjon Kodheli, Eva Lagunas, Nicola Maturo, Shree Krishna Sharma,
Bhavani Shankar, Juan Fernando Montoya Montoya, James C M Dun-
can, Danilo Spano, Symeon Chatzinotas, Steven Kisseleff, Jorge Querol,
Lei Lei, Thang X Vu, and George Goussetis. 2021. Satellite communi-
cations in the new space era: A survey and future challenges.IEEE
Communications Surveys & Tutorials23, 1 (2021), 70–109.
[13] Fan Liu, Yuanhao Cui, Christos Masouros, Jie Xu, Tony X Han, Yonina C
Eldar, and Stefano Buzzi. 2022. Integrated sensing and communications:
Toward dual-functional wireless networks for 6G and beyond.IEEE
Journal on Selected Areas in Communications40, 6 (2022), 1728–1767.
[14] Sifan Long, Jingjing Tan, Bomin Mao, Fengxiao Tang, Yangfan Li,
Ming Zhao, and Nei Kato. 2024. A Survey on Intelligent Network
Operations and Performance Optimization Based on Large Language
Models.IEEE Communications Surveys & Tutorials(2024). https:
//doi.org/10.1109/COMST.2024.3526606 Early Access.
[15] Florian Michel, Simon Kassing, Thomas Holterbach, and Adrian Per-
rig. 2022. Performance characterization of LEO satellite networks: A
Starlink-based measurement study.IEEE/ACM Transactions on Net-
working30, 6 (2022), 2374–2387.
[16] NVIDIA. 2023. NVIDIA A6000 Power and Performance Specifica-
tions. Technical Specification. Available: https://www.nvidia.com/en-
us/design-visualization/rtx-a6000/.
[17] J Andrew Zhang, Fan Liu, Christos Masouros, Robert W Heath, Zhiy-
ong Feng, Linling Zheng, and Athina Petropulu. 2021. An overview
of signal processing techniques for joint communication and radar
sensing.IEEE Journal of Selected Topics in Signal Processing15, 6 (2021),
1295–1315.
45
