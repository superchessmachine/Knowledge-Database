# E.5 Accelerators, Compilers and the Codesign Bargain

> **The thesis of this section.** A processor is a bet about what computation
> looks like. A GPU bets on throughput over latency. A TPU bets that almost
> everything is a matrix multiply. **Anton bets that it is a range-limited
> N-body problem with a fixed interaction pattern** — and that bet is the most
> successful piece of hardware-software codesign in the history of biology.
>
> This section exists so that you can read those bets rather than accept them.
> **Section E.5.4 is the centerpiece**: one Hot Chips session in which the
> architects of Graphcore, Cerebras, SambaNova and Anton 3 present back to back.
> Four different answers to the same question, in one sitting, by the people who
> made the decisions.

---

## E.5.1 TPU architecture

| # | Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|---|
| 1 | **A Domain-Specific TPU Supercomputer for Training Deep Neural Networks** | **Norm Jouppi** (Google) | 2020 | 1:05:02 | [▶](https://www.youtube.com/watch?v=F6fLwGE83Cw) |
| 2 | **Evaluation of the Tensor Processing Unit** | David Patterson (Berkeley/Google) | 2017 | 56:26 | [▶](https://www.youtube.com/watch?v=fhHAArxwzvQ) |
| 3 | Domain Specific Architectures for DNNs: Three Generations of TPUs | David Patterson (Allen School) | 2019 | 1:12:36 | [▶](https://www.youtube.com/watch?v=VCScWh966u4) |
| 4 | **Computer Architecture Lecture 27: Systolic Arrays** | **Onur Mutlu** (ETH Zürich) | 2021 | 1:04:51 | [▶](https://www.youtube.com/watch?v=8zbh4gWGa7I) |
| 5 | Computer Architecture Lecture 28: VLIW and Systolic Array Architectures | Onur Mutlu (ETH Zürich) | 2023 | 1:26:20 | [▶](https://www.youtube.com/watch?v=j9hOJZFt6rE) |
| 6 | Episode 8: Systolic Arrays | Happy Hour with Architects | 2021 | 56:05 | [▶](https://www.youtube.com/watch?v=lTlpJ2Mz4zs) |
| 7 | **TPU v4 and Trends in Accelerator Hardware** | Mike Hutton (Google) | 2023 | 45:46 | [▶](https://www.youtube.com/watch?v=osurjQmKrys) |
| 8 | Seminar in Computer Architecture: TPUv4i and Mensa | Mutlu group (ETH) | 2022 | 1:55:13 | [▶](https://www.youtube.com/watch?v=71w0ZlYNeiQ) |
| 9 | ML and the Implications for Computer System Design (Hot Chips keynote) | **Jeff Dean** (Google) | 2017 | 58:58 | [▶](https://www.youtube.com/watch?v=VWdReme_5Vg) |
| 10 | Exciting Directions for ML Models and the Implications for Computing Hardware | Jeff Dean + Amin Vahdat | 2023 | 1:03:59 | [▶](https://www.youtube.com/watch?v=EFe7-WZMMhc) |
| 11 | TPU SparseCore: Hardware and Software | OpenXLA / Google | 2026 | 22:56 | [▶](https://www.youtube.com/watch?v=HQFwi5k1jdI) |
| 12 | Architecting TPU 8t and TPU 8i for frontier AI | Google Cloud Next '26 | 2026 | 43:11 | [▶](https://www.youtube.com/watch?v=n-LfId-VVQs) |

**Watch #4 first.** Mutlu derives systolic arrays from Kung and Leiserson's
original idea through to the TPU's matrix unit, and without it the rest of this
subsection is a tour of acronyms. **Then #1**, which is Jouppi on why v2 and v3
moved from inference to training and how the 2D torus scales near-linearly to a
thousand chips. **#7** is the clearest treatment of the optical circuit switch
and the reconfigurable 3D torus; **#8** teaches you to interrogate the design
claims rather than accept them.

**Papers:** **Jouppi et al., *In-Datacenter Performance Analysis of a Tensor
Processing Unit*, ISCA 2017, arXiv:1704.04760** · Jouppi et al., *TPU v4: An
Optically Reconfigurable Supercomputer with Hardware Support for Embeddings*,
ISCA 2023, arXiv:2304.01433.

> **Why a protein person should care.** Triangle attention is not a matrix
> multiply in the shape a systolic array wants. Evoformer-class models run on
> TPUs anyway, and understanding *how badly* they fit is the beginning of
> knowing whether a different decomposition would run better. **Derivation
> checkpoint 64 is this question made concrete.**

---

## E.5.2 XLA, MLIR and the compiler layer

| # | Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|---|
| 13 | **XLA Crash Course** | OpenXLA / Google | 2026 | 31:08 | [▶](https://www.youtube.com/watch?v=3a8u6XeA9yo) |
| 14 | **XLA Architecture** (DevLab 2025) | OpenXLA / Google | 2025 | 1:00:32 | [▶](https://www.youtube.com/watch?v=TdBdmV0mD4s) |
| 15 | **Operator Fusion** (DevLab 2025) | OpenXLA / Google | 2025 | 51:46 | [▶](https://www.youtube.com/watch?v=yydJ6ZGCiVQ) |
| 16 | XLA GPU MLIR Codegen | OpenXLA / Google | 2024 | 1:03:16 | [▶](https://www.youtube.com/watch?v=SbViVo4TrAA) |
| 17 | StableHLO and PJRT | OpenXLA Dev Summit | 2023 | 1:06:47 | [▶](https://www.youtube.com/watch?v=e85Ceq2g5z0) |
| 18 | **MLIR: Multi-Level Intermediate Representation** | Shpeisman + **Chris Lattner** | 2019 | 40:22 | [▶](https://www.youtube.com/watch?v=qzljG6DKgic) |
| 19 | **MLIR Tutorial** (LLVM Dev Meeting) | Amini + Riddle (Google) | 2020 | 1:15:09 | [▶](https://www.youtube.com/watch?v=Y4SvqTtOIDk) |
| 20 | The Golden Age of Compiler Design in an Era of HW/SW Co-design | Chris Lattner (ASPLOS keynote) | 2021 | 52:21 | [▶](https://www.youtube.com/watch?v=4HgShra-KnY) |
| 21 | **TVM: An End to End Deep Learning Compiler Stack** | **Tianqi Chen** | 2020 | 28:16 | [▶](https://www.youtube.com/watch?v=QXp5ebZzLuE) |
| 22 | TVM Tutorial: AutoTVM | Eddie Yan (UW SAMPL) | 2019 | 31:20 | [▶](https://www.youtube.com/watch?v=e4QjghCzYO0) |
| 23 | **Making a blur faster in Halide** | **Andrew Adams** (Adobe) | 2020 | 41:17 | [▶](https://www.youtube.com/watch?v=UeyWo42_PS8) |
| 24 | **ML for ML Compilers** (Stanford MLSys #80) | Mangpo Phothilimthana (DeepMind) | 2023 | 58:06 | [▶](https://www.youtube.com/watch?v=VASg2XNgj-4) |

**#15 is the one you came for.** Fusion is the dominant optimization in every ML
compiler, for exactly the reason Section E.2 gives: it eliminates round trips to
memory. **#23 is the best intuition-builder anywhere** — Halide's main author
live-scheduling a blur, showing the tiling-versus-locality tradeoff as he makes
it. Forty minutes that will change how you read any kernel.

**Also verified and worth having:** Ansor (Lianmin Zheng, OSDI '20,
[▶](https://www.youtube.com/watch?v=A2hJ_Mj02zk)) · Ragan-Kelley on the
algorithm/schedule separation ([▶](https://www.youtube.com/watch?v=bgkji8TrBDI)) ·
Tillet on Triton ([▶](https://www.youtube.com/watch?v=G951lCm_qnk)) and **Triton
Internals** ([▶](https://www.youtube.com/watch?v=njgow_zaJMw)) · IREE GPU codegen
([▶](https://www.youtube.com/watch?v=9Fy2jxj0ARE)) · **Pallas / Mosaic**
([▶](https://www.youtube.com/watch?v=WWkfXUj2w2k)) · Tianqi Chen's full MLC
course, episode 1 ([▶](https://www.youtube.com/watch?v=Oc_wVXdnrrM)).

**Papers:** Chen et al., *TVM*, OSDI 2018, arXiv:1802.04799 · Lattner et al.,
*MLIR*, CGO 2021, arXiv:2002.11054 · **Ragan-Kelley et al., *Halide*, PLDI
2013** · Zheng et al., *Ansor*, OSDI 2020.

---

## E.5.3 JAX, and JAX for molecular simulation

| # | Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|---|
| 25 | **JAX: accelerated ML research via composable function transformations** | **Matthew Johnson** (Google Brain) | 2021 | 57:05 | [▶](https://www.youtube.com/watch?v=mVf3HJ6gNDc) |
| 26 | Stanford MLSys Ep. 6: JAX | Roy Frostig (Google Brain) | 2020 | 1:06:58 | [▶](https://www.youtube.com/watch?v=mbUwCPiqZBM) |
| 27 | Outgrowing NumPy | Dougal Maclaurin (Google) | 2021 | 13:29 | [▶](https://www.youtube.com/watch?v=5XRphWnFkNM) |
| 28 | Intro to JAX on Cloud TPUs | Skye Wanderman-Milne (Google) | 2021 | 1:57:05 | [▶](https://www.youtube.com/watch?v=fuAyUQcVzTY) |
| 29 | Debugging JAX models | Skye Wanderman-Milne | 2025 | 49:22 | [▶](https://www.youtube.com/watch?v=3iP1MvQNWtQ) |
| 30 | **Large scale training techniques and best practices** | Google (DevLab 2025) | 2025 | 1:01:45 | [▶](https://www.youtube.com/watch?v=ep6ISVDG_i4) |
| 31 | Sharding the Sphere with `jax.shard_map` | Google | 2025 | 16:09 | [▶](https://www.youtube.com/watch?v=jVWSuEj9hWE) |
| 32 | **Pallas tutorial** (custom kernels in JAX) | Google JAX team | 2026 | 56:50 | [▶](https://www.youtube.com/watch?v=3u5Md0GGY5E) |
| 33 | **JAX MD: A Framework for Differentiable Atomistic Physics** | **Samuel Schoenholz** (Google Brain) | 2021 | 1:33:38 | [▶](https://www.youtube.com/watch?v=Bkm8tGET7-w) |
| 34 | **Hybridization of Neural Networks and Numerical Solvers in JAX** | Felix Köhler (TU Munich) | 2026 | 1:21:53 | [▶](https://www.youtube.com/watch?v=carwzAOfuPE) |
| 35 | Diffrax: Numerical Differential Equation Solvers in JAX | Patrick Kidger | 2022 | 24:29 | [▶](https://www.youtube.com/watch?v=lT3cmlKUyJY) |

**#33 is the one that matters for you.** Neighbour lists, energy functions and
an end-to-end differentiable molecular dynamics engine — which means you can
take gradients *through* a simulation with respect to force field parameters.
A near-identical reupload is at [▶](https://www.youtube.com/watch?v=iqf8LcT17_0).
**#34** is the best single lecture on coupling a learned component to a
differentiable simulator, which is the architecture behind half of Atlas D.6.

**Also verified:** Rafi Witten's 10-part *High Performance LLMs in JAX* course,
TPU-centric, session 1 at [▶](https://www.youtube.com/watch?v=W0Cix2KNyXc) ·
NERSC *Python on GPUs: JAX* ([▶](https://www.youtube.com/watch?v=YhXUymsQ_3g)) ·
*JAX-GCM, a differentiable atmospheric model*
([▶](https://www.youtube.com/watch?v=aoWj8ku_0r4)).

**Papers:** **Schoenholz & Cubuk, *JAX MD*, NeurIPS 2020, arXiv:1912.04232** ·
Bradbury et al., JAX (2018) · Austin, Douglas, Frostig, Levskaya et al.,
***How to Scale Your Model*, jax-ml.github.io/scaling-book** — a book, with no
recorded lecture; #30 is the closest substitute.

---

## E.5.4 The codesign argument, and four answers to it

**Watch entry 40 as a single sitting.** It is the most valuable two hours in
Part IV.

| # | Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|---|
| 36 | **Hennessy and Patterson, 2017 Turing Award Lecture** | Hennessy + Patterson | 2018 | 1:19:38 | [▶](https://www.youtube.com/watch?v=3LVeEjsn8Ts) |
| 37 | A New Golden Age for Computer Architecture | David Patterson (Berkeley) | 2018 | 1:16:09 | [▶](https://www.youtube.com/watch?v=ctwj53r07yI) |
| 38 | New Golden Age for Computer Architecture | John Hennessy (Stanford) | 2018 | 1:15:20 | [▶](https://www.youtube.com/watch?v=bfPV4x-HrUI) |
| 39 | Domain-Specific Architectures for Deep Neural Networks | David Patterson (ScaledML) | 2019 | 1:00:16 | [▶](https://www.youtube.com/watch?v=FSwKCL8A9JQ) |
| **40** | **ML and Computation Platforms — Graphcore + Cerebras + SambaNova + Anton 3, one session** | Knowles, Lie, Prabhakar, **Butts** | 2021 | 2:16:44 | [▶](https://www.youtube.com/watch?v=mJNln5LCLC8) |
| 41 | **Cerebras Architecture Deep Dive** | Sean Lie (CTO, Cerebras) | 2022 | 27:00 | [▶](https://www.youtube.com/watch?v=8i1_Ru5siXc) |
| 42 | **Thinking Outside the Die** (SAFARI seminar, ETH) | Sean Lie (Cerebras) | 2022 | 1:58:56 | [▶](https://www.youtube.com/watch?v=x2-qB0J7KHw) |
| 43 | Groq architecture (Cornell ECE 5545 guest lecture) | Dennis Abts (Chief Architect, Groq) | 2023 | 59:29 | [▶](https://www.youtube.com/watch?v=rDefOnSq0Uk) |
| 44 | Domain-Specific Networks for Machine Learning (NOCS keynote) | Dennis Abts (Groq) | 2020 | 38:29 | [▶](https://www.youtube.com/watch?v=47QR2Z5pTtA) |
| 45 | **Designing Processors for Intelligence** | Simon Knowles (CTO, Graphcore) | 2017 | 1:16:22 | [▶](https://www.youtube.com/watch?v=7XtBZ4Hsi_M) |

**Read the claims, because they are different claims.** Cerebras claims
*bandwidth* — on-wafer SRAM and fabric bandwidth orders of magnitude above HBM,
with capacity as the acknowledged weakness. Groq claims *latency* — fully
deterministic, compiler-scheduled execution with no caches and no reorder
buffers, and SRAM-only capacity as the binding constraint. Graphcore claims
bandwidth too, via large in-processor memory plus fine-grained MIMD. SambaNova
claims *capacity* — tiered memory holding very large or many models, plus kernel
fusion to remove memory traffic. **None of these is "faster" in the same sense,
and conflating them is the most common error in reading accelerator claims.**

**Also verified:** Graphcore at Hot Chips 2021
([▶](https://www.youtube.com/watch?v=TA4WHnuXCsc)) · Olukotun, *Let the Data
Flow!* ([▶](https://www.youtube.com/watch?v=UAugWwTNAV8)) · **Bill Dally's
GPU-side rebuttal** at Cornell ([▶](https://www.youtube.com/watch?v=HtrR1HRZIGA))
and Hot Chips ([▶](https://www.youtube.com/watch?v=rsxCZAE8QNA)) · Jim Keller's
DAC keynote ([▶](https://www.youtube.com/watch?v=cy-9Jl666Aw)) · Cerebras for
scientific computing ([▶](https://www.youtube.com/watch?v=7mT7sBI-Iyg)).

**Papers:** **Hennessy & Patterson, *A New Golden Age for Computer
Architecture*, CACM 62(2):48–60, 2019** · Abts et al., *Think Fast: A Tensor
Streaming Processor*, ISCA 2020.

---

## E.5.5 Anton — the biology codesign result

**This is the most important subsection in Part IV for someone in your field**,
and it is also the hardest material to source. What follows is everything that
exists on free video.

| # | Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|---|
| 46 | **Anton: A Special-Purpose Machine That Achieves a Hundred-Fold Speedup in Biomolecular Simulations** | **David E. Shaw** | 2012 | 1:20:34 | [▶](https://www.youtube.com/watch?v=PGqCeSjNuTY) |
| 47 | **SC23 Test of Time Award Talk** — retrospective across Anton 1, 2 and 3 | **David E. Shaw** | 2023 | 54:55 | [▶](https://www.youtube.com/watch?v=Ifrm_RhPhlc) |
| 48 | **Anton 2: A 2nd-Generation ASIC for Molecular Dynamics** (Hot Chips 26; segment begins 1:05:53) | J. Adam Butts + D. E. Shaw | 2014 | 34:45 | [▶](https://www.youtube.com/watch?v=b8bxhyXf3fQ&t=3953s) |
| 49 | **The Anton 3 ASIC: a Fire-Breathing Monster for Molecular Dynamics** (Hot Chips 33; segment begins 1:40:31) | **J. Adam Butts** | 2021 | 36:13 | [▶](https://www.youtube.com/watch?v=mJNln5LCLC8&t=6031s) |
| 50 | High Speed Protein Simulations with Anton (UW) | David E. Shaw | 2014 | 58:29 | [▶](https://www.youtube.com/watch?v=ceQ6Kqz8VoY) |
| 51 | Long Molecular Dynamics Simulations: Progress, Problems, and Promise (ISMB keynote) | David E. Shaw | 2016 | 1:35:36 | [▶](https://www.youtube.com/watch?v=OK1POuFOH2Y) |
| 52 | **MDGRAPE-4A: A Special-Purpose Computer for Molecular Dynamics** | Makoto Taiji (RIKEN) | 2020 | 33:03 | [▶](https://www.youtube.com/watch?v=aIpc-v8W4nE) |
| 53 | RISC-V Tokyo: special-purpose MD silicon | Makoto Taiji (RIKEN) | 2020 | 28:33 | [▶](https://www.youtube.com/watch?v=XBIa4Cro6rY) |
| 54 | **Codesign from Semiconductors to AI** | **Cliff Young** (Google) — Anton co-architect *and* TPU co-designer | 2023 | 31:47 | [▶](https://www.youtube.com/watch?v=dHKHuwsrcC4) |

**#49 is the only recorded Anton 3 architecture talk in existence**, and it sits
in the same session as Graphcore, Cerebras and SambaNova. **#47 states the thing
worth knowing**: the gap between Anton and general-purpose machines has *grown*
to more than 400× for drug-discovery-sized systems. **#52 is the honest
counterexample** — a different special-purpose MD machine, explicitly framed
against Anton, explaining why attached-accelerator designs hit a host-side
strong-scaling wall and had to become systems-on-chip.

> **#54 is the bridge, and it is why this section is placed here.** Cliff Young
> co-architected Anton 1 and 2, then co-designed the TPU. **Brian Towles** is an
> author on both the Anton 2 network paper and the TPU v4 paper. The lineage
> from molecular dynamics silicon to machine learning silicon is not an analogy.
> **It is literally the same people**, carrying the same codesign discipline
> across.

**Secondary, all verified:** PSC *Anton 3 Capabilities and Enhanced Sampling*
2025 ([▶](https://www.youtube.com/watch?v=CPh8jr3Y7io)) and 2024
([▶](https://www.youtube.com/watch?v=TD29I5nVKBY)) — allocation-oriented, not
architectural · Tiankai Tu on fault-tolerant parallel analysis of millisecond
trajectories ([▶](https://www.youtube.com/watch?v=xX6qogICuVg)).

**Papers, DOIs resolved rather than recalled:** Shaw et al., *Anton, a
special-purpose machine for molecular dynamics simulation*, ISCA 2007,
`10.1145/1250662.1250664` · **Shaw et al., *Millisecond-scale molecular dynamics
simulations on Anton*, SC09 (Gordon Bell Prize), `10.1145/1654059.1654126`** ·
Shaw et al., *Anton 2*, SC14, `10.1109/SC.2014.9` · **Shaw et al., *Anton 3:
Twenty Microseconds of Molecular Dynamics Simulation Before Lunch*, SC21,
`10.1145/3458817.3487397`** · *Anton: A Specialized Machine for Millisecond-Scale
MD Simulations of Proteins*, IEEE ARITH 2009, `10.1109/arith.2009.33` — **the
best source on Anton's custom arithmetic, and the direct pair for E.6.3** ·
Towles et al., *Unifying On-Chip and Inter-Node Switching Within the Anton 2
Network*, ISCA 2014 · Shim et al., *The Specialized High-Performance Network on
Anton 3*, HPCA 2022.

**Slides, both link-checked:** the Anton 2 and Anton 3 Hot Chips decks are at
`old.hotchips.org/.../HC26.11.130-Anton-2-Butts-Shaw-Shaw-Res-Search.pdf` and
`hc33.hotchips.org/assets/program/conference/day2/HC2021.DESRES.AdamButts.v03.pdf`.

---

## E.5.6 FPGAs and reconfigurable computing

| # | Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|---|
| 55 | **Productive Parallel Programming for FPGA with High Level Synthesis** (SC'20 tutorial) | **Torsten Hoefler** + de Fine Licht (ETH) | 2021 | 3:21:54 | [▶](https://www.youtube.com/watch?v=2UvUP2hxMyI) |
| 56 | **Scientific Applications of FPGAs at the LHC** (FPGA 2021 keynote) | Philip Harris (MIT) | 2021 | 1:00:01 | [▶](https://www.youtube.com/watch?v=rEYgAH4XcDI) |
| 57 | A Reconfigurable Fabric for Accelerating Datacenter Services (Catapult; segment at 34:05) | Putnam, Caulfield, Chung (Microsoft) | 2014 | ~40:00 | [▶](https://www.youtube.com/watch?v=Scm_-xiWc4g&t=2045s) |
| 58 | Reconfigurable Computing at HyperScale | Andrew Putnam (MSR) | 2018 | 54:31 | [▶](https://www.youtube.com/watch?v=mPi2LHLQ9OQ) |
| 59 | Accelerating HPC Applications with Reconfigurable Logic | Microsoft Research | 2016 | 1:09:00 | [▶](https://www.youtube.com/watch?v=pMT_eMvOfKY) |
| 60 | **Comparing FPGA vs Custom CMOS and the Impact on Processor Architecture** | U. Toronto EECG | 2013 | 28:47 | [▶](https://www.youtube.com/watch?v=f4r7W0HDT-I) |
| 61 | hls4ml: Co-Design for Scientific Low-Power ML Devices | Javier Duarte (UCSD) | 2021 | 20:31 | [▶](https://www.youtube.com/watch?v=9p7pRqise8I) |
| 62 | Real-Time ML for Massive LHC Data Streams | Thea Aarrestad (ETH/CERN) | 2023 | 57:52 | [▶](https://www.youtube.com/watch?v=3OP-j8kdD1c) |

**Watch #60 first, for one number.** The FPGA-versus-ASIC tax is 17–27× in area
and 18–26× in delay for soft logic, but only 2–7× for hard blocks. **That single
fact explains why Anton is an ASIC and Catapult is not**, and it is the whole
decision procedure for anyone wondering whether to build custom hardware.

**Also verified:** AI Engine Architecture (SPCL,
[▶](https://www.youtube.com/watch?v=bNTeob7KfiQ)) · Doug Burger, *Transitioning
from the Era of Multicore to the Era of Specialization*
([▶](https://www.youtube.com/watch?v=vo1qHEqLK4c)) · FBLAS: streaming linear
algebra on FPGA ([▶](https://www.youtube.com/watch?v=DG7YVewW0Vc)).

---

## E.5.7 Paired reading — E.5

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Mutlu, *Systolic Arrays*** | Kung & Leiserson 1979 | Why does a systolic array suit matrix multiply and not N-body? |
| **Jouppi, *TPU supercomputer*** | **arXiv:1704.04760** then arXiv:2304.01433 | Roofline the TPU. Where would an Evoformer land on it? |
| OpenXLA, *Operator Fusion* | The XLA fusion documentation | What does fusion eliminate? Connect it to Section E.2. |
| **Adams, *Making a blur faster in Halide*** | **Ragan-Kelley et al., PLDI 2013** | Separate algorithm from schedule for one MD kernel on paper. |
| Chen, *TVM* | arXiv:1802.04799 | Learned cost models for kernel search. Could you autotune a force kernel? |
| **Schoenholz, *JAX MD*** | **arXiv:1912.04232** | Differentiating through a simulation. What becomes possible? |
| Köhler, *NNs and numerical solvers in JAX* | The accompanying paper | Where does the gradient through a long trajectory become useless? |
| **Hot Chips session (#40)** | Compare the four claims | Bandwidth, latency, or capacity? Classify each vendor correctly. |
| Lie, *Thinking Outside the Die* | Cerebras WSE papers | What does wafer-scale buy, and what does it give up? |
| **Shaw, *Anton*** | **Shaw et al., SC09, `10.1145/1654059.1654126`** | What was specialized, and what was deliberately left general? |
| **Butts, *Anton 3*** | **Shaw et al., SC21, `10.1145/3458817.3487397`** | Twenty microseconds before lunch. What changed from Anton 2? |
| Shaw, *SC23 Test of Time* | The retrospective | The gap to general-purpose hardware grew to 400×. Why? |
| Taiji, *MDGRAPE-4A* | The MDGRAPE papers | Why did attached accelerators have to become SoCs? |
| **Young, *Codesign from Semiconductors to AI*** | Anton ISCA 2007 + TPU ISCA 2017 | The same people built both. What transferred, and what did not? |
| U. Toronto, *FPGA vs Custom CMOS* | The paper | 17–27× area tax. When is an FPGA the right answer? |
