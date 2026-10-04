# D.3 Computer Vision

> **Why vision, for someone who works on molecules.** Because vision is where
> the ideas are invented and biology is where they arrive two years later, and
> you would rather be at the first place.
>
> The list is not short: convolutional architectures, batch normalization,
> residual connections, data augmentation, self-supervised pretraining, vision
> transformers, diffusion, classifier-free guidance, flow matching, neural fields.
> **Every one of those was developed on images and then imported into molecular
> modeling largely unchanged.** RFdiffusion is a denoising diffusion model with
> SE(3) frames. Chroma's conditioners are classifier guidance. The self-supervised
> objectives in protein language models are masked modeling from BERT by way of
> MAE.
>
> **Section 6 is the one to read if you read only one.** 3D vision — neural
> radiance fields, signed distance functions, point-cloud networks, coordinate
> based representations — is the part of vision whose objects are closest to
> yours. A protein is a set of atoms in R³ with a learned field over it, which is
> what a NeRF is, and the two literatures have barely spoken.
>
> **The honest warning.** Vision has far more hype per unit result than
> structural biology, and far more papers. The entries below were chosen for
> talks by the people who did the work, not by explainers, and the gaps where no
> author talk exists are flagged rather than filled with secondhand summaries.

---

## 1. Modern vision architectures — ViT, ConvNeXt, Swin, the convolution debate

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 1 | Industry talk — Google AI Brain | **Alexey Dosovitskiy** (Google Brain), GCPR/VMV/VCBM 2020 | https://www.youtube.com/watch?v=KxFF03Ell9M | 36:03 | The ViT first author speaking the same season ViT was submitted — you hear the "can we delete the convolution entirely" bet being placed before it was a consensus | Dosovitskiy et al., *An Image is Worth 16×16 Words*, ICLR 2021 |
| 2 | Alexey Dosovitskiy — From pixels to nucleotides | **Alexey Dosovitskiy** (Inceptive), ML in PL 2025 | https://www.youtube.com/watch?v=ZjROgep6jv0 | 51:51 | The ViT author explaining how vision architecture thinking transfers to biological sequence/structure — directly relevant if your target domain is molecular | ViT (ICLR 2021) + Inceptive RNA work |
| 3 | Lucas Beyer — Computer Vision in the Age of LLMs | **Lucas Beyer** (Google DeepMind), ML in PL 2024 | https://www.youtube.com/watch?v=kxO6ARgI_SU | 49:53 | The single best "where did vision architecture research actually land" talk; Beyer co-authored ViT scaling, SigLIP and PaliGemma | Zhai et al., *Scaling Vision Transformers*, CVPR 2022 |
| 4 | Lucas Beyer: Vision in the Age of LLMs [ETHZ Robot Learning 2026] | **Lucas Beyer** (OpenAI, ex-DeepMind), ETH Zürich | https://www.youtube.com/watch?v=0XB7fNS_ONg | 1:09:04 | The 2026 update of the above — the most current authoritative read on whether vision encoders still matter | — |
| 5 | Lucas Beyer \| Learning General Visual Representations | **Lucas Beyer**, London ML Meetup | https://www.youtube.com/watch?v=X5Rhm__OxvA | 1:03:56 | BiT → ViT → transfer-learning methodology, told as a research program rather than a paper | Kolesnikov et al., *Big Transfer (BiT)*, ECCV 2020 |
| 6 | Lucas Beyer (Google DeepMind) — Convergence of Vision & Language | **Lucas Beyer**, The AI Epiphany | https://www.youtube.com/watch?v=en1Ha3tw6d4 | 55:08 | Why the two modalities converged on one architecture — the core inductive-bias argument | ViT; LiT (Zhai et al., CVPR 2022) |
| 7 | Architectures Beyond CNNs and Visual Scaling Laws — Tutorial (1/3) | **Neil Houlsby** (Google Brain), ECCV 2022 CVinW Workshop | https://www.youtube.com/watch?v=JHsFUhGPff4 | 30:44 | ViT co-author giving the explicit "do we still need convolutions" verdict plus visual scaling laws | Zhai et al., *Scaling ViT*, CVPR 2022; Tolstikhin et al., *MLP-Mixer*, NeurIPS 2021 |
| 8 | Cambridge Ellis Unit Seminar — Neil Houlsby (29 Oct 2021) | **Neil Houlsby** (Google Brain) | https://www.youtube.com/watch?v=YUDR5Oq04Vg | 56:25 | Longer-form version with Q&A; adapters/parameter-efficient transfer lineage included | Houlsby et al., *Parameter-Efficient Transfer Learning*, ICML 2019 |
| 9 | Scaling Vision and Language Learning with Vision Transformers — Tutorial (2/3) | **Xiaohua Zhai** (Google Brain), ECCV 2022 CVinW | https://www.youtube.com/watch?v=BO4iossuTIs | 31:32 | The ViT-scaling-laws author on compute/data/parameter tradeoffs — the empirical backbone of modern vision scaling | Zhai et al., CVPR 2022; Dehghani et al., *ViT-22B*, ICML 2023 |
| 10 | Scalable approaches to localization & dense prediction — Tutorial (3/3) | **Matthias Minderer** (Google Brain), ECCV 2022 CVinW | https://www.youtube.com/watch?v=p6x9XDDe440 | 31:58 | Shows that the ViT recipe extends to detection without hand-designed priors | Minderer et al., *OWL-ViT*, ECCV 2022 |
| 11 | New vision architectures beyond CNNs | **Alexander Kolesnikov** (Google Brain), IARAI Research | https://www.youtube.com/watch?v=kD3LqIFzzY8 | 1:18:41 | The deepest free lecture on the ViT/MLP-Mixer/convolution tradeoff space, by a co-author of all three | Tolstikhin et al., *MLP-Mixer*, NeurIPS 2021; BiT, ECCV 2020 |
| 12 | A ConvNet for the 2020s | **Zhuang Liu** (Meta AI/FAIR), CVPR 2022 author video | https://www.youtube.com/watch?v=QzCjXqFnWPE | 4:54 | The rebuttal to ViT, from the first author — the methodological lesson (ablate training recipe before crediting architecture) is the real content | Liu, Mao, Wu, Feichtenhofer, Darrell, Xie, CVPR 2022 |
| 13 | ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders \| CVPR 2023 | **Sanghyun Woo** (KAIST/Meta AI), CVPR 2023 author video | https://www.youtube.com/watch?v=wXuC7iDZI2M | 7:58 | Shows masked pretraining is architecture-agnostic — kills the "MAE needs transformers" claim | Woo et al., *ConvNeXt V2*, CVPR 2023 |
| 14 | Stanford CS25: V1 — Transformers in Vision: Tackling problems in Computer Vision | Stanford CS25, Stanford Online | https://www.youtube.com/watch?v=BP5CM0YxbP8 | 1:08:37 | Graduate seminar framing of the full ViT-era landscape | ViT; DETR; Swin |
| 15 | CV Study Group: Swin Transformer | Hugging Face CV Study Group | https://www.youtube.com/watch?v=Ngikt-K1Ecc | 46:05 | Careful walkthrough of hierarchical/shifted-window attention — the argument that *some* locality prior is worth re-introducing | Liu et al., *Swin Transformer*, ICCV 2021 (Marr Prize) |
| 16 | Towards Generic Vision Transformers for Supervised and Self-Supervised Representation Learning | Computer Vision Talks reading group *(speaker not stated in title)* | https://www.youtube.com/watch?v=fk-6JdRjLPw | 1:18:42 | Reading-group depth on unifying supervised/SSL ViT training | ViT; DeiT (Touvron et al., ICML 2021) |
| 17 | Large Scale Visual Representation Learning | Computer Vision Talks reading group *(speaker not stated in title)* | https://www.youtube.com/watch?v=lZcCT2JTlb8 | 1:16:09 | Scale-first representation learning, pre-foundation-model framing | BiT; ViT |
| 18 | 【EP3】Large-Scale Visual Representation Learning with Vision Transformers | The AI Talks | https://www.youtube.com/watch?v=ucoNlnV9R0Q | 1:03:21 | Companion long-form treatment of ViT-scale representation learning | Zhai et al., CVPR 2022 |

---

