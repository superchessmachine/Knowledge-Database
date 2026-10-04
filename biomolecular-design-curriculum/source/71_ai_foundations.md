# D.2 Foundations — The Courses Everything Else Assumes

> **Read the caveat before the list.** This section is deliberately organized by
> *course*, not by individual lecture, and that is a departure from the rest of
> this document. The reason is that these are the few places where watching the
> whole thing in order is actually correct — a course is a sequenced argument, and
> cherry-picking lecture 11 of CS236 will not teach you what lecture 11 of CS236
> teaches someone who watched the first ten.
>
> **Where the Atlas enumerates, this section sequences.** Appendix A.7 enumerates
> the IPD classical course lecture by lecture because you will dip into it.
> CS231n you should watch.
>
> **What to skip.** If you already train models daily, skip §1 entirely except
> Karpathy's *Let's reproduce GPT-2* and the NYU energy-based-model lectures. The
> sections that will actually add something are §2 (probabilistic ML — the
> weakest area for most people coming from structural biology), §3 (geometric
> deep learning, which is the theory behind every equivariant protein model you
> use), and §4 (diffusion and flow matching derived properly rather than
> assembled from blog posts).

---

## 1. Core deep learning courses with full recorded lectures

**MIT 6.S191: Introduction to Deep Learning (2026)** | Alexander Amini & Ava Amini, MIT | YouTube + course site | https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI and https://introtodeeplearning.com/ | 90 videos in the channel playlist across editions; the 2026 edition is 9 lectures of ~45–60 min, including "AI for Science" and "Secrets to Massively Parallel Training" | Fastest route to a working mental model of the whole stack, and the 2026 edition explicitly covers scientific applications and large-scale training.

**Stanford CS231n: Convolutional Neural Networks for Visual Recognition (Spring 2017)** | Fei-Fei Li, Justin Johnson, Serena Yeung | YouTube | https://www.youtube.com/playlist?list=PLC1qU-LWwrF64f4QKQT-Vg5Wr4qEE1Zxk | 16 lectures, ~1h15 each | Still the clearest derivation of backprop, conv architectures and training dynamics, which is the substrate every structure-prediction network sits on.

**Stanford CS231N: Deep Learning for Computer Vision (Spring 2025)** | Stanford Online | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16 | 18 lectures | The modernized version, with lectures on transformers, generative models and large-scale distributed training that the 2017 course predates.

**Stanford CS224N: NLP with Deep Learning (Spring 2024)** | Christopher Manning, Stanford | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D | 23 videos, ~1h20 each | Sequence modeling, attention and pretraining taught properly; protein language models are this machinery applied to a 20-letter alphabet. (2023 edition also live: https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4)

**Deep Learning Course (NYU, Spring 2020)** | Yann LeCun & Alfredo Canziani, NYU | YouTube | https://www.youtube.com/playlist?list=PL80I41oVxglKcAHllsU0txr3OuTTaWX2v | 32 videos | LeCun's energy-based-model framing of learning is unusually well-suited to thinking about protein conformational landscapes. Later editions with full notes: https://atcold.github.io/NYU-DLSP21/ and https://atcold.github.io/NYU-DLFL22/

**Practical Deep Learning for Coders (Part 1)** | Jeremy Howard, fast.ai | course.fast.ai | https://course.fast.ai/ | 9 lessons, ~90 min each | Top-down, code-first counterweight to the theory courses; gets you shipping experiments quickly.

**Practical Deep Learning for Coders Part 2: Deep Learning Foundations to Stable Diffusion** | Jeremy Howard, fast.ai | course.fast.ai | https://course.fast.ai/Lessons/part2.html | ~30 hours | Builds a diffusion model from scratch line by line, which is exactly the skill needed to modify RFdiffusion-class models rather than just call them.

**Neural Networks: Zero to Hero** | Andrej Karpathy | YouTube | https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ and https://karpathy.ai/zero-to-hero.html | 10 videos, 1–4 h each | Builds autograd and a transformer from nothing; the single best preparation for writing a novel architecture instead of fine-tuning someone else's.

**Let's build GPT: from scratch, in code, spelled out** | Andrej Karpathy | YouTube | https://www.youtube.com/watch?v=kCc8FmEb1nY | 1h56 | The attention mechanism derived in code, which demystifies every pair-representation and triangle-attention block in structure models.

