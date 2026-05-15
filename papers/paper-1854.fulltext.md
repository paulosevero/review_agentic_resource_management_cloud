---
paper_id: "paper-1854"
source_pdf_sha: "045eac03698b7bbe221047a551dd03107b0beea1d1e1e37d139fc1423e5ff4cb"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 1
  page_count: 6
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-1854 — fulltext
## §unknown-1

Internet Technology Letters
SPECIAL ISSUE ARTICLE
Leveraging Large Language Models for Network Security: A
Multi-Expert Approach
TianshunLin1 | ChangguiXu2 | JianshanZhang3 | NanLin1 | YuxinLiu1 | YuanjunZheng4
1StateGridPutianElectricPowerSupplyCompany,Putian,China | 2SchoolofInformationScienceandTechnology,ShanghaiTechUniversity,
Shanghai,China | 3SchoolofComputerandDataScience,MinjiangUniversity,Fuzhou,Fujian,China | 4StateGridFuzhouElectricPowerSupply
Company,Fuzhou,China
Correspondence:ChangguiXu( xuchg2022@shanghaitech.edu.cn)
Received:15February2025 | Revised:27February2025 | Accepted:4March2025
Funding:ThisresearchwassupportedbytheNaturalScienceFoundationofFujianProvince,China(No.2024J08277).
Keywords:deepreinforcementlearning | industrialedgecomputing | largelanguagemodels
ABSTRACT
The optimization of diverse industrial edge computing tasks presents a significant challenge due to the dynamic and hetero-
geneous nature of industrial operational demands. While deep reinforcement learning (DRL) has shown promise, task-specific
DRLmodelsareoftenrequiredincomplexindustrialedge networks,suchasreal-timeanomalydetectionandlatency-sensitive
decision-making, increasing computational overhead. This leads to large computational overheads, unstable performance, and
increased energy consumption. Such a cost has become a concern in resource-limited industrial edge networks. In this paper,
we propose a novel multi-expert optimization approach with the help of powerful large language models (LLMs). Our goals
are to dynamically interpret industrial task requirements, activate specialized DRL experts, and synthesize their outputs into
context-awaredecisions.Specifically,wereplaceconventionalgatenetworkswithanLLM-basedorchestrator.LLMsprovidethe
benefitsofsemanticreasoningandcontextualunderstandingwhenmanagingexpertselectionandcollaboration.Thisapproach
eliminates the need to train unique DRL models for each industrial optimization task, thereby reducing deployment costs and
improvingscalability.Ourexperimentsindicatethatourapproachachieves13%higheranomalydetectionaccuracywhencom-
paredwithtraditionalDRLmethods.
1 | Introduction
The emergence of sixth-generation (6G) networks [1] rapidly
changesindustrialedgecloudinfrastructures.Itenablesmassive
applicationssuchasreal-timedevicemaintenance,autonomous,
and latency-sensitive industrial automation. In particular, 6G
networks promise ultra-reliable connectivity and intelligence.
These characteristics support the industrial edge networks that
connect smart factories, energy grids, and IoT ecosystems,
------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------
©2025JohnWiley&SonsLtd.
where computational workloads are increasingly offloaded to
resource-constrainededgenodes[ 2–5].
However, the heterogeneous and dynamic nature of industrial
networksecurityoperationsrangingfromtime-sensitivecontrol
to distributed anomaly detection in manufacturing pipelines
needs adaptive optimizations. Those optimizations should be
able to reconcile conflicting objectives like energy efficiency,
computational scalability, and sub-millisecond latency [ 6].
Internet Technology Letters,2025;8:e70016 1of6
https://doi.org/10.1002/itl2.70016

