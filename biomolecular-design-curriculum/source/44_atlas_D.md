# Atlas D — Enhanced Sampling

> **Problem.** The event you care about takes a millisecond. Your simulation
> reaches a microsecond. Buy the three orders of magnitude without lying about
> the ensemble.
>
> Every method here is a trade: you distort the sampling, then correct for the
> distortion. **The correction is the method.** When you read a talk in this
> family, the question is always *what exactly is being reweighted, and is the
> reweighting unbiased?*

---

## D.1 The taxonomy — learn this before any individual method

Enhanced sampling splits cleanly in two, and conflating them is the most common
error in the field:

**Collective-variable methods** bias along a chosen low-dimensional coordinate —
umbrella sampling, metadynamics, OPES, adaptive biasing force, steered MD. They
are powerful and they are only as good as the CV. **If your CV misses the slow
degree of freedom, the method converges confidently to the wrong answer**, and
nothing in the output warns you.

**CV-free methods** avoid choosing — replica exchange, simulated tempering,
weighted ensemble, Markov state models built from many short runs, transition
path sampling. They pay for it in cost or in complexity.

> **Derivation checkpoint 21.** Write down, for each of umbrella sampling,
> metadynamics, replica exchange and weighted ensemble, (a) what distribution is
> actually sampled, (b) the exact reweighting that recovers the Boltzmann
> distribution, and (c) the condition under which that reweighting fails. If you
> can do this for all four, you understand this family.

---

## D.2 Collective-variable methods