**Let's reproduce GPT-2 (124M)** | Andrej Karpathy | YouTube | https://www.youtube.com/watch?v=l8pRSuU81PU | 4h01 | Covers the engineering of a real training run end to end: mixed precision, throughput, LR schedules, gradient accumulation.

**Deep Learning for Computer Vision (EECS 498-007 / 598-005)** | Justin Johnson, University of Michigan | YouTube | https://www.youtube.com/playlist?list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r | 22 lectures, ~1h15 each | Johnson's rewrite of CS231n with better coverage of 3D vision and generative models; the 3D lectures transfer directly to coordinate-based protein models.

**Neural networks (3Blue1Brown)** | Grant Sanderson | YouTube | https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi | 10 videos | Geometric intuition for backprop and attention; worth watching before the formal courses.

**DeepMind x UCL Deep Learning Lecture Series 2021** | DeepMind researchers / UCL | YouTube | https://www.youtube.com/playlist?list=PLqYmG7hTraZDVH599EItlEWsUOsJbAodm | 13 lectures | Research-level survey from people building the models, including generative modeling and attention lectures.

---

## 2. Probabilistic ML and Bayesian methods

**Probabilistic Machine Learning 2025** | Philipp Hennig, University of Tübingen | YouTube | https://www.youtube.com/playlist?list=PL05umP7R6ij0hPfU7Yuz8J9WXjlb3MFjm | 25 lectures, ~1h20 each | The most rigorous free treatment of Gaussian processes, inference and uncertainty; essential if you want calibrated confidence on designed sequences rather than bare point predictions. Earlier editions: 2023 https://www.youtube.com/playlist?list=PL05umP7R6ij2YE8rRJSb-olDNbntAQ_Bx and 2021 (29 lectures) https://www.youtube.com/playlist?list=PL05umP7R6ij1tHaOFY96m5uX3J21a6yNd

**Numerics of Machine Learning (Winter 2022/23)** | Philipp Hennig and colleagues, Tübingen | YouTube | https://www.youtube.com/playlist?list=PL05umP7R6ij2lwDdj7IkuHoP9vHlEcH0s | 14 lectures, ~1h20 each | Covers ODE/PDE solvers, Monte Carlo, Bayesian quadrature and uncertainty in deep learning — the numerical toolkit behind diffusion samplers and MD-coupled models.

**Stanford CS236: Deep Generative Models (2023)** | Stefano Ermon, Stanford | YouTube (Stanford Online) | https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8 | 18 lectures, ~1h20 each | The canonical unified treatment of autoregressive models, VAEs, normalizing flows, EBMs, GANs and score-based diffusion; this is the taxonomy you need to place any new protein generative model.

**Variational Inference: Foundations and Modern Methods (NIPS 2016 tutorial)** | David Blei, Rajesh Ranganath, Shakir Mohamed | YouTube | https://www.youtube.com/watch?v=ogdv_6dbvVQ | 1h53 | The reference tutorial for the ELBO, reparameterization and black-box VI, which underpins every latent-variable protein model.

**The Four Pillars of Machine Learning (Distinguished Colloquium)** | Kevin Murphy, Google DeepMind | YouTube (Princeton CS) | https://www.youtube.com/watch?v=uhcdw5rvqqE | 1h04 | Murphy's own unifying frame for his two-volume *Probabilistic Machine Learning* books; a fast map of the territory the books cover in 2,000 pages.

**Gaussian Process Summer School 2024** | Neil Lawrence and colleagues, GPSS | YouTube | https://www.youtube.com/playlist?list=PLZ_xn3EIbxZEoWLlm9y6OizFkontrhA6G | 8 lectures, ~1h30 each | Deep dive on GPs, deep GPs and multi-task GPs — the surrogate models that drive Bayesian optimization over sequence space.

**Math for Deep Learning (MaDL)** | Andreas Geiger, University of Tübingen | YouTube | https://www.youtube.com/playlist?list=PL05umP7R6ij0bo4UtMdzEJ6TiLOqj4ZCm | 18 lectures | Guided tour of the linear algebra and probability theory assumed by everything above; useful remediation if the Hennig lectures feel steep.

---

## 3. Geometric deep learning and equivariance

**AMMI Geometric Deep Learning Course, Second Edition (2022)** | Michael Bronstein (Oxford), Joan Bruna (NYU), Taco Cohen (Qualcomm), Petar Veličković (DeepMind) | YouTube | https://www.youtube.com/playlist?list=PLn2-dEmQeTfSLXW8yXP4q_Ii58wFdxb3C | 18 videos (12 lectures + tutorials + seminars), ~1h15 each | The "Erlangen programme" framing of grids, groups, graphs, geodesics and gauges is the single most useful theoretical lens for inventing new protein and RNA architectures.