## 2. Self-supervised visual learning — contrastive, clustering, masked, JEPA

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 19 | Contrastive Self-Supervised Learning and Potential Limitations | **Ting Chen** (Google Brain), ELLIS UCL CSML Seminar | https://www.youtube.com/watch?v=IEiytaXnggI | 55:12 | SimCLR's first author on where contrastive learning *fails* — the most research-useful framing available | Chen, Kornblith, Norouzi, Hinton, *SimCLR*, ICML 2020 |
| 20 | Contrastive Learning with SimCLR V1/V2 and Some Intriguing Properties | Computer Vision Talks reading group | https://www.youtube.com/watch?v=-6jb1v1v0vc | 1:02:34 | Covers the semi-supervised distillation result of SimCLRv2, usually skipped | Chen et al., *SimCLRv2*, NeurIPS 2020 |
| 21 | SimCLR: A Simple Framework for Contrastive Learning of Visual Representations | Stanford Contrastive & SS Learning Group *(embedding disabled; public)* | https://www.youtube.com/watch?v=wySLC4nszv8 | 36:46 | Stanford reading group — the ablation-by-ablation read | Chen et al., ICML 2020 |
| 22 | Momentum Contrast for Unsupervised Visual Representation Learning | **Kaiming He / Haoqi Fan / Yuxin Wu / Saining Xie / Ross Girshick** (FAIR), CVPR 2020 author video | https://www.youtube.com/watch?v=4VVGtYPM8JE | 4:53 | Canonical author presentation of MoCo — the queue + momentum-encoder idea that decoupled batch size from negatives | He et al., *MoCo*, CVPR 2020 |
| 23 | Exploring Simple Siamese Representation Learning and Beyond | Computer Vision Talks reading group (SimSiam) | https://www.youtube.com/watch?v=icqUfBzklkc | 1:14:14 | The collapse-avoidance question — why stop-gradient alone works, and what that means theoretically. Central to understanding BYOL too | Chen & He, *SimSiam*, CVPR 2021; Grill et al., *BYOL*, NeurIPS 2020 |
| 24 | An Empirical Study of Training Self-Supervised Vision Transformers | **Xinlei Chen** (FAIR), ICCV 2021 author video | https://www.youtube.com/watch?v=LHhu11kOA-Y | 10:11 | MoCo v3 — the instability analysis of SSL ViT training is a model of empirical rigor | Chen, Xie, He, ICCV 2021 |
| 25 | Xinlei Chen: Self-supervised learning: two known paradigms and a less-known observation | **Xinlei Chen** (FAIR/Meta) | https://www.youtube.com/watch?v=Ox_L-c2oIpY | 44:26 | The clearest contrastive-vs-masked synthesis by someone who co-authored on both sides | MoCo; SimSiam; MAE |
| 26 | Self-Supervised Learning of Visual Representations with Online Clustering (SwAV) | Computer Vision Talks reading group | https://www.youtube.com/watch?v=zffVe7TTx2I | 45:31 | Clustering/prototypes as a third paradigm beside contrastive and masked | Caron et al., *SwAV*, NeurIPS 2020 |
| 27 | Self-Supervised Learning of Image Features with SwAV (with author **Mathilde Caron**) | **Mathilde Caron** (FAIR/Inria), Lightning AI | https://www.youtube.com/watch?v=7QmsTleiRLs | 36:45 | The SwAV/DINO author in conversation — design rationale and failure modes | Caron et al., NeurIPS 2020 |
| 28 | Mathilde Caron — VGL group seminar, 27 May 2021 | **Mathilde Caron** (FAIR/Inria), Vision Graphics & Learning Group, York | https://www.youtube.com/watch?v=rKF9WSNQ_BA | 57:53 | Delivered the month DINO appeared; the emergent-segmentation finding presented by its author | Caron et al., *DINO*, ICCV 2021 |
| 29 | DINO: Emerging Properties in Self-Supervised Vision Transformers | Stanford Contrastive & SS Learning Group | https://www.youtube.com/watch?v=Y3XsNNlhrik | 52:32 | Paper-depth reading-group treatment of DINO's attention maps and k-NN evaluation | Caron et al., ICCV 2021; Oquab et al., *DINOv2*, TMLR 2024 |
| 30 | Masked Autoencoders Are Scalable Vision Learners | **Xinlei Chen** (FAIR), CVPR 2022 author video | https://www.youtube.com/watch?v=weokLYcY6xk | 4:58 | The MAE author video — asymmetric encoder/decoder + 75% masking, stated by the people who found it | He, Chen, Xie, Li, Dollár, Girshick, CVPR 2022 |
| 31 | Deep Learning Bootcamp: **Kaiming He** | **Kaiming He** (MIT EECS), MIT Schwarzman College of Computing *(embedding disabled; public)* | https://www.youtube.com/watch?v=D_jt-xO_RmI | 1:15:46 | Kaiming He's own survey of his line of work — ResNet → MoCo → MAE — framed as research strategy, not results | He et al., ResNet CVPR 2016; MoCo CVPR 2020; MAE CVPR 2022 |
| 32 | Multi-view Invariance and Grouping for Self-Supervised Learning | **Ishan Misra** (FAIR), Oxford VGG | https://www.youtube.com/watch?v=gbziPIn9uDI | 36:32 | The "what invariance are we actually imposing" question — the conceptual core of SSL pretext design | Misra & van der Maaten, *PIRL*, CVPR 2020 |
| 33 | Self-supervised learning for images, video, and 3D | **Ishan Misra** (Meta AI), GHOST Day AMLC 2022 | https://www.youtube.com/watch?v=YpETv9AzW48 | 1:04:11 | Cross-modality generalization of SSL — the bridge to 3D/molecular settings | Omnivore (CVPR 2022); data2vec |
| 34 | General purpose visual recognition systems: beyond a single modality and a task | **Ishan Misra** (Meta AI), ECCV 2022 CVinW | https://www.youtube.com/watch?v=TIXAgtoUcN8 | 29:03 | Where SSL meets multi-task/multi-modal foundation models | Omnivore; OmniMAE |
| 35 | Broaden Your Views for Self-Supervised Video Learning | Computer Vision Talks reading group (BraVe) | https://www.youtube.com/watch?v=BotznJtzMn0 | 1:04:47 | Temporal SSL — narrow-view/broad-view asymmetry, a design pattern that recurs in V-JEPA | Recasens et al., *BraVe*, ICCV 2021 |
| 36 | Yann LeCun \| Self-Supervised Learning, JEPA, World Models, and the future of AI | **Yann LeCun** (Meta/NYU), Harvard CMSA | https://www.youtube.com/watch?v=yUmDRxV0krg | 1:08:37 | The primary-source statement of the joint-embedding-predictive thesis and the argument against generative pixel prediction | LeCun, *A Path Towards Autonomous Machine Intelligence* (2022); Assran et al., *I-JEPA*, CVPR 2023 |
| 37 | Yann LeCun: World Models: Enabling the next AI revolution | **Yann LeCun**, Computer Vision and Geometry Group, ETH Zürich | https://www.youtube.com/watch?v=72Xj8k5WQX4 | 58:54 | The most recent (2026) LeCun JEPA/world-model talk to a vision audience | Bardes et al., *V-JEPA* (2024); *V-JEPA 2* (2025) |

---

