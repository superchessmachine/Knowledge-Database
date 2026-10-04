# Atlas F — Coarse-Graining and Reduced Models

> **Problem.** An all-atom simulation of a nucleosome is 10⁶ particles and
> reaches microseconds. A chromosome is 10⁹ base pairs and reorganizes over
> minutes. No amount of hardware closes that gap. Coarse-graining asks what you
> can throw away and still be right — and, crucially, **about what you can still
> be right.** A coarse-grained model that reproduces structure almost always gets
> dynamics wrong, and the reason is a specific term in a specific equation that
> most practitioners have never seen.

This family was entirely missing from the first edition. It should not have
been: it is the only systematic theory of approximation in the whole document,
and it is the closest thing the physics culture has to a theory of what a
learned representation is allowed to discard.

---

## F.1 The theory — why coarse-graining works and where it fails

### Voth and multiscale coarse-graining

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Theory of Coarse-graining** | Gregory Voth (Chicago) | 58:45 | [▶](https://www.youtube.com/watch?v=wG8V29RolLc) |
| Theory of Ultra-Coarse-Graining | Gregory Voth | 1:08:56 | [▶](https://www.youtube.com/watch?v=NqCu8MSfRvg) |
| Molecular Modeling: A Window to the Biochemical World | Gregory Voth | 1:06:25 | [▶](https://www.youtube.com/watch?v=w2-B54lbYjA) |

The first is **the single most important theory lecture in this family**: the
variational / force-matching derivation of multiscale coarse-graining, which
shows that the correct CG potential is the many-body potential of mean force
obtained by integrating out the discarded degrees of freedom. Everything else
here is a tractable approximation to that object.

### Force matching and iterative Boltzmann inversion — the PASI 2012 school

| Title | Speaker | Length | Link |
|---|---|---|---|
| Force matching fundamentals | Monica Lamm (Iowa State) | 1:02:50 | [▶](https://www.youtube.com/watch?v=YXXhV74OI18) |
| **Fundamentals of the Iterative Boltzmann Inversion** | Roland Faller (UC Davis) | 52:14 | [▶](https://www.youtube.com/watch?v=YeqEOwtWS2E) |
| Using the IBI for polymers | Roland Faller | 43:07 | [▶](https://www.youtube.com/watch?v=MN61rOEiM3s) |
| **Developing numerical potentials and their state point dependence** | Roland Faller | 50:24 | [▶](https://www.youtube.com/watch?v=5RUYGbvKvu8) |
| From high to low resolution: the mapping problem | Marco Giulini | 29:31 | [▶](https://www.youtube.com/watch?v=qezOl493Uk8) |

Faller's state-point-dependence lecture states the central weakness of all
structure-based coarse-graining plainly: a potential fitted at one temperature
and density is not valid at another. **That is a transferability failure with an
exact analogue in machine learning — a model fitted to one distribution does not
transfer to another — and the CG community has thought about it far longer.**

Giulini's lecture treats *choice of mapping* as the real open problem via mapping
entropy, which is the question nobody in representation learning asks either.

### Mori-Zwanzig and the memory kernel

| Title | Speaker | Length | Link |
|---|---|---|---|
| Entropic Barriers and Dynamical Coarse-Graining via Mori-Zwanzig | Xingjie Li | 25:43 | [▶](https://www.youtube.com/watch?v=5djGtLNP_Cg) |
| CM4: Mori-Zwanzig | George Karniadakis (Brown) | 1:18:30 | [▶](https://www.youtube.com/watch?v=81RySGYvRXA) |
| Mori-Zwanzig Formulation / Model order reduction | CRUNCH Group, Brown | 2:02:11 | [▶](https://www.youtube.com/watch?v=0alQZzR09nM) |
| Generalized Langevin Equations from MD simulations | Laura Scalfi | 57:28 | [▶](https://www.youtube.com/watch?v=qZ-a3qmXMsk) |

> **This is derivation checkpoint 29 and it is the intellectual core of the
> family.** Projecting out degrees of freedom produces exactly three terms: a
> mean force, a memory kernel, and a noise. Virtually every coarse-grained model
> keeps the first and discards the other two. That is why CG dynamics is wrong
> even when CG structure is right, and why you cannot read kinetics off a MARTINI
> trajectory. Watch Xingjie Li first for the short version, then Karniadakis for
> the derivation.

### Machine-learned coarse-graining — Clementi

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Coarse-graining classical and quantum systems** | Cecilia Clementi (FU Berlin/Rice) | 56:52 | [▶](https://www.youtube.com/watch?v=1NeCvLqOy60) |
| Coarse-graining for classical and quantum systems (GGI) | Cecilia Clementi | 37:47 | [▶](https://www.youtube.com/watch?v=V2xu1Kfu4JU) |
| Learning molecular models from simulation and experimental data | Cecilia Clementi (IPAM) | 54:53 | [▶](https://www.youtube.com/watch?v=WVSy8bdD4Gg) |
| Designing molecular models by ML and experimental data | Cecilia Clementi | 54:42 | [▶](https://www.youtube.com/watch?v=T-iDv6QTqg4) |
| Clementi, TCBG seminar (CGnet/CGSchNet results) | Cecilia Clementi | 1:00:37 | [▶](https://www.youtube.com/watch?v=9enkGwXfWZ0) |
| Designing molecular models with ML and experimental data (IPAM) | Cecilia Clementi | 46:18 | [▶](https://www.youtube.com/watch?v=pccb758tOlI) |
| ML Coarse-Grained Models with Graph Neural Networks | Computational Biomedicine | 1:12:21 | [▶](https://www.youtube.com/watch?v=soU4S2mqqzM) |
| HITS-SIMPLAIX Colloquium: protein dynamics and ML | Cecilia Clementi | 50:45 | [▶](https://www.youtube.com/watch?v=2HAI_o1fcMg) |

### Learned mappings and backmapping

| Title | Speaker | Length | Link |
|---|---|---|---|
| Physics in and out of machine learning for molecular simulations | Tristan Bereau (Amsterdam) | 52:34 | [▶](https://www.youtube.com/watch?v=pXVmVr85NF8) |
| Tractable Mapping Entropy and Generative Backmapping via Split-Flows | Tristan Bereau | 55:30 | [▶](https://www.youtube.com/watch?v=mqau8j_ypx8) |
| Chemically Transferable Generative Backmapping of CG Proteins | Soojung Yang (MIT) | 1:06:07 | [▶](https://www.youtube.com/watch?v=tIqW51d2a5g) |
| Coarse-graining autoencoders and evolutionary learning | Rafael Gómez-Bombarelli (MIT) | 36:42 | [▶](https://www.youtube.com/watch?v=l_NfukhR2XU) |
| Generative Coarse-Graining of Molecular Conformations | Wujie Wang (MIT) | 1:53:41 | [▶](https://www.youtube.com/watch?v=p7Frc4o2RHI) |
| **Simulate Time-integrated CG Molecular Dynamics with Geometric ML** | Xiang Fu (MIT) | 1:40:25 | [▶](https://www.youtube.com/watch?v=r_ZTOoGxFC0) |
| Utilizing ML for Scale Bridging: atomistic to CG and back | CaSToRC | 1:20:39 | [▶](https://www.youtube.com/watch?v=mcRk_lo0UXg) |

**Xiang Fu's talk is the one that does something genuinely new**: rather than
learning a CG force field and integrating it, it learns CG *dynamics* with large
timesteps directly — circumventing the memory-kernel problem rather than solving
it. Whether that is legitimate is a live question and exactly the kind of thing
worth having an opinion about.

---

## F.2 The models in practice

### MARTINI

| Title | Speaker | Length | Link |
|---|---|---|---|
| Perspective on the Martini model: the road to simulating entire cells | Siewert-Jan Marrink (Groningen) | 40:22 | [▶](https://www.youtube.com/watch?v=Ax6DaYJ9Eeg) |
| BioExcel #24: Perspective on the Martini Force Field | BioExcel CoE | 1:19:47 | [▶](https://www.youtube.com/watch?v=Yq1f8vDfPe4) |
| BioExcel #84: Simulating whole cells with Martini | BioExcel CoE | 1:01:50 | [▶](https://www.youtube.com/watch?v=fvFaPgSoM90) |
| **Coarse Grain (full workshop session)** | Manuel Melo (MoBioChem) | 2:02:57 | [▶](https://www.youtube.com/watch?v=mY6dj4_Nizw) |
| Key aspects when modelling amphiphiles with MARTINI | Germán Pérez-Sánchez | 43:00 | [▶](https://www.youtube.com/watch?v=qXdBttFoj0g) |
| OpenMM + Martini3: Simulating Proteins in Membrane Systems | Neurosnap | 6:52 | [▶](https://www.youtube.com/watch?v=EVcw-w-Lcnk) |
| Martinize.py: Generate Martini Protein Topology | Ubeiden Samboni | 11:21 | [▶](https://www.youtube.com/watch?v=xw9ZJxLxcwY) |
| Increasing complexity in simulations of biological membranes | D. Peter Tieleman (Calgary) | 1:16:01 | [▶](https://www.youtube.com/watch?v=D2fU5fznNUg) |
| Tieleman, TCBG seminar (Martini 3 validation) | D. Peter Tieleman | 1:04:31 | [▶](https://www.youtube.com/watch?v=VPvXPIp6NXk) |
| TCBG 2003: Coarse Grained Modeling of Lipid Phases | UIUC TCBG | 48:00 | [▶](https://www.youtube.com/watch?v=MXH6u93v_mA) |

### Structure-based (Gō) models and the funnel lineage

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Structure-based model workshop, part 1 (SMOG)** | Paul Whitford (Northeastern) | 58:35 | [▶](https://www.youtube.com/watch?v=pGN2nwrvexs) |
| Structure-based model workshop, part 2 | Paul Whitford | 49:31 | [▶](https://www.youtube.com/watch?v=CCDaBreMv18) |
| **Funnels and Landscapes in protein folding: a historical perspective** | José Onuchic (Rice) | 1:05:51 | [▶](https://www.youtube.com/watch?v=3rwebPsipvs) |
| **Funnels, cooperativity, desolvation, and enthalpic barriers** | Hue Sun Chan (Toronto) | 1:00:52 | [▶](https://www.youtube.com/watch?v=nXIzhxNfTUQ) |

**Watch Onuchic and then immediately watch Chan.** Onuchic explains why
structure-based models work — minimal frustration licenses a funnel. Chan is the
principal critique: naive Gō models get cooperativity and desolvation barriers
wrong because they build the answer into the potential. That disagreement is the
most instructive hour in this family.

### AWSEM, UNRES, SIRAH and the rest

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Coarse-Grained Modeling of Biomolecules: A Brief History and Overview** | Garegin Papoian (Maryland) | 51:19 | [▶](https://www.youtube.com/watch?v=gCWJqYAJo8U) |
| Structure and Dynamics of Nucleosomes from Atomistic and CG Simulations | Garegin Papoian | 1:01:02 | [▶](https://www.youtube.com/watch?v=USFJ0qAvqoQ) |
| SIRAH: a CG force field for biomolecular simulations | Sergio Pantano (Pasteur Montevideo) | 1:04:48 | [▶](https://www.youtube.com/watch?v=HuqjJ2PIWrM) |
| Introduction to coarse-grained modeling for biological systems | L. Silva (SIRAH) | 17:43 | [▶](https://www.youtube.com/watch?v=0QobG5LKAzE) |
| Geometry-consistent expressions for energy terms (UNRES) | Adam Liwo (Gdańsk) | 42:57 | [▶](https://www.youtube.com/watch?v=Fdnn-y16068) |
| Template-based prediction using coarse-grained UNRES | Adam Liwo | 43:31 | [▶](https://www.youtube.com/watch?v=bcxLt0_tE-E) |
| CABS-flex 2.0: predicting structural ensembles | Bernal Institute | 26:49 | [▶](https://www.youtube.com/watch?v=oN7KHWswHio) |
| Protein folding simulation using SURPASS | Bio Comp Pictures | 3:37 | [▶](https://www.youtube.com/watch?v=QG7Co4T7oaA) |
| Coarse-Grained Simulation of Proteins to Capture Conformational Change | IIT Madras | 1:11:55 | [▶](https://www.youtube.com/watch?v=SX5sIRCJXSE) |

Papoian's history lecture is **the best opening item in this family** — a survey
of the whole coarse-graining enterprise by someone who built one of its major
models.

### Adaptive resolution and multiscale coupling

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Adaptive resolution simulation methods for soft matter** | Kurt Kremer (MPI-P Mainz) | 52:58 | [▶](https://www.youtube.com/watch?v=FaQmlW9muoE) |
| BioExcel #20: Adaptive resolution methods in soft matter | BioExcel CoE | 1:00:48 | [▶](https://www.youtube.com/watch?v=84_Xw59umZI) |
| BioExcel #19: Hybrid MM/Coarse-Grained approaches | BioExcel CoE | 58:46 | [▶](https://www.youtube.com/watch?v=vQ32JdPMCmY) |
| Coarse-grained / multiscale simulation in NAMD, with validation | NanoBio Node | 56:28 | [▶](https://www.youtube.com/watch?v=PYH8VKgfNnA) |

AdResS lets resolution vary across space with particles changing representation
as they move — the molecular analogue of adaptive mesh refinement, and an idea
with no counterpart whatsoever in protein machine learning.

---

## F.3 Mesoscale and continuum

### Membrane elasticity — the Deserno course

| Title | Speaker | Length | Link |
|---|---|---|---|
| Membrane Elasticity and Thermodynamics I | Markus Deserno (CMU) | 1:33:32 | [▶](https://www.youtube.com/watch?v=crNk96HtrAQ) |
| Membrane Elasticity and Thermodynamics II | Markus Deserno | 1:40:11 | [▶](https://www.youtube.com/watch?v=eQeYUhT_7Uo) |
| Membrane Elasticity and Thermodynamics III | Markus Deserno | 1:43:25 | [▶](https://www.youtube.com/watch?v=wVX3XeNgW3E) |
| A Physicist's View on Biological Membranes (single-lecture version) | Markus Deserno | 1:14:13 | [▶](https://www.youtube.com/watch?v=Hh_LxkDJxe8) |
| Coarse-grained Simulation Studies of membranes | Markus Deserno (Nordita) | 56:36 | [▶](https://www.youtube.com/watch?v=onls4_UaHgM) |
| Helfrich Energy: From Heisenberg Spins to Mean Curvature | PhysicsOfLifeLMU | 45:41 | [▶](https://www.youtube.com/watch?v=gcr3prnBPt0) |
| Physics approaches of biological membranes | Patricia Bassereau (Institut Curie) | 1:08:10 | [▶](https://www.youtube.com/watch?v=VAe2f_Q-Prg) |
| Coarse-Graining Phase Separation: Flory-Huggins to Ginzburg-Landau | PhysicsOfLifeLMU | 48:20 | [▶](https://www.youtube.com/watch?v=t4b5rRa-tZE) |

Deserno's three-part course is the best membrane theory available free — from
differential geometry to the Helfrich Hamiltonian, properly derived. The LMU
Flory-Huggins-to-Ginzburg-Landau lecture is **the cleanest worked example of
coarse-graining as a concept anywhere in this document**: a lattice model becomes
a continuum field theory, and you can see exactly what was discarded.

### Dissipative particle dynamics and lattice Boltzmann

| Title | Speaker | Length | Link |
|---|---|---|---|
| Lec 31: Dissipative Particle Dynamics | IIT Madras | 39:54 | [▶](https://www.youtube.com/watch?v=VxkQn3H_Q3k) |
| Mesoscale Modeling of Soft Matter with DPD | ATOMS UFRJ | 1:19:41 | [▶](https://www.youtube.com/watch?v=6v4rlYo4MKk) |
| DPD Simulation of Red Blood Cells | Bruce Caswell | 1:02:02 | [▶](https://www.youtube.com/watch?v=gpdImhQJIOQ) |
| DL_MESO (hands-on) | CCPBioSim | 1:15:06 | [▶](https://www.youtube.com/watch?v=c90TPnu2ewA) |
| Lattice Boltzmann for simple fluids 1/4 | Ignacio Pagonabarraga (EPFL) | 19:45 | [▶](https://www.youtube.com/watch?v=GU8a3cJ9rgc) |
| Lattice Boltzmann for simple fluids 2/4 | Ignacio Pagonabarraga | 23:09 | [▶](https://www.youtube.com/watch?v=5b2-NqOXNrU) |
| Lattice Boltzmann for simple fluids 3/4 | Ignacio Pagonabarraga | 33:24 | [▶](https://www.youtube.com/watch?v=ZuKBuO80330) |
| Lattice Boltzmann for simple fluids 4/4 | Ignacio Pagonabarraga | 35:52 | [▶](https://www.youtube.com/watch?v=7_rgL2M2jVs) |
| Introduction to Lattice Boltzmann Method | ESPResSo | 1:03:56 | [▶](https://www.youtube.com/watch?v=jfk4feD7rFQ) |

---

## F.4 BUILD — Atlas F

1. **Implement iterative Boltzmann inversion** on a simple liquid. Match the
   radial distribution function. Then change the temperature by 20% and measure
   how badly the potential transfers. Plot it. That plot is the transferability
   problem, and it has an exact analogue in every protein model you use.
2. **Implement force matching** on the same system and compare the resulting
   potential to the IBI one. They will differ. Explain why in terms of what each
   objective is actually minimizing.
3. **Measure the memory kernel.** Take an atomistic trajectory, define a CG
   coordinate, and extract the friction kernel. Show that it is not a delta
   function. That is checkpoint 29, made real.
4. **The research exercise.** Take any learned coarse-grained model (CGnet-style)
   and ask what Mori-Zwanzig says it is missing. Write two pages on whether
   adding a learned memory kernel is tractable. Nobody has done this properly and
   it is a clean thesis.

**Derivation checkpoints due: 28, 29, 30.**

---

## F.5 Paired reading — Atlas F

| Watch this | Then read this | Hold this question |
|---|---|---|
| Voth, *Theory of Coarse-graining* | **Izvekov & Voth 2005, JPC B 109:2469; Noid et al. 2008, JCP 128:244114** | Derive the force-matching objective. What is it a projection of? |
| Voth, *Ultra-Coarse-Graining* | Dama et al. 2013, JCTC 9:2466 | What breaks when CG sites must change internal state? |
| Faller, *IBI fundamentals* | Reith, Pütz & Müller-Plathe 2003, JCC 24:1624 | IBI inverts an RDF to a potential. Why is that inversion not unique? |
| Faller, *State point dependence* | **Louis 2002, *Beware of density dependent pair potentials*** | State the transferability failure formally. What is the ML analogue? |
| Giulini, *The mapping problem* | Giulini et al. 2020, JCTC 16:6795 | Mapping entropy scores a choice of CG sites. Could you optimize a mapping? |
| **Xingjie Li / Karniadakis, Mori-Zwanzig** | **Zwanzig 1961, Phys Rev 124:983; Mori 1965** | Derive the three terms. Which does your favourite CG model keep? |
| Scalfi, *GLE from MD* | Jung, Hanke & Schmid 2017, JCTC 13:2481 | How do you actually measure a memory kernel from a trajectory? |
| Clementi, *Coarse-graining classical and quantum* | **Wang et al. 2019, ACS Cent Sci 5:755 (CGnets)** | The loss is force matching. What guarantees thermodynamic consistency? |
| Clementi, *Learning from simulation and experiment* | Olsson et al. 2017, PNAS 114:8265 | How do you constrain a CG model with experiment rather than simulation? |
| Fu, *Time-integrated CG dynamics* | Fu et al. 2023, TMLR, arXiv:2204.10348 | Learning dynamics directly sidesteps the memory kernel. Is that legitimate? |
| Yang, *Generative backmapping* | Yang & Gómez-Bombarelli 2023, arXiv:2303.01569 | Backmapping is a conditional generative problem. What makes it ill-posed? |
| Marrink, *Perspective on Martini* | **Marrink et al. 2007, JPC B 111:7812; Souza et al. 2021, Nat Methods 18:382** | Four heavy atoms per bead. What chemistry is lost at that resolution? |
| Whitford, *SMOG workshop* | **Noel et al. 2016, PLoS Comput Biol 12:e1004794** | A Gō model builds the native state into the potential. What can it still predict? |
| **Onuchic, *Funnels*** | **Bryngelson, Onuchic, Socci & Wolynes 1995, Proteins 21:167** | Derive the condition for minimal frustration. |
| **Chan, *Funnels, cooperativity, desolvation*** | Chan et al. 2011, Annu Rev Phys Chem 62:301 | Name three things Gō models get wrong and say why. |
| Papoian, *Brief History* | Kmiecik et al. 2016, Chem Rev 116:7898 | Place five CG models on a resolution-vs-transferability axis. |
| Liwo, *Geometry-consistent energy terms* | Liwo et al. 2001, JCP 115:2323 | UNRES derives terms as cumulant expansions of the PMF. What does that buy? |
| Kremer, *Adaptive resolution* | **Praprotnik, Delle Site & Kremer 2005, JCP 123:224106** | Particles change representation as they move. What must be conserved? |
| Deserno I–III | **Helfrich 1973, Z Naturforsch C 28:693** | Derive the Helfrich Hamiltonian. What is the Gaussian modulus and why is it usually ignored? |
| LMU, *Flory-Huggins to Ginzburg-Landau* | Cahn & Hilliard 1958, JCP 28:258 | Trace exactly what is discarded going from lattice to field theory. |
| Pagonabarraga, LBM 1–4 | Dünweg & Ladd 2009, Adv Polym Sci 221:89 | LBM solves hydrodynamics on a lattice. When do biomolecules need it? |
