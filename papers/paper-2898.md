---
id: "paper-2898"
title: "Multiview stereo 3D reconstruction research: a survey; [多视角立体匹配三维重建研究综述]"
authors: ["Yuan, Zhenlong", "Li, Zehao", "Chen, Kehua", "Mao, Tianlu", "Jiang, Hao", "Wang, Zhaoqi"]
year: 2026
venue: "Journal of Image and Graphics"
venue_type: "journal"
doi: "10.11834/jig.250348"
url: "https://www.scopus.com/pages/publications/105033674434?origin=resultslist"
publisher: "Editorial and Publishing Board of JIG"
pages: "657--685"
keywords: ["3D Gaussian splatting(3DGS)", "3D reconstruction", "3D vision", "multiview stereo(MVS)", "neural radiance field(NeRF)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2898 — Multiview stereo 3D reconstruction research: a survey; [多视角立体匹配三维重建研究综述]

## Metadata

- **Authors:** Yuan, Zhenlong and Li, Zehao and Chen, Kehua and Mao, Tianlu and Jiang, Hao and Wang, Zhaoqi
- **Year:** 2026
- **Venue:** Journal of Image and Graphics
- **DOI:** 10.11834/jig.250348
- **URL:** https://www.scopus.com/pages/publications/105033674434?origin=resultslist
- **Publisher:** Editorial and Publishing Board of JIG
- **Pages:** 657--685
- **Language:** English
- **Keywords:** 3D Gaussian splatting(3DGS); 3D reconstruction; 3D vision; multiview stereo(MVS); neural radiance field(NeRF)

### Abstract

Multiview stereo(MVS)3D reconstruction aims to recover the three-dimensional geometric structure of a scene from multiple two-dimensional images or videos, enabling precise modeling of objects and environments. This task is fundamental to applications such as virtual reality, autonomous driving, smart city construction, and cultural heritage preservation. Traditional MVS methods rely on geometric constraints such as homography mappings and epipolar geometry to align multiview images and infer depth. However, these approaches are limited by their dependence on hand-crafted features and struggle with low-texture regions or dynamic scenes. The advent of deep learning has driven significant advancements, enabling end-to-end networks to automatically learn image-depth relationships and achieve higher accuracy and robustness. Despite these breakthroughs, challenges such as computational efficiency, generalization to complex scenes, and real-time performance remain unresolved. To systematically analyze the current state of MVS 3D reconstruction, this work categorizes existing methods into image projection-driven and geometry reasoning-driven paradigms, further subdividing them on the basis of local modeling and global modeling strategies. The paper also explores widely used datasets, evaluation metrics, and technical innovations within each category while identifying key challenges and proposing future research directions. First, this study investigates commonly used datasets and evaluation indicators in MVS 3D reconstruction. Datasets serve as the foundation for training and benchmarking algorithms and can be classified into three categories: synthetic datasets, real-scene datasets, and hybrid datasets. Synthetic datasets, such as DTU and Tanks and Temples, provide high resolution, precisely annotated data for algorithm training and validation. Real-scene datasets, including ETH3D and LLFF, capture realistic environments with varying textures and lighting conditions, enabling evaluation under practical constraints. Hybrid datasets, such as nerf-synthesis and Synthetic Soccer NeRF, combine synthetic and real-world elements to address domain adaptation challenges. Evaluation metrics are critical for quantifying algorithm performance and are primarily divided into geometric accuracy metrics and rendering quality metrics. Geometric accuracy metrics, such as chamfer distance (CD) and F-score, measure the spatial fidelity between reconstructed and ground-truth models, with lower CD values and higher F-score values indicating better performance. Rendering quality metrics, including peak signal-to-noise ratio (PSNR), structural similarity index measure (SSIM), and learned perceptual image patch similarity(LPIPS), are used to assess the visual consistency of synthesized views, with higher PSNR and SSIM scores and lower LPIPS scores reflecting superior perceptual quality. These metrics collectively provide a comprehensive framework for evaluating MVS methods across diverse scenarios. Second, the paper classifies MVS 3D reconstruction methods on the basis of their technical frameworks and innovations. Methods can be broadly categorized into image projection-driven approaches and geometry reasoning-driven approaches. Image projection-driven methods, such as MVSNet and its variants(e. g. , CasMVSNet, R-MVSNet), focus on explicit cost volume construction and global optimization to infer depth maps. These methods leverage feature pyramids and attention mechanisms to enhance robustness in low-texture regions and complex geometries. Geometry reasoning-driven methods, including NeRF, Plenoxels, and 3D Gaussian splatting, adopt implicit or explicit representations to model scenes. NeRF and its derivatives(e. g. , mip-NeRF, Ref-NeRF)use neural radiance fields to achieve photorealistic view synthesis, while 3DGS introduces Gaussian point clouds for efficient rendering and dynamic scene modeling. Within these categories, methods can further be divided into local modeling and global modeling subcategories. Local modeling approaches, such as PatchMatch and Gipuma, emphasize pixel-level matching and plane-induced homography, while global modeling techniques prioritize holistic scene consistency through volumetric or hierarchical representations. Innovations in recent works include sparse-to-dense depth estimation, adaptive sampling strategies, and hybrid architectures that combine explicit structures(e. g. , octrees)with implicit neural networks to balance efficiency and detail preservation. Third, the paper identifies unresolved challenges and outlines future research directions. Data-related challenges include the difficulty of collecting high-quality multi-view datasets for dynamic scenes and the need for scalable annotation tools to reduce human labor. From a methodological perspective, existing techniques face limitations in computational efficiency(e. g. , cubic memory complexity in NeRF)and generalization to unseen environments(e. g. , natural vegetation or translucent objects). Training paradigms also need to be improved; supervised methods depend on expensive 3D annotations, while unsupervised and self-supervised approaches often sacrifice reconstruction quality for reduced data dependency. To address these issues, future research should focus on the following: 1)lightweight and real-time optimization, which involves developing hardware-aware architectures(e. g. , edge computing frameworks) and dynamic resolution adjustment to reduce GPU memory consumption and inference latency; 2)dynamic scene modeling, integrating temporal consistency constraints and physics-based priors to handle motion, occlusions, and deformable objects in real-world applications; 3)cross-modal fusion, leveraging multimodal inputs(e. g. , LiDAR, inertial sensors) to enhance robustness in low-texture or adverse lighting conditions, and 4)semantic-aware reconstruction, incorporating semantic segmentation and instance-level reasoning to enable editable 3D models for virtual production and interactive design. The convergence of MVS with emerging technologies such as multimodal large models and metaverse platforms will further expand its applications. For example, real-time 3D reconstruction in autonomous vehicles requires not only geometric precision but also semantic understanding for obstacle detection. Similarly, metaverse environments demand highfidelity, scalable reconstructions of large-scale urban scenes. To bridge the gap between academic advancements and industrial deployment, future efforts must prioritize domain adaptation, computational efficiency, and cross-modal learning. By addressing these challenges, MVS 3D reconstruction will play a pivotal role in shaping next-generation immersive technologies, robotics, and digital twins. Additionally, the integration of multitask learning and meta-learning could further enhance model generalization by jointly optimizing geometric and semantic tasks. For instance, meta-learning frameworks could adapt to novel object categories with minimal samples, while multitask architectures might simultaneously reconstruct geometry and infer surface properties(e. g. , material reflectance). Furthermore, the development of 3D foundation models that are pretrained on vast heterogeneous datasets could unlock universal reconstruction capabilities across diverse domains. Ethical considerations, such as privacy in public space reconstruction and bias in dataset curation, must be addressed to ensure responsible deployment. Addressing these multidimensional challenges will enable MVS to evolve from a research-oriented technique to an indispensable tool for real-world 3D perception. © 2026 Editorial and Publishing Board of JIG. All rights reserved.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