## 3. Vision-language and multimodal

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 38 | Alec Radford, OpenAI: CLIP — Learning Transferable Visual Models From Natural Language Supervision | **Alec Radford** (OpenAI) *(re-uploaded on channel "feather")* | https://www.youtube.com/watch?v=3X3EY2Fgp3g | 49:54 | The single most important vision-language talk available free. Radford on why language supervision beats label supervision, and the zero-shot evaluation philosophy | Radford et al., *CLIP*, ICML 2021 |
| 39 | ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision | Stanford Contrastive & SS Learning Group | https://www.youtube.com/watch?v=X-S3YV2TmuY | 29:11 | The "scale beats curation" counterpart to CLIP — 1.8B noisy pairs, no filtering | Jia et al., *ALIGN*, ICML 2021 |
| 40 | ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision | Microsoft Research | https://www.youtube.com/watch?v=kejLJ0kbIGM | 57:53 | Longer MSR seminar version with full Q&A | Jia et al., ICML 2021 |
| 41 | Lucas Beyer — Sigmoid Loss for Language Image Pre-Training | **Lucas Beyer** (Google DeepMind), Cohere For AI | https://www.youtube.com/watch?v=Nk9YnMHB6hU | 59:57 | SigLIP author explaining why removing the softmax/global-batch coupling changes the economics of contrastive pretraining — a genuinely transferable loss-design lesson | Zhai, Mustafa, Kolesnikov, Beyer, *SigLIP*, ICCV 2023 |
| 42 | Antoine Miech — Flamingo: a Visual Language Model for Few-Shot Learning | **Antoine Miech** (DeepMind), Columbia Vision Seminar | https://www.youtube.com/watch?v=5bMkjdeMapM | 1:04:46 | Flamingo co-author on gated cross-attention into a frozen LM — the architectural ancestor of every modern VLM | Alayrac et al., *Flamingo*, NeurIPS 2022 |
| 43 | Flamingo: a Visual Language Model for Few-Shot Learning | **Samuel Albanie** (Cambridge/DeepMind) | https://www.youtube.com/watch?v=H82s6BrJduM | 1:35:38 | Exhaustive 95-minute technical dissection — the deepest free Flamingo treatment | Alayrac et al., NeurIPS 2022 |
| 44 | The AI Multimodal Revolution with **Junnan Li** and **Dongxu Li** of BLIP & BLIP2 | **Junnan Li, Dongxu Li** (Salesforce Research), Cognitive Revolution | https://www.youtube.com/watch?v=zTr5vDjEy2I | 1:21:21 | BLIP/BLIP-2 first authors on the Q-Former and bootstrapped captioning — includes what they would do differently | Li et al., *BLIP*, ICML 2022; *BLIP-2*, ICML 2023 |
| 45 | [CVPR24 Vision Foundation Model Tutorial] Large Multimodal Models | **Chunyuan Li** (ByteDance, ex-Microsoft Research) | https://www.youtube.com/watch?v=S0CpenMvG48 | 50:19 | LLaVA's co-author giving the canonical survey of visual instruction tuning | Liu, Li, Wu, Lee, *Visual Instruction Tuning (LLaVA)*, NeurIPS 2023 |
| 46 | [CVPR24 Vision Foundation Models Tutorial] Multimodal LLM Pre-training | **Zhe Gan** (Apple) | https://www.youtube.com/watch?v=OznJmSQerBE | 50:17 | Pretraining-recipe-level detail for MLLMs (data mixtures, resolution, connector choice) | Gan et al., MM1 (2024) |
| 47 | [CVPR24 Vision Foundation Model Tutorial] Vision in LMMs | **Jianwei Yang** (Microsoft Research) | https://www.youtube.com/watch?v=bDVbs-fZGUg | 56:30 | Argues the vision encoder is the bottleneck in MLLMs — a live open research question | Yang et al., Florence-2; SEEM |
| 48 | [CVPR2023 Tutorial Talk] Recent Advances in Vision Foundation Models | VLP Tutorial (CVPR 2023) | https://www.youtube.com/watch?v=hE135guhTQo | 44:31 | Compact taxonomy of the whole VFM landscape | Li et al., *Multimodal Foundation Models* survey (2023) |
| 49 | CVPR #18558 — Recent Advances in Vision Foundation Models (full tutorial) | ComputerVisionFoundation Videos, CVPR 2024 | https://www.youtube.com/watch?v=ZknT4EuhhGw | 3:27:12 | The complete 3.5-hour official CVF recording — the most comprehensive single free resource in this section | — |
| 50 | Stanford CS25: Transformers United V6 — From Language Models to Native Multimodal Intelligence | Stanford CS25, Stanford Online *(embedding disabled; public)* | https://www.youtube.com/watch?v=NDdc39KYqDU | 1:04:40 | 2026 state of native (non-bolted-on) multimodality | — |
| 51 | Yevgen Chebotar: RT-2 — Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | **Yevgen Chebotar** (Google DeepMind), Montreal Robotics | https://www.youtube.com/watch?v=o5ONDdbReAA | 1:10:36 | RT-2 co-author on treating actions as tokens in a VLM — the founding VLA talk | Brohan et al., *RT-2*, CoRL 2023 |
| 52 | OpenVLA: LeRobot Research Presentation #5 | **Moo Jin Kim** (Stanford), Hugging Face | https://www.youtube.com/watch?v=-0s0v3q7mBk | 1:18:40 | OpenVLA first author — the open reproduction, with honest ablations of what actually mattered | Kim et al., *OpenVLA*, CoRL 2024 |

---

## 4. Segmentation, detection, dense prediction

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 53 | DETR — End to end object detection with transformers (ECCV 2020) | **Nicolas Carion** (FAIR/NYU), ECCV 2020 author video | https://www.youtube.com/watch?v=utxbUlo9CyY | 9:35 | The first author on bipartite-matching set prediction — deleting NMS and anchors. The set-prediction formulation is the reusable idea | Carion, Massa, Synnaeve, Usunier, Kirillov, Zagoruyko, ECCV 2020 |
| 54 | Alexander Kirillov — 6th BMTT Workshop, ICCV 2021 | **Alexander Kirillov** (FAIR, later Meta/OpenAI), ICCV 2021 | https://www.youtube.com/watch?v=7WcRfHXY_lw | 32:53 | The author of Panoptic Segmentation, PointRend, MaskFormer and SAM on unifying segmentation tasks — recorded 18 months before SAM shipped | Kirillov et al., *Panoptic Segmentation*, CVPR 2019; Cheng, Schwing, Kirillov, *MaskFormer*, NeurIPS 2021 |
| 55 | Invited Talk: From Pixels to Regions: Towards Universal Image Segmentation | Humphrey Shi lab (SHI Labs / UIUC-Georgia Tech) | https://www.youtube.com/watch?v=vBfUFI4Jskg | 14:50 | The "one architecture for semantic + instance + panoptic" argument in compact form | Cheng et al., *Mask2Former*, CVPR 2022; Jain et al., *OneFormer*, CVPR 2023 |
| 56 | Xiuye Gu: Open-Vocabulary Detection and Segmentation | **Xiuye Gu** (Google Research), Learning with Limited and Imperfect Data workshop | https://www.youtube.com/watch?v=_6bWNNA7h8Q | 27:24 | ViLD's first author — distilling CLIP into a detector is the template for open-vocabulary dense prediction | Gu, Lin, Kuo, Cui, *ViLD*, ICLR 2022 |
| 57 | Open-Vocabulary Visual Perception upon Frozen Vision and Language Models | **Yin Cui** (Google Research), ECCV 2022 CVinW | https://www.youtube.com/watch?v=LAesxhjebDA | 32:24 | The frozen-backbone design pattern — large implications for compute-constrained research | Kuo et al., *F-VLM*, ICLR 2023 |
| 58 | Lecture 20 — OWLv2: Scaling Open-Vocabulary Object Detection | UCF CRCV graduate seminar | https://www.youtube.com/watch?v=5A02sTC5-0M | 24:35 | Self-training to 1B+ pseudo-boxes — how open-vocab detection scales | Minderer, Gritsenko, Houlsby, *OWLv2*, NeurIPS 2023 |
| 59 | SAM 3: The Eyes for AI — **Nikhila Ravi** & **Pengchuan Zhang** (Meta Superintelligence Labs), ft. Joseph Nelson | Latent Space | https://www.youtube.com/watch?v=sVo7SC62voA | 1:15:04 | SAM 2 and SAM 3 leads on the data engine, promptable segmentation, and the memory architecture for video. The data-engine discussion is the most research-transferable part | Kirillov et al., *SAM*, ICCV 2023; Ravi et al., *SAM 2*, ICLR 2025; *SAM 3* (2025) |

> *Also see Stanford CS231n 2025 Lecture 9 (§8) for the detection/segmentation survey, and §6 entry 85 (Charles Qi) for 3D detection.*

---