| Method | Talk / resource | Speaker / host | Link |
|---|---|---|---|
| Umbrella sampling, WHAM | Alchemistry and CECAM free-energy schools | — | → Atlas E |
| **Metadynamics** | PLUMED Masterclass 21.4 — **all 43 sessions in Appendix B.3** | PLUMED consortium | [▶](https://www.plumed.org/masterclass) |
| Metadynamics theory | Bussi / Laio / Parrinello lecture recordings | CECAM | [cecam.org](https://www.cecam.org) |
| **OPES** (On-the-fly Probability Enhanced Sampling) | PLUMED Masterclass 22.3 (Appendix B.3) | Michele Invernizzi | [▶](https://www.plumed.org/masterclass) |
| Adaptive biasing force | NAMD / Chipot tutorials | Chipot lab | — |
| **ML collective variables** | Accelerate Atomistic Simulations, Sampling, and Dynamics | **Pratyush Tiwary** (ML4DD Day 2) | [▶](https://youtu.be/DKNeV0pOpiU) |
| ML collective variables | Boltzmann Weighted Ensembles | Tiwary (MLSB 2025) | [▶](https://youtu.be/S4K5A0M6EN0) |
| Differentiable sampling | Differentiable Simulations for Enhanced Sampling of Rare Events | Gómez-Bombarelli (Valence) | [▶](https://youtu.be/75q4tXyugYs) |
| Differentiable sampling | second session | Martin Šípka (Valence) | [▶](https://youtu.be/X0mlsm1jDig) |

**Papers:** Torrie & Valleau 1977, *J Comput Phys* 23:187 (umbrella sampling) ·
Kumar et al. 1992, *J Comput Chem* 13:1011 (WHAM) · **Laio & Parrinello 2002,
*PNAS* 99:12562 (metadynamics)** · Barducci et al. 2008, *PRL* 100:020603
(well-tempered metadynamics) · **Invernizzi & Parrinello 2020, *JPCL* 11:2731
(OPES)** · Darve et al. 2008, *JCP* 128:144120 (ABF) · **Tiwary & Berne 2016,
*PNAS* 113:2839 (SGOOP — learning the CV)** · Bonati et al. 2021, *PNAS*
118:e2113533118 (deep-LDA CVs) · Ribeiro et al. 2018, *JCP* 149:072301 (RAVE).

> **The PLUMED Masterclass — enumerated in full in Appendix B.3 — is the
> single best hands-on resource in this entire
> Atlas family and it is free.** Twenty-plus sessions, each with code, data and
> exercises, taught by the people who wrote the software. If you do nothing else
> in Atlas D, do Masterclasses 21.01 through 21.06 and 22.03.
>
> **A practical note from the field:** many conda PLUMED builds **do not include
> the OPES module**. If `opes_metad` is missing, you will need to build PLUMED
> from source against your MD engine. Budget half a day.

---

## D.3 Replica exchange and tempering

| Method | Resource | Link |
|---|---|---|
| Temperature REMD | GROMACS / CECAM REMD tutorials | → B.8 |
| Hamiltonian REMD, REST2 | PLUMED Masterclass 22.10 (Appendix B.3) | [▶](https://www.plumed.org/masterclass) |
| Solute tempering | REST2 tutorials | — |

**Papers:** **Sugita & Okamoto 1999, *Chem Phys Lett* 314:141 (REMD)** ·
Wang, Friesner & Berne 2011, *JPCB* 115:9431 (REST2) · Rosta & Hummer 2009,
*JCP* 131:165102 (**the paper showing REMD's efficiency gain is smaller than
usually claimed**) · Nymeyer 2008, *JCTC* 4:626.

> **Read Rosta & Hummer before you run REMD.** The naive argument — more replicas
> means faster barrier crossing — does not survive a careful analysis of round-trip
> times. REMD helps, but the scaling with system size is unfavorable because the
> number of replicas needed grows with the square root of the number of degrees of
> freedom. For a solvated protein, that is a lot of replicas.

---

## D.4 Path and trajectory-space methods

| Method | Talk | Speaker / host | Length | Link |
|---|---|---|---|---|
| **Weighted ensemble** | WESTPA 2015 workshop + Zuckerman's own talks — **Appendix B.9** | Zwier, Zuckerman, Chong | — | [▶](https://westpa.github.io) |
| Transition path sampling | CECAM rare-events schools | Bolhuis, Dellago | — | → B.8 |
| **Action-Minimization Meets Generative Modeling: Transition Path Sampling** | Sanjeev Raja (Valence) | 1:04:36 | [▶](https://youtu.be/YAWo8gKi7b4) |
| Diffusion Models on Sampling Rare Events | Chenru Duan (Valence) | 48:08 | [▶](https://youtu.be/7IJnosb0kNA) |
| Milestoning, forward flux | Elber / Allen lecture recordings | — | — |

**Papers:** **Huber & Kim 1996, *Biophys J* 70:97 (weighted ensemble, the
original)** · **Zuckerman & Chong 2017, *Annu Rev Biophys* 46:43 (the review
to read)** · Zwier et al. 2015, *JCTC* 11:800 (WESTPA) · Bolhuis et al. 2002,
*Annu Rev Phys Chem* 53:291 (TPS) · Allen et al. 2009, *J Phys Condens Matter*
21:463102 (forward flux) · Faradjian & Elber 2004, *JCP* 120:10880.

> **Weighted ensemble is Zuckerman's method and it is the most
> under-appreciated technique in this family.** It is *unbiased* — no reweighting
> approximation, no CV-dependent distortion of the ensemble — because it runs
> unmodified dynamics and only manipulates trajectory *weights* through splitting
> and merging. The cost is bookkeeping, and WESTPA does the bookkeeping.
>
> **Derivation checkpoint 22.** Show that weighted ensemble's resampling leaves
> the ensemble average of any observable unbiased. Then explain why this is a
> fundamentally different kind of guarantee than metadynamics' asymptotic
> convergence — and why that difference matters for a rate constant.

---

## D.5 Markov state models — many short runs instead of one long one

| Talk / resource | Speaker / host | Link |
|---|---|---|
| **PyEMMA workshops** — all 29 videos enumerated in **Appendix B.10** | Noé group | [▶](http://www.emma-project.org) |
| **MSMBuilder / Folding@home** | Pande / Bowman lineage | — |
| **Accelerating Cryptic Pocket Discovery With Deep Learning (PocketMiner)** | **Greg Bowman** (Valence) | [▶](https://youtu.be/hNdPrioGQ7k) |
| Cryptic Pocket Discovery Using AlphaFold and Markov State Modelling | Valence | [▶](https://youtu.be/nwNKpJVBzSo) |
| VAMPnets and deep MSMs | Noé group talks | — |

**Papers:** **Prinz et al. 2011, *JCP* 134:174105 (MSMs: the definitive
construction paper)** · Husic & Pande 2018, *JACS* 140:2386 (MSM review) ·
Bowman et al. 2009, *Methods* 49:197 · **Bowman & Geissler 2012, *PNAS*
109:11681 (equilibrium fluctuations reveal cryptic pockets)** · Mardt et al.
2018, *Nat Commun* 9:5 (VAMPnets) · Wu & Noé 2020, *J Nonlinear Sci* 30:23
(variational approach to Markov processes) · **Meller et al. 2023,
*Nat Commun* 14:1177 (PocketMiner)**.

> **Greg Bowman's thread, one of your ten, is here.** The MSM argument is that
> you do not need one long trajectory — you need many short ones that collectively
> visit the states and the transitions between them, plus an estimator that stitches
> them into a kinetic model. Folding@home is that argument at planetary scale.
>
> The payoff that matters for design: **cryptic pockets**. Bowman & Geissler
> showed that equilibrium fluctuations open binding sites invisible in the crystal
> structure. PocketMiner then learned to predict where those are without running
> the simulation — which is exactly the carry across cultures the whole curriculum
> is about: a physics-first result becoming a learning-first predictor.
>
> **Derivation checkpoint 23.** State the implied-timescale test and explain what
> it diagnoses. Then explain why a *lag time* is needed at all and what you lose by
> making it longer. Checkpoint 24: explain why an MSM's slowest timescale is a lower
> bound, not an estimate.

---

## D.6 The learned-sampler frontier

This is where Atlas D meets Part III, and it is the most active research area in
the whole physics-first culture.

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Designing Losses for Data-Free Training of Normalizing Flows on Boltzmann Distributions** | Valence | 1:07:25 | [▶](https://youtu.be/B8ftFTKZcCo) |
| **Rigid Body Flows for Sampling Molecular Crystal Structures** | Jonas Köhler (Valence) | 1:24:24 | [▶](https://youtu.be/TasdvyXGwGs) |
| **Timewarp: Transferable Acceleration of MD by Time-Coarsened Dynamics** | Klein & Foong (Valence) | 54:35 | [▶](https://youtu.be/fD_1V5HgGTQ) |
| Timewarp (extended) | Valence | 1:14:35 | [▶](https://youtu.be/4rtT-hE9Xqo) |
| **Scalable Emulation of Protein Equilibrium Ensembles (BioEmu)** | Valence | 1:17:02 | [▶](https://youtu.be/zaZAAWUISGE) |
| **AlphaFold Meets Flow Matching (AlphaFlow)** | Bowen Jing (Valence) | 56:30 | [▶](https://youtu.be/yDDXF6XJZck) |
| Consistent Sampling and Simulation: MD with Energy-Based Diffusion Models | Valence | 43:48 | [▶](https://youtu.be/PGqyagbXoyc) |
| PepFlow: Direct Conformational Sampling From Peptide Energy Landscapes | Abdin (Valence) | 55:42 | [▶](https://youtu.be/B__DMqLJpSY) |
| Converging Advances to Accelerate Molecular Simulation | **Max Welling** (Valence) | 1:14:04 | [▶](https://youtu.be/t7q_ZNrBghY) |

**Papers:** **Noé et al. 2019, *Science* 365:eaaw1147 (Boltzmann generators)
[landmark]** · Klein et al. 2023, NeurIPS (Timewarp) · **Lewis et al. 2025,
*Science* 389:eadv9817 (BioEmu)** · Jing et al. 2024, ICML (AlphaFlow) ·
Zheng et al. 2024, *Nat Mach Intell* 6:558 (DiG) · Köhler et al. 2020, ICML
(equivariant flows) · Midgley et al. 2023, ICLR (flow annealed importance
sampling bootstrap).

> **The question that decides this entire subsection.** A Boltzmann generator
> promises samples from the equilibrium distribution without dynamics. Does it
> deliver, or does it deliver samples that look like the training distribution?
>
> The honest answer in 2026: **for small systems with good training data, yes,
> with importance weights that can be checked. For a new protein with no
> simulation data, the guarantee degrades to "it generalizes as well as the
> training set covers."** That is a real advance and it is not the same claim.
>
> **Derivation checkpoint 25** asks you to write down the importance weight for
> a normalizing-flow sampler and identify exactly where the Boltzmann guarantee
> enters and where it can be lost. **Capstone IV** asks you to test it.

---

## D.7 BUILD — Atlas D

1. **Pick a system with a known slow transition** — a ligand unbinding, a loop
   flip, a side-chain rotamer switch with a real barrier.
2. **Sample it three ways:** long unbiased MD, metadynamics along a CV you
   choose, and either weighted ensemble or an MSM from many short runs.
3. **Compare the free energy profiles.** They will not agree. Find out why.
4. **Deliberately choose a bad CV** for the metadynamics run — one that misses
   the slow coordinate — and show what the output looks like. It will look
   converged. That is the lesson.
5. **Write the one page.** What would have told you the CV was wrong, using only
   the metadynamics output?

**Derivation checkpoints due: 21, 22, 23, 24, 25.**

---

## D.8 Paired reading — Atlas D

| Watch this | Then read this | Hold this question |
|---|---|---|
| PLUMED Masterclass 21.01–06 | **Laio & Parrinello 2002, *PNAS* 99:12562** | What exactly is deposited, and what is the converged bias? |
| PLUMED Masterclass 22.03 (OPES) | **Invernizzi & Parrinello 2020, *JPCL* 11:2731** | What does OPES fix about well-tempered metadynamics? |
| Tiwary, *ML collective variables* | **Tiwary & Berne 2016, *PNAS* 113:2839** | Learning a CV from data. What prevents it from learning a fast coordinate? |
| Gómez-Bombarelli, *Differentiable simulations* | The accompanying paper | Backprop through a simulation. Where does the gradient become useless? |
| GROMACS REMD tutorial | **Sugita & Okamoto 1999** then **Rosta & Hummer 2009, *JCP* 131:165102** | How many replicas for your system? Is the gain worth it? |
| WESTPA tutorials | **Zuckerman & Chong 2017, *Annu Rev Biophys* 46:43** | Why is WE unbiased where metadynamics is asymptotic? |
| Raja, *Action minimization for TPS* | The paper + Bolhuis et al. 2002 | Paths, not states. What object is being sampled? |
| PyEMMA 2017 workshop (Appendix B.10) | **Prinz et al. 2011, *JCP* 134:174105** | Implied timescales. What does the plateau actually prove? |
| **Bowman, *PocketMiner*** | **Bowman & Geissler 2012, *PNAS* 109:11681** then **Meller et al. 2023, *Nat Commun* 14:1177** | A physics result became a learned predictor. What was kept and what was discarded? |
| Valence, *Boltzmann flows* | **Noé et al. 2019, *Science* 365:eaaw1147** | Write the importance weight. Where can the guarantee be lost? |
| Klein & Foong, *Timewarp* | Klein et al. 2023, NeurIPS | Learning the propagator rather than the distribution. What transfers? |
| Valence, *BioEmu* | **Lewis et al. 2025, *Science* 389:eadv9817** | Emulated equilibrium ensembles. What was the validation, and is it enough? |
| Jing, *AlphaFlow* | Jing et al. 2024, ICML | AF2 as a generative prior over conformations. Is the output Boltzmann? |
| **Tiwary, *Boltzmann Weighted Ensembles*** | Compare to BioEmu and AlphaFlow | State the physics-first objection to all of D.6 in one sentence. |