**AMMI Geometric Deep Learning Course, First Edition (2021)** | same four instructors | YouTube | https://www.youtube.com/playlist?list=PLn2-dEmQeTfQ8YVuHBOvAhUlnIPYxkeu3 | 13 lectures | Different emphasis and pacing from the 2022 edition; Cohen's geometric-priors lectures are especially good here. Course hub with slides: https://geometricdeeplearning.com/lectures/

**Group Equivariant Deep Learning (UvA, 2022)** | Erik Bekkers, University of Amsterdam | YouTube | https://www.youtube.com/playlist?list=PL8FnQMH2k7jzPrxqdYufoiYVHim8PyZWd | 21 videos, 10–50 min each | The most constructive course on building G-CNNs and steerable/3D-equivariant networks, including 3D steerable graph NNs — this is the mathematics behind e3nn, NequIP and SE(3)-Transformers.

**An Orientation in Symmetry-Aware ML Methods** | Tess Smidt, MIT (Materials Project Seminars) | YouTube | https://www.youtube.com/watch?v=R3N6BocbknM | 1h01 | Smidt's own taxonomy of how to choose among invariant, equivariant and data-augmented approaches; directly applicable to deciding what symmetry your protein model should enforce.

**Applications of Euclidean neural networks to understand and design atomistic systems** | Tess Smidt, MIT (Harvard CMSA) | YouTube | https://www.youtube.com/watch?v=Iah-YIFdmbs | 55 min | Current state of e3nn-based design on real atomistic systems, including symmetry breaking.

**Symmetry-Aware Neural Networks for the Material Sciences with e3nn (MRS 2021 Fall tutorial)** | Tess Smidt, Mario Geiger and others | YouTube | https://www.youtube.com/watch?v=q9EwZsHY1sk | 6-part tutorial, ~45 min for part 1 | Hands-on introduction to the e3nn library itself. Companion material: https://blondegeek.github.io/e3nn_tutorial/ and https://e3nn.org/

**Symmetries in Inference and Learning** | Max Welling, University of Amsterdam (TUM AI Lecture Series) | YouTube | https://www.youtube.com/watch?v=YihnfamwA_s | 57 min | Welling's argument for why equivariance buys data efficiency — the core justification for using it in low-data protein regimes.

**Equivariant Networks (NeurIPS 2020 tutorial)** | Taco Cohen & Risi Kondor | neurips.cc | https://neurips.cc/virtual/2020/tutorial/16650 | ~2h | Cohen and Kondor's joint treatment of equivariant convolutions and their representation theory, from the two people who formalized the field.

**Stanford CS224W: Machine Learning with Graphs** | Jure Leskovec, Stanford | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn | 60 videos, ~1h each | Proteins and RNA are graphs before they are coordinates; this is the most complete free GNN course. Site: https://cs224w.stanford.edu/

---

## 4. Diffusion models and flow matching

**MIT 6.S184: Generative AI with Stochastic Differential Equations / Flow Matching and Diffusion Models (2025)** | Peter Holderrieth & Ezra Erives, MIT CSAIL | YouTube + course site | https://www.youtube.com/playlist?list=PL57nT7tSGAAUDnli1LhTOoCxlEPGS19vH and https://diffusion.csail.mit.edu/ | 6 lectures plus full lecture notes and 3 labs | Derives diffusion and flow matching from the SDE/ODE perspective and ends on molecular design applications — the most direct bridge from theory to protein generative models.

**Flow Matching for Generative Modeling (NeurIPS 2024 tutorial)** | Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu (Meta FAIR) | neurips.cc / SlidesLive | https://neurips.cc/virtual/2024/tutorial/99531 and https://slideslive.com/39031675/flow-matching-for-generative-modeling | ~2h | Includes the non-Euclidean (Riemannian) and discrete generalizations that matter for backbone frames and sequences. Companion library and docs: https://facebookresearch.github.io/flow_matching/

**Denoising Diffusion-based Generative Modeling: Foundations and Applications (CVPR 2022 tutorial)** | Arash Vahdat, Karsten Kreis, Ruiqi Gao (NVIDIA / Google) | YouTube | https://www.youtube.com/watch?v=cS6JQpEY9cs | 3h46 | The most thorough single-sitting derivation of DDPM, score matching and the SDE/ODE unification.