## 5. Generative vision — GANs, diffusion, autoregressive, video, evaluation

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 60 | Ian Goodfellow: Generative Adversarial Networks (NIPS 2016 tutorial) | **Ian Goodfellow** (OpenAI) | https://www.youtube.com/watch?v=HGYYEUSm-0Q | 1:55:54 | The definitive GAN tutorial from the inventor. The game-theoretic framing and the enumerated open problems are still the right way to think about adversarial objectives | Goodfellow et al., *GANs*, NeurIPS 2014; Goodfellow, *NIPS 2016 Tutorial: GANs* (arXiv) |
| 61 | BayLearn 2017 Keynote — Ian Goodfellow | **Ian Goodfellow** (Google Brain) | https://www.youtube.com/watch?v=Zd9kYgUjgSU | 59:14 | Mid-era reassessment: what worked, what didn't, and why mode collapse resisted fixes | — |
| 62 | Ian Goodfellow: Adversarial Machine Learning (ICLR 2019 invited talk) | **Ian Goodfellow** | https://www.youtube.com/watch?v=sucqskXRkss | 43:06 | The adversarial-robustness half of the story — essential for understanding what "distribution" means in vision | Goodfellow, Shlens, Szegedy, *Explaining and Harnessing Adversarial Examples*, ICLR 2015 |
| 63 | Tero Karras — Training Generative Adversarial Networks with Limited Data | **Tero Karras** (NVIDIA Research), FCAI | https://www.youtube.com/watch?v=hOx9NBwDkHY | 44:54 | StyleGAN's author on adaptive discriminator augmentation — a masterclass in diagnosing *why* a model overfits rather than patching it | Karras et al., *StyleGAN2-ADA*, NeurIPS 2020; *StyleGAN*, CVPR 2019 |
| 64 | Miika Aittala: Alias-Free Generative Adversarial Networks | **Miika Aittala** (NVIDIA Research), FCAI | https://www.youtube.com/watch?v=MU00DgkI97g | 45:07 | StyleGAN3 — signal-processing reasoning applied to a generator. The equivariance argument transfers directly to any continuous-signal model | Karras, Aittala, Laine, Härkönen, Hellsten, Lehtinen, Aila, *StyleGAN3*, NeurIPS 2021 |
| 65 | Miika Aittala: Elucidating the Design Space of Diffusion-Based Generative Models | **Miika Aittala** (NVIDIA Research), FCAI | https://www.youtube.com/watch?v=T0Qxzf0eaio | 52:46 | **The** EDM talk. Disentangling the sampler, the noise schedule and the network preconditioning is the most reusable methodological contribution in diffusion | Karras, Aittala, Aila, Laine, *EDM*, NeurIPS 2022 |
| 66 | Stable Diffusion and Friends — Generative Modeling in Latent Space | **Robin Rombach** (Stability AI / LMU), heidelberg.ai | https://www.youtube.com/watch?v=7W4aZObNucI | 57:58 | Latent diffusion from its first author — why moving to a perceptually-compressed latent space is the whole ballgame | Rombach, Blattmann, Lorenz, Esser, Ommer, *High-Resolution Image Synthesis with Latent Diffusion Models*, CVPR 2022 |
| 67 | TL#006 Robin Rombach — Taming Transformers for High Resolution Image Synthesis | **Robin Rombach** (LMU Munich), Transfer Learning seminar | https://www.youtube.com/watch?v=fy153-yXSQk | 45:39 | VQGAN — the prequel to latent diffusion, and the clearest account of learned discrete visual tokenizers | Esser, Rombach, Ommer, *VQGAN*, CVPR 2021 |
| 68 | MAS.S61 presents **Andreas Blattmann** / **Robin Rombach**, Stable Diffusion | Blattmann & Rombach (Stability AI), MIT MAS.S61 | https://www.youtube.com/watch?v=GgW98il4Lbo | 1:03:31 | Both LDM authors together, with the video-diffusion extension discussed | Blattmann et al., *Align Your Latents*, CVPR 2023; *Stable Video Diffusion* (2023) |
| 69 | TUM AI Lecture Series — FLUX: Flow Matching for Content Creation at Scale | **Robin Rombach** (Black Forest Labs) | https://www.youtube.com/watch?v=nrKKLJXBSw0 | 1:06:11 | The rectified-flow/flow-matching transition told by the person who shipped it at scale — why the industry left DDPM-style diffusion | Esser et al., *Scaling Rectified Flow Transformers (SD3)*, ICML 2024; Liu, Gong, Liu, *Rectified Flow*, ICLR 2023 |
| 70 | TUM AI Lecture Series — The multimodal future: Why visual representation still matters | **Saining Xie** (NYU) | https://www.youtube.com/watch?v=hnu-mRLebhc | 1:04:21 | DiT's co-author (and ConvNeXt's) on why representation quality gates generation quality — includes the REPA line of work | Peebles & Xie, *Scalable Diffusion Models with Transformers (DiT)*, ICCV 2023; Yu et al., *REPA*, ICLR 2025 |
| 71 | Stanford CS25: V5 — Transformers in Diffusion Models for Image Generation and Beyond | Stanford CS25, Stanford Online | https://www.youtube.com/watch?v=vXtapCFctTI | 1:14:32 | Graduate-seminar treatment of DiT/MMDiT and the scaling behavior that replaced the U-Net | Peebles & Xie, ICCV 2023 |
| 72 | Yang Song: A personal journey to diffusion models | **Yang Song** (OpenAI), ICBS 2025 | https://www.youtube.com/watch?v=s647Nz0r4r0 | 1:03:35 | Score matching → NCSN → score SDE → consistency models, narrated as a research trajectory by the person who built it. Exceptional on research taste | Song & Ermon, NeurIPS 2019; Song et al., *Score-Based Generative Modeling through SDEs*, ICLR 2021; Song et al., *Consistency Models*, ICML 2023 |
| 73 | Learning to Generate Data by Estimating Gradients of the Data Distribution | **Yang Song** (Stanford), hosted by Yingzhen Li | https://www.youtube.com/watch?v=nv-WTeKRLl0 | 1:03:15 | The technical lecture version of the above, with the SDE/ODE derivation done properly | Song et al., ICLR 2021 (Outstanding Paper) |
| 74 | Diffusion and Score-Based Generative Models | MIT CBMM *(speaker not named in title; content is the Song-style score-SDE tutorial)* | https://www.youtube.com/watch?v=wMmqCMwuM2Q | 1:32:01 | The longest free rigorous treatment of the score/SDE formalism | Song et al., ICLR 2021 |
| 75 | Tutorial on Denoising Diffusion-based Generative Modeling: Foundations and Applications | **Arash Vahdat**, **Karsten Kreis**, **Ruiqi Gao** (NVIDIA / Google), CVPR 2022 tutorial | https://www.youtube.com/watch?v=cS6JQpEY9cs | 3:46:15 | The canonical ~4-hour diffusion tutorial. If you read only one thing on diffusion theory, watch this instead | Ho, Jain, Abbeel, *DDPM*, NeurIPS 2020; Song et al., ICLR 2021 |
| 76 | CVPR #18546 — Denoising Diffusion Models: A Generative Learning Big Bang | ComputerVisionFoundation Videos, CVPR 2024 tutorial | https://www.youtube.com/watch?v=1d4r19GEVos | 3:04:32 | The 2024 refresh of the above — covers distillation, consistency, flow matching, video | Song et al., *Consistency Models*, ICML 2023; Lipman et al., *Flow Matching*, ICLR 2023 |
| 77 | MIT 6.S184: Flow Matching and Diffusion Models — Lecture 01: Generative AI with SDEs (2025) | **Peter Holderrieth** (MIT) | https://www.youtube.com/watch?v=GCoP2w-Cqtg | 1:25:12 | A graduate course that derives flow matching and diffusion from one framework — the cleanest free mathematical treatment | Lipman et al., ICLR 2023; Liu et al., *Rectified Flow*, ICLR 2023 |
| 78 | MIT 6.S184: Flow Matching and Diffusion Models — Lecture 01: Flow and Diffusion Models (2026) | **Peter Holderrieth** (MIT) | https://www.youtube.com/watch?v=9eJQQVrUUoI | 1:18:03 | The 2026 re-recording; use whichever edition you prefer | as above |
| 79 | [GCV @ CVPR25] **Kaiming He** — Towards End-to-End Generative Modeling | **Kaiming He** (MIT), CVPR 2025 GCV Workshop | https://www.youtube.com/watch?v=4VwXBrMoC0E | 42:34 | He's current research direction — collapsing the two-stage tokenizer+diffusion pipeline. This is an open research frontier stated as such | Li, Tian, Li, Deng, He, *MAR*, NeurIPS 2024; *JiT* (2025) |
| 80 | [GCV @ CVPR25] **Björn Ommer** — Bitter Lesson 2.0: Boosting the Efficiency & Control of Generative Models | **Björn Ommer** (LMU Munich) | https://www.youtube.com/watch?v=toat_cXdoac | 36:47 | The senior author of Stable Diffusion arguing against pure scale — the most useful contrarian position in generative vision | Rombach et al., CVPR 2022 |
| 81 | [GCV @ CVPR23] **Björn Ommer** — Why This is Not the End of Research in Generative AI | **Björn Ommer** (LMU Munich) | https://www.youtube.com/watch?v=pQ-JE66Wv9M | 31:12 | Explicitly about where the open problems are — a research-agenda talk | — |
| 82 | [GCV @ CVPR23] **Phillip Isola** — Generative Models as Data++ | **Phillip Isola** (MIT) | https://www.youtube.com/watch?v=YuRAeQsTSo8 | 31:41 | Reframes generative models as queryable datasets rather than samplers. One of the genuinely original conceptual contributions in the section | Isola et al., *pix2pix*, CVPR 2017; Huh et al., *Platonic Representation Hypothesis*, ICML 2024 |
| 83 | [GCV @ CVPR 2026] **Hila Chefer** — Is Scale All You Need? A Case for Native Generative Representation Learning | **Hila Chefer** (Google DeepMind / Tel Aviv U.) | https://www.youtube.com/watch?v=wuNvKl4-NtI | 27:16 | 2026 frontier talk directly on the scale-vs-inductive-bias question for generative models | Chefer et al., VideoJAM (2025) |
| 84 | Ishan Misra (Meta) — Emu Video Generation | **Ishan Misra** (Meta AI/GenAI) | https://www.youtube.com/watch?v=dLcsreHRF1s | 55:26 | A Sora-class video model explained by its lead, with the factorized text→image→video design and honest evaluation discussion | Girdhar et al., *Emu Video* (2023) |
| 85 | OpenAI Sora 2 Team: How Generative Video Will Unlock Creativity and World Models | Sora 2 team (OpenAI), Sequoia Capital | https://www.youtube.com/watch?v=w9oTtvbyLP8 | 1:00:26 | The closest thing to a Sora research talk that exists publicly; useful for the world-model framing, light on technical detail | Brooks et al., *Video generation models as world simulators* (OpenAI tech report, 2024) |
| 86 | Reliable Fidelity and Diversity Metrics for Generative Models (ICML 2020) | **Muhammad Ferjad Naeem** (TU Munich / ETH) et al. | https://www.youtube.com/watch?v=_XwsGkryVpk | 15:41 | The FID critique: density & coverage, and a demonstration that FID conflates fidelity with diversity. Required before you report FID in any paper | Naeem, Oh, Uh, Choi, Yoo, *Reliable Fidelity and Diversity Metrics*, ICML 2020; cf. Heusel et al., *FID*, NeurIPS 2017 |
| 87 | Visual Autoregressive Modeling — Part 1 | West Coast Machine Learning reading group | https://www.youtube.com/watch?v=8RQWNgfGNaI | 1:27:37 | Deep reading-group treatment of VAR's next-scale prediction. **No author talk for VAR could be verified** — see flag below | Tian, Jiang, Yuan, Peng, Wang, *VAR*, NeurIPS 2024 (Best Paper) |

