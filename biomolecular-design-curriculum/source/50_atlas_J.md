# Atlas J — Structure Determination Algorithms

> **Problem.** Experimental data — diffraction intensities, particle images,
> NOE cross-peaks, scattering curves — do not contain coordinates. Turning them
> into coordinates is an inverse problem, usually underdetermined, always noisy,
> and solved by algorithms that embed strong priors. **Every structure you have
> ever trained a model on is the output of one of these algorithms, and the
> prior is baked into the answer.** A computational person who does not know
> which parts of a PDB entry are measurement and which are prior will
> systematically over-trust their training data.

This family is where the learning-first culture is weakest, and the weakness is
consequential. A model trained on coordinates inherits every assumption in this
section without being told.

---

## J.1 Cryo-EM reconstruction

### Maximum likelihood and the Bayesian framework

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Cryo-EM17 lecture 06: Image refinement in 2D and 3D** | Sjors Scheres (MRC-LMB) | 53:46 | [▶](https://www.youtube.com/watch?v=TfLFCeehfjM) |
| Cryo-EM Image Processing (2024) | Sjors Scheres | 52:16 | [▶](https://www.youtube.com/watch?v=78fARw2jAvk) |
| Reconstruction of Cryo-EM Images of Proteins to Atomic Resolution | Sjors Scheres (EPFL Imaging) | 47:18 | [▶](https://www.youtube.com/watch?v=LfxnwGZZXLE) |
| **EM Image Formation and Single-particle Reconstruction** | Fred Sigworth (Yale) | 1:31:22 | [▶](https://www.youtube.com/watch?v=3Y-ztr53WUg) |
| Algorithms and foundational math, Part II | Fred Sigworth (NCCAT) | 56:29 | [▶](https://www.youtube.com/watch?v=mASM02JNmjI) |
| CryoEM 1.1: Two Astonishing Phenomena | Fred Sigworth | 13:32 | [▶](https://www.youtube.com/watch?v=iGreXoFqS3s) |
| Cryo-EM Workshop (the dissenting view) | Marin van Heel | 38:42 | [▶](https://www.youtube.com/watch?v=ElWsgWfxp8I) |

The Scheres lecture is the canonical derivation of empirical-Bayes refinement:
**marginalize over unknown orientations rather than assigning them, and learn
the regularization from the data instead of hand-tuning a filter.** That move —
treating a nuisance parameter as something to integrate out rather than estimate
— is one of the most transferable ideas in this entire document.

Watch van Heel afterward specifically because he disagrees. Pedagogically that
is worth more than a second agreeing lecture.

### Image formation, CTF and Fourier theory

| Title | Speaker | Length | Link |
|---|---|---|---|
| Cryo-EM14 lecture 2: Image formation, Fourier analysis and CTF theory | Sjors Scheres | 1:00:52 | [▶](https://www.youtube.com/watch?v=YL6I-QDdAi8) |
| Cryo-EM17 lecture 03: Image formation, Fourier analysis, CTF | Paula da Fonseca | 45:15 | [▶](https://www.youtube.com/watch?v=WkYLgj_D6dM) |
| Part 3: CTF Correction | Grant Jensen (Caltech) | 31:44 | [▶](https://www.youtube.com/watch?v=GYDLhg49UQA) |
| Fourier transforms in cryo-EM: convolution, Gaussians, FSC, FFT | Pavel Afanasyev (ETH) | 59:45 | [▶](https://www.youtube.com/watch?v=mRrM0cus1HE) |
| Basics of single-particle cryo-EM image processing | Pavel Afanasyev | 1:00:03 | [▶](https://www.youtube.com/watch?v=rD6qYsCUHfE) |
| Cryo-EM17 lecture 01: Cryo-EM past, present and future | Richard Henderson | 59:38 | [▶](https://www.youtube.com/watch?v=aHhmnxD6RCI) |

Henderson's lecture contains the Rosenthal-Henderson B-factor plot, which
predicts how many particles you need for a given resolution. It is the
information-theoretic limit of the experiment and it is the kind of result that
should exist for design methods and does not.

### Resolution and validation

| Title | Speaker | Length | Link |
|---|---|---|---|
| Theory of CryoEM SPA 9: Resolution | Carlos Oscar Sorzano (CNB-CSIC) | 33:39 | [▶](https://www.youtube.com/watch?v=Bs4Ygpo9kLU) |
| Theory of CryoEM SPA 1: Basics of image processing operations | Carlos Oscar Sorzano | 1:39:06 | [▶](https://www.youtube.com/watch?v=cdIuLguRi8Q) |
| Theory of CryoEM SPA 7: Validation | Carlos Oscar Sorzano | 32:43 | [▶](https://www.youtube.com/watch?v=gglZdNEskJs) |
| 3DEM map-model validation using Q-scores | Greg Pintilie (Stanford) | 1:00:28 | [▶](https://www.youtube.com/watch?v=MCPDR_gjCTA) |
| **Practical validation in cryo-EM (and common pitfalls)** | Oliver Clarke (Columbia) | 1:15:31 | [▶](https://www.youtube.com/watch?v=x7uDEDaiWQk) |
| Cryo-EM map validation | Kako Stapleton (Glasgow/eBIC) | 41:26 | [▶](https://www.youtube.com/watch?v=876Mc4oopxo) |

**Clarke's talk is a catalogue of the specific ways reconstruction algorithms
produce confident garbage** — model bias, Einstein-from-noise, mask artifacts.
Watch it and then ask what the equivalent catalogue would be for a generative
design model. Nobody has written that one.

### Particle picking with deep learning

| Title | Speaker | Length | Link |
|---|---|---|---|
| Detection of objects in cryo-EM micrographs using geometric deep learning | Tristan Bepler (NYSBC) | 42:58 | [▶](https://www.youtube.com/watch?v=HeW8a059HxQ) |
| Topaz (developer walkthrough) | SBGrid | 44:49 | [▶](https://www.youtube.com/watch?v=I6PUxeVBQt8) |
| crYOLO | SBGrid | 39:14 | [▶](https://www.youtube.com/watch?v=JTgldM4wAAk) |
| AI methods for picking, refinement and model building | Jianlin Cheng (Missouri) | 59:53 | [▶](https://www.youtube.com/watch?v=2bRiPO1Ah6w) |

Bepler frames picking as **positive-unlabeled learning** — the key insight that
your labels are incomplete rather than negative. That reframing generalizes
directly to protein design datasets, where "not reported to bind" is routinely
and wrongly treated as "does not bind."

### Heterogeneity — the frontier

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Resolving flexibility and heterogeneity with 3D Variability Analysis** | Ali Punjani (Structura/Toronto) | 1:28:55 | [▶](https://www.youtube.com/watch?v=0O781Od1z_E) |
| CryoSPARC 3D Flexible Refinement Tutorial | Structura | 1:22:11 | [▶](https://www.youtube.com/watch?v=o1srM6PkIP0) |
| New Developments for SPA Data Processing in CryoSPARC | Ali Punjani | 28:41 | [▶](https://www.youtube.com/watch?v=RilgeYTy7IU) |
| Cryo-EM Workshop (ab initio branch-and-bound) | Ali Punjani | 30:40 | [▶](https://www.youtube.com/watch?v=ejV1Qur00pU) |
| **New methods in cryoDRGN: cryoDRGN-ET and cryoDRGN-AI** | Ellen Zhong (Princeton) | 58:14 | [▶](https://www.youtube.com/watch?v=iXb5qrtiYbo) |
| ML for determining protein structure and dynamics from cryo-EM images | Ellen Zhong (IPAM) | 48:30 | [▶](https://www.youtube.com/watch?v=SQDLlZkoCJU) |
| Reconstructing continuous distributions of 3D protein structure (MLCB 2019) | Ellen Zhong | 15:44 | [▶](https://www.youtube.com/watch?v=zd6YcUyDhPE) |
| Algorithms for Biomolecular Structures at Proteome Scale (2026) | Ellen Zhong | 58:24 | [▶](https://www.youtube.com/watch?v=TOia5lEwaQ4) |
| CryoDRGN (developer deep dive) | SBGrid | 1:02:55 | [▶](https://www.youtube.com/watch?v=P9c1dUO3-Hg) |
| Contextual Conformational Variability using Deep Learning | Steven Ludtke (Baylor) | 41:06 | [▶](https://www.youtube.com/watch?v=HcxoaEEWjII) |
| FaNaC1 and Continuous Heterogeneity (case study) | Structura | 1:28:45 | [▶](https://www.youtube.com/watch?v=TFcTP33TKUo) |

**This subsection is the most important in Atlas J for your purposes.** A
particle stack contains an ensemble; 3DVA, 3DFlex and cryoDRGN are three
different answers to the question of how to extract it. 3DVA is probabilistic
PCA in volume space. 3DFlex learns a deformation field in a canonical frame, so
flexibility becomes warping rather than a mixture of rigid volumes. cryoDRGN is
a VAE with a coordinate-based decoder.

These are MSM-style reasoning with learned representations, arrived at
independently by the cryo-EM community. **Nobody has properly connected them to
Atlas family I.** That connection — what is the relationship between a cryoDRGN
latent coordinate and a TICA coordinate, and can one be used to validate the
other — is an unclaimed project.

### Motion correction and the inverse problem

| Title | Speaker | Length | Link |
|---|---|---|---|
| Bayesian Particle-Polishing in Detail | Jasenko Zivanov (Basel) | 31:39 | [▶](https://www.youtube.com/watch?v=Fa0Vl_aH5Og) |
| Cryo-EM Workshop (compact version) | Jasenko Zivanov | 23:42 | [▶](https://www.youtube.com/watch?v=cPNoxLsMeqQ) |
| CryoSPARC v4.4: Reference-Based Motion Correction | Structura | 17:22 | [▶](https://www.youtube.com/watch?v=gnM_IvJShwY) |
| **Mathematics of Cryo-Electron Microscopy (2025)** | Amit Singer (Princeton) | 59:26 | [▶](https://www.youtube.com/watch?v=mbNk6hRGMdU) |
| Mathematics for cryo-EM — ICM 2018 plenary | Amit Singer | 50:35 | [▶](https://www.youtube.com/watch?v=csg5p2Oo6HI) |
| RECOVAR: regularized covariance estimation for heterogeneity | Amit Singer | 34:36 | [▶](https://www.youtube.com/watch?v=7ycfzGcWOVI) |
| Method of moments in cryo-EM | Joe Kileel | 48:37 | [▶](https://www.youtube.com/watch?v=5CEPxPuG5pU) |
| Hyper-molecules: continuous heterogeneity before deep learning | Roy Lederman (Yale) | 33:08 | [▶](https://www.youtube.com/watch?v=o8LlPB0Vy10) |
| Imaging biomolecules and high-resolution SPA | Alberto Bartesaghi (Duke) | 41:23 | [▶](https://www.youtube.com/watch?v=hRK-e09YyUc) |
| Machine learning for SPA by cryo-EM | Carlos Oscar Sorzano | 40:12 | [▶](https://www.youtube.com/watch?v=A3jxb7BCvVU) |

Singer's ICM plenary is the most mathematically rigorous item in this family.
Kileel's method of moments — reconstruction without ever estimating orientations,
by matching low-order moments — is algebraically elegant and worth an hour even
if you never use it, because it demonstrates that the obvious formulation of a
problem is not always the necessary one.

### Symmetry, strategy, maps and models

| Title | Speaker | Length | Link |
|---|---|---|---|
| Cryo-EM17 lecture 07: Data processing strategy | Rafael Fernandez-Leiro | 47:27 | [▶](https://www.youtube.com/watch?v=Z5KzEk-5pMI) |
| Processing difficult datasets in cryo-EM | Kelly Nguyen (MRC-LMB) | 44:43 | [▶](https://www.youtube.com/watch?v=9GszV5W4riI) |
| RELION 5 (Blush regularization, DynaMight) | Sjors Scheres | 28:28 | [▶](https://www.youtube.com/watch?v=poToOzOObEw) |
| RELION 4.0 (subtomogram averaging unified) | MRC-LMB | 33:48 | [▶](https://www.youtube.com/watch?v=kZTX4K4KeOY) |
| Map post-processing with DeepEMhancer | Ruben Sanchez-Garcia (Oxford) | 17:21 | [▶](https://www.youtube.com/watch?v=az7WERpdVtY) |
| DeepEMhancer (long form, failure modes) | SBGrid | 43:20 | [▶](https://www.youtube.com/watch?v=_iDI2f7Q2Sc) |
| **Cryo-EM map density modification and model building** | Tom Terwilliger (Phenix) | 38:56 | [▶](https://www.youtube.com/watch?v=T3fiMcXgKuU) |
| **ModelAngelo: automated atomic modelling and protein identification** | Kiarash Jamali (MRC-LMB) | 20:03 | [▶](https://www.youtube.com/watch?v=JT0hogC6zNA) |
| ModelAngelo (architecture detail) | SBGrid | 38:10 | [▶](https://www.youtube.com/watch?v=k9xz7Vbpe_c) |
| Phenix automated model building (map_to_model) | Phenix | 1:23:26 | [▶](https://www.youtube.com/watch?v=FQ5ChzckzmE) |
| Cryo-EM17 lecture 08: Atomic modeling and validation | Alan Brown (Harvard) | 49:59 | [▶](https://www.youtube.com/watch?v=byAFhhDt-f4) |
| Refinement and validation using TEMPy2 | Maya Topf (Birkbeck) | 39:54 | [▶](https://www.youtube.com/watch?v=cSOZ6Hu0hZk) |
| Seven years of ISOLDE: model building as restrained MD | Tristan Croll | 33:52 | [▶](https://www.youtube.com/watch?v=1aPA5H0wEnU) |

**Pair DeepEMhancer with Terwilliger.** One is a neural sharpener trained to map
raw reconstructions to locally sharpened targets, with a frank account of the
hallucination risk; the other is maximum-likelihood density modification carried
over from crystallography, using half-map statistics as an error model. Same
goal, learned versus principled. That pairing is the whole learning-versus-physics
argument in miniature, on a problem small enough to see clearly.

ModelAngelo's striking result is that a graph network consuming density,
sequence and geometry **can identify which protein is in the map by searching a
proteome.** That is structure-based search, and it is the cryo-EM community
inventing Foldseek's problem independently.

### Tomography

| Title | Speaker | Length | Link |
|---|---|---|---|
| Cryo-EM17 lecture 09: Tomography | John Briggs (MRC-LMB) | 40:07 | [▶](https://www.youtube.com/watch?v=4Z0sQ_GhBkk) |
| High-throughput algorithms for subtomogram averaging | Mikhail Kudryashev | 46:46 | [▶](https://www.youtube.com/watch?v=o3NGxOk0Eog) |
| Cryo-ET and subtomogram averaging | Giulia Zanetti (Birkbeck) | 22:46 | [▶](https://www.youtube.com/watch?v=jWrldrOsnbY) |
| Dynamo (geometry-constrained alignment) | SBGrid | 46:49 | [▶](https://www.youtube.com/watch?v=IBPlVZj9N2w) |
| Representation learning for picking in cryo-ET with TomoTwin | MPI Dortmund | 27:31 | [▶](https://www.youtube.com/watch?v=rrdI58wBqGM) |

---

## J.2 Crystallographic algorithms

### The phase problem

| Title | Speaker | Length | Link |
|---|---|---|---|
| X-ray Crystallography: Phase Problem Part I | IIT Roorkee | 58:31 | [▶](https://www.youtube.com/watch?v=5aaBtzh-D2g) |
| Direct Methods: Phase Determination in Crystallography | BioXFEL | 23:25 | [▶](https://www.youtube.com/watch?v=tAbjwZl5fqU) |
| Phase problem, direct methods, Patterson method | Vidya-mitra | 45:42 | [▶](https://www.youtube.com/watch?v=wns4QTwSeoE) |

### Molecular replacement

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Molecular Replacement and cryo-EM docking** | Randy Read (Cambridge) | 22:30 | [▶](https://www.youtube.com/watch?v=k9jiepXvfwU) |
| Information content in molecular replacement | Randy Read (CCP4 SW2019) | 27:32 | [▶](https://www.youtube.com/watch?v=he7MP6LNs2Y) |
| Trueblood Award Lecture 2022 | Airlie McCoy (Cambridge) | 55:04 | [▶](https://www.youtube.com/watch?v=iHomjhpo2NI) |
| Solve your structure with MR at warp speed | Airlie McCoy | 33:06 | [▶](https://www.youtube.com/watch?v=tAh4cNfKq3k) |
| Phasing and Molecular Replacement | Andrea Thorn (ThornLab) | 50:27 | [▶](https://www.youtube.com/watch?v=f5tjUX8EP_c) |
| Phaser (algorithm walkthrough) | SBGrid | 43:42 | [▶](https://www.youtube.com/watch?v=HX-wc-ygFnM) |

**Read's "information content" talk is the one to steal from.** It reframes
molecular replacement as an information problem — expected log-likelihood gain
as a predictor of success *before you run anything*. The protein design analogue
would be a quantity that predicts, before synthesis, whether a design campaign
will succeed. No such quantity exists. That is a thesis.

McCoy's warp-speed talk covers how AlphaFold models with per-residue error
estimates get weighted into the search — one of the cleanest existing examples
of a learned model's uncertainty being used correctly downstream.

### Experimental phasing, density modification, refinement

| Title | Speaker | Length | Link |
|---|---|---|---|
| Pattersons, locating heavy atoms, and SHELXC/D/E | Andrea Thorn | 1:05:16 | [▶](https://www.youtube.com/watch?v=aMfZX4rKkVo) |
| Experimental Phasing | Andrea Thorn (ThornLab) | 54:15 | [▶](https://www.youtube.com/watch?v=PUsEvtBVIUs) |
| Advanced SHELXC/D/E | ThornLab | 37:32 | [▶](https://www.youtube.com/watch?v=h1TfsVaGKT0) |
| Experimental Phasing (SIR/SAD/MAD) | BioXFEL | 1:00:55 | [▶](https://www.youtube.com/watch?v=akk8Q17gRgg) |
| **Map Improvement, Averaging, and Density Modification** | Kevin Cowtan (York) | 1:04:42 | [▶](https://www.youtube.com/watch?v=r3f__K8aoIE) |
| Mini-lecture: Density modification | Phenix | 4:49 | [▶](https://www.youtube.com/watch?v=_BK2ETHuZhU) |
| **Refinement** | Garib Murshudov (MRC-LMB) | 1:10:09 | [▶](https://www.youtube.com/watch?v=EuAJd7YUlCw) |
| Refinement, X-ray and cryo-EM | Pavel Afonine (Phenix) | 1:00:19 | [▶](https://www.youtube.com/watch?v=2EQxQzv0C1M) |
| Refinement | Andrea Thorn (ThornLab) | 54:36 | [▶](https://www.youtube.com/watch?v=KuG85T77AYM) |
| **CC*: linking crystallographic model and data quality** | SBGrid | 50:08 | [▶](https://www.youtube.com/watch?v=LirxJIcQ6T0) |
| Densities in X-ray crystallography and electron microscopy | Garib Murshudov | 30:34 | [▶](https://www.youtube.com/watch?v=mOwFkoJG7BQ) |
| Twinning | ThornLab | 44:48 | [▶](https://www.youtube.com/watch?v=WF7j94sUi1w) |
| PDB-REDO as data source for refinement and validation | Robbie Joosten (NKI) | 20:04 | [▶](https://www.youtube.com/watch?v=CqgR_HgqRWY) |
| cctbx.xfel: software for serial crystallography | SBGrid | 43:47 | [▶](https://www.youtube.com/watch?v=pXurebQliSY) |
| DIALS | SBGrid | 46:02 | [▶](https://www.youtube.com/watch?v=moeaBbg2ewg) |

Cowtan's lecture contains the phase-combination bookkeeping that stops you from
double-counting information — a discipline the ML community has no equivalent of
and badly needs when combining MSA, template and structural priors.

**The CC* lecture matters disproportionately.** Karplus and Diederichs showed
that model quality bounds data quality and vice versa, which is the statistically
defensible replacement for arbitrary resolution cutoffs. If you filter PDB
training data by "quality," this lecture tells you what you are actually doing.

### Multiconformer models and room-temperature crystallography

| Title | Speaker | Length | Link |
|---|---|---|---|
| **Automated Multiconformer Model Building (qFit)** | Fraser/van den Bedem lineage, ML4PE | 57:53 | [▶](https://www.youtube.com/watch?v=RXFPojFrz7I) |
| qFit (developer treatment) | SBGrid | 1:00:17 | [▶](https://www.youtube.com/watch?v=NbktfxlSu2I) |
| TSRC Workshop on Protein Dynamics | James Fraser (UCSF) | 44:09 | [▶](https://www.youtube.com/watch?v=F_t4mTvuMPw) |
| Multitemperature data and diffuse scattering | BioCAT / BioXFEL | 59:54 | [▶](https://www.youtube.com/watch?v=328z3CBfZN8) |
| **CASP SIG on Modeling Conformational Ensembles** | Wankowicz & Fraser | 1:14:26 | [▶](https://www.youtube.com/watch?v=IUgFg0X7GDY) |
| Refactoring the B-factor | Nick Pearce (VU Amsterdam) | 16:40 | [▶](https://www.youtube.com/watch?v=UJADAEIq_jg) |
| Modeling structural heterogeneity in crystallography and cryo-EM | Rutgers IQB | 37:27 | [▶](https://www.youtube.com/watch?v=LtUCgHG2r-c) |

qFit's algorithm is worth knowing in detail: **sample backbone and side-chain
alternates, then select a sparse subset by quadratic and mixed-integer
programming** so that you fit the density without fitting the noise. That is a
sparse model selection problem, and the same formulation would apply directly to
selecting a sub-ensemble from a generative model's samples. Nobody has made that
carry.

The Wankowicz and Fraser CASP talk asks how you would even *score* a predicted
ensemble against experiment. That is the open problem that gates every ensemble
prediction method in Atlas family P.

---

## J.3 NMR structure calculation

The thinnest area in this family, and the gap is real rather than a search
failure: the primary method developers have not put algorithm lectures online.

| Title | Speaker | Length | Link |
|---|---|---|---|
| Structure determination of biomolecules by NMR | Antonio Rosato (CERM Florence) | 1:08:16 | [▶](https://www.youtube.com/watch?v=kb60I14ru4E) |
| **Biomolecular NMR for Protein Structure and Dynamics (L03)** | Bruce Donald (Duke) | 1:50:01 | [▶](https://www.youtube.com/watch?v=MlxiHqUlWr0) |
| **NMR, RDCs and Protein Structure Calculation (L04)** | Bruce Donald (Duke) | 1:54:38 | [▶](https://www.youtube.com/watch?v=Wx-l2yWQsnM) |
| Automated High-Resolution Structure Determination Using RDCs | Bruce Donald | 54:29 | [▶](https://www.youtube.com/watch?v=yhYxAZbMrsc) |
| Residual Dipolar Couplings: Theory and Applications, Part 1 | Ad Bax (NIH) | 45:52 | [▶](https://www.youtube.com/watch?v=cjXgUPsJjgQ) |
| Residual Dipolar Couplings, Part 2 | Ad Bax | 1:03:13 | [▶](https://www.youtube.com/watch?v=bmx56Fjv8Hc) |
| The NOE for distance measurement | AMPERE Encyclopedia | 24:14 | [▶](https://www.youtube.com/watch?v=4BRCKnI64JQ) |
| Paramagnetic NMR and the MAXOCC portal | Antonio Rosato | 1:03:49 | [▶](https://www.youtube.com/watch?v=XkOtziPJBZc) |
| Introduction to Paramagnetic NMR Spectroscopy | ANZMAG | 1:14:53 | [▶](https://www.youtube.com/watch?v=gL4AlPWlQJ0) |
| Protein Structure Determination Using Paramagnetic NMR | Alireza Bahramzadeh | 58:32 | [▶](https://www.youtube.com/watch?v=VLDhefrUyms) |
| **The important role of dynamics** | Lewis Kay (Toronto) | 1:18:31 | [▶](https://www.youtube.com/watch?v=zbx8exkZOgQ) |
| Making the Invisible Visible: Molecular Machines in Motion | Lewis Kay | 1:16:53 | [▶](https://www.youtube.com/watch?v=2E0BIHnZHuk) |

**The Bruce Donald lectures are the find here.** He is a computer scientist, and
he treats NMR structure determination as a constraint-satisfaction and search
problem with complexity arguments — including RDC-EXACT, polynomial-time
structure determination from sparse RDCs, deliberately contrasted with the
simulated-annealing paradigm everyone else uses. That framing exists nowhere
else and it is exactly the posture this curriculum is trying to teach.

Kay's relaxation-dispersion work recovers the structure, population *and*
exchange rate of a state that is spectroscopically invisible. It is the cleanest
experimental ground truth available for any excited-state prediction method, and
it is what would falsify an ensemble generator.

*Gaps: no algorithm lectures by Güntert (CYANA), Schwieters (XPLOR-NIH), Clore,
or on CS-Rosetta. Read Güntert et al. 1997, Herrmann et al. 2002, Schwieters et
al. 2003 and Shen et al. 2008 instead.*

---

## J.4 SAXS, SANS and low-resolution methods

| Title | Speaker | Length | Link |
|---|---|---|---|
| **WeNMR Lecture on SAXS, Part I** | Alexey Kikhney (EMBL Hamburg) | 1:51:33 | [▶](https://www.youtube.com/watch?v=xjnOCvvPNms) |
| WeNMR SAXS Part II (DAMMIN/DAMMIF) | Alexey Kikhney | 1:02:51 | [▶](https://www.youtube.com/watch?v=uURuKtYfLWI) |
| WeNMR SAXS Part III (rigid-body and hybrid modeling) | Alexey Kikhney | 1:01:23 | [▶](https://www.youtube.com/watch?v=OOtp6nr8qmg) |
| SAXS Part I: Introduction to Biological Small Angle Scattering | SBGrid | 49:18 | [▶](https://www.youtube.com/watch?v=SevPRumWqsE) |
| SAXS Part II: Advanced Applications | SBGrid | 51:53 | [▶](https://www.youtube.com/watch?v=mPoshDWJucI) |
| **Analyzing Flexible and Disordered Macromolecules with SAXS** | BioCAT (APS) | 44:55 | [▶](https://www.youtube.com/watch?v=ABnxBq18ozo) |
| DENSS: Ab initio electron density maps from SAXS | Thomas Grant (SBGrid) | 1:03:36 | [▶](https://www.youtube.com/watch?v=VO3n918l76Y) |
| SEC-SAXS and Advanced SAXS Analysis | BioCAT | 1:10:19 | [▶](https://www.youtube.com/watch?v=6k_-l8OHaPw) |
| Small Angle Neutron Scattering: a complementary technique | BioCAT | 49:50 | [▶](https://www.youtube.com/watch?v=y09Vd2sKBFQ) |
| Deuteration for biological neutron scattering | LINXS (Lund) | 1:05:55 | [▶](https://www.youtube.com/watch?v=MTPtm5KpJnc) |

The Ensemble Optimization Method in the BioCAT flexible-molecules lecture is a
**genetic-algorithm selection of a sub-ensemble whose averaged profile fits the
data** — the only honest way to treat a flexible system with an averaging
observable. It is the same sparse-selection problem as qFit and as ensemble
reweighting in Atlas K, arrived at independently a third time. When the same
problem shape appears three times in three communities, that is the signature of
something worth generalizing.

---

## J.5 Crosslinking-MS, HDX and native MS

| Title | Speaker | Length | Link |
|---|---|---|---|
| Developing crosslinking mass spectrometry | Francis O'Reilly (TU Berlin) | 17:40 | [▶](https://www.youtube.com/watch?v=U2AlN_8ed3E) |
| Elucidating large molecular architectures by crosslinking and MS | Nir Kalisman (HUJI) | 35:05 | [▶](https://www.youtube.com/watch?v=rATz6D3aNZY) |
| Crosslinking MS (search algorithms and FDR) | Jürgen Cox (MaxQuant) | 35:50 | [▶](https://www.youtube.com/watch?v=4oDfUM6nw5I) |
| Advancing crosslinking MS to elucidate cellular networks | ASBMB | 50:32 | [▶](https://www.youtube.com/watch?v=70XWhwSUFk0) |
| Structural Insights from HDX Mass Spectrometry | Trajan Scientific | 1:14:30 | [▶](https://www.youtube.com/watch?v=C3l4P5aTfhk) |
| FPOP Tutorial Series: Introduction | The Sharp Lab | 33:16 | [▶](https://www.youtube.com/watch?v=u_zJJpr2wlA) |
| Native Mass Spectrometry for Structural Biology | The Protein Society | 2:19:08 | [▶](https://www.youtube.com/watch?v=jqw6yVp8SUc) |

Note the recurring theme: **HDX restrains modeling only through a forward model
relating structure to exchange rate.** Every one of these data types does. The
quality of a structural inference from sparse data is bounded by the quality of
its forward model, and forward models are where almost no machine learning has
been applied. That observation is row six in the unexchanged-ideas table.

---

## J.6 BUILD — Atlas J

1. **Implement 2D single-particle alignment and averaging** from scratch on
   simulated noisy projections. Add a CTF. Watch your average degrade as SNR
   falls, and find the particle count where it recovers.
2. **Implement the FSC** and reproduce the relationship between particle number
   and resolution. Then deliberately over-mask and watch the FSC lie to you.
3. **Take one structure you use in training data.** Find its validation report,
   its resolution, its Rfree, its occupancies and its alternate conformations.
   Write one page on which parts of that coordinate file are measurement and
   which are prior. Do this for a 1.2 Å structure and a 3.5 Å structure and
   compare.
4. **The carry exercise.** Read the qFit selection formulation. Write down how
   you would use the same mixed-integer formulation to select a sub-ensemble
   from RFdiffusion samples. Two pages. That is a paper outline.

**Derivation checkpoints due: 43, 44, 45, 46.**

---

## J.7 Paired reading — Atlas J

| Watch this | Then read this | Hold this question |
|---|---|---|
| Scheres, *Image refinement in 2D and 3D* | Scheres 2012, *J Mol Biol* 415:406; *J Struct Biol* 180:519 | What is marginalized over, and what would break if you estimated instead? |
| Sigworth, *EM Image Formation* | Sigworth 1998, *J Struct Biol* 122:328 | Write the likelihood for one particle image. What are the nuisance parameters? |
| Henderson, *past present and future* | Rosenthal & Henderson 2003 | Derive the particle-number vs resolution relation. What is its design analogue? |
| Sorzano, *Resolution* | Scheres & Chen 2012 | Why 0.143? What would the right threshold be if you derived it? |
| Clarke, *Practical validation* | Any Einstein-from-noise analysis | List every failure mode. Which has a generative-design equivalent? |
| Bepler, *Topaz* | Bepler et al. 2019, *Nat Methods* 16:1153 | Positive-unlabeled learning. Where else are your labels incomplete rather than negative? |
| Punjani, *3DVA* | Punjani & Fleet 2021, *J Struct Biol* 213:107702 | 3DVA is probabilistic PCA over volumes. What is the analogue of a TICA coordinate here? |
| Punjani, *3DFlex* | Punjani & Fleet 2023, *Nat Methods* 20:860 | A learned deformation field versus a mixture of volumes. When does each win? |
| Zhong, *cryoDRGN-AI* | Zhong et al. 2021, *Nat Methods* 18:176 | What does the latent space mean, and how would you validate that interpretation? |
| Zivanov, *Bayesian particle polishing* | Zivanov et al. 2019, *IUCrJ* 6:5 | A spatial-coherence prior plus damage-weighted B-factors. What is the prior doing? |
| Singer, ICM plenary | Any sample-complexity result for cryo-EM | How many images does the inverse problem require at a given SNR? |
| Terwilliger + DeepEMhancer | Terwilliger et al. 2020, *Nat Methods* 17:923; Sanchez-Garcia et al. 2021 | Principled versus learned map improvement. How would you detect hallucination? |
| Jamali, *ModelAngelo* | Jamali et al. 2024, *Nature* 628:450 | It identifies the protein by searching a proteome. How does that relate to Foldseek? |
| Read, *Information content in MR* | Oeffner, McCoy & Read 2013 | Expected LLG predicts success before you run. What predicts design success? |
| Cowtan, *Density modification* | Cowtan 1994; Wang 1985 | How do you combine phase information without double-counting? |
| SBGrid, *CC** | **Karplus & Diederichs 2012, *Science* 336:1030** | Model quality bounds data quality. What does that imply for filtering training data? |
| Murshudov, *Refinement* | Murshudov, Vagin & Dodson 1997 | Write the ML refinement target. Where do restraints enter, and with what weight? |
| ThornLab, *Refinement* | Brünger 1992, *Nature* 355:472 | What does Rfree detect that Rwork cannot? What is the ML analogue? |
| qFit talks | van den Bedem et al. 2009; Riley et al. 2021 | Sparse selection by mixed-integer programming. Apply it to generative samples. |
| Fraser, *TSRC Protein Dynamics* | Keedy et al. 2015, *eLife* 4:e07574 | Cryocooling erases substates. What fraction of the PDB is a cryo artifact? |
| Wankowicz & Fraser, CASP SIG | Any ensemble-scoring proposal | How would you score a predicted ensemble? Propose a metric and its failure mode. |
| Donald, L03–L04 | Wang & Donald 2004 | Structure determination as constraint satisfaction. What becomes tractable? |
| Bax, *RDCs Part 1* | Tjandra & Bax 1997, *Science* 278:1111 | Orientational versus distance restraints. What does each underdetermine? |
| Kay, *The important role of dynamics* | Korzhnev et al. 2004, *Nature* 430:586 | An invisible state with a measured population. Could a generative model predict it? |
| Kikhney, SAXS II | Svergun 1999; Franke & Svergun 2009 | DAMMIN regularizes by compactness. What does that prior exclude? |
| BioCAT, *Flexible molecules* | Bernadó et al. 2007; Tria et al. 2015 | Sub-ensemble selection by genetic algorithm. Same problem as qFit. Generalize it. |
| O'Reilly, *XL-MS* | O'Reilly & Rappsilber 2018, *Nat Struct Mol Biol* 25:1000 | A crosslink is an upper-bound distance restraint. What is its false-positive rate? |
| HDX lecture | Engen 2009, *Anal Chem* 81:7870 | Write the forward model from structure to protection factor. Could it be learned? |
