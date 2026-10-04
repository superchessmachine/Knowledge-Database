# E.4 GPU Architecture and Kernel Engineering

> **This is the section that will make the most immediate difference to your
> daily work**, because it answers the question you have never asked: *why is my
> GPU idle?* The answer is almost always memory movement, and almost never the
> thing you assumed.
>
> **Two structural facts about this literature, both discovered in compiling it.**
> First, **GPU MODE is the richest free archive in this entire curriculum** —
> 116 numbered lectures, enumerated below in full. Second, **NVIDIA
> systematically does not put its deep GTC sessions on YouTube.** Stephen Jones's
> canonical architecture talks, Micikevicius's mixed-precision sessions and the
> CUTLASS deep-dives live behind the free-but-registration-walled NVIDIA
> On-Demand portal. The community archives below exist largely because of that
> absence.

---

## E.4.1 Architecture fundamentals

| Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|
| **Notes on AI Hardware** (Stanford MLSys #88) | **Benjamin Spector** (Stanford, ThunderKittens) | 2024 | 1:16:48 | [▶](https://www.youtube.com/watch?v=PlraH57ey4k) |
| CUDA + ThunderKittens, but increasingly drunk | Benjamin Spector | 2024 | 4:25:26 | [▶](https://www.youtube.com/watch?v=xcpEl0cGCC4) |
| **GPU Programming Fundamentals + ThunderKittens** | Brandon (Anthropic) & Arora (Stanford) | 2025 | 2:39:22 | [▶](https://www.youtube.com/watch?v=Cl2B_hmg4gA) |
| **Nvidia's H100 GPU** (Stanford Seminar) | **Jack Choquette** (H100 chief architect) | 2023 | 50:05 | [▶](https://www.youtube.com/watch?v=MC223HlPdK0) |
| **Computer Architecture Lecture 26: GPU Programming** | Onur Mutlu (ETH) | 2022 | 2:32:38 | [▶](https://www.youtube.com/watch?v=bh9cbi_HN4A) |
| **HetSys Lecture 5: GPU Performance Considerations** | ETH Zürich | 2022 | 1:23:30 | [▶](https://www.youtube.com/watch?v=ODeprwr3Jho) |
| Stanford CS149 L7: GPU Architecture and CUDA Programming | Stanford | 2024 | 1:18:47 | [▶](https://www.youtube.com/watch?v=qQTDF0CBoxE) |
| Stanford CS149 L8: Data-Parallel Thinking | Stanford | 2024 | 1:17:49 | [▶](https://www.youtube.com/watch?v=Ba3TqxSgnTk) |
| **Introduction to SASS and GPU Microarchitecture** | Arun Demeure | 2024 | 1:50:40 | [▶](https://www.youtube.com/watch?v=we3i5VuoPWk) |
| **The One-Decade Task: Putting std::atomic in CUDA** | **Olivier Giroux** (NVIDIA memory-model architect) | 2019 | 1:05:38 | [▶](https://www.youtube.com/watch?v=VogqOscJYvk) |
| Designing (New) C++ Hardware | Olivier Giroux (NVIDIA) | 2017 | 59:57 | [▶](https://www.youtube.com/watch?v=86seb-iZCnI) |
| **Hardware for Deep Learning** (Hot Chips keynote) | **Bill Dally** (NVIDIA Chief Scientist) | 2023 | 1:05:28 | [▶](https://www.youtube.com/watch?v=rsxCZAE8QNA) |
| Trends in Deep Learning Hardware | Bill Dally (Berkeley) | 2025 | 1:13:07 | [▶](https://www.youtube.com/watch?v=4u8iMr3iXR4) |
| **What is the Hardware Lottery?** (MLSys #15) | Sara Hooker (Google Brain) | 2021 | 1:00:24 | [▶](https://www.youtube.com/watch?v=vMhA-xl3dbA) |
| **Hardware-aware Algorithms for Sequence Modeling** (MLSys #87) | **Tri Dao** (Princeton) | 2024 | 1:19:06 | [▶](https://www.youtube.com/watch?v=foG0ebzuw34) |
| **A Performance Engineer's Guide to NVIDIA Blackwell GPUs** | Chris Sullivan (NVIDIA) | 2025 | 35:17 | [▶](https://www.youtube.com/watch?v=GL7ImGZj-Oc) |
| Introduction to GPU Architecture and Programming Models (ATPESC) | Tim Warburton (Virginia Tech) | 2018 | 2:14:04 | [▶](https://www.youtube.com/watch?v=uvVy3CqpVbM) |
| GPU optimization workshop (OpenAI, NVIDIA, PyTorch) | Saroufim, Chetlur, **Tillet** | 2024 | 2:33:53 | [▶](https://www.youtube.com/watch?v=v_q2JTIqE20) |

### The Stephen Jones sequence — and a caveat about where it lives

**Stephen Jones is NVIDIA's CUDA architect and his two most famous talks are the
best forty minutes in existence on why GPUs are bandwidth machines rather than
FLOP machines.** They exist on YouTube *only as third-party re-uploads* —
NVIDIA has not posted them, and the canonical versions sit behind the
free-but-registration-gated GTC On-Demand portal. The re-uploads below are
complete and verified live.

| Talk | Yr | Len | Link |
|---|---|---|---|
| **How GPU Computing Works** — latency hiding and arithmetic intensity from first principles | 2021 | 39:36 | [▶](https://www.youtube.com/watch?v=3l10o0DYJXg) |
| **How CUDA Programming Works** — coalescing, occupancy, caches, and why the hardware rewards specific access patterns | 2022 | 41:15 | [▶](https://www.youtube.com/watch?v=QQceTDjA4f4) |
| CUDA: New Features and Beyond, GTC 2024 *(official NVIDIA upload)* | 2024 | 50:08 | [▶](https://www.youtube.com/watch?v=pC0SIzZGFSc) |
| CUDA: New Features and Beyond, GTC 2025 *(official)* | 2025 | 44:04 | [▶](https://www.youtube.com/watch?v=6o_Wme-FdCU) |
| CUDA: New Features and Beyond, GTC 2026 *(official, most current)* | 2026 | 44:27 | [▶](https://www.youtube.com/watch?v=VdIVQcMn0CA) |
| Interview with CUDA Architect Stephen Jones — CUDA's design history | 2024 | 1:01:50 | [▶](https://www.youtube.com/watch?v=dNUMNifgExs) |

**NVIDIA's official CUDA C++ Class** is a genuine course rather than marketing:
*Accelerating Applications with Parallel Algorithms* (2:05:27,
[▶](https://www.youtube.com/watch?v=Sdjn9FOkhnA)) · *Asynchrony and CUDA
Streams* (47:43, [▶](https://www.youtube.com/watch?v=pyW9St8uM8w)) ·
*Implementing New Algorithms with CUDA Kernels* (1:12:29,
[▶](https://www.youtube.com/watch?v=kTWoGCSugB4)).

> **Start with Spector's *Notes on AI Hardware*.** It is the talk that argues a
> researcher should learn the hardware, then teaches the memory hierarchy and
> tensor-core throughput ratios well enough to act on it. **Then Hooker's
> *Hardware Lottery*** — the argument that which algorithms "win" is partly an
> accident of what silicon happened to exist, which is a sobering frame for
> anyone choosing a method.
>
> **Giroux's `std::atomic` talk is the only serious free treatment of the GPU
> memory consistency model** — forward progress, scopes, and the Volta
> scheduling change. If you have ever written a kernel with a race you could not
> explain, this is why.

**Papers:** Jia et al., *Dissecting the NVIDIA Volta GPU Architecture via
Microbenchmarking*, arXiv:1804.06826 (Turing sequel arXiv:1903.07486) · the
Hopper and Blackwell architecture whitepapers · the CUDA C++ Programming Guide
memory-model chapter.

---

## E.4.2 Programming Massively Parallel Processors — the complete course

**Izzat El Hajj (American University of Beirut), 23 lectures, ~25 hours**, keyed
to the Hwu/Kirk/El Hajj textbook. This is the single best free CUDA course that
exists and it is almost unknown. **Lectures 4 through 7 are the
performance-engineering spine.**

| # | Lecture | Len | Link |
|---|---|---|---|
| 1 | Introduction | 42:34 | [▶](https://www.youtube.com/watch?v=4pkbXmE4POc) |
| 2 | Data Parallel Programming | 1:19:18 | [▶](https://www.youtube.com/watch?v=iE-xGWBQtH0) |
| 3 | Multidimensional Grids and Data | 1:11:09 | [▶](https://www.youtube.com/watch?v=c8dehGOB8mQ) |
| **4** | **GPU Architecture** | 1:23:57 | [▶](https://www.youtube.com/watch?v=pBQJAwogMoE) |
| **5** | **Memory and Tiling** | 1:24:26 | [▶](https://www.youtube.com/watch?v=31ZyYkoClT4) |
| **6** | **Performance Considerations** | 1:08:05 | [▶](https://www.youtube.com/watch?v=DA-_EK8PbTY) |
| **7** | **Profiling** | 1:00:59 | [▶](https://www.youtube.com/watch?v=zHY7iF_2RyU) |
| 8 | Convolution | 1:06:06 | [▶](https://www.youtube.com/watch?v=xEVyTZG1wlk) |
| 9 | Stencil | 1:23:20 | [▶](https://www.youtube.com/watch?v=NOoSyDCVRU0) |
| 10 | Reduction | 1:21:26 | [▶](https://www.youtube.com/watch?v=voFt2e2QXtA) |
| 11 | Scan (Kogge-Stone) | 1:12:15 | [▶](https://www.youtube.com/watch?v=-eoUw8fTy2E) |
| 12 | Scan (Brent-Kung) | 1:26:07 | [▶](https://www.youtube.com/watch?v=CcwdWP44aFE) |
| 13 | Histogram | 1:06:00 | [▶](https://www.youtube.com/watch?v=BiYieuVwUbg) |
| 14 | Merge | 1:08:36 | [▶](https://www.youtube.com/watch?v=szoc52lNufU) |
| 15 | Sort | 1:15:39 | [▶](https://www.youtube.com/watch?v=XTfH6Ll9KaA) |
| 16 | Sparse Matrix Computation (COO, CSR) | 1:03:21 | [▶](https://www.youtube.com/watch?v=H6YGKNukGMo) |
| 17 | Sparse Matrix Computation (ELL, JDS) | 1:07:28 | [▶](https://www.youtube.com/watch?v=bDbUoRrT6Js) |
| 18 | Graph Processing | 1:14:12 | [▶](https://www.youtube.com/watch?v=P3eQWkVj9dA) |
| 19 | Graph Processing, Part 2 | 1:11:39 | [▶](https://www.youtube.com/watch?v=YXHnBKSWLSU) |
| **20** | **Intra-Warp Synchronization** | 1:04:26 | [▶](https://www.youtube.com/watch?v=g5ZKBH6UQvE) |
| 21 | Pinned Memory and Streams | 1:12:12 | [▶](https://www.youtube.com/watch?v=aNchuoFCgSs) |
| 22 | Dynamic Parallelism | 1:01:48 | [▶](https://www.youtube.com/watch?v=R3d_ECmHAiI) |
| 23 | Potpourri | 50:11 | [▶](https://www.youtube.com/watch?v=wCyNd662aic) |
| **+** | **Advanced Optimizations for Matrix Multiplication** (2026) | 1:23:11 | [▶](https://www.youtube.com/watch?v=6AVEPOqJfOk) |

**The supplementary GEMM lecture is the single best worked example of this
discipline anywhere** — register tiling, thread coarsening, the full
optimization ladder from naive to competitive, in one sitting.

**The graduate sequel — UIUC ECE508, Wen-mei Hwu** (the PMPP author), on
algorithm-level transformation rather than CUDA API:
L1 Introduction [▶](https://www.youtube.com/watch?v=WJ0BAlaXFUc) ·
L2 Scatter-to-Gather [▶](https://www.youtube.com/watch?v=nD6PUe3d6ec) ·
**L3 Thread Coarsening and Register Tiling** [▶](https://www.youtube.com/watch?v=awcTLCJbNNs) ·
L4 Joint Register and Shared Memory Tiling [▶](https://www.youtube.com/watch?v=RsJobEJVdbk) ·
L5 Input Binning [▶](https://www.youtube.com/watch?v=Jomj8_6GOZc) ·
L7 Graph Representation and BFS [▶](https://www.youtube.com/watch?v=ah2KQR_lDTQ) ·
L9 Triangle Counting [▶](https://www.youtube.com/watch?v=quLDt39KQ5Y)

---

## E.4.3 GPU MODE — 116 lectures, enumerated

Channel [@GPUMODE](https://www.youtube.com/@GPUMODE); slides and code at
`github.com/gpu-mode/lectures`. **All 116 verified present with no gaps.**

> **One correction worth knowing before you use the repo:** the GitHub README's
> numbering diverges from YouTube at lectures 40 and 41. YouTube — which is
> self-consistent and authoritative — has **L40 = CUDA Docs for Humans** and
> **L41 = FlashInfer**; the README swaps them. The numbering below is YouTube's.

**★ marks the priority lectures** for a molecular-simulation person: CUDA
fundamentals, memory, profiling, Triton, CUTLASS/CuTe, quantization, fused
kernels, sparsity, collectives, PyTorch internals and Hopper/Blackwell.

| # | Lecture | Speaker | Len | Link |
|---|---|---|---|---|
| ★1 | How to profile CUDA kernels in PyTorch | Mark Saroufim | 56:13 | [▶](https://www.youtube.com/watch?v=LuhJEEJQgUM) |
| ★2 | Recap Ch. 1–3, PMPP book | Andreas Köpf | 52:26 | [▶](https://www.youtube.com/watch?v=NQ-0D5Ti2dc) |
| ★3 | Getting Started With CUDA for Python Programmers | Jeremy Howard | 1:17:56 | [▶](https://www.youtube.com/watch?v=4sgKnKbR-WE) |
| ★4 | Compute and Memory Basics | Thomas Viehmann | 56:55 | [▶](https://www.youtube.com/watch?v=lTmYrKwjSOU) |
| ★5 | Going Further with CUDA for Python Programmers | Jeremy Howard | 1:17:34 | [▶](https://www.youtube.com/watch?v=wVsR-YhaHlM) |
| 6 | Optimizing PyTorch Optimizers | Jane Xu | 1:06:13 | [▶](https://www.youtube.com/watch?v=hIop0mWKPHc) |
| ★7 | Advanced Quantization | Charles Hernandez | 1:23:26 | [▶](https://www.youtube.com/watch?v=1u9xUK3G4VM) |
| ★8 | **CUDA Performance Checklist** | Mark Saroufim | 1:08:10 | [▶](https://www.youtube.com/watch?v=SGhfUhlowB4) |
| ★9 | Reductions | Mark Saroufim | 46:42 | [▶](https://www.youtube.com/watch?v=09wntC6BT5o) |
| 10 | Build a Prod Ready CUDA Library | Oscar Amoros Huguet | 1:25:17 | [▶](https://www.youtube.com/watch?v=FHsEW0HpuoU) |
| ★11 | Sparsity | Jesse Cai | 56:43 | [▶](https://www.youtube.com/watch?v=mGDnOLcfE8g) |
| ★12 | Flash Attention | Thomas Viehmann | 1:12:14 | [▶](https://www.youtube.com/watch?v=zEuwuCTEf_0) |
| 13 | Ring Attention | Andreas Köpf | 1:15:35 | [▶](https://www.youtube.com/watch?v=ws7angQYIxI) |
| ★14 | A Practitioner's Guide to Triton | Umer Adil | 1:21:43 | [▶](https://www.youtube.com/watch?v=DdTsX6DQk24) |
| ★15 | CUTLASS | Eric Auld | 1:34:24 | [▶](https://www.youtube.com/watch?v=G6q719ck7ww) |
| ★16 | On-Hands Profiling | Taylor Robie | 55:41 | [▶](https://www.youtube.com/watch?v=SKV6kDk1s94) |
| ★17 | GPU Collective Communication (NCCL) | Dan Johnson | 59:43 | [▶](https://www.youtube.com/watch?v=T22e3fgit-A) |
| ★18 | **Fusing Kernels** | Kapil Sharma | 1:23:22 | [▶](https://www.youtube.com/watch?v=m6BSREnQ84U) |
| 19 | Data Processing on GPUs | Devavret Makkar | 59:09 | [▶](https://www.youtube.com/watch?v=FUBrIgdIuh0) |
| 20 | Scan Algorithm | Izzat El Hajj | 1:02:20 | [▶](https://www.youtube.com/watch?v=ZKrWyEqqPVY) |
| 21 | Scan Algorithm, Part 2 | Izzat El Hajj | 1:04:41 | [▶](https://www.youtube.com/watch?v=MH5_FeSSdIE) |
| 22 | Speculative Decoding in vLLM | Cade Daniel | 1:09:25 | [▶](https://www.youtube.com/watch?v=9wNAgpX6z_4) |
| ★23 | **Tensor Cores** | Thakkar & Ramani (NVIDIA) | 1:47:50 | [▶](https://www.youtube.com/watch?v=hQ9GPnV0-50) |
| 24 | Scan at the Speed of Light | Hemstad & Evtushenko (NVIDIA) | 1:06:19 | [▶](https://www.youtube.com/watch?v=VLdm3bV4bKo) |
| 25 | Composable Kernel (CK) | Haocong Wang (AMD) | 1:30:52 | [▶](https://www.youtube.com/watch?v=-732zELVbpU) |
| 26 | SYCL Mode (Intel GPU) | Patric Zhao | 1:18:35 | [▶](https://www.youtube.com/watch?v=7HqbuMBUV7A) |
| 27 | gpu.cpp — portable compute via WebGPU | Austin Huang | 58:12 | [▶](https://www.youtube.com/watch?v=Ll5Sr1L5LvA) |
| ★28 | Liger Kernel — Efficient Triton Kernels | Byron Hsu | 1:11:27 | [▶](https://www.youtube.com/watch?v=gWble4FreV4) |
| ★29 | **Triton Internals** | Kapil Sharma | 1:04:49 | [▶](https://www.youtube.com/watch?v=njgow_zaJMw) |
| ★30 | Quantized Training | Thien Tran | 1:16:40 | [▶](https://www.youtube.com/watch?v=Br07GsnnvWc) |
| 31 | Beginner's Guide to Metal Kernels | Nikita Shulga | 1:32:08 | [▶](https://www.youtube.com/watch?v=cGtiaJjLkAI) |
| 32 | Unsloth — LLM Systems Engineering | Daniel Han | 1:24:54 | [▶](https://www.youtube.com/watch?v=hfb_AIhDYnA) |
| ★33 | BitBLAS | Lei Wang (MSRA) | 1:01:48 | [▶](https://www.youtube.com/watch?v=iA49QqWwMcA) |
| ★34 | Low-Bit Triton Kernels | Hicham Badri | 1:45:31 | [▶](https://www.youtube.com/watch?v=7c3c3bCGzKU) |
| 35 | SGLang Performance Optimization | Yineng Zhang | 45:19 | [▶](https://www.youtube.com/watch?v=XQylGyG7yp8) |
| ★36 | **CUTLASS and FlashAttention 3** | **Jay Shah** (Colfax) | 1:49:16 | [▶](https://www.youtube.com/watch?v=JwUcZwPOCpA) |
| ★37 | Introduction to SASS and GPU Microarchitecture | Arun Demeure | 1:50:40 | [▶](https://www.youtube.com/watch?v=we3i5VuoPWk) |
| 38 | Low-Bit Kernels for ARM CPU | Scott Roy | 1:03:41 | [▶](https://www.youtube.com/watch?v=2iNGuZxe1ms) |
| ★39 | TorchTitan (FSDP2 / DTensor internals) | Saroufim & Liu | 1:23:38 | [▶](https://www.youtube.com/watch?v=VYWRjcUqW6w) |
| ★40 | CUDA Docs for Humans | Charles Frye (Modal) | 51:07 | [▶](https://www.youtube.com/watch?v=qmpGv72qPCE) |
| 41 | FlashInfer | Zihao Ye (UW) | 1:08:51 | [▶](https://www.youtube.com/watch?v=iOLBJwENuvA) |
| 42 | Mosaic GPU | Adam Paszke (Google) | 1:26:25 | [▶](https://www.youtube.com/watch?v=wKd90avC8Nc) |
| ★43 | int8 Tensor-Core Matmul for Turing | Erik Schultheis | 1:17:11 | [▶](https://www.youtube.com/watch?v=BgGe_erJB1A) |
| ★44 | **NVIDIA Profiling** (2h deep dive) | NVIDIA tools engineers | 2:07:16 | [▶](https://www.youtube.com/watch?v=F_BazucyCMw) |
| ★45 | **Outperforming cuBLAS on H100** | pranjalssh | 1:16:01 | [▶](https://www.youtube.com/watch?v=ErTmTCRP1_U) |
| ★46 | Distributed GEMM | Ali Hassani | 1:27:29 | [▶](https://www.youtube.com/watch?v=NHRTCQBZokg) |
| 47 | KernelBot | — | 1:02:23 | [▶](https://www.youtube.com/watch?v=wiaiv9_TgN4) |
| ★48 | **The Ultra-Scale Playbook** | Nouamane Tazi (HF) | 3:03:48 | [▶](https://www.youtube.com/watch?v=1E8GDR8QXKw) |
| 49 | Low-Bit Metal Kernels | Manuel Candales | 1:31:55 | [▶](https://www.youtube.com/watch?v=PaPuu73wowE) |
| 50 | A Learning Journey: CUDA, Triton, Flash Attention | Umar Jamil | 1:20:43 | [▶](https://www.youtube.com/watch?v=4jQTb6sRGLg) |
| 51 | Consumer GPU Performance | Jake Cannell | 1:16:01 | [▶](https://www.youtube.com/watch?v=7GO2t-8S2w0) |
| ★52 | Scaling Laws for Low Precision | Tanishq Kumar (Harvard) | 53:43 | [▶](https://www.youtube.com/watch?v=YCfzf0TunOM) |
| ★53 | torch.compile Q&A | Richard Zou (Meta) | 1:26:51 | [▶](https://www.youtube.com/watch?v=mG8TRTWs9Aw) |
| 54 | Small RL Models with LeanRL | — | 53:49 | [▶](https://www.youtube.com/watch?v=En2Wdagwe24) |
| 55 | Mojo | Modular | 2:13:12 | [▶](https://www.youtube.com/watch?v=5gPG7SXoBag) |
| ★56 | **Kernel Benchmarking Tales** | Georgii Evtushenko (NVIDIA) | 1:07:57 | [▶](https://www.youtube.com/watch?v=CtrqBmYtSEk) |
| ★57 | **CuTe** | **Cris Cecka** (NVIDIA, CuTe architect) | 1:24:33 | [▶](https://www.youtube.com/watch?v=vzUhbDO_0qk) |
| 58 | Disaggregated LLM Inference | Junda Chen | 1:15:19 | [▶](https://www.youtube.com/watch?v=tIPDwUepXcA) |
| 59 | FastVideo | — | 1:04:11 | [▶](https://www.youtube.com/watch?v=tquHfKqKo1s) |
| ★60 | Optimizing Linear Attention | Songlin Yang (MIT) | 1:07:39 | [▶](https://www.youtube.com/watch?v=RTJKXK5L8gw) |
| 61 | D-Matrix Corsair | Jain, Arunkumar, Srivastava | 1:38:09 | [▶](https://www.youtube.com/watch?v=xJ_VYUDAJZw) |
| 62 | Exo 2 — Growing a Scheduling Language | Yuka Ikarashi (MIT) | 1:08:23 | [▶](https://www.youtube.com/watch?v=62gKfSyqCkA) |
| 63 | Search-Based DL Compilers (Luminal) | Joe Fioti | 1:09:19 | [▶](https://www.youtube.com/watch?v=_aT2eo-0uWk) |
| ★64 | Multi-GPU Programming | Markus Hrywniak (NVIDIA) | 1:15:23 | [▶](https://www.youtube.com/watch?v=BgeFR4UfajQ) |
| 65 | Neighborhood Attention | Ali Hassani | 1:37:53 | [▶](https://www.youtube.com/watch?v=y5r2asbfNcs) |
| 66 | Game Arena | Lanxiang Hu | 53:33 | [▶](https://www.youtube.com/watch?v=Yb9MiSInuEs) |
| ★67 | **NCCL and NVSHMEM** | Jeff Hammond (NVIDIA) | 1:40:43 | [▶](https://www.youtube.com/watch?v=zxGVvMN6WaM) |
| ★68 | Landscape of GPU-Centric Communication | Didem Unat (Koç) | 1:00:07 | [▶](https://www.youtube.com/watch?v=beuOWBbiJfQ) |
| ★69 | Quartet — 4-bit Training | Castro & Panferov (ISTA) | 1:09:11 | [▶](https://www.youtube.com/watch?v=XVo17Q7YapA) |
| ★70 | PCCL — Fault-Tolerant Collectives | mike64_t | 1:05:23 | [▶](https://www.youtube.com/watch?v=2KUyEdlVBsw) |
| 71 | [ScaleML] FlexOlmo | Sewon Min (Berkeley) | 1:24:51 | [▶](https://www.youtube.com/watch?v=KorF7Xpozhg) |
| 72 | [ScaleML] Efficient Long-Context Modeling | Guangxuan Xiao (MIT) | 55:18 | [▶](https://www.youtube.com/watch?v=DFcKFDt0QEg) |
| ★73 | [ScaleML] Quantization in Large Models | Chris De Sa (Cornell) | 1:18:26 | [▶](https://www.youtube.com/watch?v=6Cxnnvv3DnY) |
| 74 | [ScaleML] Positional Encodings and PaTH Attention | Songlin Yang | 1:40:32 | [▶](https://www.youtube.com/watch?v=QXbXdN3KIcY) |
| ★75 | [ScaleML] GPU Fundamentals + ThunderKittens | Brandon & Arora | 2:39:22 | [▶](https://www.youtube.com/watch?v=Cl2B_hmg4gA) |
| 76 | BackendBench | Mark Saroufim | 17:54 | [▶](https://www.youtube.com/watch?v=BTfjdyZOKww) |
| ★77 | **Domain-Specific Languages for GPU Kernels** | **Tri Dao** | 23:39 | [▶](https://www.youtube.com/watch?v=5qSN-R_E3w0) |
| ★78 | Iris — Multi-GPU Programming in Triton | Awad, Osama, Potter (AMD) | 1:16:38 | [▶](https://www.youtube.com/watch?v=i6Y2EelEC04) |
| 79 | Mirage — Compiling LLMs into Megakernels | Wu & Cheng (CMU) | 1:12:52 | [▶](https://www.youtube.com/watch?v=sXDdRCy137c) |
| ★80 | **How FlashAttention 4 Works** | Charles Frye (Modal) | 1:15:09 | [▶](https://www.youtube.com/watch?v=VPslgC9piIw) |
| 81 | Futhark | Troels Henriksen | 1:11:03 | [▶](https://www.youtube.com/watch?v=dFxO1Wb5-eY) |
| ★82 | Helion — A High-Level DSL for ML Kernels | Ansel, Ulgen, Feng (Meta) | 1:06:20 | [▶](https://www.youtube.com/watch?v=MBOPzfl1JBo) |
| 83 | Formalized Kernel Derivation | Vincent Abbott (MIT) | 1:40:06 | [▶](https://www.youtube.com/watch?v=pB8jRHHGJcE) |
| ★84 | **Numerics and AI** | **Paulius Micikevicius** (NVIDIA) | 2:39:09 | [▶](https://www.youtube.com/watch?v=ua2NhlenIKo) |
| 85 | Factorio Learning Environment | Jack Hopkins | 1:06:12 | [▶](https://www.youtube.com/watch?v=iXvYa2oIMbA) |
| ★86 | Getting Started with CuTe DSL | Vicki Wang (NVIDIA) | 1:13:19 | [▶](https://www.youtube.com/watch?v=9-dfte_N3yk) |
| ★87 | Low-Latency Communication Kernels with NVSHMEM | Prajwal Singhania | 1:07:07 | [▶](https://www.youtube.com/watch?v=6bqnqDZg4_0) |
| 88 | TinyTPU | William Zhang | 54:32 | [▶](https://www.youtube.com/watch?v=qCxuLIMycCc) |
| ★89 | cuTile | Amini & Roesch (NVIDIA) | 1:43:31 | [▶](https://www.youtube.com/watch?v=_b4I4rKpsGA) |
| 90 | Building Resilient ML Engineering Skills | Stas Bekman | 1:54:07 | [▶](https://www.youtube.com/watch?v=A_20dqGfuWI) |
| 91 | Mega Lecture: RL, Agents and OpenEnv | multiple | 3:21:51 | [▶](https://www.youtube.com/watch?v=Jew4lhAiqnw) |
| 92 | Smol Training Playbook | Loubna Ben Allal (HF) | 1:26:03 | [▶](https://www.youtube.com/watch?v=PQZt5L5Mwtg) |
| 93 | Cornserve | Jeff Ma | 44:19 | [▶](https://www.youtube.com/watch?v=uIulphvtyGs) |
| 94 | tvm-ffi | Tianqi Chen (CMU) | 1:28:31 | [▶](https://www.youtube.com/watch?v=fQcCCSdAFI8) |
| 95 | Single-Controller Programming with Monarch | Wang & Taylor (Meta) | 2:02:24 | [▶](https://www.youtube.com/watch?v=PO3CN3UYx7w) |
| ★96 | TLX — Triton-Like Simplicity, Peak Performance | Hongtao Yu (Meta) | 1:29:58 | [▶](https://www.youtube.com/watch?v=TH1i-GmMZuQ) |
| ★97 | HipKittens | William Hu (Stanford) | 1:25:05 | [▶](https://www.youtube.com/watch?v=jsYyF03Fs3o) |
| ★98 | GPU Observability | Yusheng Zheng | 46:53 | [▶](https://www.youtube.com/watch?v=-6FlMJ-AP74) |
| 99 | Distributed ML on Consumer Devices | Matt Beton | 1:05:53 | [▶](https://www.youtube.com/watch?v=sV0PJC1dOmM) |
| 100 | InferenceX | — | 1:12:06 | [▶](https://www.youtube.com/watch?v=kPBTBl7xvEY) |
| ★101 | Learning CUTLASS the Hard Way | Kapil Sharma | 1:11:17 | [▶](https://www.youtube.com/watch?v=jGouxuAHIfQ) |
| ★102 | Quartet v2 | Panferov & Schultheis | 1:47:17 | [▶](https://www.youtube.com/watch?v=E0G3hf4DneA) |
| ★103 | **CuTe Layout Algebra and its Category-Theoretic Interpretation** | Carlisle & **Jay Shah** | 2:33:57 | [▶](https://www.youtube.com/watch?v=MVh_guNbWMA) |
| ★104 | Gluon and Linear Layouts | Bell, Zhou, Lezcano | 1:57:57 | [▶](https://www.youtube.com/watch?v=oYs_qtuk2Pg) |
| ★105 | cuDNN mxfp8 Attention | — | 1:00:18 | [▶](https://www.youtube.com/watch?v=HcnybHRbTcc) |
| ★106 | Hugging Face Kernels | de Kok & Holz (HF) | 1:28:19 | [▶](https://www.youtube.com/watch?v=Ok8vi6JemVQ) |
| 107 | PithTrain | Lai & Kang | 1:05:01 | [▶](https://www.youtube.com/watch?v=tBYm9PI5Jw0) |
| 108 | One Layer Deeper competition | — | 36:35 | [▶](https://www.youtube.com/watch?v=ustDJbxOu50) |
| 109 | TIRx | Bohan Hou | 38:45 | [▶](https://www.youtube.com/watch?v=nXRsasT1jIk) |
| ★110 | The 4-Bitter Lesson — NVFP4 RL stability | Ziang Li | 1:01:27 | [▶](https://www.youtube.com/watch?v=wiaUh82NEoE) |
| 111 | Spectral Compute — Compile CUDA Everywhere | Chris Kitching | 1:08:33 | [▶](https://www.youtube.com/watch?v=eujKd0lHegA) |
| ★112 | Production Megakernels for Real-World Inference | Joe Fioti | 58:05 | [▶](https://www.youtube.com/watch?v=loZ4xQ5RZuU) |
| ★113 | Near Speed-of-Light GPU Collectives | — | 52:53 | [▶](https://www.youtube.com/watch?v=TZnJYRTSGVk) |
| ★114 | **PyCuTe** | **Cris Cecka** with Saroufim | 1:44:03 | [▶](https://www.youtube.com/watch?v=_LmOPM5HnZ0) |
| 115 | Proving Kernels Correct Instead of Testing Them | Ben Koska | 40:07 | [▶](https://www.youtube.com/watch?v=7XsSd9mqay4) |
| 116 | GPU Kernel Formal Verification | Jubi Taneja | 30:35 | [▶](https://www.youtube.com/watch?v=WRAQYXBA_Qc) |

**The GPU MODE IRL 2024 keynotes are posted separately on the Accel channel and
are easy to miss:** **Wen-mei Hwu** (the PMPP author,
[▶](https://www.youtube.com/watch?v=-dJQnCPJ8VA)) · Andrej Karpathy
([▶](https://www.youtube.com/watch?v=aR6CzM0x-g0)) · Tri Dao
([▶](https://www.youtube.com/watch?v=_B6ZbRbxiMY)) · Tim Dettmers
([▶](https://www.youtube.com/watch?v=xV-cloHcTDE)) · Supriya Rao
([▶](https://www.youtube.com/watch?v=HVKE3Ye4xsM)) · Lily Liu, vLLM
([▶](https://www.youtube.com/watch?v=IqhJ5Eq8bgs)).

---

## E.4.4 Triton

**The key discovery: OpenAI maintains an official Triton channel**
([@Triton-openai](https://www.youtube.com/@Triton-openai)) carrying the full
Developer Conference archive for 2023, 2024 and 2025. It is authoritative, free,
and widely unknown.

**Philippe Tillet's own talks:** *Triton Today and Beyond* (2025, 51:59,
[▶](https://www.youtube.com/watch?v=FgesnWaMoZ4)) — the best current
state-of-the-project talk · *Keynote* (2024, 15:05,
[▶](https://www.youtube.com/watch?v=o3DrHb-mVLM)) · *The Triton Language*
(2021, 12:11, [▶](https://www.youtube.com/watch?v=G951lCm_qnk)) — the original
pitch for block-level programming · **_Maximizing Kernel Development
Productivity Under Performance Constraints_** (2024, 22:02,
[▶](https://www.youtube.com/watch?v=WnBG7je7tO4)) — his core thesis on where
Triton deliberately gives up control.

**Developer Conference 2025:** **Gluon — Tile-Based Programming with Low-Level
Control** ([▶](https://www.youtube.com/watch?v=KqeI23SpJx8)) · **Proton —
Portable Performance Profiling** ([▶](https://www.youtube.com/watch?v=PGUw2P55ZYM)) ·
TLX ([▶](https://www.youtube.com/watch?v=qRycGTCHuuY)) · **Blackwell guide**
([▶](https://www.youtube.com/watch?v=GL7ImGZj-Oc)) · Triton on AMD
([▶](https://www.youtube.com/watch?v=u7xJwEJVWdM)) · Triton-distributed
([▶](https://www.youtube.com/watch?v=ccMl2KLb-iY)) · Helion
([▶](https://www.youtube.com/watch?v=UDqg5WrgT6U)).

**Developer Conference 2024:** **Writing an MLIR Pass**
([▶](https://www.youtube.com/watch?v=etlFyqSsmL0)) · **Proton / Interpreter**
([▶](https://www.youtube.com/watch?v=Av1za_0o2Qs)) · **Pipelining Persistent
Kernels** ([▶](https://www.youtube.com/watch?v=PAsL680eWUw)) · Triton on
Blackwell ([▶](https://www.youtube.com/watch?v=RW2-HtWaOS0)) · Mosaic GPU
([▶](https://www.youtube.com/watch?v=tnADC2XuAr0)) · Exo
([▶](https://www.youtube.com/watch?v=l9OKpCP0Mnc)).

**Developer Conference 2023:** Hopper Support in Triton
([▶](https://www.youtube.com/watch?v=KMRl-SBbTDk)) — how WGMMA and TMA first
entered the compiler · Grouped GEMMs
([▶](https://www.youtube.com/watch?v=_rrhYbvNIx0)) · PyTorch 2.0 and
TorchInductor ([▶](https://www.youtube.com/watch?v=p13HpZv2S3Q)) · Pallas
([▶](https://www.youtube.com/watch?v=OR8NZyTz-yo)).

**The compiler panel** — Tillet, Ansel, Pienaar (MLIR), Tianqi Chen (TVM),
Zolotukhin and Peng Wu arguing about IR design and autotuning, 35:31,
[▶](https://www.youtube.com/watch?v=YWDzHGx8PrY) — is excellent seminar material.

**Paper:** Tillet, Kung & Cox, *Triton: An Intermediate Language and Compiler
for Tiled Neural Network Computations*, MAPL 2019.

---

## E.4.5 CUTLASS and CuTe

**Cris Cecka — the CuTe architect — has two full-length free lectures**, which
is unusual and valuable.

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **CuTe** | **Cris Cecka** (NVIDIA) | 1:24:33 | [▶](https://www.youtube.com/watch?v=vzUhbDO_0qk) |
| **PyCuTe** | Cris Cecka with Saroufim | 1:44:03 | [▶](https://www.youtube.com/watch?v=_LmOPM5HnZ0) |
| **CuTe Layout Algebra and its Category-Theoretic Interpretation** | Carlisle & Jay Shah | 2:33:57 | [▶](https://www.youtube.com/watch?v=MVh_guNbWMA) |
| **CUTLASS and FlashAttention 3** | Jay Shah (Colfax, FA3 co-author) | 1:49:16 | [▶](https://www.youtube.com/watch?v=JwUcZwPOCpA) |
| **Tensor Cores** (MMA atoms) | Thakkar & Ramani (NVIDIA) | 1:47:50 | [▶](https://www.youtube.com/watch?v=hQ9GPnV0-50) |
| CUTLASS (introduction) | Eric Auld | 1:34:24 | [▶](https://www.youtube.com/watch?v=G6q719ck7ww) |
| Getting Started with CuTe DSL | Vicki Wang (NVIDIA) | 1:13:19 | [▶](https://www.youtube.com/watch?v=9-dfte_N3yk) |
| How FlashAttention 4 Works | Charles Frye (Modal) | 1:15:09 | [▶](https://www.youtube.com/watch?v=VPslgC9piIw) |
| **Zero to Hero: Programming Hopper Tensor Core with MLIR's NVGPU Dialect** | Guray Ozen (NVIDIA) | 42:26 | [▶](https://www.youtube.com/watch?v=V3Q9IjsgXvA) |
| CUTLASS Python DSL Infrastructure (LLVM Dev Meeting) | Guray Ozen (NVIDIA) | 22:14 | [▶](https://www.youtube.com/watch?v=5NXd6MbKYNQ) |

**Ozen's EuroLLVM talk is the best free single source on TMA, warpgroup MMA and
mbarrier** — the three Hopper primitives that everything fast on that
architecture depends on.

**Paper:** Shah, Bikshandi, Zhang, Thakkar, Ramani & Dao, *FlashAttention-3*,
arXiv:2407.08608. Colfax's written tutorials at `research.colfax-intl.com/blog`
are the real substitute for their missing video channel.

---

## E.4.6 Profiling — finding the actual bottleneck

**Roofline, in the right order:** the FAU 18-minute derivation
([▶](https://www.youtube.com/watch?v=IrkNZG8MJ64)) → **Pennycook, Yang and
Deslippe on performance portability and empirical ceilings** (1:07:12,
[▶](https://www.youtube.com/watch?v=ATfDVKBU65k)) → **SOL analysis in Nsight
Compute** ([▶](https://www.youtube.com/watch?v=uHN5fpfu8As)) → Edward Yang's
LLM-era worked example ([▶](https://www.youtube.com/watch?v=5btb5qcUPbU)).

**The tool deep dives:** **GPU MODE Lecture 44** is the most complete free Nsight
treatment on YouTube at 2:07:16 ([▶](https://www.youtube.com/watch?v=F_BazucyCMw)) ·
Memory Analysis with Nsight Compute ([▶](https://www.youtube.com/watch?v=GCkdiHk6fUY)) ·
Profiling with NVTX ([▶](https://www.youtube.com/watch?v=SpZ5MYRQc0U)).

**Long-form from HPC centres:** **Introduction to Performance Analysis for NVIDIA
GPUs**, Dominik Ernst, NHR@FAU, 1:11:39
([▶](https://www.youtube.com/watch?v=27vRMM5JcSg)) · Kernel Performance Analysis
with Nsight Compute, ALCF ([▶](https://www.youtube.com/watch?v=fsC3QeZHM1U)) ·
**HPCToolkit**, John Mellor-Crummey (Rice),
([▶](https://www.youtube.com/watch?v=pe0N7LqNg9w)).

> **The single most important talk here is the one about occupancy.**
> **James Demmel's SC19 Test of Time Award talk** (40:14,
> [▶](https://www.youtube.com/watch?v=RVpf2PR1PFE)), accepting for Volkov and
> Demmel's SC08 paper, explains the result that overturned a decade of advice:
> **lower occupancy with more instruction-level parallelism beat the universal
> "maximize occupancy" rule.** If you have ever tuned a kernel by chasing
> occupancy numbers, watch this before you do it again.

**Also:** *PyTorch Unleashed*, Taylor Robie (PyTorch profiler core dev),
37:48 ([▶](https://www.youtube.com/watch?v=qRZrVNNe3gQ)) — reading real traces to
separate launch-bound from memory-bound from compute-bound.

---

## E.4.7 PyTorch internals and compilers

**Horace He's *Building ML Systems for a Trillion Trillion Floating Point
Operations*** (Jane Street, 2024, 1:03:21,
[▶](https://www.youtube.com/watch?v=139UPjoq7Kw)) **is the one talk to watch in
this subsection.** Compute-bound, memory-bound and overhead-bound as three
distinct regimes with three different fixes — the diagnostic framework that
makes everything else actionable.

**Also by He:** *Accelerating Generative AI*
([▶](https://www.youtube.com/watch?v=IWpM_9AsC-U)) · **FlexAttention**
([▶](https://www.youtube.com/watch?v=ju-KlcuWlbk)) · GPT-Fast
([▶](https://www.youtube.com/watch?v=18YupYsH5vY)).

**Edward Yang:** **torchdynamo deep dive** (1:35:59,
[▶](https://www.youtube.com/watch?v=egZB5Uxki0I)) · *torch.compile: The Missing
Manual* ([▶](https://www.youtube.com/watch?v=rew5CSUaIXg)) · symbolic shapes
([▶](https://www.youtube.com/watch?v=pLni96jtcjY)) · **a real debugging session
inside the CUDA caching allocator's private mempool** (46:37,
[▶](https://www.youtube.com/watch?v=gr487xsMpO8)) — almost nothing else free
covers allocator internals at that level.

**Jason Ansel:** **PyTorch 2 — Faster ML Through Dynamic Python Bytecode
Transformation and Graph Compilation** (Allen School, 1:01:17,
[▶](https://www.youtube.com/watch?v=WxYEoTLgdLo)) — the full ASPLOS 2024 paper
talk; anchor the module on it.

**Compiler internals:** Deep Dive on TorchDynamo
([▶](https://www.youtube.com/watch?v=5FNHwPIyHr8)) · **Inside torch.compile
Guards: How They Work, What They Cost**
([▶](https://www.youtube.com/watch?v=GmhnYe9QQoM)) · **CUTLASS backend for
Inductor** ([▶](https://www.youtube.com/watch?v=2dY8vPQ349Q)) · **CUDAGraph in a
Partial Graph World** ([▶](https://www.youtube.com/watch?v=Lg8F4F_qZxk)).

**Paper:** Ansel et al., *PyTorch 2*, ASPLOS 2024.

---

## E.4.8 Numerics and determinism

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Numerics and AI** | **Paulius Micikevicius** (NVIDIA) | 2:39:09 | [▶](https://www.youtube.com/watch?v=ua2NhlenIKo) |
| **Deep Learning Determinism** | Duncan Riach (NVIDIA) | 37:38 | [▶](https://www.youtube.com/watch?v=TB07_mUMt0U) |
| Reproducible C++ Floating-Point Reductions in CUB | Shreyas Atre | 5:25 | [▶](https://www.youtube.com/watch?v=wUiBh646hEI) |
| **Numerical Stability at Extreme Scale and Low Precisions** (ICM 2022) | **Nicholas Higham** (Manchester) | 44:30 | [▶](https://www.youtube.com/watch?v=L_lgdbYSGxY) |
| The Rise of Multiprecision Computations | Nicholas Higham | 49:52 | [▶](https://www.youtube.com/watch?v=SnUKb_w5r9s) |
| **DGEMM on Integer Tensor Cores** (the Ozaki scheme) | NHR@FAU | 35:15 | [▶](https://www.youtube.com/watch?v=ouK0gwYOA_Y) |
| AMP Training in PyTorch | NVIDIA | 19:18 | [▶](https://www.youtube.com/watch?v=b5dAmcBKxHg) |

**Micikevicius's *Numerics and AI* is the flagship of this subsection.** The
author of *Mixed Precision Training* and *FP8 Formats* giving two hours and forty
minutes on FP16, BF16, FP8, MX scaling, loss scaling, and where low precision
breaks. **It is the free long-form replacement for his gated GTC sessions, and
it is better than any of them because of its length.**

**Riach's determinism talk is the one that matters for science.** Atomics and
non-deterministic reductions mean two runs of the same code give different
answers. For a published benchmark comparison, that is a correctness problem,
not a curiosity. **Derivation checkpoint 69 is this question applied to force
accumulation.**

**Papers:** Micikevicius et al., *Mixed Precision Training*, arXiv:1710.03740 ·
*FP8 Formats for Deep Learning*, arXiv:2209.05433 · the OCP Microscaling Formats
Specification v1.0 · Kumar et al., *Scaling Laws for Precision*, arXiv:2411.04330.

---

## E.4.9 Multi-GPU and collectives

The entries that matter for a small fleet, in order: **NCCL and NVSHMEM**, Jeff
Hammond (NVIDIA), 1:40:43 ([▶](https://www.youtube.com/watch?v=zxGVvMN6WaM)) ·
**GPU Collective Communication**, Dan Johnson, 59:43
([▶](https://www.youtube.com/watch?v=T22e3fgit-A)) · **Landscape of GPU-Centric
Communication**, Didem Unat, 1:00:07
([▶](https://www.youtube.com/watch?v=beuOWBbiJfQ)) · **Multi-GPU Programming**,
Markus Hrywniak (NVIDIA), 1:15:23
([▶](https://www.youtube.com/watch?v=BgeFR4UfajQ)) · NCCL from its author,
Sylvain Jeaugey, 41:06 ([▶](https://www.youtube.com/watch?v=BHqoXoRuH-I)) ·
**HOTI keynote on accelerator clusters**, Bill Dally, 57:05
([▶](https://www.youtube.com/watch?v=napEsaJ5hMU)) — bandwidth tapering and
collective cost models, which is why NVLink and NVSwitch exist.

---

## E.4.10 Honest gaps

**The largest is structural: NVIDIA does not publish its deep GTC sessions to
YouTube.** Stephen Jones's *How GPU Computing Works* and *How CUDA Programming
Works* exist there only as third-party re-uploads. The same applies to
Micikevicius's mixed-precision sessions and the full CUTLASS deep-dives. NVIDIA
On-Demand is free but requires registration, and that is where the canonical
versions live.

**The OLCF CUDA Training Series is not on YouTube at all** — Oak Ridge publishes
to Vimeo. Slides and exercises are free at `github.com/olcf/cuda-training-series`.

**No Vasily Volkov talk exists.** *Better Performance at Lower Occupancy* was
never recorded; the Demmel Test-of-Time retrospective is the honest substitute.
Pair it with Volkov's 2016 Berkeley thesis, *Understanding Latency Hiding on
GPUs*.

**Paulius Micikevicius has no YouTube GTC session either**, despite writing both
canonical numerics papers. **GPU MODE Lecture 84, at two hours forty, is the free
substitute and is better for being unhurried.**

**There is no talk on batch-invariant determinism in LLM inference.** Every
search result was AI-generated explainer content. The Thinking Machines blog post
is the primary source; Lecture 84 and the Riach talk carry the rigorous version.

**No dedicated PyTorch caching-allocator talk exists.** Allocator internals
appear only incidentally, inside Edward Yang's refcount-bug session and Elias
Ellison's CUDA-graph talk. Zachary DeVito's *Understanding GPU Memory* posts on
pytorch.org remain the authoritative source.

**No Samuel Williams roofline lecture is recorded**, and **no William Kahan
video** exists — his floating-point lectures circulate as PDFs and audio only.
**Colfax Research's YouTube channel is empty**; their written tutorials are the
resource.

> **A methodological warning worth repeating, because it will cost you a day.**
> Sustained `yt-dlp` metadata fetches start failing wholesale under
> rate-limiting, and those failures look exactly like dead videos. When a batch
> comes back all-failed, re-check the same IDs through oEmbed before dropping
> anything.

---

## E.4.11 Paired reading — E.4

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Spector, *Notes on AI Hardware*** | Any roofline tutorial | Compute arithmetic intensity for one kernel you own. |
| Hooker, *The Hardware Lottery* | Her paper | Which molecular methods won because of hardware rather than merit? |
| **PMPP L4–L7** | Hwu, Kirk & El Hajj, *PMPP*, ch. 4–6 | Occupancy, coalescing, bank conflicts: audit one kernel against all three. |
| **PMPP supplementary GEMM lecture** | — | Re-derive the optimization ladder from naive to competitive. |
| **GPU MODE L8, *CUDA Performance Checklist*** | — | Run the checklist on a real kernel. |
| **GPU MODE L18, *Fusing Kernels*** | FlashAttention, arXiv:2205.14135 | What memory traffic does fusion eliminate? |
| **Giroux, *std::atomic in CUDA*** | CUDA memory-model docs | What is a scope, and when does forward progress fail? |
| **Demmel, SC19 Test of Time** | Volkov & Demmel, SC08 | Occupancy is not the objective. What is? |
| **He, *Trillion Trillion FLOPs*** | — | Classify your bottleneck: compute, memory, or overhead? |
| Yang, *torchdynamo deep dive* | **Ansel et al., ASPLOS 2024** | What does a guard cost, and when does it recompile? |
| **Cecka, *CuTe*** | CuTe docs `00_quickstart`–`0t_mma_atom` | What is a layout, algebraically? |
| **Shah, *CUTLASS and FA3*** | **arXiv:2407.08608** | Warp specialization and async pipelining. What is overlapped? |
| **Micikevicius, *Numerics and AI*** | arXiv:1710.03740; arXiv:2209.05433 | Where does FP8 break, and what does loss scaling fix? |
| **Riach, *Deep Learning Determinism*** | — | Are your benchmark numbers reproducible bitwise? Test it. |
| Dally, *HOTI accelerator clusters* | — | At what message size does your interconnect stop being free? |