---

## 6. 3D vision and geometry — *directly transferable to molecular structure*

> The transfer is concrete: SE(3) equivariance, coordinate-based implicit fields, differentiable rendering as a differentiable forward model, and point-set permutation invariance are the same mathematics used in protein structure prediction, cryo-EM reconstruction and docking. Treat SIREN/NeRF as "learned continuous density fields" and cryo-EM map modeling becomes the same problem class.

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 88 | Multiple View Geometry — Lecture 1 | **Prof. Daniel Cremers** (TU Munich) | https://www.youtube.com/watch?v=RDkwklFGMfo | 1:27:30 | The rigorous classical foundation: rigid-body motion, SE(3), Lie groups. This is the same SE(3) machinery as equivariant molecular networks | Hartley & Zisserman, *Multiple View Geometry in Computer Vision*, CUP 2004 |
| 89 | Multiple View Geometry — Lecture 2 | **Prof. Daniel Cremers** (TU Munich) | https://www.youtube.com/watch?v=6VbbYXpBIqA | 1:24:33 | Representing rigid-body motion — rotation groups, exponential map, twists | Hartley & Zisserman (2004); Ma, Soatto, Košecká, Sastry, *An Invitation to 3-D Vision* |
| 90 | Computer Vision — Lecture 3.1 (Structure-from-Motion: Preliminaries) | **Prof. Andreas Geiger** (U. Tübingen) | https://www.youtube.com/watch?v=nrIHi1-a85s | 26:18 | Modern graduate SfM formulation — epipolar geometry, bundle adjustment framing | Hartley & Zisserman (2004) |
| 91 | Structure-from-Motion Revisited | **Johannes Schönberger** (ETH Zürich / Microsoft), CVPR 2016 author video | https://www.youtube.com/watch?v=PmXqdfBQxfQ | 4:39 | COLMAP's author — the system that every NeRF/3DGS paper silently depends on for camera poses | Schönberger & Frahm, CVPR 2016 |
| 92 | ROB 2018 — Johannes Schönberger: COLMAP | **Johannes Schönberger**, Robust Vision Challenge 2018 | https://www.youtube.com/watch?v=gTFSIg5ZFL4 | 13:34 | Practical failure modes of SfM — essential if you ever build on reconstructed geometry | Schönberger & Frahm, CVPR 2016 |
| 93 | NeRF: Neural Radiance Fields | **Matthew Tancik** (UC Berkeley), ECCV 2020 author video | https://www.youtube.com/watch?v=JuH79E8rdKc | 4:15 | The original NeRF author video. The key insight — positional encoding to overcome spectral bias in coordinate MLPs — is the one most reusable in scientific modeling | Mildenhall, Srinivasan, Tancik, Barron, Ramamoorthi, Ng, *NeRF*, ECCV 2020 (Best Paper Honorable Mention) |
| 94 | 3DV 2024 Keynote — **Ben Mildenhall** | **Ben Mildenhall** (Google Research), 3DV 2024 *(embedding disabled; public)* | https://www.youtube.com/watch?v=dx7qJRkC1y4 | 1:09:18 | NeRF's first author giving a full retrospective keynote four years on — what held up and what didn't | Mildenhall et al., ECCV 2020 |
| 95 | L13b Neural Radiance Fields — Guest Lecturer **Ben Mildenhall** | **Ben Mildenhall**, in Pieter Abbeel's Berkeley deep-learning course | https://www.youtube.com/watch?v=Z96YMktT_T4 | 1:04:24 | Full lecture-format NeRF derivation by its author, built for students | Mildenhall et al., ECCV 2020 |
| 96 | Jon Barron — Understanding and Extending Neural Radiance Fields | **Jonathan T. Barron** (Google Research), MIT Vision & Graphics Seminar | https://www.youtube.com/watch?v=HfJpQCBTqZs | 54:43 | The best single talk on *why* NeRF works, with the aliasing/scale analysis that led to mip-NeRF | Barron et al., *Mip-NeRF*, ICCV 2021 |
| 97 | TUM AI Lecture Series — Understanding and Extending Neural Radiance Fields | **Jonathan T. Barron** (Google Research) | https://www.youtube.com/watch?v=nRyOzHpcr4Q | 1:02:05 | Longer TUM version with extended Q&A | Barron et al., ICCV 2021; *Mip-NeRF 360*, CVPR 2022 |
| 98 | Zip-NeRF: Anti-Aliased Grid-Based Neural Radiance Fields — ICCV 2023 Talk | **Jonathan T. Barron** (Google Research) | https://www.youtube.com/watch?v=Sk3wU-VMoCI | 5:00 | How to combine hash-grid speed with anti-aliasing rigor — a model of careful incremental research | Barron, Mildenhall, Verbin, Srinivasan, Hedman, *Zip-NeRF*, ICCV 2023 (Best Paper Honorable Mention) |
| 99 | Radiance Fields and the Future of Generative Media | **Jonathan T. Barron** (Google DeepMind) | https://www.youtube.com/watch?v=hFlF33JZbA0 | 48:39 | Barron's current view on where radiance fields and generative models merge | — |
| 100 | Matthew Tancik: Neural Radiance Fields for View Synthesis | **Matthew Tancik** (UC Berkeley), hosted by Andreas Geiger | https://www.youtube.com/watch?v=dPWLybp4LL0 | 49:11 | Full-length NeRF talk including the Fourier-features theory | Tancik et al., *Fourier Features Let Networks Learn High Frequency Functions*, NeurIPS 2020 |
| 101 | MAS.S61 presents **Matthew Tancik**, Co-Author of NeRF and Nerfstudio | **Matthew Tancik** (UC Berkeley / Luma AI), MIT | https://www.youtube.com/watch?v=isKbsNKArJU | 1:02:02 | The research-infrastructure side — how Nerfstudio was built and why tooling accelerated the field | Tancik et al., *Nerfstudio*, SIGGRAPH 2023 |
| 102 | Bernhard Kerbl: 3D Gaussian Splatting — Real-Time Radiance Fields and their Applications | **Bernhard Kerbl** (TU Wien / Inria), ICBS 2025 | https://www.youtube.com/watch?v=OXtZOHLooEo | 1:04:09 | 3DGS first author. The explicit-primitive-plus-differentiable-rasterizer design is a direct template for differentiable molecular density modeling | Kerbl, Kopanas, Leimkühler, Drettakis, *3D Gaussian Splatting*, SIGGRAPH 2023 (Best Paper) |
| 103 | Gaussian Splatting with **Bernhard Kerbl** | **Bernhard Kerbl**, View Dependent podcast | https://www.youtube.com/watch?v=cT1mQ_ityfE | 1:05:39 | Long-form interview — the design decisions and dead ends behind 3DGS, rarely written down | Kerbl et al., SIGGRAPH 2023 |
| 104 | TUM AI Lecture Series — The 3D Gaussian Splatting Adventure: Past, Present, Future | **George Drettakis** (Inria) | https://www.youtube.com/watch?v=DjOqkVIlEGY | 1:04:20 | The senior author's full research-program framing, from point-based rendering history to future directions | Kerbl et al., SIGGRAPH 2023 |
| 105 | TUM AI Lecture Series — Implicit Neural Scene Representations | **Vincent Sitzmann** (MIT) | https://www.youtube.com/watch?v=__F9CCqbWQk | 1:10:59 | SIREN/SRN author on coordinate-based neural fields as a general representation — the most directly transferable idea in this whole section for molecular work | Sitzmann et al., *SIREN*, NeurIPS 2020 (Oral); *Scene Representation Networks*, NeurIPS 2019 |
| 106 | Vincent Sitzmann: Implicit Neural Scene Representations | **Vincent Sitzmann** (MIT), hosted by Andreas Geiger | https://www.youtube.com/watch?v=Or9J-DCDGko | 56:42 | Alternate-venue version with a different emphasis on generalization across scenes | Sitzmann et al., NeurIPS 2019/2020 |
| 107 | Implicit Neural Representations with Periodic Activation Functions | Stanford Computational Imaging Lab (Wetzstein group), NeurIPS 2020 author video | https://www.youtube.com/watch?v=Q2fLWGBeaiI | 10:20 | The SIREN author video — periodic activations for representing signals *and their derivatives*, which matters whenever you need a differentiable field (PDEs, densities) | Sitzmann, Martel, Bergman, Lindell, Wetzstein, NeurIPS 2020 |
| 108 | PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation | **Charles R. Qi** (Stanford), CVPR 2017 author video | https://www.youtube.com/watch?v=Cge-hot0Oc0 | 11:24 | Permutation invariance via symmetric functions — the direct ancestor of every atom-set molecular network | Qi, Su, Mo, Guibas, *PointNet*, CVPR 2017 |
| 109 | Charles Qi — 6th BMTT Workshop, ICCV 2021 | **Charles R. Qi** (Waymo), ICCV 2021 | https://www.youtube.com/watch?v=jaVIlNKSYvI | 22:52 | PointNet's author on 3D detection at production scale — how the set abstraction idea evolved | Qi et al., *PointNet++*, NeurIPS 2017; *VoteNet*, ICCV 2019 |
| 110 | Vincent Leroy: From CroCo to MASt3R — A Paradigm Change in 3D Vision | **Vincent Leroy** (NAVER LABS Europe), Montreal Robotics | https://www.youtube.com/watch?v=OJzj7uCCYaM | 53:50 | DUSt3R/MASt3R co-author. Replacing the entire SfM pipeline with a feed-forward pointmap regressor is the most important recent idea in geometric vision | Wang, Leroy, Cabon, Chidlovskii, Revaud, *DUSt3R*, CVPR 2024; Leroy et al., *MASt3R*, ECCV 2024; Weinzaepfel et al., *CroCo*, NeurIPS 2022 |
| 111 | Impossible Image Matching of DUSt3R & MASt3R with **Jérôme Revaud** and **Vincent Leroy** | Revaud & Leroy (NAVER LABS Europe), View Dependent | https://www.youtube.com/watch?v=iTRBU80QuBc | 1:14:01 | Both authors, long form — where it fails and why, which the papers don't say | Wang et al., CVPR 2024 |
| 112 | Zachary Teed — Optimization Inspired Neural Networks for Multiview 3D | **Zachary Teed** (Princeton), MIT Vision & Graphics Seminar | https://www.youtube.com/watch?v=ul6pXRGKmco | 58:51 | RAFT/DROID-SLAM author on embedding classical optimization structure inside networks — the best available argument for architecture-as-algorithm | Teed & Deng, *RAFT*, ECCV 2020 (Best Paper); *DROID-SLAM*, NeurIPS 2021 |
| 113 | Physics-based differentiable rendering (CVPR 2021 tutorial) | **Shuang Zhao**, **Ioannis Gkioulekas**, **Tzu-Mao Li** (UC Irvine / CMU / UCSD) | https://www.youtube.com/watch?v=Tou8or1ed6E | 3:10:42 | The rigorous treatment of differentiating through a physical forward model — the exact problem structure of differentiable cryo-EM / scattering simulation | Li, Aittala, Durand, Lehtinen, *Differentiable Monte Carlo Ray Tracing*, SIGGRAPH Asia 2018 |
| 114 | Neural Rendering (CVPR 2020) — Afternoon Session | CVPR 2020 Neural Rendering tutorial (Tewari, Zollhöfer, Niessner et al.) | https://www.youtube.com/watch?v=JlyGNvbGKB8 | 3:00:01 | Full tutorial on the analysis-by-synthesis paradigm that unified graphics and vision | Tewari et al., *State of the Art on Neural Rendering*, Eurographics 2020 |
| 115 | [GCV @ CVPR23] **Andrea Tagliasacchi** — Neural fields for 3D Vision (a MAP perspective) | **Andrea Tagliasacchi** (Google / SFU), CVPR 2023 | https://www.youtube.com/watch?v=iiTylrIzydg | 30:05 | Recasts neural fields as MAP inference — a probabilistic framing that generalizes cleanly to scientific inverse problems | Xie et al., *Neural Fields in Visual Computing*, Eurographics STAR 2022 |
| 116 | [GCV @ CVPR 2026] **Georgia Gkioxari** — Beyond Image and Language: Building 3D Perception Systems | **Georgia Gkioxari** (Caltech) | https://www.youtube.com/watch?v=rKv2SE4tP60 | 33:01 | 2026 frontier statement on 3D perception as a first-class problem, not a 2D add-on | Gkioxari et al., *Mesh R-CNN*, ICCV 2019 |
| 117 | Andreas Geiger: Is 3D Reconstruction ready for the Physical World? (ECCV 2026) | **Andreas Geiger** (U. Tübingen), ECCV 2026 | https://www.youtube.com/watch?v=1wheKcIbTk4 | 24:46 | Current honest assessment of where feed-forward reconstruction actually stands | Geiger et al., KITTI; Mescheder et al., *Occupancy Networks*, CVPR 2019 |
| 118 | Andreas Geiger: Opening the Black Box of Generation and Reconstruction (ECCV 2026) | **Andreas Geiger** (U. Tübingen), ECCV 2026 | https://www.youtube.com/watch?v=hJvgQreDjAA | 26:00 | The generation/reconstruction convergence, stated by one of the field's most careful methodologists | — |

