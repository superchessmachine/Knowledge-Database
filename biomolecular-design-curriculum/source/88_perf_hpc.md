# E.6 Simulation Engines and Scientific HPC

> **This is the section that pays off tomorrow.** You run GROMACS across a small
> multi-GPU fleet. The material below is why your ns/day is what it is, and what
> the handful of decisions are that actually move it.
>
> **One observation before the lists, and it is the most useful thing in this
> section.** The molecular dynamics community has a decade of *public performance
> culture* — the BioExcel webinar series runs from #2 in 2016 to #93 in 2026,
> almost all of it about making simulations faster, presented by the people who
> write the code. **The structure-prediction community has nothing equivalent.**
> That asymmetry is the subject of E.8.

---

## E.6.1 GROMACS internals and performance

| Talk | Speaker | Yr | Len | Link |
|---|---|---|---|---|
| **Peeking into the black box of GROMACS performance** | **Alekseenko & Páll** (KTH) | 2026 | 59:43 | [▶](https://www.youtube.com/watch?v=f2Ohpqb8GWw) |
| **Improvements in the GROMACS heterogeneous parallelization** | **Szilárd Páll** (KTH) | 2022 | 54:09 | [▶](https://www.youtube.com/watch?v=rTUz28f8p6g) |
| Performance Tuning and Optimization of GROMACS | Mark Abraham (KTH) | 2016 | 1:02:58 | [▶](https://www.youtube.com/watch?v=FypZty7245Y) |
| **Getting good performance in GROMACS** | **Berk Hess** (KTH) | 2022 | 17:41 | [▶](https://www.youtube.com/watch?v=RUqdzntAgMc) |
| GROMACS HPC usage best practices and Q&A | Berk Hess (KTH) | 2022 | 54:13 | [▶](https://www.youtube.com/watch?v=xrqOuZNNkfQ) |
| Creating Faster Molecular Dynamics Simulations | Alan Gray (NVIDIA) | 2020 | 1:03:50 | [▶](https://www.youtube.com/watch?v=_Fch4jzwL2U) |
| A deep dive into GROMACS on GPU | Alan Gray (NVIDIA) | 2021 | 25:45 | [▶](https://www.youtube.com/watch?v=_SVr8j2VLuo) |
| More bang for your buck — improved use of GPUs | BioExcel | 2019 | 52:33 | [▶](https://www.youtube.com/watch?v=krRCKMfTEdA) |
| Optimizing cluster and simulation setup for GROMACS | BioExcel | 2016 | 58:52 | [▶](https://www.youtube.com/watch?v=iaPZHzd1nzs) |
| **NB-LIB — a performance portable force/energy library** | Jordan (KTH) & Keller (CSCS) | 2021 | 53:15 | [▶](https://www.youtube.com/watch?v=43gRI03rRWY) |
| What's new in GROMACS 2025 | Berk Hess (KTH) | 2025 | 59:03 | [▶](https://www.youtube.com/watch?v=Bp2ah2Y-xFk) |
| **What's new in GROMACS 2026** | Hess, Müllender, Miletic | 2026 | 57:31 | [▶](https://www.youtube.com/watch?v=LUnOuUdTSwA) |
| GROMACS Features and Future | Paul Bauer (KTH) | 2020 | 38:30 | [▶](https://www.youtube.com/watch?v=z58twSvbLME) |
| A walk through .mdp parameter options | BioExcel | 2019 | 1:14:00 | [▶](https://www.youtube.com/watch?v=0JwSpuysCfc) |
| MDBenchmark — scaling studies made straightforward | BioExcel | 2018 | 51:47 | [▶](https://www.youtube.com/watch?v=HRwQPC1U9uU) |
| Could free energy calculations be faster? | Suriñach (Nostrum) | 2022 | 26:43 | [▶](https://www.youtube.com/watch?v=--ldPeGFcGc) |

> **Watch *Peeking into the black box* first, then Hess's seventeen minutes.**
> The first teaches you to read an `mdrun` log line by line and infer what the
> engine is doing with your hardware — whether you are PME-bound, bonded-bound or
> PCIe-bound. The second is the highest value-per-minute item in this entire
> Part: the handful of decisions that actually move ns/day, from the person who
> wrote the algorithms.

**Papers:** **Páll et al. 2020, *J Chem Phys* 153:134110 (heterogeneous
parallelization and the GPU-resident path)** · Páll et al. 2015, EASC, LNCS
8759:3 · **Páll & Hess 2013, *Comput Phys Commun* 184:2641 — the cluster pair
algorithm, which is the actual reason GROMACS is fast, and which has no talk at
all** · Abraham et al. 2015, *SoftwareX* 1–2:19.

---

## E.6.2 OpenMM, NAMD, LAMMPS

| Talk | Source | Yr | Len | Link |
|---|---|---|---|---|
| **Introduction to the OpenMM API** | Simbios / Stanford | 2013 | 44:21 | [▶](https://www.youtube.com/watch?v=Uf2IBTfpfms) |
| **Customizing Forces and Integrators with OpenMM** | Simbios / Stanford | 2013 | 23:14 | [▶](https://www.youtube.com/watch?v=6r3_2LjCzPg) |
| **Validation of OpenMM** | Simbios / Stanford | 2013 | 15:07 | [▶](https://www.youtube.com/watch?v=VIDmDKvgglg) |
| OpenMM (library overview) | SBGrid | 2017 | 31:05 | [▶](https://www.youtube.com/watch?v=diYrnpnDIME) |
| **NAMD and Charm++: What You Should Know** | HPC-AI Advisory Council | 2020 | 50:37 | [▶](https://www.youtube.com/watch?v=-hiCMAtX0Hc) |
| Experiences with Charm++ and NAMD on Summit | **Jim Phillips** (UIUC) | 2018 | 23:25 | [▶](https://www.youtube.com/watch?v=pv1zwx1cN7k) |
| **Improving NAMD Performance on Multi-GPU Platforms** | David Hardy (UIUC) | 2018 | 31:28 | [▶](https://www.youtube.com/watch?v=TIMHJWmKv4k) |
| Lessons from Scaling NAMD | Jim Phillips (UIUC) | 2014 | 29:10 | [▶](https://www.youtube.com/watch?v=PP-YHMXa8jU) |
| **NAMD on Heterogeneous Architectures** (the GPU-resident redesign) | Charm++ Workshop | 2020 | 33:00 | [▶](https://www.youtube.com/watch?v=IIoEORrDKPE) |
| Accelerating Discovery with NAMD 3 | CCPBioSim | 2024 | 1:07:51 | [▶](https://www.youtube.com/watch?v=4I6p63JUz_U) |
| Scaling MD on Aurora with NAMD (SYCL) | IXPUG | 2025 | 26:37 | [▶](https://www.youtube.com/watch?v=6KdaIHsNIhk) |
| **Optimizing GPU Performance: the Chain Benchmark in LAMMPS** | Stan Moore (Sandia) | 2023 | 44:10 | [▶](https://www.youtube.com/watch?v=jJTQ8-vjEb0) |
| Porting LAMMPS with Kokkos/SYCL to Aurora | IWOCL | 2024 | 19:50 | [▶](https://www.youtube.com/watch?v=U-CXwJd2Q0Q) |
| HOOMD-Blue v3.0 — a GPU-native MD engine | Joshua Anderson (Michigan) | 2022 | 31:44 | [▶](https://www.youtube.com/watch?v=HCushKe2hXs) |

**OpenMM's distinctive engineering idea is in talk #2**: `CustomNonbondedForce`
and `CustomIntegrator` compile user-supplied algebraic expressions into GPU
kernels at runtime. That is why OpenMM is the engine people extend. **Talk #3,
on validation, is the one nobody watches and everybody should** — it shows how
an MD engine is proven numerically correct, which is the question behind every
force field comparison in Atlas A.

> **Honest gap: there is no substantial free talk on the AMBER GPU
> implementation**, despite its influence. Only two-minute NVIDIA marketing
> clips exist. Read **Salomon-Ferrer, Götz, Poole, Le Grand & Walker 2013,
> *JCTC* 9:3878** instead — it defines the SPFP hybrid precision model, which is
> the most important numerics idea in GPU molecular dynamics.

---

## E.6.3 The algorithms that make MD fast

| Topic | Talk | Len | Link |
|---|---|---|---|
| GPU force-loop mapping | TCBG: NAMD — MD on GPU Clusters, Part 1 | 14:08 | [▶](https://www.youtube.com/watch?v=AWrEZvXN8cE) |
| Spatial decomposition | TCBG: MD on GPU Clusters, Part 4 | 14:08 | [▶](https://www.youtube.com/watch?v=QS3IdoOZVWc) |
| **PME on GPUs** | TCBG: GPU Particle-Grid Algorithms, Part 1 | 14:08 | [▶](https://www.youtube.com/watch?v=BJKwBnpq21s) |
| PME on GPUs | TCBG: Particle-Grid Algorithms, Part 2 | 14:08 | [▶](https://www.youtube.com/watch?v=8AW47mnIoWs) |
| Ewald derivation | Ewald / PME / PPPM / SPME | 21:25 | [▶](https://www.youtube.com/watch?v=SSmIMof0KvA) |
| **The PME scaling wall** | Periodic Coulomb Tree Method | 34:00 | [▶](https://www.youtube.com/watch?v=IGVgpicqQkM) |
| Constraints | SHAKE, RATTLE, LINCS, SETTLE | 12:11 | [▶](https://www.youtube.com/watch?v=N2Lf-U8aIgM) |
| **Hydrogen mass repartitioning** | HMR in GROMACS (hands-on) | 14:45 | [▶](https://www.youtube.com/watch?v=kLFv33vCajc) |
| Multiple timestepping | BioExcel #18: multiple timescales | 1:10:03 | [▶](https://www.youtube.com/watch?v=jfSZOHa-B3U) |
| **Load balancing** | Dynamic Load-Balancing for Particle Simulations | 53:54 | [▶](https://www.youtube.com/watch?v=J18ecB-LuJI) |

**The TCBG particle-grid lectures are the only place anyone explains charge
spreading and grid interpolation on GPUs at this level of detail** — the hard,
memory-scatter half of PME that every other treatment skips.

**Papers:** Essmann et al. 1995, *JCP* 103:8577 (smooth PME) · **Hess et al.
1997, *J Comput Chem* 18:1463 (LINCS)** and Hess 2008, *JCTC* 4:116 (P-LINCS) ·
Miyamoto & Kollman 1992, *J Comput Chem* 13:952 (SETTLE) · **Hopkins, Le Grand,
Walker & Roitberg 2015, *JCTC* 11:1864 (hydrogen mass repartitioning)**.

> **Derivation checkpoint 67 lives here.** GPU molecular dynamics uses cluster
> pair lists rather than per-atom Verlet neighbour lists, and the reason is about
> warps and memory coalescing rather than algorithmic complexity. It is the
> clearest example in this document of hardware dictating an algorithm — and the
> paper that explains it, Páll & Hess 2013, has no recorded talk.

---

## E.6.4 HPC fundamentals

**The NHR@FAU Parallel Programming series (Georg Hager and colleagues, Erlangen)
is the best free university-level treatment of this material anywhere.** The
lectures that matter for a GPU fleet:

| # | Lecture | Len | Link |
|---|---|---|---|
| 4 | Basic OpenMP | 51:14 | [▶](https://www.youtube.com/watch?v=1Txkbx-AcR0) |
| 6 | Advanced OpenMP and performance issues | 1:10:43 | [▶](https://www.youtube.com/watch?v=o_MLhGkaGq4) |
| **7** | **ccNUMA and wavefront parallelization** — first-touch, pinning | 59:07 | [▶](https://www.youtube.com/watch?v=3vuano-RhEc) |
| 8 | Introduction to MPI | 45:02 | [▶](https://www.youtube.com/watch?v=SCIYgBIm6LM) |
| 10 | Collective communication and distributed-memory architecture | 59:21 | [▶](https://www.youtube.com/watch?v=ryC-L3qF33k) |
| 11 | MPI datatypes, virtual topologies, performance pitfalls | 1:00:17 | [▶](https://www.youtube.com/watch?v=nNCDgAU76D0) |
| **13** | **Hybrid Programming with MPI and OpenMP** | 1:03:57 | [▶](https://www.youtube.com/watch?v=OHijtcMGm9I) |

**Lecture 13 is exactly what `gmx mdrun -ntmpi -ntomp` is doing**, and it
explains the tradeoff you are making whenever you choose those numbers. **Lecture
7 is why thread pinning is not optional** on a multi-socket node.

**The memory wall, stated properly:**

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **A very short intro to the Roofline model** | NHR@FAU | 18:37 | [▶](https://www.youtube.com/watch?v=IrkNZG8MJ64) |
| **Memory Bandwidth and System Balance in HPC Systems** | **John McCalpin** (TACC, author of STREAM) | 1:07:58 | [▶](https://www.youtube.com/watch?v=jkwD48mGOwQ) |
| **Main Memory Trends and Importance** | Onur Mutlu (ETH) | 29:22 | [▶](https://www.youtube.com/watch?v=YinsPbgr_mM) |
| Processing-in-Memory | Onur Mutlu (ETH) | 1:23:55 | [▶](https://www.youtube.com/watch?v=vJJaYIWtyTs) |
| **Accelerating Genome Analysis** — the memory wall on a biological workload | Onur Mutlu (ETH) | 2:12:22 | [▶](https://www.youtube.com/watch?v=8MsRlPnh0HU) |
| Optimizing your HPC applications with LIKWID | HPC.NRW | 1:15:54 | [▶](https://www.youtube.com/watch?v=xsAg-KOLYmM) |
| How to use likwid-pin | NHR@FAU | 16:56 | [▶](https://www.youtube.com/watch?v=PSJKNQaqwB0) |
| **Memory & Caches** | **Matt Godbolt** (Compiler Explorer) | 1:11:20 | [▶](https://www.youtube.com/watch?v=4_smHyqgDTU) |
| What Every Programmer Should Know about How CPUs Work | Matt Godbolt | 43:28 | [▶](https://www.youtube.com/watch?v=-HNpim5x-IE) |

**McCalpin's talk is the structural reason molecular dynamics is hard to speed
up**, by the person whose benchmark defines how we measure it. **Mutlu's genome
analysis lecture is included deliberately** — it is the memory-wall argument
worked through on a biological workload rather than on matrix multiply, and it
is where the innovation opportunity is most visible.

**Papers:** **Wulf & McKee 1995, *SIGARCH Comput Archit News* 23(1):20 (Hitting
the Memory Wall)** · **Williams, Waterman & Patterson 2009, *CACM* 52(4):65
(Roofline)**.

**Also from the national labs:** NUMA and SIMD optimization, NERSC
([▶](https://www.youtube.com/watch?v=E42g-_hD8GI)) · ATPESC MPI sessions by
Thakur, Raffenetti and Gropp
([▶](https://www.youtube.com/watch?v=1MxB4PT8wgE)) · **Beyond SMP — NUMA and GPU
Programming**, Tim Mattson ([▶](https://www.youtube.com/watch?v=IckwwgP8N1s)) ·
**How learning about GPUs actually made me good at computational science**, Max
Katz ([▶](https://www.youtube.com/watch?v=lCNawhPRGD4)) · **Mixed-precision
arithmetic: hardware, algorithms and analysis**, Theo Mary
([▶](https://www.youtube.com/watch?v=9ZnwfPvAlHM)).

---

## E.6.5 MIT 6.172 — Performance Engineering of Software Systems

**Charles Leiserson and Julian Shun, MIT. The twelve most relevant of 23
lectures.** The opening lecture alone — a 53,000× speedup on matrix multiply,
built step by step — establishes that most "fast" code leaves two orders of
magnitude on the table.

| # | Lecture | Len | Link |
|---|---|---|---|
| 1 | **Introduction and Matrix Multiplication** | 1:00:20 | [▶](https://www.youtube.com/watch?v=o7h_sYMk_oc) |
| 2 | Bentley Rules for Optimizing Work | 1:20:10 | [▶](https://www.youtube.com/watch?v=H-1-X9bkop8) |
| 4 | Assembly Language and Computer Architecture | 1:17:34 | [▶](https://www.youtube.com/watch?v=L1ung0wil9Y) |
| 5 | C to Assembly | 1:21:30 | [▶](https://www.youtube.com/watch?v=wt7a5BOztuM) |
| 6 | Multicore Programming | 1:16:46 | [▶](https://www.youtube.com/watch?v=dx98pqJvZVk) |
| 9 | **What Compilers Can and Cannot Do** | 1:18:46 | [▶](https://www.youtube.com/watch?v=ulJm7_aTiQM) |
| **10** | **Measurement and Timing** | 1:21:28 | [▶](https://www.youtube.com/watch?v=LvX3g45ynu8) |
| 14 | **Caching and Cache-Efficient Algorithms** | 1:18:23 | [▶](https://www.youtube.com/watch?v=xDKnMXtZKq8) |
| 15 | Cache-Oblivious Algorithms | 1:21:47 | [▶](https://www.youtube.com/watch?v=xwE568oVQ1Y) |
| 17 | Synchronization Without Locks | 1:20:10 | [▶](https://www.youtube.com/watch?v=5sZo3SrLrGA) |
| 21 | Tuning a TSP Algorithm (a complete worked optimization) | 1:20:52 | [▶](https://www.youtube.com/watch?v=SS5KfIFzfEE) |
| 22 | Graph Optimization (irregular access — neighbour lists in disguise) | 1:18:39 | [▶](https://www.youtube.com/watch?v=IT_4fw6gfJw) |

> **Lecture 10, *Measurement and Timing*, should be watched before you trust any
> ns/day comparison you have ever made** — including your own. Variance, clock
> sources, warm-up, statistical significance. Pair it with NHR@FAU's *Experiments
> and Data Presentation in HPC* ([▶](https://www.youtube.com/watch?v=y1n0IJZiPuw)).

**On library-level optimization:** **BLIS: A Framework for Rapidly Instantiating
BLAS Functionality** ([▶](https://www.youtube.com/watch?v=eb3dXivyTzE)) is the
clearest public explanation of the Goto/Van de Geijn blocked matrix-multiply
structure. **Kazushige Goto has no public recorded lecture**; the paper is
Goto & van de Geijn 2008, *ACM TOMS* 34:12.

**On performance portability:** **C++ Performance Portability — A Decade of
Lessons Learned**, Christian Trott (Sandia, Kokkos lead),
[▶](https://www.youtube.com/watch?v=jNGGKFkt4lA) · *Kokkos: Getting Lucky By
Design* ([▶](https://www.youtube.com/watch?v=y3HHBl4kV7g)) · the ATPESC Kokkos
tutorial ([▶](https://www.youtube.com/watch?v=6Ts6k2Nas5w)).

---

## E.6.6 Scientific software engineering and fleet operations

| Talk | Source | Len | Link |
|---|---|---|---|
| **Getting it Right: System Testing of Scientific Software** | IDEAS / ECP | 59:00 | [▶](https://www.youtube.com/watch?v=EsdZlKvgRQk) |
| Writing Clean Scientific Software | IDEAS | 1:01:47 | [▶](https://www.youtube.com/watch?v=Q6Ksu_uX3bc) |
| **Benchpark with Ramble — continuous benchmarking done properly** | LLNL | 2:34:02 | [▶](https://www.youtube.com/watch?v=AeaUfpybJfg) |
| **GROMACS: Testing and testing infrastructure** | BioExcel | 1:22:04 | [▶](https://www.youtube.com/watch?v=enU2Az-cQ98) |
| GROMACS: GitLab and version control | BioExcel | 47:16 | [▶](https://www.youtube.com/watch?v=ZFqZv0XNvnU) |
| GROMACS: Structures and interfaces | BioExcel | 1:34:37 | [▶](https://www.youtube.com/watch?v=y5DQ0NVrnv0) |
| Reproducible Research | CodeRefinery | 2:01:59 | [▶](https://www.youtube.com/watch?v=vSLxtsZrprE) |
| Automated Testing | CodeRefinery | 1:31:26 | [▶](https://www.youtube.com/watch?v=4jRsbPqNf1U) |

**The three GROMACS "Learn to Code" sessions are the entry point for Capstone
XI.** If you intend to contribute a speedup upstream, the testing-infrastructure
lecture is where you start — not the algorithm.

**Fleet operations:** Slurm 21.08 and Beyond, Tim Wickberg (SchedMD CTO,
[▶](https://www.youtube.com/watch?v=-0tD7gLTxiI)) · OCI containers and `scrun`
([▶](https://www.youtube.com/watch?v=7y7IpCTj5mk)) · **Container solutions for
HPC: Singularity/Apptainer** ([▶](https://www.youtube.com/watch?v=9015kJyMBcw)) ·
NERSC container training ([▶](https://www.youtube.com/watch?v=3ZkzAuHCSSo)) ·
**Flux Framework — hierarchical scheduling**, Tom Scogland (LLNL,
[▶](https://www.youtube.com/watch?v=mV_I7rK7y0E)) — nesting a scheduler inside
an allocation, which is the right model for keeping many GPUs busy with many
small jobs · **Spack** ([▶](https://www.youtube.com/watch?v=Uoi3-_xMPtk)).

> **Honest gap, and it is your exact situation: there is no video anywhere on
> running a small multi-GPU Linux fleet for molecular dynamics.** Everything
> public is either single-workstation tutorials or facility-scale operations at
> thousands of nodes. The nearest usable substitutes are the Slurm `gres.conf`
> documentation on cgroup-based GPU binding and the Flux talks above.

---

## E.6.7 Exascale, and what actually scaled

**Frontier — The World's First Exascale Supercomputer**, Bronson Messer (OLCF
Director of Science, [▶](https://www.youtube.com/watch?v=bTvm-yhiwYY)) ·
Frontier's Exascale Architecture, Scott Atchley (ORNL,
[▶](https://www.youtube.com/watch?v=9PPGvqvWW8s)) · **ECP Applications: Lessons
Learned**, Erik Draeger (LLNL, [▶](https://www.youtube.com/watch?v=O1dVhNqlO3Y))
— unusually candid about what failed to scale · ECP Software Technology, Mike
Heroux (Sandia, [▶](https://www.youtube.com/watch?v=akHo2hJAD1o)) ·
**Performance of Particle Applications on Early Exascale Hardware**
([▶](https://www.youtube.com/watch?v=wDwtEv3grdw)) — the most directly relevant
exascale session for an MD person · **Characterizing Performance Improvements in
ECP Projects** ([▶](https://www.youtube.com/watch?v=w6bo48SaINU)) — how a large
program defines and audits a speedup claim, which is methodology you can borrow.

---

## E.6.8 Honest gaps in this family

Three absences are surprising enough to name, and in all three the paper is the
only source.

**There is no talk on the AMBER GPU implementation**, despite `pmemd.cuda`
being one of the most consequential pieces of GPU scientific software ever
written. **There is no talk on the RELION GPU port** — note that Erik Lindahl is
an author on that paper, so the same engineering culture produced both GROMACS
and RELION-2's GPU support. And **there is no talk on SVE or Arm vectorization
of MD kernels**; the GROMACS SIMD abstraction layer is documented only in the
developer manual.

**Most tellingly, the single most important GROMACS performance paper — Páll and
Hess 2013 on the cluster pair algorithm, the actual reason GROMACS is fast —
has no accompanying talk in the public record.**

**Three channel-handle traps that will waste your time:** `@MolSSI` has no videos
tab (MolSSI's software-engineering training is written, at
`education.molssi.org`), and `@NERSC`, `@olcf` and `@ALCF` all belong to
unrelated accounts. **OLCF has no public YouTube training channel at all** —
Oak Ridge publishes to Vimeo.

---

## E.6.9 Paired reading — E.6

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Alekseenko & Páll, *Black box of GROMACS performance*** | Your own `md.log` | Are you PME-bound, bonded-bound or PCIe-bound? Find out. |
| **Hess, *Getting good performance*** | **Páll et al. 2020, *JCP* 153:134110** | Which three settings move ns/day most on your hardware? |
| Páll, *Heterogeneous parallelization* | Same paper | What did GPU-resident mode change about the CPU/GPU balance? |
| — | **Páll & Hess 2013, *CPC* 184:2641** | Why cluster pairs and not Verlet lists? (Checkpoint 67.) |
| TCBG, *Particle-Grid Algorithms* | **Essmann et al. 1995, *JCP* 103:8577** | Derive the PME communication cost. (Checkpoint 68.) |
| Simbios, *Customizing Forces in OpenMM* | **Eastman et al. 2017, *PLoS Comput Biol* 13:e1005659** | Runtime kernel compilation. What does that enable? |
| Simbios, *Validation of OpenMM* | — | How would you prove your own simulation is numerically correct? |
| Hardy, *NAMD on Multi-GPU* | **Phillips et al. 2020, *JCP* 153:044130** | As GPUs got faster, what became the bottleneck? |
| **NHR@FAU L7, *ccNUMA*** | — | Check thread pinning on your own nodes. Is first-touch respected? |
| **NHR@FAU L13, *MPI + OpenMP*** | — | What are you trading when you set `-ntmpi` and `-ntomp`? |
| **McCalpin, *Memory Bandwidth and System Balance*** | **Wulf & McKee 1995** | Compute bytes-per-flop for your machine. |
| **Mutlu, *Accelerating Genome Analysis*** | The accompanying papers | The memory wall on a biological workload. Where is the opportunity? |
| **MIT 6.172 L10, *Measurement and Timing*** | — | Re-run your last benchmark with error bars. Does the conclusion hold? |
| MIT 6.172 L14, *Caching* | — | Design a neighbour-list layout against the cache model. |
| **Trott, *Performance Portability*** | The Kokkos papers | One source, every accelerator. What does the abstraction cost? |
| LLNL, *Benchpark* | — | Set up one reproducible benchmark for your fleet. Track it. |