FIGURE 1 | Overviewofourapproach.
While deep reinforcement learning (DRL) shows promise [7],
task-specific customization (e.g., for real-time anomaly
detection) often requires multiple DRL models, increasing
computationalcosts[ 8].
Moreprecisely,acriticalbottleneckliesinthecostofcustomiza-
tion.Pre-trainedDRLmodelsoftenfailtogeneralizetonewtasks.
Hence,theadoptionofnewtasksrequiresretraining,whichcon-
sumes multiple time cycles. For instance, a DRL policy opti-
mized for real-time anomaly detection in DDoS defense may
perform poorly when repurposed for dynamic resource alloca-
tion in multi-access edge computing (MEC) nodes [9, 10]. This
limitation exacerbates computational overheads and constrains
industrial AI deployments. Thus, we ask: how can industrial
edge networks achieve adaptive optimizations without training
task-specificDRLmodels?
Recent advances in multi-expert frameworks provide a promis-
ing path [11]. By coordinating specialized DRL models, each of
whichisfine-tunedforaspecifictask,theseframeworksenable
collaborativedecision-makingandavoidrelianceonmonolithic
single-task AI systems. In particular, a gate network governs
expertselection.However,itsstatictrainingparadigmcanhardly
adapttothedynamicsofindustrialedgenetworks,suchasbursts
insensordatastreamsorad-hocIoTdevicedeployments.
In response, we harness large language models (LLMs) to
overcome the limitations of existing multi-expert frameworks
(Figure 1). LLMs’ semantic reasoning and contextual ground-
ing perform well when parsing unstructured industrial secu-
rity task requirements, for example, interpreting security logs,
service-level agreements, or real-time traffic telemetry [7, 11].
Such capabilities allow LLMs to become a dynamic orchestra-
tor that achieves adaptive and human-aligned decision-making
inmulti-expertsystems.
1.1 | Contributions
Thispapermakesthreecontributions:
• We introduce a multi-expert approach tailored for indus-
trialedgecloudnetworks.ThisapproachenablesDRLmodel
coordination to address heterogeneous network security
taskswithoutretraining.
• WedesignanLLM-basedorchestratorthatinterpretsopera-
tional constraints (e.g., energy budgets, latency thresholds)
anddynamicallyassemblesspecializedDRLmodels.
• We validate our approach through an industrial case study
of real-time anomaly detection. It achieves 13% higher
accuracyoverconventionalDRL.
This paper is organized as follows. Section2 illustrates our
LLM-empowered multi-expert approach. Section3 presents an
industrial case study that uses and evaluates our approach.
Section4concludesthispaperanddiscussesfutureworks.
2 | LLM-Empowered Multi-Expert Approach
In this section, we introduce the LLM-empowered multi-expert
approachfornetworksecuritytasksinindustrialedgenetworks.
We first formulate the problem of optimizing the deployment
of an arbitrary network security task in each DRL model. Then
we introduce our LLM-empowered multi-expert approach that
assemblesthedecisionsofmultipleDRLexpertsviaLLMorches-
tration to yield the optimal deployment decisions. Finally, we
analyzetheconvergenceofourapproach.Table 1summarizesthe
notationofsymbolsusedbyourpaper.
2.1 | Problem Formulation
Consider a network security optimization task modeled as a
MarkovDecisionProcess(MDP)with:
• State space = {𝑠1,𝑠2, ...,𝑠 𝑁
} representing network con-
ditions(e.g.,dataplaneswitchstates,trafficloads).
• Action space = {𝑎1,𝑎2, ...,𝑎 𝑀
} denoting optimization
decisions (e.g., switch resource allocation, variables decid-
ing which switches to run which tasks, and traffic routing
paths).
• Rewardfunction𝑅 ∶×  → ℝ mappingstate-actionpairs
toqualityofservice(QoS)metrics.
Theobjectiveistofindanoptimalpolicy 𝜋
∗∶ →  thatmaxi-
mizestheexpecteddiscountedreturn:
𝜋∗=argmax
𝜋
𝔼
[ ∞∑
𝑡=0
𝛾𝑡𝑅 (𝑠𝑡,𝑎 𝑡
)
]
(1)
where, 𝛾 ∈[0,1)isthediscountfactor.
2.2 | Multi-Expert Approach
2.2.1 | Multiple Experts
Let {𝜋1,𝜋2, ...,𝜋 𝐾
} denote 𝐾 specialized DRL experts, each
trainedforadistincttypeofnetworksecuritytaskswithunique
rewardfunctions {𝑅
1,𝑅 2, ...,𝑅 𝐾
}.Foraninputstate 𝑠𝑡,the kth
expertproducesactionprobabilities:
𝑃 𝑘
(𝑎|𝑠𝑡
)=softmax(𝑄 𝑘
(𝑠𝑡,𝑎 )∕𝜏) (2)
2of6 Internet Technology Letters,2025
 24761508, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/itl2.70016 by Pontificia Universidade Catolica Do Rio Grande Do Sul, Wiley Online Library on [09/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 1 | Notationofsymbolsusedbythemainbodyofthispaper.
 Statespacerepresentingnetworkconditions
(e.g.,channelstates,trafficloads)
 Actionspacedenotingoptimizationdecisions
(e.g.,powerallocation,routingpaths)
𝑅 (𝑠, 𝑎) Rewardfunctionmappingstate-actionpairsto
QoSmetrics
𝛾 Discountfactorforexpecteddiscountedreturn
𝜋∗ Optimalpolicymaximizing 𝔼[∑ ∞
𝑡=0 𝛾𝑡𝑅 (𝑠𝑡,𝑎 𝑡
)]
𝜋𝑘 SpecializedDRLexpertpolicyfortask 𝑘
𝑄 𝑘(𝑠, 𝑎) Q-valueestimateofexpert 𝑘 forstate-actionpair (𝑠, 𝑎)
𝜏 Temperatureparameterinsoftmaxactionprobability
𝑃 𝑘
(𝑎|𝑠𝑡
) Actionprobabilitydistributionfromexpert 𝑘 atstate 𝑠𝑡
Φ() Latenttaskrequirementsparsedfromuserinput
byLLM
𝜙 𝑖 Semanticfeatureextractedfromuserinput
(e.g.,latency,throughput)
𝛼𝑘 Attention-basedweightforexpert 𝑘
W𝛼 Learnableprojectionmatrixforcomputingexpert
weights
𝜓 𝑘 Metadataofexpert 𝑘 (e.g.,taskspecialization,
performancehistory)
𝜋final Fusedpolicycombiningweightedexpertoutputs
𝑠𝑡 Currentnetworkstateattime 𝑡
𝑎𝑡 Optimalactionselectedattime 𝑡
 Userinputdescribingtaskrequirements(textualor
structured)
𝑃 𝑡−1 Previoustransmitpowerallocation
𝑡−1 PreviousQoSmetric(e.g.,outageprobability,datarate)
𝒈𝑡 Wirelesschannelconditionsattime 𝑡
𝛽1,𝛽2 CoefficientsinNSPutilityfunction(revenuevs.
energycost)
min, max MinimumandmaximumQoSboundsforconstraints
𝑉 𝜋(𝑠) Valuefunctionrepresentingexpectedreturnunder
policy 𝜋 atstate 𝑠
𝜀 Suboptimalityboundofexpertpolicies
where, 𝑄 𝑘
(𝑠𝑡,𝑎 )istheexpert’s Q-valueestimateand 𝜏isthetem-
peratureparameter.
2.2.2 | LLM-Based Orchestration
TheLLMorchestratesexpertcollaborationthroughthreemathe-
maticaloperations.
1. Objective parsing : For user input , extract latent task
requirements
Φ()= {𝜙1,𝜙 2, ...,𝜙 𝐿
} ∼LLM() (3)
where, 𝜙 𝑖 representssemanticfeatures (e.g.,“lowlatency”
→ 𝜙latency).
2. Expert weighting : Compute attention-based weights for
experts
𝛼𝑘 = 𝜎 (W𝛼 ⋅[Φ(); 𝜓 𝑘]) (4)
s.t.
𝐾∑
𝑘=1
𝛼𝑘 =1 (5)
where, 𝜓 𝑘 denotesexpert k’smetadataand W𝛼 isalearnable
projectionmatrix.
3. Decision fusion:Combineexpertoutputsthroughweighted
voting
𝜋final
(
𝑎|𝑠𝑡
)
=
𝐾∑
𝑘=1
𝛼𝑘 𝑃 𝑘
(
𝑎|𝑠𝑡
)
(6)
2.2.3 | Optimization
OncetheLLMcompletesitscollaboration,ourapproachmakes
the optimal decisions based on the current state, user input,
and expert policies. More precisely, given the input of current
state 𝑠
𝑡, user input , expert policies {𝜋𝑘
}𝐾
𝑘=1, our approach
aims to produce the optimal action 𝑎𝑡. Its workflow con-
tains: (1) Parse requirements:Φ←LLM(). (2) Retrieve expert
metadata {𝜓 𝑘
}𝐾
𝑘=1. (3) Compute weights:𝛼𝑘 ← 𝜎 (W𝛼
[Φ;𝜓 𝑘
]).
(4) Sample actions: 𝑎𝑘 ∼𝜋𝑘
(⋅|𝑠𝑡
). (5) Fuse decisions: 𝑎𝑡 =
argmax 𝑎
∑ 𝐾
𝑘=1 𝛼𝑘 𝕀(𝑎𝑘 = 𝑎).
2.2.4 | Deployment
After solving the above problem, which maximizes the net-
work service provider (NSP) utility, define: (1) State 𝑠𝑡 =(𝑃 𝑡−1, 𝑡−1, 𝒈𝑡
);(2)Action 𝑎𝑡 = 𝑃 𝑡 ∈{𝑃 (1), ...,𝑃 (𝐿 )};(3)Reward
𝑅 (𝑠𝑡,𝑎 𝑡
)= 𝛽1(𝑡
)−𝛽2𝑃 𝑡. The LLM resolves conflicting QoS
requirements when deploying network security tasks through
constrainedoptimization:
max
{
𝛼𝑘}
𝔼[𝑅 (𝑠, 𝑎)] s.t. min ≤
𝐾∑
𝑘=1
𝛼𝑘 𝑘 ≤max (7)
where, min, max refer to the minimum and maximum QoS
boundsforconstraints.
This formulation enables automatic adaptation to novel
requirements,like:
game =“EnsureDDoSflowdetectionwithlatency <20 ms”
→ 𝜙latency ⊕𝜙 throughput (8)
2.3 | Theoretical Analysis
Ourapproach’sconvergencefollowsfrom:
Theorem 1. For 𝐾 experts with ϵ-optimal policies, the fused
policy satisfies:
𝑉 𝜋 final(𝑠) ≥max
𝑘
𝑉 𝜋𝑘 (𝑠)− ϵ
1−𝛾
𝐾∑
𝑘=1
𝛼2
𝑘 (9)
3of6
 24761508, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/itl2.70016 by Pontificia Universidade Catolica Do Rio Grande Do Sul, Wiley Online Library on [09/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Proof. LetΔ𝑘 = 𝑉 𝜋final −𝑉 𝜋𝑘 .FromBellmanequations:
Δ𝑘(𝑠)= 𝛾𝔼𝑠′∼𝑃 (⋅|𝑠,𝑎)
[Δ𝑘
(𝑠′)]+ϵ𝑘 (10)
⇒∥Δ𝑘 ∥∞≤ ϵ𝑘
1−𝛾 (11)
Theresultfollowsfromaconvexcombinationofexperts. ◽
Such convergence guarantees performance within bounded
optimalityloss.
3 | Industrial Case Study: Real-Time Anomaly
Detection
In this section, we explain how to apply our approach in prac-
tical network security scenarios. Consider a mobile network in
a factory where IoT sensors monitor vibrations, temperatures,
and pressures in the data plane connecting 50 robotic assembly
lines. These sensors periodically report these data to the con-
trol plane via mobile transmission. In this case, the industrial
anomalies incurred by network security events such as DDoS
attacks can be: (1)Type A: Sudden vibration spikes (>15 g)
indicatingbearingfailures.(2) Type B:Thermalgradients( Δ𝑇>
25
˚C∕min) indicating device overloads. (3) Type C: Pressure
drops (<0.8𝑃nominal) indicating pneumatic leaks. Our approach
mustdetecttheaboveanomalieswithin50mslatencytoenable
automated shutdowns, minimizing revenue loss. It operates as
follows:
•Step 1:Expertspecialization:
𝜋1 ∶VibrationpatternanalysisviaLSTM-DQN
𝜋2 ∶Thermaltransientmodelingviaproximalpolicyoptimization (PPO)
𝜋3 ∶Pressuredynamicstrackingviaasynchronousadvantageactor-critic (A3C)
•Step 2:LLMorchestration:
Φ(𝑡
)=LLM
⎛
⎜
⎜
⎜⎝
⎡
⎢
⎢
⎢⎣
“Vibration ∶𝑥vib(𝑡)
“Temperature∶𝑥temp(𝑡)
“𝐿𝑜𝑔 Entry ∶AnomalyatLine7 ”
⎤
⎥
⎥
⎥⎦
⎞
⎟
⎟
⎟⎠
→ {𝜙vib,𝜙 thermal
}
(12)
•Step 3:Decisionfusion
𝛼𝑘 =
exp(W𝛼
[Φ;𝜓 𝑘
])
∑ 3
𝑗=1 exp(W𝛼
[Φ;𝜓 𝑗
]) (13)
3.1 | Simulation
3.1.1 | Setup
Thenweconductedasimulationtoevaluatetheaboveapproach.
Our simulation was conducted in a server with 16 cores, with a
3.7GHz clock speed, and 4GB of RAM running Ubuntu 22.04.
TABLE 2 | Comparisonofanomalydetectionperformance.
Metric Single DRL Gate LLM (ours)
Accuracy(%) 82.3 87.1 94.6
F1-score 0.791 0.841 0.927
Falsepositiverate(%) 8.2 6.3 1.9
Latency(ms) 41 53 38
Energy(W) 18.7 22.4 15.2
For datasets, we choose a 6-month factory telemetry trace (1M
samples)with12351labeledanomalies:
 =
{(
𝑥𝑡,𝑦 𝑡
)}
,𝑥 𝑡 ∈ℝ128×3,𝑦 𝑡 ∈{0,1}3 (14)
Then for state representation𝑠𝑡 and reward function𝑅 (𝑠, 𝑎) in
ourapproach,weemploythefollowinggeneralsettingsborrowed
frompriorstudies:
𝑠
𝑡 =
[ 𝑥 vib(𝑡)
𝜎vib
,
𝑥temp(𝑡)−25
10 ,
𝑥press(𝑡)
𝑃nominal
]
(15)
𝑅 (𝑠, 𝑎)= 10 ⋅ 𝑇𝑃𝑅⏟⏞⏟⏞⏟
Detectionbonus
− 5 ⋅ 𝐹𝑃𝑅⏟⏟⏟
Falsealarmpenalty
−0.1 ⋅Latency
⏟⏞⏞⏞⏞⏟⏞⏞⏞⏞⏟
Timeliness
(16)
For training parameters, we set (1) batch size: 512 sequences
(128-time steps); (2) discount factor: 𝛾 =0.99; (3) LLM:
GPT-4-1106-previewwith32ktokencontext.
3.1.2 | Numerical Results
Weuseourapproachandcomparisonsolutionstodetectanoma-
lies in our dataset. The comparison solutions comprise: (1) sin-
gle DRL that uses a single DRL model to infer anomalies and
(2) gate that coordinates multiple DRL-based expert models via
the conventional gate network. Table2 summarizes the perfor-
manceofthesesolutionsandourapproach.Itindicatesthatour
approachachievessuperiorperformance.Thereasonsareasfol-
lows: (1) The LLM correlates textual maintenance logs such as
unusual noise with sensor patterns. Thus, it correctly increases
vibrationexpertweightingfrom0.41to0.79.(2)Theexpertsfor
thermalandpressurecollaboratewhendetectingTypeBanoma-
lies,forexample,theirjointcontribution
(
𝛼
2 + 𝛼3 =0.63)during
deviceoverloadevents.(3)TheLLMdeactivatespressureexperts
during normal operation
(
𝛼
3 <0.1). Thus, it reduces computa-
tion energy consumption by 19% when compared to static gate
networks.
3.1.3 | Ablation Study
WefurtherconductanablationstudyonourapproachinTable 3.
Wedisablesomecriticaltechniquesusedbyourapproachinthis
case study, including LLM parsing, expert fusion, and thermal
expert.Wealsopresenttheresultswhenusingstaticweights.The
resultsindicatethat(1)the10.2% F1-scoredropwhenremoving
LLMparsingconfirmsitscriticalroleforinterpretingcontextual
4of6 Internet Technology Letters,2025
 24761508, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/itl2.70016 by Pontificia Universidade Catolica Do Rio Grande Do Sul, Wiley Online Library on [09/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

TABLE 3 | Component-wiseperformanceanalysis.
Configuration Full model w/o LLM parsing w/o Expert fusion w/o Thermal expert Static weights
F1-score 0.927 0.841 0.782 0.901 0.813
cuesand(2)the15.5%dropwhenremovingexpertfusionhigh-
lightsthenecessityofdynamiccollaborationbetweenspecialized
models.
4 | Conclusion and Future Work
Inthispaper,weproposeanovelLLM-empoweredmulti-expert
approach. Our approach dynamically interprets industrial
requirements in input tasks. It then activates specialized
DRL experts and synthesizes context-aware decisions through
semantic reasoning. By replacing conventional gate networks
with an LLM-based orchestrator, our approach eliminates
the need to train and deploy unique DRL models for every
network security task. Experimental results indicate that our
approach achieves 13% higher accuracy over single-task DRL
baselines.
Our proposed LLM-driven multi-expert approach demonstrates
significant promise for addressing security challenges in indus-
trialedgenetworks.However,severalopenquestionsremain:
Leveraging in-network techniques. In recent years, the literature
hasproposedseveralin-networktechniquesbyutilizingthepow-
erful programming capabilities of data plane devices to offload
traditional computation tasks. A typical example refers to net-
work measurement, that is, building measurement data struc-
tures such as sketches inside switch ASIC pipelines to capture
traffic dynamics [12–17]. We plan to update the substrate of
industrialedgenetworkstofurtherenhancesecurity.
Federated learning for distributed intelligence.WhiletheLLMcen-
tralizes expert orchestration, our future work plans to integrate
federated learning into collaborative model training among dis-
tributededgenodes[ 18–20].Thisbringsthebenefitsofimprov-
ing data privacy, reducing communication costs, and handling
deviceheterogeneity.
Energy-aware LLM optimization . While our approach reduces
energy consumption when compared with traditional sys-
tems, LLM inference remains computationally intensive. Thus,
our future work plans to explore LLM quantization, that
is, using 4-bit quantized LLMs to reduce memory footprint,
context window pruning, that is, dynamically pruning irrel-
evant historical contexts, and hardware-aligned sparsity, that
is, exploiting NVIDIA Ampere architecture’s 2:4 sparse tensor
cores.
Ethical considerations.WhenweadoptLLMs,addressingemerg-
ingethicalchallengesbecomescritical.First,weshoulddevelop
audit systems toward LLM decisions to prevent malicious or
unsafe behaviors. Second, we also need to ensure fairness dur-
ing expert selection in view of heterogeneous expert capa-
bilities. We plan to explore these directions in our future
work.
Data Availability Statement
The data that support the findings of this study are available from the
correspondingauthoruponreasonablerequest.
Peer Review
The peer review history for this article is available athttps://www.
webofscience.com/api/gateway/wos/peer-review/10.1002/itl2.70016.

## § References

1.S. Dang, O. Amin, B. Shihada, and M. S. Alouini, “What Should 6G
Be?,”Nature Electronics3,no.1(2020):20–29.
2.Z. Chen, J. Zhang, G. Min, Z. Ning, and J. Li, “Traffic-Aware
Lightweight Hierarchical Offloading Toward Adaptive Slicing-Enabled
SAGIN,”IEEE Journal on Selected Areas in Communications 42, no. 12
(2024):3536–3550.
3.J.Zhang,H.Luo,X.Chen,H.Shen,andL.Guo,“MinimizingResponse
Delay in UAV-Assisted Mobile Edge Computing by Joint UAV Deploy-
ment and Computation Offloading,”IEEE Transactions on Cloud Com-
puting12,no.4(2024):1372–1386.
4.J. Ali, S. K. Singh, W. Jiang, et al., “A Deep Dive Into Cybersecurity
Solutions for AI-Driven IoT-Enabled Smart Cities in Advanced Com-
munication Networks,”Computer Communications 229 (2025): 108000,
https://doi.org/10.1016/j.comcom.2024.108000.
5.H. A. Ammar, R. Adve, S. Shahbazpanahi, G. Boudreau, and K. V.
Srinivas,“User-CentricCell-FreeMassiveMIMONetworks:ASurveyof
Opportunities,ChallengesandSolutions,” IEEE Communication Surveys
and Tutorials24,no.1(2021):611–652.
6.N. C. Luong, D. T. Hoang, S. Gong, et al., “Applications of Deep
Reinforcement Learning in Communications and Networking: A Sur-
vey,”IEEE Communication Surveys and Tutorials 21, no. 4 (2019):
3133–3174.
7.L. P. Kaelbling, M. L. Littman, and A. W. Moore, “Reinforcement
Learning: A Survey,”Journal of Artificial Intelligence Research 4 (1996):
237–285.
8.H.Du,R.Zhang,D.Niyato,etal.,“User-CentricInteractiveAIforDis-
tributed Diffusion Model-Based AI-Generated Content,” arXiv Preprint
arXiv:2311.11094,2023.
9.H.Du,J.Liu,D.Niyato,etal.,“Attention-AwareResourceAllocation
and QoE Analysis for Metaverse xURLLC Services,”IEEE Journal on
Selected Areas in Communications41(2023):2158–2175.
10.D.H.Nguyen,Y.Zhang,andZ.Han,“Contract-BasedSpectrumAllo-
cationforWirelessVirtualizedNetworks,” IEEE Transactions on Wireless
Communications17,no.11(2018):7222–7235.
11.W.X.Zhao,K.Zhou,J.Li,etal.,“ASurveyofLargeLanguageModels,”
arXivPreprintarXiv:2303.18223,2023.
12.X. Chen, Q. Xiao, H. Liu, et al., “Eagle: Toward Scalable and
Near-Optimal Network-Wide Sketch Deployment in Network Measure-
ment,”inACM SIGCOMM Conference(ACM,2024),291–310.
13.Q. Huang, S. Sheng, X. Chen, et al., “Toward Nearly-Zero-Error
SketchingviaCompressiveSensing,”in USENIX NSDI (USENIX,2021),
1027–1044.
5of6
 24761508, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/itl2.70016 by Pontificia Universidade Catolica Do Rio Grande Do Sul, Wiley Online Library on [09/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

14.X. Chen, Q. Huang, P. Wang, et al., “MTP: Avoiding Control Plane
OverloadWithMeasurementTaskPlacement,”in IEEE INFOCOM Con-
ference(IEEE,2021),1–10.
15.X. Chen, H. Du, W. Liu, et al., “Virtualizing Next-Generation Pro-
grammable Networks: Techniques, Use Cases, and Promising Future
Directions,”IEEE Network(2024):1–8.
16.X.Chen,C.Wu,X.Liu,etal.,“EmpoweringNetworkSecurityWith
Programmable Switches: A Comprehensive Survey,”IEEE Communica-
tion Surveys and Tutorials25,no.3(2023):1653–1704.
17.X. Chen, H. Liu, D. Zhang, et al., “Empowering DDoS Attack Mit-
igation With Programmable Switches,”IEEE Network 37, no. 3 (2023):
112–117.
18.D. C. Nguyen, M. Ding, P. N. Pathirana, A. Seneviratne, J. Li, and
H. V. Poor, “Federated Learning for Internet of Things: A Comprehen-
siveSurvey,”IEEE Communications Surveys & Tutorials 23,no.3(2021):
1622–1658.
19.D.M.ManiasandA.Shami,“MakingaCaseforFederatedLearning
intheInternetofVehiclesandIntelligentTransportationSystems,” IEEE
Network35,no.3(2021):88–94.
20.J.Liu,J.Huang,Y.Zhou,etal.,“FromDistributedMachineLearning
to Federated Learning: A Survey,”Knowledge and Information Systems
64,no.4(2022):885–917.
6of6 Internet Technology Letters,2025
 24761508, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/itl2.70016 by Pontificia Universidade Catolica Do Rio Grande Do Sul, Wiley Online Library on [09/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
