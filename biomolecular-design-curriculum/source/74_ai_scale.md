# D.5 Training at Scale, Scaling Laws and Data

> **Why this is in a biology curriculum.** Three reasons, and they are all
> practical.
>
> First, **every compute decision you make is a scaling-law question** whether
> you frame it that way or not: how long to train, how big a model, how much
> data to collect. The language field has an explicit, quantitative theory of
> this. Yours does not, and importing it is a contribution.
>
> Second, **the numerics and memory tricks are directly reusable.** FlashAttention
> is in AlphaFold forks. Hydrogen mass repartitioning and mixed precision are the
> same kind of idea in different clothes.
>
> Third, **the data chapter is the one that transfers most cleanly.** Deduplication,
> contamination, and the measurement of what a training set actually contains are
> solved problems in language and unsolved problems in biology.

---

## D.5.1 FlashAttention and IO-aware algorithms

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **FlashAttention** | Tri Dao (Stanford MLSys #67) | 2023 | 58:58 | [▶](https://www.youtube.com/watch?v=gMOAud7hZg4) |
| **Hardware-aware Algorithms for Language Modeling** | Tri Dao (ETH SPCL) | 2024 | 1:05:15 | [▶](https://www.youtube.com/watch?v=SyB-GVnCX9Q) |
| Optimizing attention for modern hardware | Tri Dao (Princeton/Together) | 2025 | 35:45 | [▶](https://www.youtube.com/watch?v=cPwt1Y10gjI) |
| GPU MODE Lecture 12: Flash Attention | GPU MODE | 2024 | 1:12:14 | [▶](https://www.youtube.com/watch?v=zEuwuCTEf_0) |
| **GPU MODE Lecture 36: CUTLASS and Flash Attention 3** | Jay Shah (FA-3 co-author) | 2024 | 1:49:15 | [▶](https://www.youtube.com/watch?v=JwUcZwPOCpA) |
| GPU MODE Lecture 80: How FlashAttention 4 Works | Charles Frye | 2025 | 1:15:09 | [▶](https://www.youtube.com/watch?v=VPslgC9piIw) |
| FlashAttention-4 | Ted Zadouri (GPU MODE) | 2026 | 46:23 | [▶](https://www.youtube.com/watch?v=kPKKvBqQoFI) |
| ML Perf Reading Group 2: Flash Attention | EleutherAI | 2024 | 1:14:21 | [▶](https://www.youtube.com/watch?v=Lys0TpsLIEc) |
| ML Perf Reading Group 24: Flash Attention 4 | EleutherAI | 2026 | 1:05:20 | [▶](https://www.youtube.com/watch?v=W49k837lm_g) |
| ThunderKittens goes live | Stanford MLSys / Hazy Research | 2024 | 1:14:55 | [▶](https://www.youtube.com/watch?v=IAwLzkldxUk) |
| **Notes on AI Hardware** | Benjamin Spector (Stanford MLSys #88) | 2024 | 1:16:48 | [▶](https://www.youtube.com/watch?v=PlraH57ey4k) |

**Papers:** **Dao et al. 2022, NeurIPS, arXiv:2205.14135 (FlashAttention)** ·
Dao 2023, arXiv:2307.08691 (FA-2) · Shah et al. 2024, arXiv:2407.08608 (FA-3) ·
Rabe & Staats 2021 (self-attention does not need O(n²) memory) ·
Milakov & Gimelshein 2018 (online softmax).

> **Start with Spector's *Notes on AI Hardware* if you have never thought about
> arithmetic intensity.** Without it, the whole IO-aware argument is invisible —
> FlashAttention computes exactly the same function as standard attention and is
> faster entirely because of where the data sits. **That is the template for the
> most portable idea in this entire Part: performance is often about memory
> movement, not operations.**
>
> **It already transferred.** Fast AlphaFold implementations use FlashAttention
> in the Evoformer. The triangle operations do not yet have an equivalent
> treatment, and writing one is a concrete, high-value project — it is what makes
> large-complex prediction feasible on consumer hardware.

---

## D.5.2 Parallelism and distributed training

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Training LLMs at Scale** | Deepak Narayanan (Stanford MLSys #83) | 2023 | 55:59 | [▶](https://www.youtube.com/watch?v=JA1l96tjrs4) |
| Efficient Large-Scale Training with Megatron-LM | Jared Casper (NVIDIA) | 2023 | 24:03 | [▶](https://www.youtube.com/watch?v=gHaNUcS1_O4) |
| **GPU MODE Lecture 48: The Ultra Scale Playbook** | Nouamane Tazi (Hugging Face) | 2025 | **3:03:48** | [▶](https://www.youtube.com/watch?v=1E8GDR8QXKw) |
| **CS25 V6 — The Ultra-Scale Talk** | Nouamane Tazi (HF) | 2026 | 1:01:48 | [▶](https://www.youtube.com/watch?v=I5BKi32IEa8) |
| The Ultra-Scale Playbook | Thom Wolf (HF) | 2025 | 1:25:56 | [▶](https://www.youtube.com/watch?v=og8Y6z2xC0I) |
| ML Perf RG 8: Megatron-LM | EleutherAI | 2025 | 1:09:20 | [▶](https://www.youtube.com/watch?v=ImKyR1tsPPE) |
| ML Perf RG 6: Zero Bubble Pipeline Parallelism | EleutherAI | 2025 | 1:17:13 | [▶](https://www.youtube.com/watch?v=4wTuGkiob7o) |
| ML Perf RG 11: Async Tensor Parallelism | EleutherAI | 2025 | 1:07:38 | [▶](https://www.youtube.com/watch?v=Ow1FLKFcSPs) |
| ML Perf RG 13: Unified Sequence Parallelism | EleutherAI | 2025 | 1:18:41 | [▶](https://www.youtube.com/watch?v=tQzZ7oDKi6Y) |
| ML Perf RG 9: Reducing Activation Recomputation | EleutherAI | 2025 | 1:15:01 | [▶](https://www.youtube.com/watch?v=9o2TXexHUh8) |
| ML Perf RG 1: GPU Architecture, CUDA, NCCL | EleutherAI | 2024 | 47:39 | [▶](https://www.youtube.com/watch?v=Cp7g1Ll4v0M) |
| Alpa: Automated Model-Parallel Deep Learning | Zhuohan Li (Stanford MLSys #59) | 2022 | 55:07 | [▶](https://www.youtube.com/watch?v=y1NXHjcl6V0) |
| ML Perf RG 3: ZeRO | EleutherAI | 2024 | 1:08:16 | [▶](https://www.youtube.com/watch?v=azUufxKe5RE) |
| Large Model Training with DeepSpeed | Samyam Rajbhandari (ZeRO author) | 2023 | 36:23 | [▶](https://www.youtube.com/watch?v=cntxC3g22oU) |
| Trillion Parameter Training and Inference with DeepSpeed | Rajbhandari & Rasley (REFAI) | 2023 | 1:06:52 | [▶](https://www.youtube.com/watch?v=smDC_mOGQ5U) |

**Papers:** **Narayanan et al. 2021, SC'21, arXiv:2104.04473 (Megatron-LM)** ·
**Rajbhandari et al. 2020, SC'20, arXiv:1910.02054 (ZeRO)** · Zhao et al. 2023
(PyTorch FSDP) · Zheng et al. 2022, OSDI (Alpa).

> **Tazi's three-hour Ultra Scale Playbook is the most complete free resource on
> distributed training that exists**, and the 2026 CS25 condensation is the right
> entry point. Watch the short one, then use the long one as reference.
>
> **The honest assessment for your situation.** You have a handful of machines
> with 1–8 GPUs each. Tensor and pipeline parallelism are not your problem;
> **data parallelism, activation checkpointing and memory are.** Watch the ZeRO
> material and the activation-recomputation session, skip the thousand-GPU
> material unless you want it for its own sake. The yash RAM ceiling you already
> hit is exactly the constraint ZeRO is designed around.

---

## D.5.3 Numerics, precision and optimizers

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| FP8 Training From Hopper To Blackwell | Luca Wehrstedt (Meta, PyTorch Conf) | 2026 | 25:24 | [▶](https://www.youtube.com/watch?v=SBO2PmUKfUA) |
| **GPU MODE Lecture 52: Scaling Laws for Low Precision** | Tanishq Kumar (author) | 2025 | 53:42 | [▶](https://www.youtube.com/watch?v=YCfzf0TunOM) |
| Trinity: Training a 400B MoE from Scratch | Arcee | 2026 | 32:59 | [▶](https://www.youtube.com/watch?v=_GXUlM5DCL4) |
| **Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer** | **Greg Yang** (MSR) | 2022 | 1:12:52 | [▶](https://www.youtube.com/watch?v=XpU3mDKJOak) |
| Tuning GPT-3 on a Single GPU via Zero-Shot HP Transfer | Greg Yang | 2022 | 1:33:53 | [▶](https://www.youtube.com/watch?v=Hcpjgj2BD_I) |
| EI Seminar (the tight version) | Greg Yang | 2022 | 53:52 | [▶](https://www.youtube.com/watch?v=xbCibcC9Ud0) |
| Large N Limits: Random Matrices & Neural Networks | Greg Yang (Cartesian Cafe) | 2023 | 3:01:28 | [▶](https://www.youtube.com/watch?v=1aXOXHA7Jcw) |
| **Metrized Deep Learning** | **Jeremy Bernstein** (MIT, Cohere) | 2024 | 1:34:03 | [▶](https://www.youtube.com/watch?v=td9r0D3VARk) |
| Depths of First Order Optimization | Jeremy Bernstein (Cohere) | 2025 | 47:31 | [▶](https://www.youtube.com/watch?v=4OAiakkmKQs) |
| Scalable second order optimization for deep learning | Rohan Anil (JAX meetup) | 2022 | 1:28:15 | [▶](https://www.youtube.com/watch?v=YDL8NXlS8hA) |
| From the Broximal Point Method to Efficient LLM Training | Peter Richtárik (KAUST, Simons) | 2026 | 52:25 | [▶](https://www.youtube.com/watch?v=Va7ER6bRodA) |
| Muon and Kimi K-2 | Latent Space paper club | 2025 | 1:03:06 | [▶](https://www.youtube.com/watch?v=fcTNQLebHb0) |

**Papers:** **Yang et al. 2022, arXiv:2203.03466 (Tensor Programs V, μP)** ·
**Bernstein et al. 2024, arXiv:2405.14813 (modular norm)** · Bernstein & Newhouse
2024, arXiv:2409.20325 (*Old Optimizer, New Norm*) · Jordan et al. 2024 (Muon) ·
Liu et al. 2025, arXiv:2502.16982 (Muon is scalable) · Gupta et al. 2018
(Shampoo) · Kumar et al. 2024, arXiv:2411.04330 (scaling laws for precision).

> **μP is the single most directly importable idea in this entire Part.** Tune
> hyperparameters on a small model, transfer them zero-shot to a large one. Every
> structure-prediction group retunes at every scale, by hand, at enormous cost.
> **Nobody has published a μP analysis of an Evoformer or a triangle-attention
> stack.** The parameterization is nontrivial because of the pair representation —
> which is exactly why it would be a real contribution rather than an application.
>
> **Bernstein's *Metrized Deep Learning* is the intellectual foundation of Muon**
> and the deepest talk in this subsection. Steepest descent is only defined
> relative to a norm; choosing the norm *is* choosing the optimizer. Once you
> see that, the optimizer zoo organizes itself.

---

## D.5.4 Scaling laws

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **Scaling Laws and Their Implications** | **Jared Kaplan** (JHU/Anthropic, Harvard CMSA) | 2022 | 1:10:40 | [▶](https://www.youtube.com/watch?v=Suhp3OLASSo) |
| Neural Scaling Laws and GPT-3 | Jared Kaplan | 2020 | 1:15:20 | [▶](https://www.youtube.com/watch?v=sNfkZFVm_xs) |
| Neural Scaling Laws and GPT-3 (Physics Meets ML) | Jared Kaplan | 2020 | 1:35:49 | [▶](https://www.youtube.com/watch?v=QMqPAM_knrE) |
| **Understanding the Origins and Taxonomy of Neural Scaling Laws** | Yasaman Bahri (Simons) | 2023 | 1:05:24 | [▶](https://www.youtube.com/watch?v=MUvFuZpxLU8) |
| Dynamics and scaling laws in deep learning | Yasaman Bahri (Yale YINS) | 2021 | 1:07:08 | [▶](https://www.youtube.com/watch?v=WbHfM774bKc) |
| The Large Learning Rate Phase of Deep Learning | Yasaman Bahri | 2020 | 36:06 | [▶](https://www.youtube.com/watch?v=gBFmS8qyuFQ) |
| **(Mis)Fitting: A Survey of Scaling Laws** | Sneha Kudugunta (Cohere Labs) | 2026 | 54:55 | [▶](https://www.youtube.com/watch?v=ggz4iaQpzcY) |
| CS224N Guest Lecture: Scaling Language Models | Stanford | 2022 | 1:14:49 | [▶](https://www.youtube.com/watch?v=UFem7xa3Q2Q) |
| Predicting and optimizing the behavior of large ML models | Simons Institute | 2025 | 1:04:05 | [▶](https://www.youtube.com/watch?v=iePMkTFuEW8) |
| **CS336 2026 Lecture 9: Scaling Laws** | Stanford | 2026 | 1:17:57 | [▶](https://www.youtube.com/watch?v=Q15rhEWZPQ4) |
| **CS336 2026 Lecture 11: Scaling Laws** | Stanford | 2026 | 1:17:04 | [▶](https://www.youtube.com/watch?v=vTfEyOyzV9E) |

**Papers:** **Kaplan et al. 2020, arXiv:2001.08361** · **Hoffmann et al. 2022,
NeurIPS (Chinchilla)** · Bahri et al. 2021, arXiv:2102.06701 (explaining neural
scaling laws) · McCandlish et al. 2018, arXiv:1812.06162 (critical batch size) ·
Lewkowycz et al. 2020, arXiv:2003.02218 (the catapult phase).

> **Kudugunta's *(Mis)Fitting* is the most methodologically useful talk here**
> and the one to assign if you only assign one. It is a survey of how scaling
> laws get fit *badly* — wrong functional forms, too few points, extrapolating
> past the fitted range — which is precisely the error you would make on your
> first attempt.
>
> **The structural fact about biology that this reveals.** Language has effectively
> unlimited data and a clean loss; biology has a fixed PDB and a loss that is a
> proxy for a wet-lab outcome. **A scaling law for protein models is therefore a
> different object, and nobody has written down what it should look like.** That
> is Capstone X territory: "if we could measure 10× more structures, how much
> would prediction improve, and what is the functional form?" The answer is worth
> knowing before anyone spends the money.

---

## D.5.5 Data — the chapter that transfers most cleanly

| Talk | Speaker | Year | Len | Link |
|---|---|---|---|---|
| **DataComp-LM: In Search of the Next Generation of Training Sets** | Ludwig Schmidt (Stanford) | 2025 | 48:31 | [▶](https://www.youtube.com/watch?v=IsNqSmTPiWQ) |
| A data-centric view on reliable generalization | Ludwig Schmidt (MLSys #71) | 2023 | 58:41 | [▶](https://www.youtube.com/watch?v=brHeIKX8ayw) |
| **Creating a large dataset for pretraining LLMs (FineWeb)** | Guilherme Penedo (HF) | 2025 | 24:05 | [▶](https://www.youtube.com/watch?v=dRT5Vf9_OYw) |
| Why Data Holds the Key to AI Reasoning Breakthroughs | Penedo (GOSIM) | 2025 | 23:40 | [▶](https://www.youtube.com/watch?v=5mCjNAQPSLw) |
| **Better Data is All You Need** | Ari Morcos (Datology, Latent Space) | 2025 | 1:18:43 | [▶](https://www.youtube.com/watch?v=yXPPcBlcF8U) |
| **Poisoning Web-Scale Training Datasets** | Nicholas Carlini (MLSys #75) | 2023 | 58:06 | [▶](https://www.youtube.com/watch?v=h9jf1ikcGyk) |
| OLMo leads on the secrets of training language models | Groeneveld, Lo, Soldaini (AI2) | 2025 | 1:12:43 | [▶](https://www.youtube.com/watch?v=dS7QI99uJVc) |
| Open Model Pretraining Masterclass | Elie Bakouch (HF, Latent Space) | 2025 | 1:03:39 | [▶](https://www.youtube.com/watch?v=wH8YKCE82Qo) |
| **Data-distributional Approaches for Generalizable LMs (DoReMi, DSIR)** | Sang Michael Xie (Stanford) | 2024 | 1:10:57 | [▶](https://www.youtube.com/watch?v=DnhnjegbcJI) |
| Scaling Data-Constrained Language Models | Sasha Rush (Simons) | 2023 | 1:03:59 | [▶](https://www.youtube.com/watch?v=Kp5R6GZh8O0) |
| Scaling Data-Constrained Language Models | Niklas Muennighoff (author) | 2023 | 1:04:05 | [▶](https://www.youtube.com/watch?v=TK0-sitkCMw) |
| **Open Pretrained Transformers (the OPT-175B logbook)** | Susan Zhang (MLSys #77) | 2023 | 1:00:05 | [▶](https://www.youtube.com/watch?v=p9IxoSkvZ-M) |
| CS25 V4 — Behind the Scenes of LLM Pre-training: StarCoder | Loubna Ben Allal (HF) | 2024 | 1:01:36 | [▶](https://www.youtube.com/watch?v=jm2hyJLFfN8) |
| **CS336 2026 Lecture 13: Data (Sources, Datasets)** | Stanford | 2026 | 1:22:02 | [▶](https://www.youtube.com/watch?v=-qm0ln33G24) |
| **CS336 2026 Lecture 14: Data** | Stanford | 2026 | 1:24:46 | [▶](https://www.youtube.com/watch?v=5sxHosTLPF8) |

**Papers:** Li et al. 2024, arXiv:2406.11794 (DataComp-LM) · Penedo et al. 2024,
arXiv:2406.17557 (FineWeb) · **Lee et al. 2022, ACL (deduplicating training data
makes LMs better)** · Sorscher et al. 2022, arXiv:2206.14486 (beating power-law
scaling via data pruning) · Xie et al. 2023, arXiv:2305.10429 (DoReMi) ·
Muennighoff et al. 2023, arXiv:2305.16264 (data-constrained scaling) ·
Carlini et al. 2023, arXiv:2302.10149.

> **Susan Zhang's OPT-175B logbook talk is the most honest hour about what large
> training runs are actually like**, and the closest analogue in this curriculum
> is Gabe Rocklin's *Why designs fail*. Both are someone describing, in public,
> what the paper left out. **Watch them in the same week.** The parallel is the
> point: two cultures, two kinds of hidden failure, one shared norm worth
> adopting.
>
> **The transferable technique.** Deduplication, contamination detection and
> data-mixture reweighting are mature in language and essentially absent in
> protein modeling. The analogues are obvious — sequence-identity deduplication
> exists, but *structure*-level deduplication, contamination between training and
> CASP targets, and principled mixture weights over Pfam families mostly do not.
> **DoReMi applied to protein family mixtures is an afternoon's reimplementation
> and a real result.**

---

## D.5.6 Paired reading — D.5

| Watch this | Then read this | Hold this question |
|---|---|---|
| Spector, *Notes on AI Hardware* | Any roofline-model tutorial | Compute the arithmetic intensity of triangle multiplication. |
| **Dao, *FlashAttention*** | **arXiv:2205.14135** | Same function, 3× faster. Where did the time go? |
| Shah, *CUTLASS and FA-3* | arXiv:2407.08608 | What does implementing the idea actually cost? |
| Tazi, *Ultra-Scale* (CS25 version) | The Ultra-Scale Playbook (HF) | Which parallelism applies to a 4-GPU node? Which does not? |
| Rajbhandari, *DeepSpeed* | **arXiv:1910.02054 (ZeRO)** | Partition states, not compute. What does each stage buy? |
| **Yang, *Zero-Shot HP Transfer*** | **arXiv:2203.03466** | What is μP's parameterization, and what would it be for pair representations? |
| **Bernstein, *Metrized Deep Learning*** | arXiv:2405.14813; arXiv:2409.20325 | Choosing the norm is choosing the optimizer. Which norm fits your problem? |
| Kaplan, *Scaling Laws* | **arXiv:2001.08361** then **Hoffmann et al. 2022** | Why was Kaplan's compute-optimal ratio wrong, and what was the fix? |
| Bahri, *Origins of scaling laws* | arXiv:2102.06701 | Four regimes. Which one is a protein model in? |
| **Kudugunta, *(Mis)Fitting*** | The survey | List five ways to fit a scaling law badly. Check your own plan against them. |
| Penedo, *FineWeb* | arXiv:2406.17557 | Every filter is an ablation. What is the protein equivalent of a filter? |
| Morcos, *Better Data* | **Sorscher et al. 2022, arXiv:2206.14486** | Pruning can beat power-law scaling. What would you prune from the PDB? |
| Xie, *DoReMi and DSIR* | arXiv:2305.10429 | Reimplement DoReMi over Pfam families. What mixture does it find? |
| **Zhang, *OPT-175B logbook*** | Then re-watch **Rocklin, *Why designs fail*** | Two cultures, two hidden-failure literatures. What norm should both adopt? |
| Carlini, *Poisoning training data* | arXiv:2302.10149 | Could the PDB be poisoned? What would it look like? |