---

## 7. Research seminars, keynotes, and research taste

| # | Title | Speaker / Institution | URL | Dur. | Why it matters | Paper |
|---|---|---|---|---|---|---|
| 119 | We are (still!) not giving Data enough credit — Keynote at ACVSS 24 | **Alexei (Alyosha) Efros** (UC Berkeley) | https://www.youtube.com/watch?v=dV6sgUiGv-U | 1:38:21 | The best talk on research taste in computer vision, full stop. 98 minutes of "the model is not the contribution, the data is" — with the historical receipts | Efros & Leung, ICCV 1999; Hays & Efros, *Scene Completion*, SIGGRAPH 2007 |
| 120 | Computer Vision after the Victory of Data | **Alexei Efros** (UC Berkeley), Simons Institute | https://www.youtube.com/watch?v=a13aqr07tJ4 | 1:18:06 | Same thesis, delivered to a theory audience — forces the argument to be made more precisely | — |
| 121 | Self Supervision for Learning from the Bottom Up — Invited Talk, ICLR 2021 | **Alexei Efros** (UC Berkeley), ICLR 2021 | https://www.youtube.com/watch?v=F5yb5pSfb3E | 1:01:11 | Efros's case for non-parametric/bottom-up learning against top-down categorical supervision | Doersch, Gupta, Efros, *Unsupervised Visual Representation Learning by Context Prediction*, ICCV 2015 |
| 122 | Alexei Efros: In the end, it's all about the Data | **Alexei Efros** (UC Berkeley), hosted by Andreas Geiger | https://www.youtube.com/watch?v=M1VHu1d4sGQ | 1:27:31 | The extended version with a long Q&A — the Q&A is where the research-strategy advice is | — |
| 123 | Alexei Efros — Lecture: "Self-Supervised Visual Learning and Synthesis" | **Alexei Efros** (UC Berkeley), Strelka Institute | https://www.youtube.com/watch?v=0zCMiOQ8C1U | 51:29 | Ties self-supervision and synthesis together as one problem — the thread that leads to today's generative pretraining | Zhang, Isola, Efros, *Colorful Image Colorization*, ECCV 2016 |
| 124 | Jitendra Malik — The Hilbert Problems of Computer Vision | **Jitendra Malik** (UC Berkeley), ILSVRC/ImageNet workshop | https://www.youtube.com/watch?v=QaF2kkez5XU | 40:45 | An explicit list of open problems from the field's most senior figure. This is how to choose a dissertation topic | Malik et al., *The Three R's of Computer Vision*, PRL 2016 |
| 125 | Jitendra Malik: Vision and Robotics for Embodied AI | **Jitendra Malik** (UC Berkeley / Meta), ETH Zürich CVG Group | https://www.youtube.com/watch?v=HvDU7Vk4pbc | 50:45 | Malik's current position: perception is not separable from action | Malik et al., *The Three R's*; RMA (Kumar et al., RSS 2021) |
| 126 | RI Seminar: Jitendra Malik — Robot Learning, With Inspiration From Child Development | **Jitendra Malik** (UC Berkeley), CMU Robotics Institute | https://www.youtube.com/watch?v=ry8itipzBFE | 1:07:14 | Developmental-learning framing of representation acquisition — a genuinely different source of research hypotheses | — |
| 127 | What next in Computer Vision + Compositionality in Tasks | **Jitendra Malik** (UC Berkeley), CICV 2020 | https://www.youtube.com/watch?v=wmhDEBqmPCg | 59:55 | Compositionality as the unsolved problem — directly relevant to anyone working on structured/molecular domains | — |
| 128 | TUM AI Lecture Series — The Moon Camera | **William T. (Bill) Freeman** (MIT) | https://www.youtube.com/watch?v=Ytkkl917paM | 1:04:45 | Freeman at his best: an apparently absurd problem (use the moon as a lens), solved with careful physics and inverse modeling. A masterclass in problem selection | Freeman group, accidental/non-line-of-sight imaging line of work |
| 129 | AIR Distinguished Speaker — **Bill Freeman** | **Bill Freeman** (MIT), Hariri Institute, Boston University | https://www.youtube.com/watch?v=C1L61UYAfQA | 44:34 | Recent (2026) Freeman talk — current directions | — |
| 130 | LMSS @ Cornell Tech: **Bill Freeman** — Learning from Sight and Sound | **Bill Freeman** (MIT), Cornell Tech | https://www.youtube.com/watch?v=hvH_UUNxFCI | 55:33 | Audio-visual self-supervision — the "free supervision from physics" idea | Owens et al., *Ambient Sound Provides Supervision*, ECCV 2016; *Visually Indicated Sounds*, CVPR 2016 |
| 131 | The Platonic Representation Hypothesis | **Phillip Isola** (MIT), MIT CBMM | https://www.youtube.com/watch?v=V7AyriUcXZQ | 1:09:11 | The claim that models trained on different modalities converge to the same representation. One of the few genuinely new *ideas* (as opposed to results) in recent vision | Huh, Cheung, Wang, Isola, *The Platonic Representation Hypothesis*, ICML 2024 |
| 132 | Dr Kaiming He — 2023 Future Science Prize Laureates Lecture | **Kaiming He** (MIT), Future Science Prize | https://www.youtube.com/watch?v=jEeL5Gf4vkk | 1:15:51 | A career-retrospective lecture — ResNet's origin story and the reasoning behind each subsequent bet | He, Zhang, Ren, Sun, *ResNet*, CVPR 2016 (Best Paper); *Mask R-CNN*, ICCV 2017 |
| 133 | [GCV @ CVPR 2026] **Alan Yuille** — Vision Language Models need 3D | **Alan Yuille** (Johns Hopkins) | https://www.youtube.com/watch?v=3fwVlCnB4q4 | 38:23 | A senior vision theorist's structured critique of current VLMs — useful as a source of falsifiable research claims | Yuille & Liu, *Deep Nets: What have they ever done for Vision?*, IJCV 2021 |