**Denoising Diffusion Models: A Generative Learning Big Bang (CVPR 2023 tutorial)** | Jiaming Song, Chenlin Meng, Arash Vahdat | YouTube (CVF) | https://www.youtube.com/watch?v=1d4r19GEVos | 3h04 | The follow-up, covering fast samplers, guidance and conditioning — the levers you pull when conditioning a backbone generator on a binding site.

**Diffusion and Score-Based Generative Models** | Yang Song, Stanford (MIT CBMM) | YouTube | https://www.youtube.com/watch?v=wMmqCMwuM2Q | 1h32 | Song presenting his own score-SDE framework, explicitly motivated by molecular structure generation.

**A personal journey to diffusion models (ICBS 2025)** | Yang Song | YouTube (BIMSA) | https://www.youtube.com/watch?v=s647Nz0r4r0 | 1h03 | How the ideas actually developed, including dead ends — unusually instructive if your goal is to invent methods rather than apply them.

**Diffusion models for image and video generation (ML in PL 2025)** | Sander Dieleman, Google DeepMind | YouTube | https://www.youtube.com/watch?v=qFIT3mSwWEk | 51 min | Practitioner's view of latent diffusion: autoencoders, noise schedules, guidance, distillation — the design decisions papers usually omit.

**Hugging Face Diffusion Models Course** | Hugging Face | huggingface.co | https://huggingface.co/learn/diffusion-course/en/unit0/1 | 4 units, theory plus 2 notebooks each | Hands-on `diffusers` training, fine-tuning, guidance and custom pipelines; the fastest path from theory to a model you have actually trained.

**Stanford CME296: Diffusion & Large Vision Models** | Stanford Online | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu | 8 lectures | Recent course covering diffusion foundations, score matching and flow matching together in one modern syllabus.

---

## 5. Transformers and attention in depth

**Stanford CS25: Transformers United (V1–V6)** | Stanford, rotating guest researchers | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM and https://web.stanford.edu/class/cs25/ | 50 videos, ~1h15 each | Seminar series with the authors of the architectures themselves, including sessions on biology applications; the best single feed for what is actually new.

**Stanford CS25 V6: Overview of Transformers** | Stanford Online | YouTube | https://www.youtube.com/watch?v=bHSDPgZYie0 | 1h16 | The 2026 refresher lecture; the right single video if you want current framing rather than the 2017 one.

**Stanford CME295: Transformers and Large Language Models (Autumn 2025)** | Afshine & Shervine Amidi, Stanford | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rOCXd21gf0CF4xr35yINeOy | 9 lectures, ~1h40 each | A structured course rather than a seminar: attention internals, tokenization, positional encodings, efficiency.

**Structured State Space Models for Deep Sequence Modeling** | Albert Gu, CMU (LxMLS) | YouTube | https://www.youtube.com/watch?v=WC9tqkCpq4s | 1h34 | Gu's full derivation of S4/Mamba from first principles — relevant because long-sequence linear-time models are an open frontier for whole-genome and long-RNA modeling.

**On the Tradeoffs of State Space Models** | Albert Gu, CMU (Simons Institute) | YouTube | https://www.youtube.com/watch?v=ksRp_DIHWj4 | 49 min | The honest comparison of where SSMs beat attention and where they do not.

**Stanford CS25 V6: On the Tradeoffs of State Space Models and Transformers** | Stanford Online | YouTube | https://www.youtube.com/watch?v=OyimE74UMF8 | 1h17 | The seminar-length version of the same argument, more recent.

---

## 6. Reinforcement learning and optimization for design

**DeepMind x UCL: Introduction to Reinforcement Learning (2015)** | David Silver, DeepMind / UCL | YouTube | https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ | 10 lectures, ~1h30 each | Still the clearest exposition of MDPs, value functions and policy gradients; the vocabulary for any RL-driven sequence design loop.

**DeepMind x UCL RL Lecture Series (2021)** | Hado van Hasselt, Diana Borsa, Matteo Hessel, DeepMind | YouTube | https://www.youtube.com/watch?v=TCCjZe0y4Qc | 13 lectures, ~1h30–2h each | The modern replacement for the 2015 course, with deep RL and function approximation treated properly.

