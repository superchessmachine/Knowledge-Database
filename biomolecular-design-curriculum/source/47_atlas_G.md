# Atlas G — Continuum and Mesoscale

> **Problem.** The object is too big for atoms and too structured for a
> continuum average: cells, condensates, crowded cytoplasm, reaction-diffusion,
> hydrodynamics.
>
> **This family was a reading list in the second edition and that was a
> failure.** It is now filled. It remains the least familiar family to protein
> designers and therefore the most likely source of an idea nobody in your field
> has imported.

---

## G.1 Brownian and Langevin dynamics, and association kinetics

**An honest framing first.** The founding work here is from 1978 to 1984 and
predates video by decades. Ermak, McCammon, Northrup and Allison left no
lectures. What exists is the modern descendants, and they are good.

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Effects of crowding on binding and enzyme reaction rates** | **Gideon Schreiber** (Weizmann) | 1:06:51 | [▶](https://www.youtube.com/watch?v=Yqspuysc0IY) |
| Diffusional association and residence times | **Rebecca Wade** (HITS, author of SDA) | 32:25 | [▶](https://www.youtube.com/watch?v=xJIJM9fJ8FY) |
| **Protein Dynamics in Cellular Environments** | Rommie Amaro (UCSD) | 57:47 | [▶](https://www.youtube.com/watch?v=V_nwYl8c2-w) |
| **Generalized Langevin Equations from MD simulations** | Laura Scalfi (Sorbonne/FU Berlin) | 57:28 | [▶](https://www.youtube.com/watch?v=qZ-a3qmXMsk) |
| Life at Low Reynolds Number | Raymond Goldstein (Cambridge) | 15:03 | [▶](https://www.youtube.com/watch?v=gZk2bMaqs1E) |
| Batchelor Prize Lecture — low-Reynolds biological fluid dynamics | Raymond Goldstein | 48:55 | [▶](https://www.youtube.com/watch?v=Stuh73NlGKg) |

**Scheiber's talk is the one that matters for a designer.** He defined the
experimental side of protein-protein association kinetics, and this talk joins
crowding directly to *k*on. **Scalfi's derives the generalized Langevin equation
and memory kernel from atomistic trajectories** — the rigorous version of the
hand-wave that gets you from Newton to overdamped Langevin, and the direct
companion to derivation checkpoint 29.

**Papers:** **Ermak & McCammon 1978, *JCP* 69:1352** · Northrup, Allison &
McCammon 1984, *JCP* 80:1517 · **Schreiber, Haran & Zhou 2009, *Chem Rev*
109:839** · Huber & McCammon 2010, *Comput Phys Commun* 181:1896 (BrownDye) ·
Sharp, Fine & Honig 1987, *Science* 236:1460 (SOD electrostatic steering) ·
Zwanzig 1961, *Phys Rev* 124:983.

> **Why a designer should care.** Your binder's *k*on is a diffusion problem,
> not a structure problem, and electrostatic steering can buy two orders of
> magnitude. **Schreiber's review is the best document on this and the design
> literature barely cites it.** That is one of the twelve unexchanged ideas in
> the Atlas introduction.

---

## G.2 Reaction-diffusion and particle-based cell simulation

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **MCell: A 3D Monte Carlo Model of a Virtual Cell** | **Terry Sejnowski** (Salk) | 11:06 | [▶](https://www.youtube.com/watch?v=t8_fmm2gH3k) |
| How to build a synapse from molecules, membranes and Monte Carlo | Thomas Bartol (Salk) | 20:02 | [▶](https://www.youtube.com/watch?v=XRnXQkFEKe8) |
| Introduction to MCell4 | Salk CNL | 7:14 | [▶](https://www.youtube.com/watch?v=svOVC51dF3Q) |
| **MMBioS Cell Modeling Workshop, Day 1** | MMBioS (Pittsburgh/CMU/Salk) | 2:07:43 | [▶](https://www.youtube.com/watch?v=_YSAAmANRP0) |
| MMBioS Cell Modeling Workshop, Day 2 | MMBioS | 1:14:38 | [▶](https://www.youtube.com/watch?v=CosBPFoHFBM) |
| **Smoldyn inside VCell** | James Schaff (UConn Health) | 30:57 | [▶](https://www.youtube.com/watch?v=L7DS7_MdmVQ) |
| VCell tutorial | Ann Cowan (UConn Health) | 1:03:26 | [▶](https://www.youtube.com/watch?v=zo2I1ckPSC8) |
| **Multiscale and Multiphysics Modeling in VCell** | **Leslie Loew** (UConn Health) | 1:14:07 | [▶](https://www.youtube.com/watch?v=ji02ZnSsZMI) |
| Bridging Molecular to Cellular Scales | Leslie Loew | 1:00:26 | [▶](https://www.youtube.com/watch?v=DUhyPynSOas) |
| **Reaction Kinetics and Diffusion** — when diffusion limits a rate | Leslie Loew | 46:09 | [▶](https://www.youtube.com/watch?v=RKUNnwOz8AY) |
| Macromolecular Assembly (NERDSS) | Margaret Johnson (Johns Hopkins) | 1:03:30 | [▶](https://www.youtube.com/watch?v=Wt3FLkuMWLQ) |
| **The Gillespie Algorithm, by Gillespie** | **Daniel T. Gillespie** | 39:37 | [▶](https://www.youtube.com/watch?v=atOc2v8Wtcw) |
| Stochastic Chemical Kinetics 1 (chemical master equation) | MIT OCW | 53:57 | [▶](https://www.youtube.com/watch?v=42TkHA__6bk) |
| Stochastic Chemical Kinetics 2 (SSA and tau-leaping) | MIT OCW | 47:32 | [▶](https://www.youtube.com/watch?v=geVT3JYHeqI) |
| **Stochastic Simulation of Models in the Life Sciences** | Samuel Isaacson (BU) | 1:33:41 | [▶](https://www.youtube.com/watch?v=N3h0GWfc67k) |
| **Reaction-Diffusion Operator Splitting on Tetrahedral Meshes** | Erik De Schutter (OIST, STEPS) | 44:47 | [▶](https://www.youtube.com/watch?v=4nMG7GC5DV0) |
| Stochastic Simulations | Mendes & Slepchenko (UConn) | 56:00 | [▶](https://www.youtube.com/watch?v=7x5NQM5AohE) |
| COPASI tutorial | Pedro Mendes (UConn) | 1:04:38 | [▶](https://www.youtube.com/watch?v=8V10FAysb-o) |

**Gillespie explaining his own algorithm is a genuinely rare primary-source
recording.** **Isaacson's tutorial is the one to take seriously** — a
mathematician on the RDME and its convergence pathologies, which most biologists
using these codes have never confronted. **De Schutter's talk names the operator-
splitting error that silently corrupts mesh-based reaction-diffusion.**

**Papers:** **Gillespie 1977, *J Phys Chem* 81:2340** · Gillespie 2001, *JCP*
115:1716 (tau-leaping) · Andrews & Bray 2004, *Phys Biol* 1:137 (Smoldyn) ·
Kerr et al. 2008, *SIAM J Sci Comput* 30:3126 (MCell) · Isaacson 2009,
*SIAM J Appl Math* 70:77 · Hepburn et al. 2012, *BMC Syst Biol* 6:36 (STEPS).

> **Honest gaps: Steven Andrews has no Smoldyn lecture, and ReaDDy has none
> either.** The Schaff talk is the substitute for Smoldyn; for ReaDDy read
> Hoffmann, Fröhner & Noé 2019, *PLoS Comput Biol* 15:e1006830.

---

## G.3 Whole-cell modeling

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Whole cell simulation with Lattice Microbes, Part I** | **Zan Luthey-Schulten** (UIUC) | 1:11:19 | [▶](https://www.youtube.com/watch?v=rKRcPN9anHA) |
| Whole cell simulation with Lattice Microbes, Part II | Zan Luthey-Schulten | 1:19:11 | [▶](https://www.youtube.com/watch?v=ibn6Owow99M) |
| **Introduction to Simulations of Bacterial Cells** (best starting point) | Zan Luthey-Schulten | 1:11:36 | [▶](https://www.youtube.com/watch?v=DpvddDvQ6h0) |
| **4D simulations of a growing minimal bacterial cell** | Zan Luthey-Schulten | 1:02:23 | [▶](https://www.youtube.com/watch?v=NG3jPxN7QbQ) |
| 4D simulations of a growing and dividing cell | Zan Luthey-Schulten | 22:06 | [▶](https://www.youtube.com/watch?v=NpiSBhRyv9c) |
| Whole-cell modeling — a long-form interview | Luthey-Schulten with Wieczór | 1:24:04 | [▶](https://www.youtube.com/watch?v=5AR3TqgvgpA) |
| **How to build a computer model of a cell** | **Markus Covert** (Stanford) | 28:30 | [▶](https://www.youtube.com/watch?v=0Be21VwlgrQ) |
| A Computational Whole-Cell Model of *M. genitalium* (the original) | Markus Covert | 35:37 | [▶](https://www.youtube.com/watch?v=q5AeswdSe68) |
| Whole-Cell Modeling — a dialogue | Serrano (CRG) & Covert (Stanford) | 1:11:55 | [▶](https://www.youtube.com/watch?v=TeTSBRQiBAc) |
| Simulations of Ribosome Biogenesis at Whole-Cell Level | Tyler Earnest (UIUC) | 21:39 | [▶](https://www.youtube.com/watch?v=ettzIgmx354) |
| Multi-scale Simulations of Whole Yeast Cells | Tyler Earnest (UIUC) | 19:56 | [▶](https://www.youtube.com/watch?v=_-_X8fWBFH4) |
| **Integrative illustration and modeling of JCVI-syn3A** | **David Goodsell** (Scripps) | 22:56 | [▶](https://www.youtube.com/watch?v=cht9_0UyqXM) |
| MD of the JCVI-syn3A Cell Envelope | Mert Bozoflu (JCVI/UIUC) | 15:37 | [▶](https://www.youtube.com/watch?v=BIqN8Nm_1Qw) |
| **Simulating whole cells with Martini** — the coarse-grained route | BioExcel #84 | 1:01:50 | [▶](https://www.youtube.com/watch?v=fvFaPgSoM90) |

> **The Serrano–Covert dialogue is the honest one** — two whole-cell groups
> discussing where the approach has failed to scale. And the Martini webinar
> marks a genuine methodological fork: coarse-grained MD versus RDME as two
> incompatible routes to the same object.

**Papers:** **Thornburg et al. 2022, *Cell* 185:345 (a whole minimal cell)** ·
**Karr et al. 2012, *Cell* 150:389 (the first whole-cell model)** ·
Roberts, Stone & Luthey-Schulten 2013, *J Comput Chem* 34:245 (Lattice
Microbes) · Earnest et al. 2018, *Biophys J* 114:473 · Johnson et al. 2015,
*Nat Methods* 12:85 (cellPACK).

> **Capstone VI is built on the gap these talks expose.** Read Thornburg and
> ask what it would take to put a *designed* protein into that model. Enumerate
> every parameter it needs; mark which are computable today; quantify how wrong
> the computable ones are. Most of them you cannot compute at all.

---

## G.4 Crowding and the cytoplasm

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **CASP SIG on Modeling Conformational Ensembles** | Wodak (SickKids) & **Michael Feig** (Michigan State) | 59:16 | [▶](https://www.youtube.com/watch?v=mkzP80YoKwM) |
| Crowding effects on fibrillar self-assembly | Divya Nayar (IIT Delhi) | 27:46 | [▶](https://www.youtube.com/watch?v=ylIIHA7Ux-0) |
| **Measuring cytoplasmic crowding with GEMs** | **Liam Holt** (NYU Langone) | 1:17:37 | [▶](https://www.youtube.com/watch?v=WlKNDWtmU0c) |

**Holt's talk gives you the data any crowding simulation has to match**, which
is the right order to learn this in.

**Papers:** **Ellis 2001, *Trends Biochem Sci* 26:597** · **McGuffee & Elcock
2010, *PLoS Comput Biol* 6:e1000694 (atomistic cytoplasm)** · **Yu et al. 2016,
*eLife* 5:e19274 (100-million-atom *Mycoplasma* cytoplasm)** · Nawrocki et al.
2019, *PCCP* 21:876 · Delarue et al. 2018, *Cell* 174:338 (GEMs) ·
Minton 2006, *J Cell Sci* 119:2863.

> **Honest gap: Adrian Elcock has no recorded lecture, and neither does
> R. John Ellis.** The two people whose work defines this subject are absent
> from video entirely. **The design-relevant point stands regardless:** every
> affinity you compute is at infinite dilution and the cell is at 300 mg/mL.

---

## G.5 Condensates and phase separation

**The Dewpoint Kitchen Table Talk series is the richest single archive here**,
and Pappu's contribution is a genuine three-parter.

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **Pappu, Part 1 — polymer-physics foundations** | **Rohit Pappu** (WashU/JHU) | 1:07:09 | [▶](https://www.youtube.com/watch?v=GrVHXe4FtrQ) |
| **Pappu, Part 2 — stickers and spacers** | Rohit Pappu | 1:09:48 | [▶](https://www.youtube.com/watch?v=IDKVLxWAT3E) |
| **Pappu, Part 3 — material properties, aging, and what simulation cannot predict** | Rohit Pappu | 1:07:05 | [▶](https://www.youtube.com/watch?v=nRbpiM3MDR4) |
| Compact 20-minute version | Rohit Pappu | 20:11 | [▶](https://www.youtube.com/watch?v=KsGM4DvgW-0) |
| **Emergent properties of condensates** | **Tanja Mittag** (St. Jude) | 44:58 | [▶](https://www.youtube.com/watch?v=CBai9DWegAE) |
| **Liquid Phase Separation in Living Cells** | **Clifford Brangwynne** (Princeton) | 46:04 | [▶](https://www.youtube.com/watch?v=AP47mIkd-h0) |
| Multiphase Liquid Behavior of the Nucleus | Clifford Brangwynne | 38:08 | [▶](https://www.youtube.com/watch?v=HzG5_Q1whiI) |
| Using Light to Study and Control Phase Behavior (optoDroplets) | Clifford Brangwynne | 34:40 | [▶](https://www.youtube.com/watch?v=6k8m-7y7zkY) |
| MBL Friday Evening Lecture (the most complete) | Clifford Brangwynne | 1:20:21 | [▶](https://www.youtube.com/watch?v=DkhFiW5n7rQ) |
| **Cell organization by LLPS** | **Michael Rosen** (UTSW) | 1:00:13 | [▶](https://www.youtube.com/watch?v=Vezrj7FqMlY) |
| **Multiscale Dynamics of Charged Protein Condensates** | **Jeetain Mittal** (Texas A&M) | 29:59 | [▶](https://www.youtube.com/watch?v=-FCzirVHKC0) |
| **Simulations of Intrinsically Disordered Proteins** | **Robert Best** (NIH) | 1:01:07 | [▶](https://www.youtube.com/watch?v=jFmGNUUVHzg) |
| From disordered proteins to complexes and assemblies | Robert Best | 1:35:21 | [▶](https://www.youtube.com/watch?v=NxSeqlYiIU8) |
| **Conformational ensembles of IDRs (CALVADOS)** | **Kresten Lindorff-Larsen** (Copenhagen) | 1:02:59 | [▶](https://www.youtube.com/watch?v=_6iAcwmknek) |
| Driving forces in condensates from atomistic simulations | BioExcel #97 | 1:01:35 | [▶](https://www.youtube.com/watch?v=TvR3cUSHpn8) |
| Sequence-to-ensemble prediction | Alex Holehouse (WashU) | 1:28:52 | [▶](https://www.youtube.com/watch?v=ofse9Ku1GME) |
| Analytical statistical mechanics of condensates | Jeremy Schmit (Kansas State) | 1:10:35 | [▶](https://www.youtube.com/watch?v=lyDtfWAPMCA) |
| **Prediction of small-molecule partitioning into condensates** | Jerelle Joseph (Princeton) | 33:55 | [▶](https://www.youtube.com/watch?v=lgO7cRn0Qac) |
| Field-theoretic approaches to sequence-dependent phase separation | Hue Sun Chan (Toronto) | 29:08 | [▶](https://www.youtube.com/watch?v=Jf3e3M8TJR4) |
| Conformational entropy of IDPs in condensates | Ned Wingreen (Princeton) | 32:26 | [▶](https://www.youtube.com/watch?v=6oMOZa5JgpE) |
| Role of condensates in protein aggregation | Tuomas Knowles (Cambridge) | 45:40 | [▶](https://www.youtube.com/watch?v=1dTHn7ryMqs) |
| Condensates in stress responses and disease | Simon Alberti (TU Dresden) | 45:47 | [▶](https://www.youtube.com/watch?v=F6xa9Rr4DSQ) |
| **Active processes in condensates** | **Frank Jülicher** (MPI-PKS) | 30:36 | [▶](https://www.youtube.com/watch?v=9oDKpKhD-ts) |
| Continuum models for elastic phenomena around condensates | David Zwicker (MPI-DS) | 32:14 | [▶](https://www.youtube.com/watch?v=z8iN-AuEi7U) |
| LLPS in and out of equilibrium | **Alexander Grosberg** (NYU) | 1:03:01 | [▶](https://www.youtube.com/watch?v=OF5IOdanYFI) |
| Single-molecule dynamics inside coacervates | Ben Schuler (Zurich) | 41:10 | [▶](https://www.youtube.com/watch?v=FV36N7cDM1I) |
| Stress-induced mRNP condensation | Allan Drummond (Chicago) | 46:35 | [▶](https://www.youtube.com/watch?v=IrVn-plXvnk) |
| Condensates and Phase Separation in Biology, Session 1 | Sharp, Gladfelter, Kornberg | 1:40:01 | [▶](https://www.youtube.com/watch?v=jhhjfqnfcEU) |

**Joseph's talk is the most design-relevant one here**: can you predict whether
your compound enters a droplet? **Jülicher's is the physics that distinguishes a
living condensate from an oil drop** — non-equilibrium droplet theory.

**Papers:** **Banani et al. 2017, *Nat Rev Mol Cell Biol* 18:285** ·
**Dignon, Zheng, Kim, Best & Mittal 2018, *PLoS Comput Biol* 14:e1005941 (the
HPS coarse-grained model most LLPS simulation rests on)** · Martin et al. 2020,
*Science* 367:694 (stickers and spacers) · **Tesei et al. 2021, *PNAS*
118:e2111696118 (CALVADOS)** · Brangwynne et al. 2009, *Science* 324:1729 ·
Li et al. 2012, *Nature* 483:336 (multivalency) · Zwicker et al. 2017,
*Nat Phys* 13:408 · Lin, Forman-Kay & Chan 2016, *PRL* 117:178101.

---

## G.6 Continuum electrostatics and mesoscale hydrodynamics

**The `@ProteinElectrostatics` channel is a dedicated seminar series and is
effectively the only sustained video resource on Poisson-Boltzmann anywhere.**

| Talk | Speaker | Len | Link |
|---|---|---|---|
| **The Multi-Faceted Roles of Electrostatics in Biomolecular Simulation** | Walter Rocchia (IIT) | 1:01:08 | [▶](https://www.youtube.com/watch?v=va25fb1uDbM) |
| **Modeling electrostatics and polarization in biomolecules** | **Ray Luo** (UC Irvine, Amber PB solver) | 52:11 | [▶](https://www.youtube.com/watch?v=6Frl-o5jNDY) |
| **Where the PB picture of ion atmospheres fails** | António Baptista (ITQB) | 1:06:40 | [▶](https://www.youtube.com/watch?v=-3TF-uyYEP8) |
| Boundary-element PB (PyGBe) | Christopher Cooper (UTFSM) | 32:05 | [▶](https://www.youtube.com/watch?v=DZx8_HUUUCs) |
| **CECAM workshop on Advances in Electrostatics** | Christopher Cooper | 1:08:55 | [▶](https://www.youtube.com/watch?v=MMQEwnYN8Oo) |
| Treecode-accelerated PB solvers | Weihua Geng (SMU) | 42:07 | [▶](https://www.youtube.com/watch?v=zUQNmp1zU0o) |
| **Beyond PB into Poisson-Nernst-Planck** | Robert Krasny (Michigan) | 50:07 | [▶](https://www.youtube.com/watch?v=WcUcwqQQJhs) |
| ddCOSMO / ddPCM domain decomposition | Michele Nottoli (Stuttgart) | 46:27 | [▶](https://www.youtube.com/watch?v=birZ-K7oDSI) |
| **Solvation Models: Continuum (Implicit) Solvent Electrostatics** | **Christopher Cramer** (Minnesota) | 23:10 | [▶](https://www.youtube.com/watch?v=tB4xZLUGJqM) |
| Using 3D structure to predict interactions | **Barry Honig** (Columbia) | 40:57 | [▶](https://www.youtube.com/watch?v=auUTXW7KbgQ) |

**Mesoscale and hydrodynamics:** **DL_MESO** — DPD and lattice Boltzmann in one
framework, taught to a biosimulation audience, Michael Seaton (STFC), 1:15:05
([▶](https://www.youtube.com/watch?v=c90TPnu2ewA)) · Lattice Boltzmann for
biomedical flow ([▶](https://www.youtube.com/watch?v=OsNi6p8LY18)) ·
**Sauro Succi, *Boltzmann and The Lattice*** — the conceptual foundation by the
person who wrote the book ([▶](https://www.youtube.com/watch?v=RFWvXFW6FuY)) ·
Mesoscale modeling of soft matter with DPD
([▶](https://www.youtube.com/watch?v=6v4rlYo4MKk)) · **DPD simulation of red
blood cells**, Bruce Caswell (Brown)
([▶](https://www.youtube.com/watch?v=gpdImhQJIOQ)) · **Stokesian Dynamics**,
Rishabh More (Stanford) ([▶](https://www.youtube.com/watch?v=6YNoMx4HfTc)) ·
**Modeling Complex and Active Fluids**, Michael Shelley (Flatiron CCB), 1:33:39
([▶](https://www.youtube.com/watch?v=iNXrnjnJvDY)).

**Papers:** **Baker et al. 2001, *PNAS* 98:10037 (APBS)** · Jurrus et al. 2018,
*Protein Sci* 27:112 · Honig & Nicholls 1995, *Science* 268:1144 ·
**Onufriev & Case 2019, *Annu Rev Biophys* 48:275 (the implicit-solvent
critique)** · Groot & Warren 1997, *JCP* 107:4423 (DPD) · Brady & Bossis 1988,
*Annu Rev Fluid Mech* 20:111.

> **Honest gap: Nathan Baker has no APBS lecture** — his channel contains only
> four silent ten-second animations. Read Baker et al. 2001 and Jurrus et al.
> 2018 instead.

---

## G.7 Paired reading — Atlas G

| Watch this | Then read this | Hold this question |
|---|---|---|
| **Scalfi, *Generalized Langevin Equations*** | Zwanzig 1961; **Ermak & McCammon 1978** | Derive overdamped Langevin. What timescale separation is assumed? |
| **Schreiber, *Crowding and reaction rates*** | **Schreiber, Haran & Zhou 2009, *Chem Rev* 109:839** | How much *k*on can electrostatic steering buy, and can you design for it? |
| **Gillespie, on his own algorithm** | **Gillespie 1977, *J Phys Chem* 81:2340** | Derive the SSA. When does tau-leaping break it? |
| **Isaacson, *Stochastic Simulation*** | Isaacson 2009, *SIAM J Appl Math* 70:77 | The RDME has convergence pathologies. Name them. |
| De Schutter, *Operator Splitting* | Hepburn et al. 2012 | What error does splitting introduce, and how would you detect it? |
| **Luthey-Schulten, *Bacterial Cells*** | **Thornburg et al. 2022, *Cell* 185:345** | What parameters does a whole-cell model need that you cannot compute? |
| Covert & Serrano, *dialogue* | Karr et al. 2012, *Cell* 150:389 | Where has whole-cell modeling failed to scale, and why? |
| **Holt, *Measuring crowding with GEMs*** | **Ellis 2001; Yu et al. 2016, *eLife* 5:e19274** | Quantify how much crowding shifts a binding equilibrium. |
| **Pappu, Parts 1–3** | **Pappu et al. 2023, *Chem Rev* 123:8945** | Which sequence features drive phase separation? Are they designable? |
| **Mittal, *Charged condensates*** | **Dignon et al. 2018, *PLoS Comput Biol* 14:e1005941** | What does the HPS model assume, and where does it fail? |
| Lindorff-Larsen, *CALVADOS* | Tesei et al. 2021, *PNAS* 118 | How is a CG model for IDRs actually parameterized? |
| Joseph, *Small-molecule partitioning* | Her paper | Can you predict whether your compound enters a droplet? |
| Jülicher, *Active processes* | Zwicker et al. 2017, *Nat Phys* 13:408 | What distinguishes a living condensate from an oil drop? |
| **Luo, *Electrostatics and polarization*** | **Baker et al. 2001, *PNAS* 98:10037** | Where does Poisson-Boltzmann fail, and what replaces it there? |
| Baptista, *pH and ion distributions* | **Onufriev & Case 2019** | Implicit solvent versus explicit ions. What is lost? |
| Seaton, *DL_MESO* | Groot & Warren 1997 | When does DPD beat atomistic MD, and what conserves hydrodynamics? |