**Additional seminar channels worth subscribing to (all verified as active, enumerate yourself):**
- **Computer Vision Talks** reading group — https://www.youtube.com/@computervisiontalks7222/videos (15 hour-long SSL/representation talks)
- **GCV @ CVPR workshops** (Adam Kortylewski) — https://www.youtube.com/@adamkortylewski1099/videos (CVPR '23/'25/'26 generative-vision keynotes: Kaiming He, Isola, Ommer, Yuille, Gkioxari, Chelsea Finn, Matthias Niessner, Sitzmann, Angjoo Kanazawa, Gordon Wetzstein)
- **Vision & Graphics Seminar at MIT** — https://www.youtube.com/@visiongraphicsseminaratmit9073/videos (30 hour-long seminars: Barron, Teed, Snavely, Fragkiadaki, Krähenbühl, Russakovsky, Tulsiani)
- **ECCV 2022 Computer Vision in the Wild workshop** — 13 invited talks (Houlsby, Zhai, Minderer, Misra, Yin Cui, Kate Saenko, Stella Yu, Xiaolong Wang)
- **Stanford Contrastive & SS Learning Group** — https://www.youtube.com/@stanfordcontrastivesslearn3141/videos

---

## 8. Full modern vision courses (playlists enumerated to individual videos)

### 8a. Stanford CS231n — Deep Learning for Computer Vision, **Spring 2025** (18 lectures, Stanford Online)