**CS 185/285: Deep Reinforcement Learning (Spring 2026)** | Sergey Levine, UC Berkeley | YouTube | https://www.youtube.com/playlist?list=PLKq1TCpsv3Y4 and https://rail.eecs.berkeley.edu/deeprlcourse/ | 27 videos, ~1h00–1h56 each | The graduate standard, including offline RL and model-based RL — directly relevant to learning design policies from fixed experimental datasets.

**Stanford CS224R: Deep Reinforcement Learning** | Chelsea Finn, Stanford | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL | 19 lectures | Strong complement to CS285 with more meta-learning and few-shot adaptation, which maps onto low-data protein design.

**INFORMS TutORial: Bayesian Optimization** | Peter Frazier, Cornell | YouTube | https://www.youtube.com/watch?v=c4KKvyWW_Xk | 1h27 | GP regression plus expected improvement, entropy search and knowledge gradient — the exact machinery behind active-learning loops that pick which variants to assay next. Written companion: arXiv:1807.02811.

(See also Gaussian Process Summer School 2024 under section 2, which supplies the surrogate-model theory this tutorial assumes.)

---

## 7. ML systems practicalities

**Stanford CS336: Language Modeling from Scratch (Spring 2025)** | Percy Liang & Tatsunori Hashimoto, Stanford | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_ and https://stanford-cs336.github.io/spring2025/ | 17 lectures, ~22 hours total | Includes GPU programming, Triton kernels, and data/tensor/pipeline parallelism; the best free course on actually scaling a model you wrote yourself.

**Stanford CS336 (Spring 2026)** | same instructors | YouTube | https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV | 18 lectures | The updated edition.

**MIT 6.5940: TinyML and Efficient Deep Learning Computing (EfficientML.ai, Fall 2023)** | Song Han, MIT | YouTube | https://www.youtube.com/playlist?list=PL80kAHvQbh-pT4lCkDT53zT8DKmhE0idB and https://efficientml.ai/ | 46 videos, ~1h10 each | Pruning, quantization, NAS, distributed training and on-device training; how to make a large structure model fit and run on the hardware you actually have. Fall 2026 edition in progress: https://www.youtube.com/playlist?list=PLH7PIPKvCm38

**Stanford MLSys Seminars** | Stanford, rotating industry and academic speakers | YouTube | https://www.youtube.com/playlist?list=PLSrTvUm384I9PV10koj_cqit9OfbJXEkq | 100 episodes, ~1h each | Covers automated model parallelism (Alpa), distributed ML, deployment and monitoring — the practical counterpart to the research courses.

**Stanford CS231N Spring 2025, Lecture 11: Large Scale Distributed Training** | Stanford Online | YouTube | https://www.youtube.com/watch?v=9MvD-XsowsE | 1h12 | A single self-contained lecture on data/model/pipeline parallelism if you do not want the full CS336 commitment.

**Intro to JAX: Accelerating Machine Learning research** | Google / DeepMind | YouTube | https://www.youtube.com/watch?v=WdTeDXsOSj4 | 10 min | `jit`, `grad`, `vmap`, `pmap` in one sitting; AlphaFold, Boltz-adjacent and many equivariant codebases are JAX-native.

**Keynote: PyTorch Technical Deep Dive** | Alban Desmaison, Peng Wu, Mark Saroufim, Edward Yang (Meta), PyTorch Conference | YouTube | https://www.youtube.com/watch?v=XdORM2pkyH8 | 43 min | Current internals from the core developers: compile stack, autograd, distributed — what you need when your custom equivariant op is slow.

---

## Flagged as unverifiable

**UNVERIFIED — search term: "Stanford CS329S Machine Learning Systems Design lecture videos public"** — The course site (https://stanford-cs329s.github.io/) is live and all slides and lecture notes are public, but recordings were released only on Canvas to enrolled students, and no public video set exists. Only scattered guest-lecture clips and the 2022 Demo Day are on YouTube. The content was expanded into Chip Huyen's book *Designing Machine Learning Systems* (O'Reilly, 2022). Use the Stanford MLSys Seminars playlist above as the video substitute.

Two notes on what I could not do. My web-search budget ran out partway through, so the second half of the discovery work was done by fetching YouTube's search and channel pages and course websites directly with curl, which is actually stricter verification than search snippets since every URL above returned HTTP 200 with the title and video count I have quoted. And I deliberately dropped several third-party re-uploads of CS236 and David Silver that ranked highly in search, in favor of the official Stanford Online and Google DeepMind playlists, because re-uploads get taken down.
