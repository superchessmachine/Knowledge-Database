# Atlas A — Potential Energy Functions

> **Problem.** Given the positions of every atom, what is the energy? Everything
> downstream — dynamics, sampling, free energy, design scoring — is an operation
> on this function. **The accuracy of the potential is the ceiling on every
> number produced by families B through E**, and it is a ceiling the field has
> been pressing against for twenty years.

There are four tiers: empirical molecular mechanics, continuum solvation added
on top, quantum mechanics for the small region where chemistry happens, and —
new and genuinely disruptive — machine-learned potentials that aim at quantum
accuracy at empirical cost.

---

## A.1 Empirical force fields

Covered principally in Module B.6 and Atlas B; the construction side lives here.

| Title | Speaker | Scale | Link |
|---|---|---|---|
| **Open Force Field Workshops (2019–2026)** | OpenFF / OMSF | 10 workshop playlists | [Channel](https://www.youtube.com/channel/UCh0aJSUm_sYr7nuTzhW806g) |
| Introduction to Classical Force Fields | Emad Tajkhorshid (UIUC TCBG) | 1:33:42 | [▶](https://www.youtube.com/watch?v=bhYWPZbT0uA) |
| Introduction to Force Field Toolkit (ffTK) | Christopher Mayne (UIUC) | 1:08:24 | [▶](https://www.youtube.com/watch?v=gyC241l9pAc) |
| BioExcel #58: CHARMM Force Field Development History and Features | BioExcel CoE | 1:07:56 | [▶](https://www.youtube.com/watch?v=pAZ-vj8Ysr8) |
| Electrostatics: Fixed Point Charges and Polarization | OpenFF | 1:00:12 | [▶](https://www.youtube.com/watch?v=JdJkFh2T9X4) |
| Accuracy of the AMOEBA Force Field in Binding Free Energy Simulations | Jay Ponder (WashU) | 30:24 | [▶](https://www.youtube.com/watch?v=I2zm3hAO-eI) |
| Strategies for ab initio Biomolecular Force Field Development | David Cerutti | 58:42 | [▶](https://www.youtube.com/watch?v=JapaP-c4AU0) |
| Automated Optimization of the CHARMM Lipid Force Field | Andreas Krämer | 1:03:55 | [▶](https://www.youtube.com/watch?v=Hsq1nGr_jo8) |
| Fragmenting molecules for QC torsion drives | Chaya Stern | 57:06 | [▶](https://www.youtube.com/watch?v=afZp538VpMA) |
| Graph Nets for partial charge prediction | Yuanqing Wang | 51:18 | [▶](https://www.youtube.com/watch?v=ndIgAV2Xwfk) |
| Machine-learned MM force fields from large-scale QC data | Ken Takaba | 23:08 | [▶](https://www.youtube.com/watch?v=Vf2KhGlSlIg) |
| Parameterization of AMBER ff19SB | Chuan Tian | 50:32 | [▶](https://www.youtube.com/watch?v=M2ZRKc5FeVE) |
| Data Curation: The Forgotten Practice in the Era of AI | Pankaj Daga | 59:02 | [▶](https://www.youtube.com/watch?v=pjlFHGuVlLo) |

**Open Force Field is where force-field construction is taught publicly** —
torsion fragmentation, training-set selection, Bayesian parameterization, and
the move toward graph-neural-network parameter assignment. If you ever want to
*fit* rather than consume a force field, this is the only free curriculum.

Ponder's AMOEBA talk is the honest assessment of what polarizability actually
buys in binding free energies, which is less than its cost would suggest — a
useful calibration on the general claim that more physics is always better.

---

## A.2 Electrostatics and continuum solvation

| Title | Speaker | Length | Link |
|---|---|---|---|
| **CompChem 06.04: Solvation Models — Continuum (Implicit) Solvent Electrostatics** | Chris Cramer (Minnesota) | 23:11 | [▶](https://www.youtube.com/watch?v=tB4xZLUGJqM) |
| CompChem 06.01: Solvation Models — Chemical Phenomena | Chris Cramer | 19:00 | [▶](https://www.youtube.com/watch?v=Fx3zkPxt2qc) |
| CECAM Advances in Electrostatics: boundary elements | Christopher Cooper (UTFSM) | 1:08:00 | [▶](https://www.youtube.com/watch?v=MMQEwnYN8Oo) |
| CECAM Advances in Electrostatics: treecodes | Leighton Wilson (Michigan) | 57:00 | [▶](https://www.youtube.com/watch?v=GJ53D5mR-kI) |
| The Multi-Faceted Roles of Electrostatics in Biomolecular Simulation | Protein Electrostatics seminar | 1:01:00 | [▶](https://www.youtube.com/watch?v=va25fb1uDbM) |
| How does pH affect the distribution of ions around proteins? | Protein Electrostatics seminar | 1:06:00 | [▶](https://www.youtube.com/watch?v=-3TF-uyYEP8) |
| Modeling electrostatics and polarization in biomolecules | Protein Electrostatics seminar | 52:00 | [▶](https://www.youtube.com/watch?v=6Frl-o5jNDY) |
| Generalized Born and implicit solvent | Alexey Onufriev (Virginia Tech) | 35:00 | [▶](https://www.youtube.com/watch?v=8qApNJdLkEw) |
| Using 3D structure to predict protein-protein and protein-ligand interactions | Barry Honig (Columbia) | 40:00 | [▶](https://www.youtube.com/watch?v=auUTXW7KbgQ) |
| Constant-pH Methods in Biomolecular Simulations, Class 1 | Fernando Barroso da Silva (ICTP-SAIFR) | 1:08:00 | [▶](https://www.youtube.com/watch?v=uYZInkXW5q4) |
| Constant pH molecular dynamics in GROMACS | BioExcel CoE | 19:05 | [▶](https://www.youtube.com/watch?v=YQ8eRyScuyk) |
| TABI-PB 2.0 boundary-element solver | Protein Electrostatics | 50:00 | [▶](https://www.youtube.com/watch?v=WcUcwqQQJhs) |

**Cramer's 23-minute lecture is the cleanest derivation anywhere** of why a
continuum dielectric is a legitimate approximation and exactly where it breaks.
Watch it before anything else in this subsection.

Onufriev is the generalized Born authority, and the key point is one most people
get wrong: **GB is a specific analytic approximation to Poisson-Boltzmann, not
an independent theory.** Knowing that tells you precisely which of its failures
are fixable and which are structural.

Constant-pH MD is the correct answer to the pKa problem and the one almost
everyone skips. If your designed protein has a buried ionizable residue — and
peptide binders routinely do — a fixed protonation state is an assumption you
have not tested.

---

## A.3 Quantum mechanics and QM/MM

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Hybrid QM/MM — Day 1 Lectures** | CECAM | 4:04:00 | [▶](https://www.youtube.com/watch?v=0WQmXbJjOP4) |
| **Hybrid QM/MM — Day 2 Lectures** | CECAM | 4:03:00 | [▶](https://www.youtube.com/watch?v=lMk6NtOYPLU) |
| QM/MM Best Practice: Kick-off webinar | BioExcel CoE | 1:36:00 | [▶](https://www.youtube.com/watch?v=ajj8NUvva-0) |
| QM/MM Best Practice: Accurate structures and energies with QM/MM | BioExcel CoE | 1:23:00 | [▶](https://www.youtube.com/watch?v=aQdjC-W9Wy4) |
| QM/MM Best Practice: Chemical accuracy in enzyme catalytic mechanisms | BioExcel CoE | 1:23:00 | [▶](https://www.youtube.com/watch?v=8PGHcNKOLqY) |
| QM/MM Best Practice: Studies on enzyme-catalysed reactions | BioExcel CoE | 1:11:00 | [▶](https://www.youtube.com/watch?v=XIHMcR_tR7E) |
| **QM/MM Best Practice: Validation of DFT functionals in QM/MM** | BioExcel CoE | 53:00 | [▶](https://www.youtube.com/watch?v=uP1px6Yul2s) |
| BioExcel #51: Multiscale QM/MM with the GROMACS/CP2K interface | BioExcel CoE | 51:00 | [▶](https://www.youtube.com/watch?v=XwfXXitVW1U) |
| Modelling Enzymes with QM/MM | CCPBioSim | 42:00 | [▶](https://www.youtube.com/watch?v=ROd0libkRy0) |
| Introduction to QM/MM, Part 1 | BioExcel CoE | 30:23 | [▶](https://www.youtube.com/watch?v=V2_ppEF5whA) |
| QM/MM Methods and development | Andres Cisneros (BAGIM) | 1:00:00 | [▶](https://www.youtube.com/watch?v=42FdoIuLcg0) |
| Introduction to DFTB | Bálint Aradi (Bremen) | 31:00 | [▶](https://www.youtube.com/watch?v=dl4Y-v-l0io) |
| Extended Tight Binding (GFN-xTB) | Sebastian Ehlert (Grimme group) | 26:00 | [▶](https://www.youtube.com/watch?v=Yu-m9FmDU4U) |
| Online-ICNI Symposium | Stefan Grimme (Bonn) | 41:00 | [▶](https://www.youtube.com/watch?v=SkZzv2kX5fM) |
| Introduction to Density Functional Theory | David Sherrill (Georgia Tech) | 52:00 | [▶](https://www.youtube.com/watch?v=QGyfGCZT110) |
| Basis Sets, part 1 | David Sherrill (Georgia Tech) | 34:00 | [▶](https://www.youtube.com/watch?v=Hk4YRb4okC4) |
| MIT OCW: Modern Electronic Structure Theory — Basis Sets | MIT OCW | 50:00 | [▶](https://www.youtube.com/watch?v=BOryXuUMjI0) |
| **Nobel Lecture 2013** | Arieh Warshel (USC) | 28:00 | [▶](https://www.youtube.com/watch?v=FnAKzcAmmhk) |

The two CECAM days are **over eight hours of formal QM/MM theory** — embedding
schemes, link atoms, boundary treatment, mechanical versus electrostatic
embedding — and nothing else free comes close to that depth.

**The DFT-functional validation lecture will save you real time**: it is a direct
empirical answer to "which functional do I actually use for a barrier height,"
which is otherwise a question you resolve by burning a month.

Warshel's Nobel lecture is the origin of both QM/MM and the empirical valence
bond method, from the person who invented them. It pairs with Atlas family R's
enzyme design material: electrostatic preorganization is the hypothesis every
enzyme design objective is implicitly betting on.

---

## A.4 Machine-learned interatomic potentials — the disruptive tier

> **Why this subsection matters more than its length suggests.** If
> machine-learned potentials reach biomolecular scale with transferable
> accuracy, they collapse the ceiling that bounds every number in Atlas families
> B through E. That is the largest single thing that could happen to
> computational biophysics this decade, and it is currently happening in
> materials science rather than in biology.

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Tutorial: How to Train and Use MACE Interatomic Potentials, Part 1** | Ilyes Batatia (Cambridge) | 1:06:00 | [▶](https://www.youtube.com/watch?v=j6vjEGBDCyo) |
| Tutorial: How to Train and Use MACE, Part 2 | Ilyes Batatia | 50:00 | [▶](https://www.youtube.com/watch?v=MaX3nCzQy54) |
| Foundation Models for Materials and Molecules | Gábor Csányi (Cambridge) | 58:00 | [▶](https://www.youtube.com/watch?v=ZXT_ZZmvVUw) |
| Machine Learning Meets Quantum Chemistry | Klaus-Robert Müller (TU Berlin) | 51:00 | [▶](https://www.youtube.com/watch?v=HSxMtyjxf-g) |
| **Challenges for General-Purpose MLFFs** | Alexandre Tkatchenko (Luxembourg) | 51:00 | [▶](https://www.youtube.com/watch?v=id5RNIZsNSE) |
| MACE: Higher Order Equivariant Message Passing NNs | Valence Labs | 1:22:00 | [▶](https://www.youtube.com/watch?v=I9Y2le9e74A) |
| **Local Equivariant Representations for Large-Scale Atomistic Dynamics** | Batzner & Musaelian (Harvard) | 1:26:00 | [▶](https://www.youtube.com/watch?v=ZR1NTBPBDOo) |
| The state of neural network interatomic potentials | Justin Smith (ANI author) | 41:00 | [▶](https://www.youtube.com/watch?v=3ci69rq6-JA) |
| Uncertainty-aware ML models of many-body atomic interactions | Boris Kozinsky (Harvard) | 57:00 | [▶](https://www.youtube.com/watch?v=QnZ2BI1leVE) |
| Learning how to break symmetry with symmetry-preserving networks | Tess Smidt (MIT) | 59:00 | [▶](https://www.youtube.com/watch?v=Qr-k_oXTuqw) |
| AIMNet2: A Robust Neural Network Potential | Roman Zubatyuk (CMU) | 40:00 | [▶](https://www.youtube.com/watch?v=_60AZiwdO_I) |
| AI Solutions for Computational and Organic Chemistry | Olexandr Isayev (CMU) | 1:05:00 | [▶](https://www.youtube.com/watch?v=QvYL4MaSMCo) |

**Batzner and Musaelian's talk is the conceptual centerpiece**: it explains why
*strict* equivariance buys extreme data efficiency, and why Allegro's strict
locality buys scale. That argument — a symmetry constraint as a substitute for
data — is the single most transferable idea from this subsection into protein
design, where data is the binding constraint.

**Tkatchenko's "Challenges" talk is the necessary skepticism.** It asks what
"foundation model" means for a potential and whether current benchmarks measure
transferability at all. Watch it immediately after Csányi's foundation-model
talk and notice that they disagree.

AIMNet2 is the one currently usable for drug-like molecules, including charged
species — which is why it, rather than the materials-focused models, is the one
to try on your own systems.

---

## A.5 BUILD — Atlas A

1. **Implement a Lennard-Jones plus Coulomb energy function** from scratch for a
   small molecule. Add a simple reaction-field or generalized-Born correction.
   Compare solvation free energies to a PB solver.
2. **Write the Poisson-Boltzmann equation** and solve it numerically in 1D for a
   charged plane. Derive the Debye length from your solution and check against
   the analytic result.
3. **Run a constant-pH simulation** on a protein with a buried ionizable residue.
   Compare the computed pKa to the fixed-protonation assumption your pipelines
   normally make. Quantify the error that assumption introduces.
4. **Train a small machine-learned potential** on a dataset of your own QM
   calculations — your CAPN5 DFT work is directly usable here. Measure how it
   degrades off the training manifold. That degradation curve is the
   transferability question of Section A.4, measured on your own data.

**Derivation checkpoints due: 1, 2, 3, 4, 5, 34, 35, 36.**

---

## A.6 Paired reading — Atlas A

| Watch this | Then read this | Hold this question |
|---|---|---|
| Tajkhorshid, *Classical Force Fields* | **Best et al. 2012 (CHARMM36); Maier et al. 2015 (ff14SB)** | For each term, name the experimental or QM data it was fit to. |
| OpenFF workshops | Any OpenFF parameterization paper | How is a torsion parameter determined, and how transferable is it? |
| Ponder, *AMOEBA accuracy* | **Ponder et al. 2010, JPCB 114:2549** | What does polarizability buy, and is it worth the cost? |
| **Cramer, *Continuum solvent electrostatics*** | **Honig & Nicholls 1995, Science 268:1144** | When is a continuum dielectric legitimate, and what is the dielectric constant of a protein? |
| Cooper / Wilson, CECAM electrostatics | **Baker et al. 2001, PNAS 98:10037 (APBS)** | How is PB actually solved at protein scale, and what is the discretization error? |
| Onufriev, *Generalized Born* | **Still et al. 1990, JACS 112:6127; Onufriev et al. 2004, Proteins 55:383** | GB approximates PB. Derive the approximation and state when it fails. |
| Barroso / BioExcel, *Constant-pH MD* | **Swails, York & Roitberg 2014, JCTC 10:1341** | A fixed protonation state is an assumption. How large is the error? |
| **CECAM QM/MM Days 1–2** | **Warshel & Levitt 1976, JMB 103:227; Senn & Thiel 2009, Angew Chem 48:1198** | Compare mechanical and electrostatic embedding. What does the link atom break? |
| BioExcel, *DFT functional validation* | Any QM/MM barrier-height benchmark | Which functional for a barrier height, and what is the residual error? |
| Grimme / Ehlert, *xTB* | **Bannwarth, Ehlert & Grimme 2019, JCTC 15:1652 (GFN2-xTB)** | Semi-empirical at near-DFT accuracy. What is sacrificed? |
| Warshel, Nobel Lecture | Warshel & Weiss 1980, JACS 102:6218 (EVB) | Electrostatic preorganization is the mechanism. What design objective follows? |
| **Batatia, *MACE tutorial*** | **Batatia et al. 2022, NeurIPS (MACE); Kovács et al. 2023 (MACE-OFF23)** | Train one. Then measure its error on a molecule outside the training set. |
| **Batzner & Musaelian** | **Batzner et al. 2022, Nat Commun 13:2453 (NequIP); Musaelian et al. 2023 (Allegro)** | Strict equivariance buys data efficiency. Quantify how much. |
| Csányi, *Foundation Models* vs. Tkatchenko, *Challenges* | Both sides' position papers | Write the strongest version of each case. Which benchmark would settle it? |
| Zubatyuk, *AIMNet2* | Anstine, Zubatyuk & Isayev 2024/25 | Charged species break most MLIPs. How does AIMNet2 handle them? |
| Smidt, *Breaking symmetry* | Thomas, Smidt et al. 2018 (tensor field networks) | When should a model be allowed to break a symmetry it was given? |