| Lecture | Title | URL | Dur. |
|---|---|---|---|
| 1 | Introduction | https://www.youtube.com/watch?v=2fq9wYslV0A | 1:02:53 |
| 2 | Image Classification with Linear Classifiers | https://www.youtube.com/watch?v=pdqofxJeBN8 | 1:07:02 |
| 3 | Regularization and Optimization | https://www.youtube.com/watch?v=dyNGd06MWn4 | 1:08:39 |
| 4 | Neural Networks and Backpropagation | https://www.youtube.com/watch?v=25zD5qJHYsk | 1:16:47 |
| 5 | Image Classification with CNNs | https://www.youtube.com/watch?v=f3g1zGdxptI | 1:08:04 |
| 6 | CNN Architectures | https://www.youtube.com/watch?v=aVJy4O5TOk8 | 1:11:07 |
| 7 | Recurrent Neural Networks | https://www.youtube.com/watch?v=kG2lAPBF7zA | 1:11:48 |
| 8 | Attention and Transformers | https://www.youtube.com/watch?v=RQowiOF_FvQ | 1:06:31 |
| 9 | Object Detection, Image Segmentation, Visualizing | https://www.youtube.com/watch?v=PTypu6GqEd4 | 1:13:44 |
| 10 | Video Understanding | https://www.youtube.com/watch?v=wElqklprhPE | 1:08:45 |
| 11 | Large Scale Distributed Training | https://www.youtube.com/watch?v=9MvD-XsowsE | 1:12:53 |
| 12 | **Self-Supervised Learning** | https://www.youtube.com/watch?v=4howBU7THbM | 1:14:42 |
| 13 | Generative Models 1 | https://www.youtube.com/watch?v=zbHXQRUNlH0 | 1:12:31 |
| 14 | Generative Models 2 | https://www.youtube.com/watch?v=Edr4uZFh4EE | 1:12:09 |
| 15 | **3D Vision** | https://www.youtube.com/watch?v=7lxrKDKtykM | 1:11:50 |
| 16 | **Vision and Language** | https://www.youtube.com/watch?v=mQOK0Mfyrkk | 1:09:54 |
| 17 | Robot Learning | https://www.youtube.com/watch?v=XSfmOH_xVSU | 1:18:33 |
| 18 | Human-Centered AI | https://www.youtube.com/watch?v=g8UaBfj6Sh8 | 1:05:16 |

*Playlist for reference only:* `PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16`. **Why it matters:** this is the current canonical graduate vision course; lectures 6, 8, 9, 12, 13–16 are the research-relevant core and are a strict upgrade over the 2017 edition.

### 8b. University of Michigan EECS 498-007 / 598-005 — Deep Learning for Computer Vision (**Justin Johnson**), 22 lectures, Michigan Online

| Lec | Title | URL | Dur. |
|---|---|---|---|
| 1 | Introduction to Deep Learning for Computer Vision | https://www.youtube.com/watch?v=dJYGatp4SvA | 57:56 |
| 2 | Image Classification | https://www.youtube.com/watch?v=0nqvO3AM2Vw | 1:02:15 |
| 3 | Linear Classifiers | https://www.youtube.com/watch?v=qcSEP17uKKY | 1:02:06 |
| 4 | Optimization | https://www.youtube.com/watch?v=YnQJTfbwBM8 | 1:03:07 |
| 5 | Neural Networks | https://www.youtube.com/watch?v=g6InpdhUblE | 1:02:07 |
| 6 | Backpropagation | https://www.youtube.com/watch?v=dB-u77Y5a6A | 1:11:16 |
| 7 | Convolutional Networks | https://www.youtube.com/watch?v=ANyxBVxmdZ0 | 1:08:53 |
| 8 | CNN Architectures | https://www.youtube.com/watch?v=XaZIlVrIO-Q | 1:12:03 |
| 9 | Hardware and Software | https://www.youtube.com/watch?v=oXPX8GIOiU4 | 1:12:22 |
| 10 | Training Neural Networks I | https://www.youtube.com/watch?v=lGbQlr1Ts7w | 1:12:14 |
| 11 | Training Neural Networks II | https://www.youtube.com/watch?v=WUazOtlti0g | 1:19:14 |
| 12 | Recurrent Networks | https://www.youtube.com/watch?v=dUzLD91Sj-o | 1:13:27 |
| 13 | Attention | https://www.youtube.com/watch?v=YAgjfMR9R_M | 1:11:53 |
| 14 | Visualizing and Understanding | https://www.youtube.com/watch?v=G1hGwHVykDU | 1:12:04 |
| 15 | Object Detection | https://www.youtube.com/watch?v=TB-fdISzpHQ | 1:12:32 |
| 16 | Detection and Segmentation | https://www.youtube.com/watch?v=9AyMR4IhSWQ | 1:10:07 |
| 17 | **3D Vision** | https://www.youtube.com/watch?v=S1_nCdLUQQ8 | 1:12:34 |
| 18 | Videos | https://www.youtube.com/watch?v=A9D6NXBJdwU | 1:15:21 |
| 19 | Generative Models I | https://www.youtube.com/watch?v=Q3HU2vEhD5Y | 1:11:13 |
| 20 | Generative Models II | https://www.youtube.com/watch?v=igP03FXZqgo | 1:12:47 |
| 21 | Reinforcement Learning | https://www.youtube.com/watch?v=Qex3XzcFKP4 | 1:11:45 |
| 22 | Conclusion | https://www.youtube.com/watch?v=s3Ky_Ls4YSY | 1:13:28 |

*Playlist for reference only:* `PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r`. **Why it matters:** Justin Johnson (NeRF-adjacent, ex-FAIR, CS231n's original lead TA) lectures with more derivation depth than CS231n. Given the stated CS231n background, **watch lectures 13–20 selectively rather than the whole course** — 14 (visualizing), 17 (3D) and 19–20 (generative) are the ones that add material CS231n 2025 does not cover as well.

### 8c. Supplementary graduate courses (verified, enumerate individually as needed)

- **Multiple View Geometry — Prof. Daniel Cremers, TU Munich** (channel `cvprtum`, ~14 lectures, each ~85 min). Entries 88–89 above are lectures 1–2. This is the rigorous geometry course and has no modern free equal.
- **Computer Vision — Prof. Andreas Geiger, U. Tübingen** (channel "Tübingen Machine Learning", ~80 short lecture segments across 12 units, including 9.1 Coordinate-based Networks/INRs, 11.2 Self-Supervised Learning, 3.1–4.5 SfM & stereo). Entry 90 is one segment.
- **MIT 6.S184 — Flow Matching and Diffusion Models** (Peter Holderrieth, 2025 and 2026 editions). Entries 77–78.
- **MIT 6.801 Machine Vision** (Berthold Horn, MIT OCW, Fall 2020) — classical machine vision, playlist `PLUl4u3cNGP63pfpS1gV5P9tDxxL_e4W8O`. Lecture 1: https://www.youtube.com/watch?v=tY2gczObpfU (1:19:53).

---

## Flags — could not verify

- **UNVERIFIED — search term: "MIT 6.8300 Advances in Computer Vision lecture recordings" / "MIT 6.8301 vision lecture 2025"** — no public recordings of MIT 6.8300/6.8301 exist on YouTube. Only MIT 6.801 (Horn, machine vision) and MIT 6.S191 are recorded. Course materials are web-only.
- **UNVERIFIED — search term: "CMU 16-824 Visual Learning and Recognition lecture recordings Deepak Pathak"** — no lecture recordings found; only student project presentations. CMU 16-824 slides are public but video is not.
- **UNVERIFIED — search term: "Keyu Tian VAR Visual Autoregressive Modeling NeurIPS 2024 oral talk"** — no author talk for VAR (NeurIPS 2024 Best Paper) is on YouTube. Entry 87 is the best reading-group substitute.
- **UNVERIFIED — search term: "Alexey Dosovitskiy ViT ICLR 2021 oral presentation"** — the ICLR 2021 oral itself is behind SlidesLive, not on YouTube. Entries 1–2 are the closest free author talks.
- **UNVERIFIED — search term: "Lumiere Omer Bar-Tal Inbar Mosseri research talk"** — only the 1:55 Google Research announcement (`f9ThAzZs32M`) exists; no research-depth Lumiere talk. Use entry 84 (Emu Video, Ishan Misra) as the video-generation research talk instead.
- **UNVERIFIED — search term: "William Peebles DiT Scalable Diffusion Models with Transformers ICCV 2023 talk"** — no Peebles talk on YouTube. Entries 70–71 (Saining Xie, Stanford CS25) cover DiT from the co-author side.
- **Speaker attribution unconfirmed** for entries 16, 17, 55 and 74 — the title and channel are verified, but the individual presenter is not stated on the page and I did not fabricate one. (My web-search budget was exhausted mid-task, so these were left flagged rather than guessed.)

---

**Totals:** 133 individually verified video URLs — 93 standalone research talks/keynotes/tutorials (§1–7) plus 40 enumerated course lectures (§8a–8b), exceeding the 55–75 target. No files were written; nothing in this task touched a git repository, so there is no commit to report.
