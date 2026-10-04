# E.7 Systems Engineering for Biomolecular Machine Learning

> **This is the thinnest recorded literature in the entire curriculum, and that
> is the finding.** The molecular dynamics community has a decade of public
> performance culture — BioExcel webinar #2 in 2016 through #93 in 2026, almost
> all of it about making simulations faster. **The structure-prediction community
> has essentially none.** The most-run model in computational biology has no
> public profile.
>
> Read this section as a map of where the work has not been done.

---

## E.7.1 AlphaFold, OpenFold and what training actually costs

| Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|
| **OpenFold: Lessons Learned and Insights Gained From Rebuilding and Retraining AlphaFold2** | **Mohammed AlQuraishi** (Columbia) | 2023 | 39:28 | [▶](https://www.youtube.com/watch?v=KvCvdFQ4Mrk) |
| OpenFold: retraining AlphaFold2 yields insights on learning mechanisms | OpenFold team (OpenBioML) | 2023 | 1:03:54 | [▶](https://www.youtube.com/watch?v=W92xVnUMkU0) |
| OpenFold (IPAM version) | AlQuraishi (UCLA/IPAM) | 2023 | 48:12 | [▶](https://www.youtube.com/watch?v=1Y9n7g6xX4Q) |
| OpenFold Keynote | AlQuraishi (OMSF Symposium) | 2024 | 40:40 | [▶](https://www.youtube.com/watch?v=ZJSnfaBJC3Q) |
| **Insights from retraining OpenFold** | **Nazim Bouatta** (Harvard Medical School) | 2023 | 1:16:29 | [▶](https://www.youtube.com/watch?v=sNkZjgy6QfE) |
| **FastFold: Reducing AlphaFold Training Time from 11 Days to 67 Hours** | Shenggan Cheng (NUS, first author) | 2023 | 9:56 | [▶](https://www.youtube.com/watch?v=rkolMB4z6xQ) |
| **Lessons from implementing AlphaFold3 in the wild** | Arda Goreci (Ligo Biosciences) | 2024 | 25:51 | [▶](https://www.youtube.com/watch?v=97K0_b65oto) |
| Boltz-1 and the Future of Biomolecular Foundation Models | Corso & Wohlwend (MIT) | 2025 | 1:09:45 | [▶](https://www.youtube.com/watch?v=K-gzTJMy1ag) |
| Boltz-2: Accurate and Efficient Binding Affinity Prediction | Wohlwend et al. (MIT/Recursion) | 2025 | 59:26 | [▶](https://www.youtube.com/watch?v=iHDauMATkr0) |
| **SeedFold: Scaling Biomolecular Structure Prediction** | Zhou & Lu (ByteDance Seed) | 2026 | 59:59 | [▶](https://www.youtube.com/watch?v=qyxftQJdE3I) |
| Accelerating Biomolecular Modeling with AtomWorks and RF3 | Nathaniel Corley (IPD) | 2025 | 52:10 | [▶](https://www.youtube.com/watch?v=Jyv7a1LhBwE) |
| **Model. Package. Deploy. Repeat: DevOps for Biomolecular Scalability** | Colby Ford (BPDMC) | 2025 | 1:19:04 | [▶](https://www.youtube.com/watch?v=k63Xh-oJMs0) |
| What could AlphaFold 4 look like? | **Sergey Ovchinnikov** (MIT) | 2025 | 2:06:39 | [▶](https://www.youtube.com/watch?v=6_RFXNxy62c) |

> **The OpenFold cluster is the most important material in this section, because
> AlphaFold2's training recipe was never released.** OpenFold is the only public
> account of what it actually costs: roughly 50,000 GPU-hours, the
> initial-training and fine-tuning split, the observation that **the model
> converges in the first 3% of training**, and the memory optimizations —
> in-place operations, chunked attention, low-memory recycling — that made a
> 40 GB A100 sufficient.
>
> **Goreci's talk is the best single account of what breaks when you rebuild AF3
> from the paper alone**: diffusion-module instabilities, the cost of the
> atom-level representation, and what the paper omits. It is twenty-five minutes
> and it is the only talk of its kind in existence.

**Papers:** **Ahdritz et al. 2024, *Nat Methods* 21:1514 (OpenFold)** ·
Cheng et al. 2022, arXiv:2203.00854 (FastFold) · Abramson et al. 2024,
*Nature* 630:493 (AF3) · Wohlwend et al., Boltz-1 and Boltz-2.

*Alternate recordings of the OpenFold talk, all verified:* Chalmers
([▶](https://www.youtube.com/watch?v=gYjAvOfP1Sc)) · Rutgers IQB
([▶](https://www.youtube.com/watch?v=rxxy5R1Eoy8)) · SBGrid
([▶](https://www.youtube.com/watch?v=EnKqDD8fSZY)).

---

## E.7.2 Triangle attention — the memory wall nobody has written about

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **AlphaFold Decoded: Evoformer** | Kilian Mandon (Bamberg) | 24:21 | [▶](https://www.youtube.com/watch?v=gY4-vVRTkpk) |
| AlphaFold Decoded: Attention | Kilian Mandon | 23:51 | [▶](https://www.youtube.com/watch?v=7dS3nyEcOyE) |
| **AlphaFold 3 From Scratch in PyTorch — Introduction** | Kilian Mandon | 34:21 | [▶](https://www.youtube.com/watch?v=CTlkAMpatfI) |
| AlphaFold 3 From Scratch — Feature Extraction | Kilian Mandon | 24:22 | [▶](https://www.youtube.com/watch?v=jI31LflR1Og) |
| **ML for protein structure prediction, Part 2: AlphaFold2 architecture** | Nazim Bouatta (Harvard CMSA) | 1:18:32 | [▶](https://www.youtube.com/watch?v=ri39B0Voujc) |
| MSA Pairformer — scaling down deliberately | ML4PE | 37:58 | [▶](https://www.youtube.com/watch?v=poYqZ7Ml88E) |

**Mandon's series is a hand-implementation course, not an explainer channel** —
he writes the triangle multiplicative update and triangle self-attention in
PyTorch tensor by tensor. **It is the only recorded material that makes the
O(N³) pair-tensor cost concrete rather than asserted.**

> **Honest gap, and it is the sharpest one in this document: there is no talk
> anywhere on the performance of triangle attention itself.** FlashAttention
> solved the O(N²) sequence-attention memory problem by tiling and
> recomputation, and the whole field adopted it. The pair representation's
> O(N³) triangle multiplication has received exactly one fused kernel —
> DeepSpeed's `DS4Sci_EvoformerAttention` — **which has no recorded talk at
> all.** Everyone else falls back to `chunk_size` loops, which trade memory for
> launch overhead and leave the GPU idle.
>
> **Read instead:** the OpenFold source
> (`openfold/model/triangular_multiplicative_update.py` and the chunking logic
> in `openfold/utils/chunk_utils.py`), AlphaFold2 Supplementary Algorithms
> 11–15, and arXiv:2310.04610 for the DeepSpeed kernel. **Derivation checkpoints
> 64 and 66 are this gap made into exercises.**

---

## E.7.3 Equivariant-network performance

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **e3nn: Euclidean Neural Networks** | **Mario Geiger** (then EPFL/MIT, now NVIDIA) | 1:18:41 | [▶](https://www.youtube.com/watch?v=fexvV-RndUc) |
| **Computational Aspects of Equivariant Neural Networks** | **Risi Kondor** (Chicago) | 1:09:11 | [▶](https://www.youtube.com/watch?v=Jt_HENGL4M8) |
| **Does equivariance matter at scale?** | Johann Brehmer (Qualcomm AI) | 1:04:10 | [▶](https://www.youtube.com/watch?v=fcGfrbICsas) |
| Efficient and Expressive 3D Equivariant GNNs | Valence Labs | 54:59 | [▶](https://www.youtube.com/watch?v=bapSYo89gQw) |
| Euclidean Neural Networks: learning with 3D geometry and geometric tensors | Tess Smidt (MIT) | 1:06:01 | [▶](https://www.youtube.com/watch?v=VN2biLjqJXc) |

**Kondor's talk is the closest thing to a cost model**: the computational
structure of Clebsch-Gordan products and where the complexity actually sits.

> **A major gap with a direct bearing on your hardware. There is no recorded
> talk on NVIDIA cuEquivariance**, and none by Mario Geiger about his NVIDIA
> kernel work. Read the cuEquivariance docs — particularly the
> segmented-polynomial representation and the fused `TensorProduct` kernels —
> and **Bharadwaj et al. 2025, *OpenEquivariance: a GPU kernel generator for
> equivariant deep learning***, which benchmarks fused CG kernels against e3nn
> and reports the speedups. **This is the single highest-leverage unrecorded
> topic in Part IV.**

---

## E.7.4 Interatomic potential inference at scale

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Learning Local Equivariant Representations for Large-Scale Atomistic Dynamics** (Allegro) | **Albert Musaelian** (Harvard) | 1:09:17 | [▶](https://www.youtube.com/watch?v=-mRl5Uk8IWk) |
| NequIP and local equivariant representations | Batzner & Musaelian (Harvard) | 1:26:42 | [▶](https://www.youtube.com/watch?v=ZR1NTBPBDOo) |
| Improving Speed and Accuracy of NN Interatomic Potentials | Valence Labs | 54:24 | [▶](https://www.youtube.com/watch?v=OOp2v9-stXo) |
| **Orb-v3: atomistic simulation at scale** | Duignan & Vandenhaute (Orbital) | 1:13:34 | [▶](https://www.youtube.com/watch?v=pRbvRl0_FyE) |
| MACE: Higher Order Equivariant Message Passing | Valence Labs | 1:22:55 | [▶](https://www.youtube.com/watch?v=I9Y2le9e74A) |
| Learning ML Interatomic Potentials | **Gianni De Fabritiis** (TorchMD author) | 51:38 | [▶](https://www.youtube.com/watch?v=4EfUus1qh9Q) |
| JAX MD: A Framework for Differentiable Atomistic Physics | Samuel Schoenholz | 1:27:51 | [▶](https://www.youtube.com/watch?v=iqf8LcT17_0) |
| First Principles Molecular Dynamics on a Large Scale | **Gábor Csányi** (Cambridge) | 1:07:45 | [▶](https://www.youtube.com/watch?v=XP20N8ZwvM0) |
| AquaGen: generative models at MD precision on thousands of atoms | Valence Labs | 1:16:26 | [▶](https://www.youtube.com/watch?v=vQD7VcZxXLI) |

**Watch Batzner first, then Musaelian.** NequIP's story is data efficiency;
Allegro's is that **strict locality removes the message-passing communication
that caps NequIP's scaling**, which is what let them reach 100M+ atoms on
Perlmutter. **Orb-v3 is the clearest statement of the production trade**: it
deliberately drops strict equivariance to buy inference throughput.

**Papers:** **Musaelian et al. 2023, *Nat Commun* 14:579 (Allegro)** and
**Musaelian et al. 2023, SC'23 — read this one for the actual scaling numbers** ·
Batzner et al. 2022, *Nat Commun* 13:2453 (NequIP) · Pelaez et al. 2024, *JCTC*
(TorchMD-NET 2.0) · **Eastman et al. 2024, *J Phys Chem B* 128:109 (OpenMM 8
with ML potentials)** — no talk exists for the last two.

---

## E.7.5 Serving, batching and memory

**Read this subsection as transferable mechanism, not as language-model
content.** The entries: **Fast LLM Serving with vLLM and PagedAttention**,
Woosuk Kwon (Berkeley), 32:07 ([▶](https://www.youtube.com/watch?v=5ZlavKF_98U)) ·
**Exploring the Latency/Throughput and Cost Space for Inference**, Timothée
Lacroix (Mistral CTO), 30:25
([▶](https://www.youtube.com/watch?v=mYRqvB1_gRk)) · **Faster and Cheaper
Offline Batch Inference with Ray**, 28:04
([▶](https://www.youtube.com/watch?v=qzgphfXMNUU)) · Efficient LLM Inference with
SGLang ([▶](https://www.youtube.com/watch?v=Ny4xxErgFgQ)) · Disaggregated
Inference ([▶](https://www.youtube.com/watch?v=tIPDwUepXcA)).

> **The transferable insight is continuous batching.** Static batching wastes
> capacity whenever sequence lengths differ — which is exactly a folding
> campaign where targets range from 80 to 2,000 residues. Lacroix's thirty
> minutes on choosing an operating point on the latency/throughput frontier maps
> almost one-to-one onto "I have ten thousand Boltz predictions and four GPUs."

**On memory:** **ZeRO**, Samyam Rajbhandari (author), 1:05:10
([▶](https://www.youtube.com/watch?v=zqsOEzKZX2Y)) · ZeRO-Offload
([▶](https://www.youtube.com/watch?v=Hdzh4fJv4yY)) · **Too Big to Train — FSDP**,
Sharcnet, 47:33 ([▶](https://www.youtube.com/watch?v=T13tYOGcclk)) and **the
FSDP2 rewrite** ([▶](https://www.youtube.com/watch?v=SgRKWKwQbQE)) ·
**Slaying OOMs with PyTorch FSDP and torchao**, Saroufim & Xu, 49:37
([▶](https://www.youtube.com/watch?v=UvRl4ansfCg)) — the most practically useful
hour here, debugging real OOMs with the memory snapshot tool.

**Papers:** **Kwon et al. 2023, SOSP (PagedAttention)** · Rajbhandari et al.
2020, SC'20 (ZeRO) · **Chen et al. 2016, arXiv:1604.06174 (gradient
checkpointing)** — the paper OpenFold leans on heavily.

---

## E.7.6 The data pipeline — where the time actually goes

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **ColabFold — Making protein folding accessible to all** | **Ovchinnikov, Mirdita & Steinegger** | 1:46:09 | [▶](https://www.youtube.com/watch?v=Rfw7thgGTwI) |
| Exploring the Protein Universe | **Martin Steinegger** (SNU) | 1:17:41 | [▶](https://www.youtube.com/watch?v=lHNeBIGkroM) |
| **MMseqs software suite** | Martin Steinegger | 1:29:37 | [▶](https://www.youtube.com/watch?v=LqiHyCLjPno) |
| MMseqs2 profile/profile searches | Martin Steinegger | 14:03 | [▶](https://www.youtube.com/watch?v=aNCQIePmlGY) |
| **Foldseek** | Martin Steinegger (SBGrid) | 57:17 | [▶](https://www.youtube.com/watch?v=k5Rbi22TtOA) |
| Faster AlphaFold predictions using ColabFold | UCSF ChimeraX | 10:08 | [▶](https://www.youtube.com/watch?v=gIbCAcMDM7E) |
| Zarr vs HDF5 | Joe Jevnik (PyData) | 52:15 | [▶](https://www.youtube.com/watch?v=-l445lCPTts) |
| HDF5 at the speed of Zarr | Pangeo | 25:15 | [▶](https://www.youtube.com/watch?v=iRboOFIB74o) |

> **The ColabFold talk is the single most important entry in this section and
> one of the most important in Part IV.** All three authors, one hour and
> forty-six minutes, explaining the actual engineering: **why MSA generation
> dominated AlphaFold2 wall-clock**, how MMseqs2 replaced JackHMMER and HHblits
> at 40–60× less compute, and how the public MSA server absorbs that load.
>
> **Derivation checkpoint 70 is this talk as an exercise.** Most people assume
> the network dominates. Measure it before you believe it.

**Papers:** **Mirdita et al. 2022, *Nat Methods* 19:679 (ColabFold)** ·
**Steinegger & Söding 2017, *Nat Biotechnol* 35:1026 (MMseqs2)** ·
Steinegger & Söding 2018, *Nat Commun* 9:2542 · van Kempen et al. 2024,
*Nat Biotechnol* 42:243 (Foldseek).

---

# E.8 The Open Engineering Problems

> **This section is the point of Part IV.** Eight problems, drawn from what the
> survey of this literature could *not* find. Several are holes in the field,
> not just in the recorded record. Each is stated with enough specificity that
> you could start it this month.

**1. Nobody has published a profile of a structure-prediction model.** The
survey turned up a dozen good GPU profiling talks and zero that point the tooling
at AlphaFold-class inference. **A careful Nsight profile of Boltz-2 or OpenFold
across sequence lengths** — reporting the split between MSA stack, triangle
operations, diffusion sampling and data loading — would be genuinely citable and
costs a weekend on hardware you already own. **Nothing else on this list is
blocked on it, and everything else gets easier once you have the numbers.**
Start here.

**2. Triangle attention has no public cost model and no general kernel.**
FlashAttention solved the O(N²) problem by tiling and recomputation and the
field adopted it universally. The O(N³) triangle update has one fused kernel,
from DeepSpeed, with no talk and limited adoption. **A FlashAttention-style
treatment of the triangle multiplicative update is unwritten.**

**3. There is no serving stack for structure prediction.** PagedAttention pages a
KV cache; AF3-class models have no KV cache. The expensive resident object is
the pair tensor, whose size grows quadratically in a length that varies ten-fold
across a campaign, so static batching wastes most of the allocation on short
targets. **A length-bucketed continuous batcher for folding models does not
exist publicly**, and for anyone running thousands of predictions on four GPUs
it is worth more than any accuracy improvement.

**4. The MSA bottleneck was solved once, in 2017, and never revisited.**
ColabFold cut MSA cost by an order of magnitude by swapping JackHMMER for
MMseqs2, and that is still the state of the art. Meanwhile models are moving
toward fewer MSAs. **The open question nobody has a talk on is the trade curve:
for a given accuracy target, what is the cheapest MSA you can get away with?**
Measurable, publishable, and it needs no new model.

**5. Equivariant kernels are fast now and nobody has said so publicly.**
cuEquivariance and OpenEquivariance both report large speedups on
Clebsch-Gordan tensor products and neither has a recorded talk. Simultaneously
Brehmer argues equivariance's advantage shrinks with scale, and Orb-v3 ships a
deliberately non-equivariant model for throughput. **These two facts have never
been put in the same room.** If fused kernels close the speed gap, the Orb-style
accuracy sacrifice may be unnecessary.

**6. Precision discipline does not transfer between the two halves of a
bio-ML fleet.** Molecular dynamics precision is a conservation-law question with
thirty years of careful work behind it — Le Grand's SPFP model uses fixed-point
accumulation precisely because naive FP32 breaks energy conservation. Structure
prediction precision is an unexamined throughput knob. **Nobody has published
where bf16 actually costs accuracy in a folding trunk** — whether the triangle
updates, the diffusion sampler or the recycling accumulator is the sensitive
stage. It is a weekend's ablation and it would be widely cited precisely because
it is unglamorous.

**7. Memory sharding assumes weights are the problem.** ZeRO and FSDP partition
parameters, gradients and optimizer states, which is right when weights
dominate. **In a folding model the activation dominates: the pair tensor dwarfs
the parameters.** Ring attention is the only talk in the whole survey that
shards an activation along a sequence axis, and it does so for a 2D object.
Sharding a 3D pair representation, with the triangle update's all-to-all
communication pattern, is unaddressed everywhere. FastFold's Dynamic Axial
Parallelism is the one attempt and it got a ten-minute lightning slot.

**8. The reimplementation ecosystem has no shared engineering record.**
Goreci's talk is the only one in existence about what breaks when you rebuild
these models, and it is twenty-five minutes. Protenix, Chai-1 and Uni-Fold have
no verifiable engineering talks at all. **Each team is rediscovering the same
instabilities privately.** OpenFold set the precedent by publishing the
retraining recipe; nobody has done the equivalent for the AF3 generation.

---

**Which of these to attempt.** Problems 1, 3 and 4 are measurement and systems
work where a small fleet does better than a large lab, because they need careful
instrumentation rather than compute. Problems 2 and 7 are genuine kernel and
distributed-systems research. Problem 6 is the cheapest and would be the most
cited. **Capstone XI asks you to do one of them and get the change merged
upstream.**
