# Atlas B — Molecular Dynamics

> **Problem.** Integrate Newton's equations for a biomolecule in explicit solvent
> and get a trajectory you are willing to defend.
>
> The hardest part of MD is not running it. It is knowing what the trajectory
> means, and the honest answer for most published simulations is **less than the
> figures imply**. This family therefore spends as much space on convergence and
> error as it does on integrators.

---

## B.1 Foundations — the integrator, the thermostat, the box

| Course / talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Biophysical Chemistry 2016 — complete, 13 lectures (Appendix B.2)** | Erik Lindahl (KTH/Stockholm) | playlist | [▶](https://www.youtube.com/@eriklindahl/playlists) |
| Molecular Dynamics Simulation (lecture series) | Lindahl | ~50 min ea | [▶](https://www.youtube.com/@eriklindahl) |
| **Introduction to Molecular Dynamics** | Mark Tuckerman (CECAM / IAS) | ~1 hr | see B.8 |
| MD simulations of biomolecules — foundations | Alex MacKerell (CHARMM workshops) | ~1 hr | see B.8 |
| GROMACS tutorials, full playlist | Justin Lemkul | varies | [▶](http://www.mdtutorials.com/gmx/) |
| **Rosetta: Refining structures with minimization and Monte Carlo** | RosettaCommons | 39:13 | [▶](https://youtu.be/X_pLpIjEpas) |

**Required reading, in this order.** Frenkel & Smit, *Understanding Molecular
Simulation*, chapters 4 and 6 (the integrator and the thermostat); Tuckerman,
*Statistical Mechanics: Theory and Molecular Simulation*, chapter 3 (Liouville
operator, the symplectic property, why velocity Verlet is not an arbitrary
choice); Allen & Tildesley chapter 1.

> **Derivation checkpoint 7.** Derive velocity Verlet from the Trotter
> factorization of the Liouville propagator. Then explain, without hand-waving,
> why a symplectic integrator has bounded energy error over long times while a
> higher-order non-symplectic one drifts. Almost nobody who runs MD daily can do
> this, and it is the reason the field uses a second-order method in 2026.

**The thermostat trap.** Berendsen is not a thermostat — it does not sample the
canonical ensemble, and it famously produces the "flying ice cube." Nosé-Hoover
is canonical but not ergodic for a single harmonic oscillator, which is why
chains exist. Langevin is canonical and ergodic but changes the dynamics.
**Derivation checkpoint 8: write down which observables are safe under each
and why**, and then go and check what your own last three simulations used.

---

## B.2 Anton and the long-timescale program

| Talk | Speaker | Length | Link |
|---|---|---|---|
| **Millisecond-Scale Molecular Dynamics Simulations** | D. E. Shaw | ~60 min | search `"D. E. Shaw" Anton molecular dynamics lecture` |
| Biomolecular Simulation at Long Timescales | D. E. Shaw Research | varies | [▶](https://www.deshawresearch.com/publications.html) |
| **Large-scale conformational transition in a membrane transporter** | Trebesch / Fakharzadeh, Tajkhorshid lab (Broad MIA) | 1:34:25 | [▶](https://youtu.be/wT_fjRATbVY) |

**Papers, and read them as a sequence:** **Shaw et al. 2010, *Science* 330:341
(Anton, atomic-level characterization of folding)** · **Lindorff-Larsen et al.
2011, *Science* 334:517 (How fast-folding proteins fold)** · Shaw et al. 2014,
SC'14 (Anton 2) · Shaw et al. 2021 (Anton 3) · Dror et al. 2012,
*Annu Rev Biophys* 41:429 (biomolecular simulation review).

> **What Anton actually proved.** Not that proteins fold — we knew that. It
> proved that *a force field extrapolated far beyond its fitting data stays
> approximately right*, which nobody had the right to expect. The 2011 paper
> folded twelve proteins and got the right structures with the right relative
> rates. Read the supplement: the places where it failed are the places where the
> force field's limitations show, and those are still the limitations today.
>
> Then ask the question the paper does not: **if a special-purpose machine is the
> answer to timescale, why did the field spend the next decade building learned
> surrogates instead?** The answer involves cost, access, and the fact that one
> millisecond of one protein is not a research program. That tension is the
> subject of Atlas D and of Capstone IV.

---

## B.3 Force fields in practice — and the parts that are wrong

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| Force field development and validation | MacKerell lab / CHARMM workshop | ~1 hr | see B.8 |
| **Benchmark and Critical Evaluation for ML Force Fields** | Xiang Fu (Valence) | 1:00:38 | [▶](https://youtu.be/M1ooYaWQfvQ) |
| **Improving Speed and Accuracy of NN Interatomic Potentials** | Valence | 54:24 | [▶](https://youtu.be/OOp2v9-stXo) |
| **MACE: Higher Order Equivariant Message Passing for Force Fields** | Valence | 1:22:55 | [▶](https://youtu.be/I9Y2le9e74A) |
| **Allegro: Local Equivariant Representations for Large-Scale Dynamics** | Musaelian (Harvard, Valence) | 1:09:17 | [▶](https://youtu.be/-mRl5Uk8IWk) |
| NequIP (earlier session) | Batzner & Musaelian | 1:26:43 | [▶](https://youtu.be/ZR1NTBPBDOo) |
| Learning QM Using Embedding, Symmetric Polynomials and Composition | **Gábor Csányi** (Valence) | 38:34 | [▶](https://youtu.be/2LQlPY7zyPM) |
| Learning ML Interatomic Potentials | De Fabritiis (ML4DD) | 51:39 | [▶](https://youtu.be/4EfUus1qh9Q) |
| Orb-v3: atomistic simulation at scale | Duignan & Vandenhaute (Valence) | 1:13:35 | [▶](https://youtu.be/pRbvRl0_FyE) |
| **Transformers Discover Molecular Structure Without Graph Priors** | Kreiman (Berkeley, Valence) | 1:04:09 | [▶](https://youtu.be/k9IbNCKJc-c) |
| **Stability-Aware Boltzmann Estimator (StABlE) Training** | Sanjeev Raja (Valence) | 1:22:10 | [▶](https://youtu.be/hCVXXdJZJFo) |
| Scalable simulation of electrolytes with quantum chemical accuracy | Duignan (Valence) | 1:12:12 | [▶](https://youtu.be/5tmWF3bkK4Y) |
| **AquaGen: generative models at MD precision on thousands of atoms** | Valence | 1:16:27 | [▶](https://youtu.be/vQD7VcZxXLI) |

**Papers:** Best et al. 2012, *JCTC* 8:3257 (CHARMM36) · Huang et al. 2017,
*Nat Methods* 14:71 (**CHARMM36m — the IDP correction**) · Maier et al. 2015,
*JCTC* 11:3696 (ff14SB) · Tian et al. 2020, *JCTC* 16:528 (ff19SB) ·
Robustelli et al. 2018, *PNAS* 115:E4758 (**a99SB-*disp*, the honest IDP
comparison**) · **Batzner et al. 2022, *Nat Commun* 13:2453 (NequIP)** ·
Musaelian et al. 2023, *Nat Commun* 14:579 (Allegro) · **Batatia et al. 2022,
NeurIPS (MACE)** · Fu et al. 2023, TMLR (**the ML force field benchmark that
shows low force MAE does not imply stable simulation**).

> **The single most load-bearing fact in this subsection.** Fu et al. showed
> that ML potentials with excellent force errors produce *unstable* trajectories
> — they blow up, or they drift into unphysical configurations, on timescales
> long enough to matter. Force MAE is a proxy, and it is a bad one. StABlE
> training (Raja) is one attempt at a fix.
>
> **This is the cleanest generator of new methods in the Atlas.** The pattern —
> "the standard metric for this learned object is not the quantity you care
> about" — recurs in Atlas R (sequence recovery), Atlas M (docking RMSD without
> PoseBusters), Atlas Q (ProteinGym means over stratified splits) and Atlas P
> (pLDDT as a proxy for correctness). **Derivation checkpoint 9 asks you to state
> the general form of that failure.**

**In practice: the water model is a force field choice.** TIP3P is used
because CHARMM and AMBER were parameterized against it, not because it is
good — it has the wrong dielectric constant and the wrong diffusion coefficient.
TIP4P-Ew and OPC are better and change your results. If your system is an IDP or
has large solvent-exposed loops, this is not a detail.

---

## B.4 Running MD correctly — the practitioner layer

| Topic | Resource | Link |
|---|---|---|
| GROMACS complete tutorials | Justin Lemkul, 8 systems | [▶](http://www.mdtutorials.com/gmx/) |
| GROMACS performance tuning | GROMACS workshop talks (BioExcel) | [▶](https://www.youtube.com/@BioExcelCoE) |
| **BioExcel Building Blocks: interoperable simulation workflows** | RosettaCommons Workflows | [▶](https://youtu.be/vw55OE08x_0) |
| OpenMM | OpenMM workshop recordings | [▶](https://openmm.org) |
| MDAnalysis | MDAnalysis UGM talks | [▶](https://www.mdanalysis.org) |
| Setup and parameterization | CHARMM-GUI tutorials | [▶](https://www.charmm-gui.org) |

**The practitioner's checklist that papers never print.** Hydrogen mass
repartitioning buys you 1.7× at 4 fs — and silently breaks if your water model's
oxygen mass was repartitioned too. Periodic image artifacts in a rhombic
dodecahedron are not fixed by any ordering of `trjconv` flags when you have two
chains plus a ligand. `-pbc nojump` splits a receptor that crosses the boundary;
`-fit` re-images a bound peptide into the void. Every one of these has cost
someone a month.

> **BUILD, and do this before anything else in this family.** Take one of your
> own completed trajectories. Compute the density. If it is near 926 kg/m³
> instead of ~1028, your water was light — a repartitioned oxygen mass under
> HMR — and the trajectory is wrong. This exact failure has been found in
> production force field directories. **Checking is one `gmx energy` call.**

---

## B.5 Convergence, error bars, and what a trajectory does not tell you

**This is the most important subsection in Atlas B and the one most often
skipped.**

| Talk | Speaker / host | Length | Link |
|---|---|---|---|
| **Statistical analysis and error estimation in MD** | Michael Shirts (Alchemistry / CECAM) | ~1 hr | see B.8 |
| **Big Data for Protein Dynamics** | Hannah Wayment-Steele (MLSB 2025) | 33:47 | [▶](https://youtu.be/dBZSGeQl1Q4) |
| Systematic Analysis of Conformational Ensembles with PENSA | Vögele (Stanford, Valence) | 50:33 | [▶](https://youtu.be/HKOneHKZVuA) |
| **Boltzmann Weighted Ensembles** | **Pratyush Tiwary** (MLSB 2025) | 31:12 | [▶](https://youtu.be/S4K5A0M6EN0) |

**Papers:** **Grossfield & Zuckerman 2009, *Annu Rep Comput Chem* 5:23
(Quantifying uncertainty and sampling quality) [read this one twice]** ·
Chodera 2016, *JCTC* 12:1799 (automatic equilibration detection) ·
Zuckerman & Chong 2017, *Annu Rev Biophys* 46:43 (weighted ensemble) ·
Shirts & Chodera 2008, *JCP* 129:124105 (MBAR) · Flyvbjerg & Petersen 1989,
*JCP* 91:461 (block averaging) · Romo & Grossfield 2011, *JCTC* 7:2464.

> **Daniel Zuckerman's thread, which is one of your ten, runs straight through
> here.** His position, compressed: *RMSD plateauing is not convergence.* A
> trajectory can look flat for a microsecond and be stuck in one basin. The
> quantities that do diagnose sampling are block-averaged observables with
> honest error bars, multiple independent runs started from different seeds, and
> overlap measures between replicate ensembles.
>
> **Derivation checkpoint 10.** Take a trajectory you already own. Compute the
> statistical inefficiency and effective sample size of three observables: total
> energy, radius of gyration, and a specific side-chain dihedral. They will
> differ by orders of magnitude. Write down what that means for the error bar on
> any claim you have made from that trajectory.
>
> **Checkpoint 11.** Explain precisely why RMSF computed from a single
> trajectory is not an estimate of equilibrium fluctuation unless the trajectory
> is ergodic on the relevant timescale — and state the test that would tell you
> whether it is.

---

## B.6 Specialized regimes

| Regime | Talk / resource | Link |
|---|---|---|
| Membranes | CHARMM-GUI membrane builder tutorials; MARTINI workshops | [▶](http://cgmartini.nl) |
| Constant-pH MD | CECAM constant-pH workshops | see B.8 |
| QM/MM | **CECAM QM/MM school, ~8 hrs** | see Atlas A.3 |
| Polarizable force fields | AMOEBA / Drude workshop talks | see B.8 |
| Nucleic acids | OL15/OL21 parameterization talks (Šponer, Otyepka) | — |
| Enhanced-sampling MD | → **Atlas D** | — |
| Coarse-grained MD | → **Atlas F** | — |

**Papers for nucleic acids specifically**, because the Atlas is otherwise
protein-heavy and this is where DNA/RNA simulation lives: Zgarbová et al. 2011,
*JCTC* 7:2886 (χOL3 for RNA) · Galindo-Murillo et al. 2016, *JCTC* 12:4114
(OL15 for DNA) · **Šponer et al. 2018, *Chem Rev* 118:4177 (RNA structural
dynamics — the honest review of what RNA force fields get wrong)**.

---

## B.7 BUILD — Atlas B

1. **Run the same system three times** with three different random seeds, 100 ns
   each. Not one run — three.
2. **Compute block-averaged error bars** on three observables across the
   replicates. Plot the error bar as a function of block size and find the
   plateau.
3. **Compute the overlap** between the three ensembles in a reduced space (PCA
   on backbone, or a few collective variables). Report it as a number.
4. **Write the one page.** Which of your observables converged in 100 ns, which
   did not, and what would it have taken? Put a number on the shortfall.

**Derivation checkpoints due: 7, 8, 9, 10, 11.**

---

## B.8 Where the workshop recordings live

Several resources above are workshop series rather than single videos. These
are the standing archives for this family:

| Archive | What it has | Link |
|---|---|---|
| **CECAM** | Schools on QM/MM, enhanced sampling, coarse-graining, free energy | [cecam.org](https://www.cecam.org) |
| **BioExcel CoE** | GROMACS, HADDOCK, PMX workshops and performance tuning | [▶](https://www.youtube.com/@BioExcelCoE) |
| **MolSSI** | Software-engineering-for-simulation schools | [molssi.org](https://molssi.org) |
| **Alchemistry / Chodera lab** | The 2018 free-energy workshop, 43 talks | → Atlas E |
| **PRACE / PATC** | HPC-for-simulation training | — |
| **Valence Labs** | The ML-potential talks listed in B.3 | [▶](https://www.youtube.com/@valence_labs) |

---

## B.9 Paired reading — Atlas B

| Watch this | Then read this | Hold this question |
|---|---|---|
| Lindahl, *Biophysical Chemistry* | Frenkel & Smit ch. 4, 6 | Derive velocity Verlet from Trotter. Why second order and not fourth? |
| Lindahl, thermostats | Tuckerman ch. 4 | Which thermostats sample the canonical ensemble, and which merely control T? |
| Shaw, *Millisecond MD* | **Shaw et al. 2010, *Science* 330:341** | Special-purpose silicon. What question did it make askable? |
| — | **Lindorff-Larsen et al. 2011, *Science* 334:517** | Read the supplement. Which proteins failed, and what does that say about the force field? |
| MacKerell, force fields | **Huang et al. 2017, *Nat Methods* 14:71 (CHARMM36m)** | What was wrong with CHARMM36 for IDPs, and how was it diagnosed? |
| — | **Robustelli et al. 2018, *PNAS* 115:E4758** | Four force fields on folded and disordered proteins. Who wins where? |
| Valence, *MACE* | **Batatia et al. 2022, NeurIPS** | Higher-order equivariant messages. What does body-order buy? |
| Musaelian, *Allegro* | **Batzner et al. 2022, *Nat Commun* 13:2453** | Strictly local versus message-passing. What scales, and what is lost? |
| **Fu, *ML force field benchmark*** | **Fu et al. 2023, TMLR** | Low force MAE, unstable simulation. Write the general form of this failure. |
| Raja, *StABlE training* | The StABlE paper | How do you train against a simulation observable rather than against forces? |
| Kreiman, *Transformers without graph priors* | The paper | If a transformer rediscovers the geometry, what was the inductive bias worth? |
| **Shirts, *Error estimation*** | **Grossfield & Zuckerman 2009, *Annu Rep Comput Chem* 5:23** | Compute statistical inefficiency for your own trajectory. |
| Tiwary, *Boltzmann weighted ensembles* | Zuckerman & Chong 2017, *Annu Rev Biophys* 46:43 | A sample is not a sample from the right distribution. How would you test? |
| Broad MIA, *Membrane transporter transition* | The accompanying paper | A large conformational change in explicit membrane. How was it sampled? |
